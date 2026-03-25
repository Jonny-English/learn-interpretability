import { flattenTimeline, getCourse } from "@/lib/course";

export default function TimelinePage() {
  const items = flattenTimeline(getCourse());

  return (
    <main className="content-grid">
      <section className="hero module-hero">
        <p className="eyebrow">Frozen at 2026-03-25</p>
        <h1>Interpretability paper timeline</h1>
        <p className="hero-copy">
          A chronological view of the official papers and posts that anchor the course.
        </p>
      </section>

      <section className="panel timeline-panel">
        {items.map((item) => (
          <article className="timeline-card" key={`${item.date}-${item.url}`}>
            <span>{item.date}</span>
            <strong>{item.title}</strong>
            <p>{item.moduleId} · {item.moduleTitleEn}</p>
            <a href={item.url} rel="noreferrer" target="_blank">
              Open source page
            </a>
          </article>
        ))}
      </section>
    </main>
  );
}
