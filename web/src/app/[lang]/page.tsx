import Link from "next/link";

import { ConceptGraph } from "@/components/ConceptGraph";
import { GlossaryCards } from "@/components/GlossaryCards";
import { ProgressTracker } from "@/components/ProgressTracker";
import {
  getConceptGraph,
  getCourse,
  getGlossary,
  getLocalizedSummary,
  getLocalizedTitle,
} from "@/lib/course";

export function generateStaticParams() {
  return [{ lang: "zh" }, { lang: "en" }];
}

export default async function LanguageHome({
  params,
}: {
  params: Promise<{ lang: "zh" | "en" }>;
}) {
  const { lang: language } = await params;
  const course = getCourse();
  const modules = course.map((module) => ({
    ...module,
    title: getLocalizedTitle(module, language),
    summary: getLocalizedSummary(module, language),
  }));
  const glossary = getGlossary();
  const graph = getConceptGraph();

  return (
    <main className="content-grid">
      <section className="hero module-hero">
        <p className="eyebrow">{language === "zh" ? "课程总览" : "Course overview"}</p>
        <h1>{language === "zh" ? "从视觉电路走到语言模型内部" : "From visual circuits to internal language-model structure"}</h1>
        <p className="hero-copy">
          {language === "zh"
            ? "先用直观的视觉实验建立心智图，再用 Anthropic 的主线论文把 superposition、feature、circuit tracing 和 character control 串起来。"
            : "Build intuition with visual experiments first, then connect superposition, features, circuit tracing, and character control through Anthropic's core papers."}
        </p>
      </section>

      <section className="panel module-grid">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{language === "zh" ? "模块" : "Modules"}</p>
            <h3>{language === "zh" ? "按顺序学习" : "Follow the numbered path"}</h3>
          </div>
        </div>
        <div className="cards">
          {modules.map((module) => (
            <Link className="module-card" href={`/${language}/modules/${module.id}`} key={module.id}>
              <span className="module-id">{module.id}</span>
              <strong>{module.title}</strong>
              <p>{module.summary}</p>
              <small>{module.runnable_tier}</small>
            </Link>
          ))}
        </div>
      </section>

      <ProgressTracker
        heading={language === "zh" ? "本地进度" : "Local progress"}
        modules={modules.map((module) => ({ id: module.id, title: module.title }))}
      />
      <ConceptGraph graph={graph} language={language} />
      <GlossaryCards terms={glossary} language={language} />
    </main>
  );
}
