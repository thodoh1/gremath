import Link from "next/link";
import { buttonVariants } from "@/components/ui/button";
import { getCatalog, getSections } from "@/lib/content";
import { cn } from "@/lib/utils";

export default function HomePage() {
  const catalog = getCatalog();
  const sections = getSections();
  const critical = catalog.filter((s) => s.priority === "Critical").length;
  const high = catalog.filter((s) => s.priority === "High").length;
  const medium = catalog.filter((s) => s.priority === "Medium").length;

  return (
    <article className="mx-auto max-w-3xl">
      <p className="text-[11px] uppercase tracking-[0.22em] text-burgundy">
        GRE Mathematics Subject Test
      </p>
      <h1 className="mt-3 font-serif text-4xl font-semibold leading-tight tracking-tight sm:text-5xl">
        A book that teaches every skill, from nothing to a perfect score.
      </h1>
      <p className="mt-6 text-lg leading-relaxed text-ink/80">
        This is not a formula sheet. It is a full course through{" "}
        <strong>{catalog.length} atomic skills</strong> — the same checklist a
        perfect-score attempt has to own. Each lesson starts from first
        principles, builds the precise idea, works examples by hand, then
        trains the exact GRE motion: speed, hypotheses, traps, and mixed
        problems.
      </p>
      <p className="mt-4 text-lg leading-relaxed text-ink/80">
        If you knew none of this yesterday, you can still use this book. Read
        in order. Do the drills before you turn the page. Do not skip the
        foundations because calculus is fifty percent of the exam: calculus
        without algebraic fluency is how people lose easy points.
      </p>
      <div className="mt-8 flex flex-col gap-3 sm:flex-row">
        <Link
          href="/front/preface"
          className={cn(buttonVariants({ size: "lg" }))}
        >
          Start with the preface
        </Link>
        <Link
          href="/lesson/M-001"
          className={cn(buttonVariants({ size: "lg", variant: "outline" }))}
        >
          Open Lesson M-001
        </Link>
      </div>
      <dl className="mt-12 grid grid-cols-2 gap-4 sm:grid-cols-4">
        {[
          [String(catalog.length), "Atomic lessons"],
          [String(sections.length), "Parts A–Y"],
          [String(critical), "Critical skills"],
          ["170 min", "Exam clock"],
        ].map(([k, v]) => (
          <div key={v} className="rounded-lg border border-rule bg-paper-dark/50 p-4">
            <dt className="text-[11px] uppercase tracking-[0.16em] text-ink/45">
              {v}
            </dt>
            <dd className="mt-1 font-serif text-2xl">{k}</dd>
          </div>
        ))}
      </dl>
      <p className="mt-6 text-sm text-ink/60">
        {critical} critical · {high} high · {medium} medium. Priorities are
        study-planning judgments, not official ETS weights. Calculus is still
        about half the test.
      </p>
      <h2 className="mt-14 font-serif text-2xl">How the book is built</h2>
      <ol className="mt-4 list-decimal space-y-3 pl-5 text-ink/85">
        <li>
          <strong>Front matter</strong> tells you how the exam works and how to
          study so that “I read it” becomes “I can do it timed.”
        </li>
        <li>
          <strong>Parts A–Y</strong> are the fields themselves: algebra,
          calculus, linear algebra, algebra, analysis, discrete math,
          probability, geometry, complex analysis, numerical methods, and
          mixed GRE craft.
        </li>
        <li>
          <strong>One lesson per skill.</strong> You never get a table in place
          of an explanation. You get the idea, the precise statement, a worked
          example, a GRE-style problem, traps, and drills with solutions.
        </li>
      </ol>
      <h2 className="mt-14 font-serif text-2xl">The parts</h2>
      <ul className="mt-4 divide-y divide-rule border-y border-rule">
        {sections.map((sec) => (
          <li key={sec.letter}>
            <Link
              href={`/part/${sec.letter}`}
              className="flex items-baseline justify-between gap-4 py-3 hover:text-burgundy"
            >
              <span className="font-medium">{sec.section}</span>
              <span className="text-sm text-ink/45">
                {sec.skills.length} lessons
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </article>
  );
}
