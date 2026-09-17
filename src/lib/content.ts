import { readFileSync, existsSync } from "fs";
import path from "path";

export type Priority = "Critical" | "High" | "Medium" | "Supplemental";

export type Skill = {
  id: string;
  n: number;
  letter: string;
  section: string;
  priority: Priority;
  topic: string;
  title: string;
  prerequisites: string;
  reconstructed?: boolean;
};

export type FrontPage = {
  slug: string;
  title: string;
  subtitle: string;
};

export const FRONT_PAGES: FrontPage[] = [
  {
    slug: "preface",
    title: "Preface",
    subtitle: "What this book is, and who it is for",
  },
  {
    slug: "exam",
    title: "The GRE Mathematics Subject Test",
    subtitle: "Format, weights, and how a perfect score is actually made",
  },
  {
    slug: "how-to-study",
    title: "How to study this book",
    subtitle: "A method that turns 1036 skills into exam fluency",
  },
  {
    slug: "notation",
    title: "Notation and conventions",
    subtitle: "The language used in every lesson",
  },
  {
    slug: "study-plan",
    title: "Ten-phase study plan",
    subtitle: "The path from first arithmetic to mixed timed mastery",
  },
];

const ROOT = path.join(process.cwd(), "content");

let cachedCatalog: Skill[] | null = null;

export function getCatalog(): Skill[] {
  if (cachedCatalog) return cachedCatalog;
  const raw = readFileSync(path.join(ROOT, "catalog.json"), "utf8");
  cachedCatalog = JSON.parse(raw) as Skill[];
  return cachedCatalog;
}

export function getSkill(id: string): Skill | undefined {
  return getCatalog().find((s) => s.id === id);
}

export function getSections() {
  const catalog = getCatalog();
  const map = new Map<
    string,
    { letter: string; section: string; skills: Skill[] }
  >();
  for (const skill of catalog) {
    const cur = map.get(skill.letter);
    if (cur) cur.skills.push(skill);
    else
      map.set(skill.letter, {
        letter: skill.letter,
        section: skill.section,
        skills: [skill],
      });
  }
  return [...map.values()];
}

export function getTopics(letter: string) {
  const skills = getCatalog().filter((s) => s.letter === letter);
  const map = new Map<string, Skill[]>();
  for (const skill of skills) {
    const cur = map.get(skill.topic);
    if (cur) cur.push(skill);
    else map.set(skill.topic, [skill]);
  }
  return [...map.entries()].map(([topic, items]) => ({ topic, skills: items }));
}

export function neighbors(id: string): { prev?: Skill; next?: Skill } {
  const catalog = getCatalog();
  const i = catalog.findIndex((s) => s.id === id);
  if (i < 0) return {};
  return {
    prev: catalog[i - 1],
    next: catalog[i + 1],
  };
}

export function readMarkdown(rel: string): string {
  const file = path.join(ROOT, rel);
  if (!existsSync(file)) {
    return "_This page has not been generated yet._";
  }
  return readFileSync(file, "utf8");
}

export function lessonMarkdown(id: string): string {
  return readMarkdown(path.join("lessons", `${id}.md`));
}

export function partMarkdown(letter: string): string {
  return readMarkdown(path.join("parts", `${letter}.md`));
}

export function frontMarkdown(slug: string): string {
  return readMarkdown(path.join("front", `${slug}.md`));
}

export function priorityVariant(
  priority: Priority
): "critical" | "high" | "medium" {
  if (priority === "Critical") return "critical";
  if (priority === "High") return "high";
  return "medium";
}
