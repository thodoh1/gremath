import Link from "next/link";
import { FRONT_PAGES, getSections } from "@/lib/content";

export default function TocPage() {
  const sections = getSections();
  return (
    <article className="mx-auto max-w-3xl pb-16">
      <p className="text-[11px] uppercase tracking-[0.2em] text-burgundy">
        Contents
      </p>
      <h1 className="mt-2 font-serif text-4xl">The whole book</h1>
      <p className="mt-4 text-ink/75">
        Read front matter first, then Parts A through Y in order. Inside a
        part, stay inside a topic until the drills are easy.
      </p>
      <h2 className="mt-10 font-serif text-2xl">Front matter</h2>
      <ul className="mt-2 divide-y divide-rule border-y border-rule">
        {FRONT_PAGES.map((f) => (
          <li key={f.slug}>
            <Link href={`/front/${f.slug}`} className="block py-3 hover:text-burgundy">
              <span className="font-medium">{f.title}</span>
              <span className="mt-1 block text-sm text-ink/55">
                {f.subtitle}
              </span>
            </Link>
          </li>
        ))}
      </ul>
      {sections.map((sec) => (
        <section key={sec.letter} className="mt-10">
          <h2 className="font-serif text-2xl">
            <Link href={`/part/${sec.letter}`} className="hover:text-burgundy">
              {sec.section}
            </Link>
          </h2>
          <ul className="mt-2 columns-1 gap-x-8 sm:columns-2">
            {sec.skills.map((sk) => (
              <li key={sk.id} className="break-inside-avoid">
                <Link
                  href={`/lesson/${sk.id}`}
                  className="block py-1 text-sm hover:text-burgundy"
                >
                  <span className="font-mono text-[11px] text-ink/40">
                    {sk.id}
                  </span>{" "}
                  {sk.title}
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </article>
  );
}
