"use client";

import { useState } from "react";

import type { GlossaryTerm } from "@/lib/course";

export function GlossaryCards({
  terms,
  language,
}: {
  terms: GlossaryTerm[];
  language: "zh" | "en";
}) {
  const [selected, setSelected] = useState(terms[0]?.id ?? "");

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{language === "zh" ? "术语卡片" : "Glossary cards"}</p>
          <h3>{language === "zh" ? "快速复习本课程反复出现的词" : "Review the terms that keep returning"}</h3>
        </div>
      </div>
      <div className="glossary-grid">
        {terms.map((term) => (
          <button
            className={`glossary-card ${selected === term.id ? "active" : ""}`}
            key={term.id}
            onClick={() => setSelected(term.id)}
            type="button"
          >
            <strong>{language === "zh" ? term.term_zh : term.term_en}</strong>
            <p>{language === "zh" ? term.definition_zh : term.definition_en}</p>
          </button>
        ))}
      </div>
    </section>
  );
}
