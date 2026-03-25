import type { Metadata } from "next";
import Link from "next/link";

import "./globals.css";

export const metadata: Metadata = {
  title: "From Circuits to Claude",
  description: "A bilingual interpretability course that connects visual circuits to Anthropic's research arc.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <div className="page-shell">
          <header className="site-header">
            <Link className="brand" href="/">
              From Circuits to Claude
            </Link>
            <nav>
              <Link href="/zh">中文</Link>
              <Link href="/en">English</Link>
              <Link href="/timeline">Timeline</Link>
            </nav>
          </header>
          {children}
        </div>
      </body>
    </html>
  );
}
