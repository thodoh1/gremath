import Link from "next/link";
import { notFound } from "next/navigation";
import { Markdown } from "@/components/Markdown";
import {
  getSections,
  getTopics,
  partMarkdown,
} from "@/lib/content";

export function generateStaticParams() {
  return getSections().map((s) => ({ letter: s.letter }));
}

export default async function PartPage({
  params,
}: {
  params: Promise<{ letter: string }>;
}) {
  const { letter } = await params;
  const sections = getSections();
  const sec = sections.find((s) => s.letter === letter);
  if (!sec) notFound();
  const topics = getTopics(letter);
  const source = partMarkdown(letter);

  return (
    <article className="mx-auto max-w-3xl pb-16">
      <p className="text-[11px] uppercase tracking-[0.2em] text-burgundy">
        Part {letter}
      </p>
      <Markdown source={source} />
      <h2 className="mt-12 font-serif text-2xl">Lessons in this part</h2>
      {topics.map((t) => (
        <section key={t.topic} className="mt-8">
          <h3 className="font-serif text-lg">{t.topic}</h3>
          <ul className="mt-2 divide-y divide-rule border-y border-rule">
            {t.skills.map((sk) => (
              <li key={sk.id}>
                <Link
                  href={`/lesson/${sk.id}`}
                  className="flex flex-col gap-1 py-2.5 hover:text-burgundy sm:flex-row sm:items-baseline sm:justify-between"
                >
                  <span>
                    <span className="font-mono text-xs text-ink/45">
                      {sk.id}
                    </span>{" "}
                    {sk.title}
                  </span>
                  <span className="text-xs uppercase tracking-wide text-ink/40">
                    {sk.priority}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </article>
  );
}
