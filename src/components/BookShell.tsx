"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useMemo, useState } from "react";
import { BookOpen, Menu, Search, X } from "lucide-react";
import type { FrontPage, Skill } from "@/lib/content";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { cn } from "@/lib/utils";
import { loadMastery } from "@/lib/progress";

type Section = { letter: string; section: string; skills: Skill[] };

export function BookShell({
  sections,
  front,
  children,
}: {
  sections: Section[];
  front: FrontPage[];
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [mastery, setMasteryState] = useState<Record<string, number>>({});
  const [openLetter, setOpenLetter] = useState<string | null>(null);

  useEffect(() => {
    setMasteryState(loadMastery());
    const onChange = () => setMasteryState(loadMastery());
    window.addEventListener("gre-mastery", onChange);
    window.addEventListener("storage", onChange);
    return () => {
      window.removeEventListener("gre-mastery", onChange);
      window.removeEventListener("storage", onChange);
    };
  }, []);

  useEffect(() => {
    setOpen(false);
    const m = pathname.match(/\/part\/([A-Y])/);
    const l = pathname.match(/\/lesson\/M-(\d+)/);
    if (m) setOpenLetter(m[1]);
    if (l) {
      const n = parseInt(l[1], 10);
      const skill = sections.flatMap((s) => s.skills).find((s) => s.n === n);
      if (skill) setOpenLetter(skill.letter);
    }
  }, [pathname, sections]);

  const total = sections.reduce((a, s) => a + s.skills.length, 0);
  const fluent = Object.values(mastery).filter((v) => v >= 3).length;
  const started = Object.values(mastery).filter((v) => v >= 1).length;

  const hits = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (q.length < 2) return [];
    return sections
      .flatMap((s) => s.skills)
      .filter(
        (s) =>
          s.title.toLowerCase().includes(q) ||
          s.topic.toLowerCase().includes(q) ||
          s.id.toLowerCase().includes(q) ||
          s.section.toLowerCase().includes(q)
      )
      .slice(0, 12);
  }, [query, sections]);

  return (
    <div className="min-h-screen bg-paper text-ink">
      <header className="sticky top-0 z-40 border-b border-rule/80 bg-paper/95 backdrop-blur">
        <div className="mx-auto flex h-14 max-w-[1600px] items-center gap-3 px-4">
          <button
            className="rounded-md p-2 hover:bg-paper-dark lg:hidden"
            onClick={() => setOpen((v) => !v)}
            aria-label="Toggle contents"
          >
            {open ? <X size={18} /> : <Menu size={18} />}
          </button>
          <Link href="/" className="flex items-center gap-2 font-semibold">
            <BookOpen size={18} className="text-burgundy" />
            <span className="hidden sm:inline">GRE Mathematics Book</span>
            <span className="sm:hidden">GRE Math</span>
          </Link>
          <div className="ml-auto hidden w-full max-w-md items-center gap-2 md:flex">
            <Search size={16} className="text-ink/40" />
            <Input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search 1036 skills…"
              className="h-9 bg-paper-dark/50"
              onKeyDown={(e) => {
                if (e.key === "Enter" && hits[0]) {
                  router.push(`/lesson/${hits[0].id}`);
                  setQuery("");
                }
              }}
            />
          </div>
          <Link
            href="/toc"
            className="text-sm text-ink/70 hover:text-burgundy"
          >
            Contents
          </Link>
        </div>
        <Progress value={total ? (fluent / total) * 100 : 0} />
      </header>

      <div className="mx-auto flex max-w-[1600px]">
        <aside
          className={cn(
            "fixed inset-y-14 left-0 z-30 w-[min(22rem,90vw)] overflow-y-auto border-r border-rule bg-paper p-4 lg:static lg:inset-auto lg:block lg:h-[calc(100vh-3.6rem)] lg:w-80 lg:sticky lg:top-14",
            open ? "block" : "hidden lg:block"
          )}
        >
          <p className="mb-3 text-[11px] uppercase tracking-[0.18em] text-ink/45">
            {started} begun · {fluent} exam-fluent / {total}
          </p>
          <div className="mb-4 md:hidden">
            <Input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search skills…"
            />
          </div>
          {hits.length > 0 && (
            <div className="mb-4 rounded-md border border-rule bg-paper-dark/60 p-2">
              {hits.map((h) => (
                <Link
                  key={h.id}
                  href={`/lesson/${h.id}`}
                  className="block rounded px-2 py-1.5 text-sm hover:bg-paper"
                  onClick={() => setQuery("")}
                >
                  <span className="font-mono text-[11px] text-burgundy">
                    {h.id}
                  </span>{" "}
                  {h.title}
                </Link>
              ))}
            </div>
          )}
          <nav className="space-y-4 text-sm">
            <div>
              <p className="mb-1 text-[11px] uppercase tracking-[0.18em] text-ink/45">
                Front matter
              </p>
              <ul className="space-y-0.5">
                {front.map((f) => (
                  <li key={f.slug}>
                    <Link
                      href={`/front/${f.slug}`}
                      className={cn(
                        "block rounded px-2 py-1 hover:bg-paper-dark",
                        pathname === `/front/${f.slug}` &&
                          "bg-paper-dark text-burgundy"
                      )}
                    >
                      {f.title}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
            {sections.map((sec) => (
              <div key={sec.letter}>
                <button
                  className="flex w-full items-center justify-between rounded px-2 py-1 text-left hover:bg-paper-dark"
                  onClick={() =>
                    setOpenLetter((cur) =>
                      cur === sec.letter ? null : sec.letter
                    )
                  }
                >
                  <Link
                    href={`/part/${sec.letter}`}
                    className="font-medium hover:text-burgundy"
                    onClick={(e) => e.stopPropagation()}
                  >
                    {sec.section}
                  </Link>
                  <span className="text-[11px] text-ink/40">
                    {sec.skills.length}
                  </span>
                </button>
                {openLetter === sec.letter && (
                  <ul className="mt-1 max-h-80 space-y-0.5 overflow-y-auto border-l border-rule ml-3 pl-2">
                    {sec.skills.map((sk) => (
                      <li key={sk.id}>
                        <Link
                          href={`/lesson/${sk.id}`}
                          className={cn(
                            "block rounded px-1.5 py-1 text-[13px] leading-snug hover:bg-paper-dark",
                            pathname === `/lesson/${sk.id}` &&
                              "bg-paper-dark text-burgundy"
                          )}
                        >
                          <span className="font-mono text-[10px] text-ink/45">
                            {sk.id}
                          </span>{" "}
                          {sk.title}
                        </Link>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            ))}
          </nav>
        </aside>
        <main className="min-w-0 flex-1 px-4 py-8 sm:px-8 lg:px-12">
          {children}
        </main>
      </div>
    </div>
  );
}
