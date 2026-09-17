import { notFound } from "next/navigation";
import { Markdown } from "@/components/Markdown";
import { FRONT_PAGES, frontMarkdown } from "@/lib/content";

export function generateStaticParams() {
  return FRONT_PAGES.map((f) => ({ slug: f.slug }));
}

export default async function FrontPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const page = FRONT_PAGES.find((f) => f.slug === slug);
  if (!page) notFound();
  return (
    <article className="mx-auto max-w-3xl pb-16">
      <p className="text-[11px] uppercase tracking-[0.2em] text-burgundy">
        Front matter
      </p>
      <Markdown source={frontMarkdown(slug)} />
    </article>
  );
}
