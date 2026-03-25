"use client";

import { useState } from "react";

import type { PersonaPayload } from "@/lib/course";

export function PersonaPreview({
  payload,
  language,
}: {
  payload: PersonaPayload;
  language: "zh" | "en";
}) {
  const [selectedId, setSelectedId] = useState(payload.personas[0]?.id ?? "");
  const selected = payload.personas.find((persona) => persona.id === selectedId) ?? payload.personas[0];
  const traits = Object.keys(selected.scores_before);

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{language === "zh" ? "Artifact 预览" : "Artifact preview"}</p>
          <h3>{language === "zh" ? "Persona vector 对比" : "Persona-vector comparison"}</h3>
        </div>
      </div>
      <div className="case-switcher">
        {payload.personas.map((persona) => (
          <button
            className={persona.id === selected.id ? "active" : ""}
            key={persona.id}
            onClick={() => setSelectedId(persona.id)}
            type="button"
          >
            {language === "zh" ? persona.label_zh : persona.label_en}
          </button>
        ))}
      </div>
      <div className="trait-bars">
        {traits.map((trait) => (
          <div className="trait-row" key={trait}>
            <span>{trait}</span>
            <div className="bar-track">
              <div className="bar before" style={{ width: `${selected.scores_before[trait] * 100}%` }} />
              <div className="bar after" style={{ width: `${selected.scores_after[trait] * 100}%` }} />
            </div>
          </div>
        ))}
      </div>
      <div className="prompt-stack">
        {payload.prompts.map((prompt) => (
          <article className="prompt-card" key={prompt.id}>
            <strong>{prompt.prompt}</strong>
            <p>{language === "zh" ? "干预前" : "Before"}: {prompt.response_before}</p>
            <p>{language === "zh" ? "干预后" : "After"}: {prompt.response_after}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
