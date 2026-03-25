import Link from "next/link";

import { CircuitExplorer } from "@/components/CircuitExplorer";
import { PersonaPreview } from "@/components/PersonaPreview";
import {
  getAttributionCases,
  getCourse,
  getDoc,
  getLocalizedSummary,
  getLocalizedTitle,
  getModule,
  getPersonaPayload,
  type CourseModule,
} from "@/lib/course";

function renderDoc(markdown: string) {
  return markdown
    .split("\n\n")
    .map((block) => block.trim())
    .filter(Boolean)
    .map((block, index) => {
      if (block.startsWith("# ")) {
        return <h1 key={index}>{block.slice(2)}</h1>;
      }
      if (block.startsWith("## ")) {
        return <h2 key={index}>{block.slice(3)}</h2>;
      }
      if (block.startsWith("- ")) {
        const items = block.split("\n").map((line) => line.replace(/^- /, ""));
        return (
          <ul className="doc-list" key={index}>
            {items.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        );
      }
      return <p key={index}>{block}</p>;
    });
}

export function generateStaticParams() {
  const course = getCourse();
  return ["zh", "en"].flatMap((lang) => course.map((module) => ({ lang, id: module.id })));
}

function modulePaths(module: CourseModule, language: "zh" | "en") {
  const notebookName = `${module.id.toLowerCase()}_${module.web_slug.replaceAll("-", "_")}.ipynb`;
  const docName = `${module.id.toLowerCase()}-${module.web_slug}.md`;
  return {
    notebook: `notebooks/${language}/${notebookName}`,
    doc: `docs/${language}/modules/${docName}`,
  };
}

export default async function ModulePage({
  params,
}: {
  params: Promise<{ lang: "zh" | "en"; id: string }>;
}) {
  const { lang: language, id } = await params;
  const module = getModule(language, id);
  const doc = getDoc(language, module);
  const title = getLocalizedTitle(module, language);
  const summary = getLocalizedSummary(module, language);
  const paths = modulePaths(module, language);

  return (
    <main className="content-grid">
      <section className="hero module-hero">
        <p className="eyebrow">{module.id}</p>
        <h1>{title}</h1>
        <p className="hero-copy">{summary}</p>
        <div className="meta-row">
          <span>{module.runnable_tier}</span>
          <span>{language === "zh" ? "先修：" : "Prereqs:"} {module.prereqs.join(", ") || "none"}</span>
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{language === "zh" ? "正文" : "Module note"}</p>
            <h3>{language === "zh" ? "直接来自同步文档" : "Rendered from the mirrored docs"}</h3>
          </div>
        </div>
        <article className="doc-article">{renderDoc(doc)}</article>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{language === "zh" ? "材料入口" : "Materials"}</p>
            <h3>{language === "zh" ? "文档、notebook 与论文" : "Docs, notebook, and papers"}</h3>
          </div>
        </div>
        <div className="link-stack">
          <code>{paths.doc}</code>
          <code>{paths.notebook}</code>
          {module.paper_refs.map((paper) => (
            <a href={paper.url} key={paper.url} rel="noreferrer" target="_blank">
              {paper.date} · {paper.title}
            </a>
          ))}
        </div>
      </section>

      {module.id === "M04" ? <CircuitExplorer cases={getAttributionCases()} language={language} /> : null}
      {module.id === "M05" ? <PersonaPreview payload={getPersonaPayload()} language={language} /> : null}

      <section className="panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{language === "zh" ? "继续学习" : "Next step"}</p>
            <h3>{language === "zh" ? "回到总览" : "Back to the overview"}</h3>
          </div>
        </div>
        <div className="hero-actions">
          <Link href={`/${language}`}>{language === "zh" ? "返回课程首页" : "Return to course home"}</Link>
          <Link href="/timeline">{language === "zh" ? "查看论文时间线" : "Open paper timeline"}</Link>
        </div>
      </section>
    </main>
  );
}
