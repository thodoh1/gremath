# GRE Mathematics Book

A complete course through **1036 atomic skills** for the GRE Mathematics Subject Test. This is a teaching book, not a formula sheet: each skill is a lesson with the idea from zero, a precise statement, a worked example, a GRE-style problem, traps, and drills with solutions.

## Run locally

```bash
npm install
python3 scripts/generate_book.py   # regenerates lessons if you edit the generators
npm run dev
```

Open [http://127.0.0.1:43147](http://127.0.0.1:43147).

## How to use it

1. Read **Front matter** (preface, exam, how to study, notation, ten-phase plan).
2. Work **Parts A–Y** in order. Do not skip foundations.
3. On each lesson: copy the definition, cover the worked example and finish it, time the GRE-style problem, then do both drills on paper.
4. Mark mastery **0–3** in the reader (saved in the browser). **3** means you can solve an unfamiliar timed item that uses the skill.

## What is in the repo

- `content/catalog.json` — the 1036-skill checklist
- `content/front/` — preface and study method
- `content/parts/` — part introductions (A–Y)
- `content/lessons/M-XXX.md` — one lesson per skill
- `scripts/` — generators that rebuild the book
- `src/` — the Next.js reader (KaTeX, search, progress)

Official GRE Mathematics resources live at ETS (practice book and content structure). This book teaches the skills those items use. A handful of checklist titles were truncated at page breaks in the source table; those lessons are reconstructed from the surrounding topic and labeled in the text.

## Mastery scale

| Level | Meaning |
| --- | --- |
| 0 | Unseen |
| 1 | Learned (can explain with the book closed) |
| 2 | Can solve standard problems |
| 3 | Can solve unfamiliar timed GRE-style problems |
