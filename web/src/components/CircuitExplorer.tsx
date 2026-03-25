"use client";

import { useMemo, useState } from "react";

import type { AttributionCase } from "@/lib/course";

export function CircuitExplorer({
  cases,
  language,
}: {
  cases: AttributionCase[];
  language: "zh" | "en";
}) {
  const [selectedId, setSelectedId] = useState(cases[0]?.id ?? "");
  const selectedCase = useMemo(
    () => cases.find((entry) => entry.id === selectedId) ?? cases[0],
    [cases, selectedId],
  );
  const nodeMap = new Map(selectedCase.nodes.map((node) => [node.id, node]));

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{language === "zh" ? "Artifact 预览" : "Artifact preview"}</p>
          <h3>{language === "zh" ? "可点击的 attribution graph" : "Clickable attribution graph"}</h3>
        </div>
      </div>
      <div className="case-switcher">
        {cases.map((item) => (
          <button
            className={item.id === selectedCase.id ? "active" : ""}
            key={item.id}
            onClick={() => setSelectedId(item.id)}
            type="button"
          >
            {language === "zh" ? item.title_zh : item.title_en}
          </button>
        ))}
      </div>
      <p className="artifact-copy">
        <strong>{language === "zh" ? "问题：" : "Question:"}</strong> {selectedCase.question}
        <br />
        <strong>{language === "zh" ? "答案：" : "Answer:"}</strong> {selectedCase.answer}
      </p>
      <svg className="graph compact" viewBox="0 0 1000 360" role="img">
        {selectedCase.edges.map((edge) => {
          const source = nodeMap.get(edge.source);
          const target = nodeMap.get(edge.target);
          if (!source || !target) {
            return null;
          }
          return (
            <line
              key={`${edge.source}-${edge.target}`}
              x1={source.x * 1000}
              x2={target.x * 1000}
              y1={source.y * 360}
              y2={target.y * 360}
              stroke="#c96a28"
              strokeOpacity={0.6}
              strokeWidth={2 + edge.score * 4}
            />
          );
        })}
        {selectedCase.nodes.map((node) => (
          <g key={node.id}>
            <circle
              cx={node.x * 1000}
              cy={node.y * 360}
              fill={node.kind === "feature" ? "#123b63" : "#b5893a"}
              r={22}
            />
            <text x={node.x * 1000} y={node.y * 360 + 46} textAnchor="middle">
              {language === "zh" ? node.label_zh : node.label_en}
            </text>
          </g>
        ))}
      </svg>
      <ul className="edge-list">
        {selectedCase.edges
          .slice()
          .sort((a, b) => b.score - a.score)
          .map((edge) => (
            <li key={`${edge.source}-${edge.target}`}>
              <strong>
                {language === "zh"
                  ? nodeMap.get(edge.source)?.label_zh
                  : nodeMap.get(edge.source)?.label_en}{" "}
                →{" "}
                {language === "zh"
                  ? nodeMap.get(edge.target)?.label_zh
                  : nodeMap.get(edge.target)?.label_en}
              </strong>
              <span>{edge.score.toFixed(2)}</span>
            </li>
          ))}
      </ul>
    </section>
  );
}
