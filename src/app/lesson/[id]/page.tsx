import Link from "next/link";
import { notFound } from "next/navigation";
import { Markdown } from "@/components/Markdown";
import { Badge } from "@/components/ui/badge";
import { MasteryControl } from "@/components/MasteryControl";
import {
  getSkill,
  getCatalog,
  lessonMarkdown,
  neighbors,
  priorityVariant,
} from "@/lib/content";
import { buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";

export function generateStaticParams() {
  return getCatalog().map((s) => ({ id: s.id }));
}

export default async function LessonPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const skill = getSkill(id);
  if (!skill) notFound();
  const { prev, next } = neighbors(id);
  const source = lessonMarkdown(id);

  return (
    <article className="mx-auto max-w-3xl pb-16">
      <div className="mb-6 flex flex-wrap items-center gap-2 text-sm">
        <Link href={`/part/${skill.letter}`} className="text-burgundy hover:underline">
          {skill.section}
        </Link>
        <span className="text-ink/30">/</span>
        <span className="text-ink/60">{skill.topic}</span>
      </div>
      <div className="mb-4 flex flex-wrap gap-2">
        <Badge variant="outline">{skill.id}</Badge>
        <Badge variant={priorityVariant(skill.priority)}>{skill.priority}</Badge>
        {skill.prerequisites ? (
          <Badge variant="outline">Needs {skill.prerequisites}</Badge>
        ) : (
          <Badge variant="outline">No prerequisites</Badge>
        )}
      </div>
      <Markdown source={source} />
      <div className="mt-10">
        <MasteryControl id={skill.id} />
      </div>
      <div className="mt-8 flex flex-col gap-3 border-t border-rule pt-6 sm:flex-row sm:justify-between">
        {prev ? (
          <Link
            href={`/lesson/${prev.id}`}
            className={cn(buttonVariants({ variant: "outline" }), "max-w-full sm:max-w-[48%]")}
          >
            ← {prev.id} {prev.title}
          </Link>
        ) : (
          <Link href="/front/study-plan" className={cn(buttonVariants({ variant: "outline" }))}>
            ← Study plan
          </Link>
        )}
        {next ? (
          <Link
            href={`/lesson/${next.id}`}
            className={cn(
              buttonVariants({ variant: "outline" }),
              "max-w-full sm:max-w-[48%] sm:ml-auto"
            )}
          >
            {next.id} {next.title} →
          </Link>
        ) : (
          <span />
        )}
      </div>
    </article>
  );
}
