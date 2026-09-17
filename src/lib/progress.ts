"use client";

export type Mastery = 0 | 1 | 2 | 3;

const KEY = "gre-math-book-mastery-v1";

export function loadMastery(): Record<string, Mastery> {
  if (typeof window === "undefined") return {};
  try {
    const raw = window.localStorage.getItem(KEY);
    return raw ? (JSON.parse(raw) as Record<string, Mastery>) : {};
  } catch {
    return {};
  }
}

export function setMastery(id: string, value: Mastery) {
  const all = loadMastery();
  all[id] = value;
  window.localStorage.setItem(KEY, JSON.stringify(all));
  window.dispatchEvent(new Event("gre-mastery"));
}

export function masteryLabel(value: Mastery | undefined) {
  switch (value) {
    case 1:
      return "Learned";
    case 2:
      return "Can solve";
    case 3:
      return "Exam-fluent";
    default:
      return "Unseen";
  }
}
