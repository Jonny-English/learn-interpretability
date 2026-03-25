"use client";

import { useMemo, useState } from "react";

import type { ConceptGraph as Graph } from "@/lib/course";

export function ConceptGraph({
  graph,
  language,
}: {
  graph: Graph;
  language: "zh" | "en";
}) {
  const [selected, setSelected] = useState(graph.nodes[0]?.id ?? "");
  const nodeMap = useMemo(() => new Map(graph.nodes.map((node) => [node.id, node])), [graph.nodes]);
  const relatedEdges = useMemo(
    () => graph.edges.filter((edge) => edge.source === selected || edge.target === selected),
    [graph.edges, selected],
  );
  const selectedNode = nodeMap.get(selected);

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{language === "zh" ? "概念依赖图" : "Concept dependency graph"}</p>
          <h3>{language === "zh" ? "点节点看它连接到哪里" : "Click a node to inspect its neighborhood"}</h3>
        </div>
      </div>
      <svg className="graph" viewBox="0 0 1000 420" role="img">
        {graph.edges.map((edge) => {
          const source = nodeMap.get(edge.source);
          const target = nodeMap.get(edge.target);
          if (!source || !target) {
            return null;
          }
          const active = edge.source === selected || edge.target === selected;
          return (
            <line
              key={`${edge.source}-${edge.target}`}
              x1={source.x * 1000}
              x2={target.x * 1000}
              y1={source.y * 420}
              y2={target.y * 420}
              stroke={active ? "#c96a28" : "#8ea3b8"}
              strokeOpacity={active ? 0.95 : 0.35}
              strokeWidth={2 + edge.weight * 4}
            />
          );
        })}
        {graph.nodes.map((node) => (
          <g
            className={`graph-node ${selected === node.id ? "active" : ""}`}
            key={node.id}
            onClick={() => setSelected(node.id)}
          >
            <circle
              cx={node.x * 1000}
              cy={node.y * 420}
              fill={selected === node.id ? "#123b63" : "#215f8b"}
              r={selected === node.id ? 28 : 22}
            />
            <text
              x={node.x * 1000}
              y={node.y * 420 + 48}
              textAnchor="middle"
            >
              {language === "zh" ? node.label_zh : node.label_en}
            </text>
          </g>
        ))}
      </svg>
      {selectedNode ? (
        <div className="graph-details">
          <h4>{language === "zh" ? selectedNode.label_zh : selectedNode.label_en}</h4>
          <ul className="edge-list">
            {relatedEdges.map((edge) => {
              const source = nodeMap.get(edge.source);
              const target = nodeMap.get(edge.target);
              const label = language === "zh" ? edge.label_zh : edge.label_en;
              return (
                <li key={`${edge.source}-${edge.target}`}>
                  <strong>
                    {language === "zh" ? source?.label_zh : source?.label_en} →{" "}
                    {language === "zh" ? target?.label_zh : target?.label_en}
                  </strong>
                  <span>{label}</span>
                </li>
              );
            })}
          </ul>
        </div>
      ) : null}
    </section>
  );
}
