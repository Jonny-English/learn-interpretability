import Link from "next/link";

export default function HomePage() {
  return (
    <main className="landing">
      <section className="hero">
        <p className="eyebrow">Bilingual interpretability course</p>
        <h1>From Circuits to Claude</h1>
        <p className="hero-copy">
          Start with visual circuits, then move through superposition, sparse features,
          steering, circuit tracing, and character control.
        </p>
        <div className="hero-actions">
          <Link href="/zh">进入中文课程</Link>
          <Link href="/en">Open English course</Link>
          <Link href="/timeline">View paper timeline</Link>
        </div>
      </section>
    </main>
  );
}
