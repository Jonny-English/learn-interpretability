import fs from "node:fs";
import path from "node:path";

export type PaperRef = {
  title: string;
  url: string;
  date: string;
};

export type CourseModule = {
  id: string;
  order: number;
  title_zh: string;
  title_en: string;
  summary_zh: string;
  summary_en: string;
  prereqs: string[];
  paper_refs: PaperRef[];
  artifact_refs: string[];
  runnable_tier: string;
  web_slug: string;
};

export type GlossaryTerm = {
  id: string;
  term_zh: string;
  term_en: string;
  definition_zh: string;
  definition_en: string;
};

export type ConceptGraph = {
  nodes: Array<{
    id: string;
    label_zh: string;
    label_en: string;
    x: number;
    y: number;
    group: string;
  }>;
  edges: Array<{
    source: string;
    target: string;
    weight: number;
    label_zh: string;
    label_en: string;
  }>;
};

export type AttributionCase = {
  id: string;
  title_zh: string;
  title_en: string;
  question: string;
  answer: string;
  nodes: Array<{
    id: string;
    label_zh: string;
    label_en: string;
    x: number;
    y: number;
    kind: string;
  }>;
  edges: Array<{
    source: string;
    target: string;
    score: number;
  }>;
};

export type PersonaPayload = {
  personas: Array<{
    id: string;
    label_zh: string;
    label_en: string;
    scores_before: Record<string, number>;
    scores_after: Record<string, number>;
    vector: number[];
  }>;
  prompts: Array<{
    id: string;
    prompt: string;
    response_before: string;
    response_after: string;
  }>;
};

function repoRoot(): string {
  return path.join(process.cwd(), "..");
}

function readJson<T>(relativePath: string): T {
  const filePath = path.join(repoRoot(), relativePath);
  return JSON.parse(fs.readFileSync(filePath, "utf8")) as T;
}

export function getCourse(): CourseModule[] {
  return readJson<CourseModule[]>("content/course.json").sort((a, b) => a.order - b.order);
}

export function getGlossary(): GlossaryTerm[] {
  return readJson<GlossaryTerm[]>("content/glossary.json");
}

export function getConceptGraph(): ConceptGraph {
  return readJson<ConceptGraph>("artifacts/concept_graph.json");
}

export function getAttributionCases(): AttributionCase[] {
  return readJson<{ cases: AttributionCase[] }>("artifacts/m04_attribution_graph.json").cases;
}

export function getPersonaPayload(): PersonaPayload {
  return readJson<PersonaPayload>("artifacts/m05_persona_vectors.json");
}

export function getModule(language: "zh" | "en", id: string): CourseModule {
  const module = getCourse().find((entry) => entry.id === id);
  if (!module) {
    throw new Error(`Unknown module: ${id}`);
  }
  return module;
}

export function getDoc(language: "zh" | "en", module: CourseModule): string {
  const filename = `${module.id.toLowerCase()}-${module.web_slug}.md`;
  return fs.readFileSync(path.join(repoRoot(), "docs", language, "modules", filename), "utf8");
}

export function getLocalizedTitle(module: CourseModule, language: "zh" | "en"): string {
  return language === "zh" ? module.title_zh : module.title_en;
}

export function getLocalizedSummary(module: CourseModule, language: "zh" | "en"): string {
  return language === "zh" ? module.summary_zh : module.summary_en;
}

export function flattenTimeline(course: CourseModule[]) {
  const seen = new Set<string>();
  const timeline = [];
  for (const module of course) {
    for (const paper of module.paper_refs) {
      const key = `${paper.url}:${module.id}`;
      if (seen.has(key)) {
        continue;
      }
      seen.add(key);
      timeline.push({
        ...paper,
        moduleId: module.id,
        moduleTitleEn: module.title_en,
        moduleTitleZh: module.title_zh,
      });
    }
  }
  return timeline.sort((a, b) => a.date.localeCompare(b.date));
}
