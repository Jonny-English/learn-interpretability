"use client";

import { useEffect, useMemo, useState } from "react";

type ModuleInfo = {
  id: string;
  title: string;
};

const STORAGE_KEY = "from-circuits-to-claude-progress";

export function ProgressTracker({
  modules,
  heading,
}: {
  modules: ModuleInfo[];
  heading: string;
}) {
  const [completed, setCompleted] = useState<Record<string, boolean>>({});

  useEffect(() => {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (raw) {
      setCompleted(JSON.parse(raw) as Record<string, boolean>);
    }
  }, []);

  const doneCount = useMemo(
    () => modules.filter((module) => completed[module.id]).length,
    [completed, modules],
  );

  function toggle(id: string) {
    setCompleted((current) => {
      const next = { ...current, [id]: !current[id] };
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
  }

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">{heading}</p>
          <h3>Progress</h3>
        </div>
        <strong>
          {doneCount}/{modules.length}
        </strong>
      </div>
      <div className="checklist">
        {modules.map((module) => (
          <button
            className={`check-item ${completed[module.id] ? "complete" : ""}`}
            key={module.id}
            onClick={() => toggle(module.id)}
            type="button"
          >
            <span>{module.id}</span>
            <span>{module.title}</span>
          </button>
        ))}
      </div>
    </section>
  );
}
