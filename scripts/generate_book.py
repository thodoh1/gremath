#!/usr/bin/env python3
"""Generate the GRE Mathematics teaching book from the 1036-skill catalog."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
CONTENT = ROOT / "content"
CATALOG = json.loads((CONTENT / "catalog.json").read_text())

PRIORITY_WHY = {
    "Critical": "This is a Critical skill: it is used constantly, and a hole here leaks points all over the paper.",
    "High": "This is a High skill: it is standard GRE material. You should be able to do it without warming up.",
    "Medium": "This is a Medium skill: it appears less often, but when it appears it is often a discriminator.",
    "Supplemental": "This is supporting fluency. Own it so it never becomes the reason you miss a mixed problem.",
}


def md_escape_title(s: str) -> str:
    return s.replace("*", r"\*").replace("_", r"\_")


def latex_ok(s: str) -> str:
    return s.strip()


# ---------------------------------------------------------------------------
# Front matter
# ---------------------------------------------------------------------------

FRONT = {}

FRONT["preface"] = r'''# Preface

This book exists for one job: take a person who does not yet own the GRE Mathematics Subject Test skills and, through thorough study, make a perfect score possible.

It is built from a 1036-skill master checklist covering algebra, precalculus, trigonometry, complex numbers, single-variable and multivariable calculus, differential equations, linear algebra, number theory, abstract algebra, real analysis, topology, logic and proof, combinatorics, graph theory, probability, statistics, geometry, complex analysis, numerical methods, and the mixed exam craft that turns knowledge into points.

It is not a digest. A digest is what you use *after* you can already do the problems. If you cannot yet factor a cubic, write an $\varepsilon$-$N$ proof, row-reduce a matrix, or see that a vector field is conservative, a table of formulas will not save you. Each skill here is a lesson: why the idea exists, how it is defined, how to think with it, how to compute with it, how the GRE asks it, and how people miss it.

## Who this is for

You can start with almost no undergraduate mathematics, provided you will not skip. The early parts rebuild arithmetic, algebra, functions, and trigonometry as working tools, not as memories of high school. Later parts assume you have actually done the earlier drills. Prerequisites are listed on every lesson; they are not decoration.

If you already have a mathematics degree, do not skim the “easy” lessons. The GRE’s cruelty is not that it asks research-level questions. It is that it asks undergraduate questions *under a clock, without a calculator, in mixed order, with hypotheses that matter*. Perfect scores die on sign errors, illegal cancellation, theorems used without hypotheses, and off-by-one counting — not on ignorance of sheaves.

## What “perfect” means here

ETS does not publish a public conversion that makes “66/66” a promise. Scaled scores move. What you can control is this: every skill on the checklist reaches **Level 3 mastery** — you can solve unfamiliar, timed, GRE-style problems that use the skill, not merely recite a definition.

The mastery scale used throughout:

- **0** unseen
- **1** learned (you can explain it with the book closed)
- **2** you can solve standard problems
- **3** you can solve unfamiliar timed GRE-style problems

Do not mark 3 because the worked example made sense. Mark 3 after you can do the drills cold, then a mixed problem that did not announce the topic.

## How a lesson is built

Every skill lesson has the same spine, on purpose:

1. Why the skill exists on this exam
2. The idea from zero
3. The precise statement
4. The working method
5. A fully worked example
6. A GRE-style problem with a full solution
7. Traps that cost points
8. Drills with solutions
9. What this skill unlocks next

Read with a pencil. Rewrite the examples. Then close the page and do the drills. If you cannot do the drills, you did not finish the lesson.

## Honesty about source material

The skill list comes from a GRE Mathematics perfect-score checklist. A handful of titles at page breaks in that table were truncated; those lessons are reconstructed from the surrounding topic and labeled as such. The mathematics is standard undergraduate mathematics. Official exam details and practice tests live at ETS; this book teaches the skills the exam uses.

Official starting points:

- ETS GRE Mathematics content structure
- ETS GRE Mathematics Practice Book (the official practice test)
- ETS Subject Tests prepare page

Use official items as the final judge of timing. Use this book as the thing that makes those items possible.

Turn the page. Start at the exam chapter if you do not know the test. Start at How to study if you know the test and keep studying wrong. Then open Part A.
'''

FRONT["exam"] = r'''# The GRE Mathematics Subject Test

The GRE Mathematics Subject Test is a paper-based multiple-choice exam of undergraduate mathematics. Recent administrations use on the order of **66 questions in 170 minutes**. There is **no calculator**. You will not be told which “chapter” a question belongs to. A question that looks like calculus may be linear algebra in disguise; a question that looks like algebra may be a counting argument.

## What is on it

ETS describes three large blocks. Treat the percentages as a compass, not a contract:

- **Calculus — about 50%.** Limits, derivatives, integrals, sequences and series, and a real amount of multivariable and vector calculus. This is why Parts E–I are not optional extras.
- **Algebra — about 25%.** Elementary algebra, linear algebra, number theory, and abstract algebra. “Algebra” on this exam includes groups, rings, and fields at the level of a first course, not only high-school factoring.
- **Additional topics — about 25%.** Discrete math, probability, statistics, real analysis, topology, geometry, complex analysis, numerical methods, and anything else ETS decides is fair game from a standard mathematics major.

The master checklist this book follows *expands* ETS’s short labels. ETS itself says its topic list is not exhaustive. That is why there are 1036 skills rather than a one-page syllabus.

## How the questions behave

GRE Math items are not homework exercises with a friendly “use the chain rule.” They are compressed. Typical shapes:

- A computation that is cheap if you see the identity and expensive if you expand everything.
- A definition check: which statement is true, which hypothesis is missing.
- A parameter problem: how many roots as $a$ varies, when a matrix becomes singular, when a series converges.
- A counterexample question: which of the following must be true? (Answer: none of the attractive ones.)
- A mixed question: a group of invertible $2\times 2$ matrices, or a generating function that is also a geometric series.

You get no partial credit. An almost-right integral that dropped a sign is worth as much as a blank: zero. That is why this book trains trap awareness as a skill, not as a sermon.

## Timing

170 minutes for about 66 questions is a little over **2.5 minutes each** if you treat them equally. You will not treat them equally.

A workable default:

- First 50–55 minutes: harvest every question you can do in under two minutes. Mark the rest.
- Middle hour: the questions that need a picture, a row reduction, or a short argument.
- Last 40–50 minutes: the hard mixed items, then a pass over flagged questions.
- Last 5 minutes: no blank answers if there is no penalty for guessing (confirm the current scoring rules before you sit; they have changed over the years). Fill remaining blanks only after you have used the time on problems you might actually get.

Speed without accuracy is how you score 70th percentile with 90th-percentile knowledge. Accuracy without speed is how you leave twelve questions blank. Part Y exists to fuse the two.

## What a perfect-score attempt feels like

You are not racing through novel mathematics. You are recognizing governing concepts, checking hypotheses, and computing cleanly. The person who scores at the top of the scale has:

- instant algebra (exponents, factoring, identities, inequalities);
- calculus that is both computational and theoretical (FTC, MVT, series tests, polar/parametric);
- linear algebra that can move from matrices to maps to eigenvalues without getting lost;
- enough algebra, analysis, and discrete math to not panic when the exam leaves the calculus comfort zone;
- a ruthless habit of not doing extra work.

That last one is a skill. Lesson M-1021 is “avoid over-solving.” It is Critical for a reason.
'''

FRONT["how-to-study"] = r'''# How to study this book

Reading mathematics is not the same as learning mathematics. The GRE does not ask whether you nodded along. It asks whether you can produce the next line on a blank page, under time, with the topic unnamed.

## The only method this book endorses

For each lesson:

1. **Read the “from zero” section once**, pencil in hand. Copy the definition. Do not highlight entire paragraphs.
2. **Cover the worked example** after the first two lines and finish it yourself. Uncover to check.
3. **Do the GRE-style problem timed** (6–8 minutes). Then read the solution as if it were a grading rubric.
4. **Do both drills on paper.** If you miss either, reset the lesson to mastery 1 and repeat the next day.
5. **Mark mastery honestly** in the reader. 3 means you could do a new problem of this type tomorrow morning, mixed among other topics.

If a lesson lists prerequisites, those lessons must already be at least mastery 2. Do not negotiate with the graph of knowledge. The GRE will not.

## Active recall, not re-reading

After a block of five to ten lessons, close the book and write:

- the definitions;
- the main theorems, including hypotheses;
- one example each.

If you cannot, you were touring the museum. Go back.

## Interleaving

The exam is interleaved. Your practice must become interleaved before test day.

- In Parts A–X, stay sequential until Level 2.
- Then mix: pick five IDs at random from previous parts and do one drill each, timed.
- Part Y is the exam gym. Do not enter it as a substitute for learning calculus. Enter it when calculus, algebra, and additional topics are already working.

## The error log

Keep a single notebook or file with four columns: **item**, **skill ID**, **what I did**, **the actual governing idea**. Every miss gets a row. Before you mark a skill as 3, that skill should not appear twice in the log for the same trap.

People who “do a lot of problems” without a log repeat the same three mistakes for months.

## Calculator abstinence

There is no calculator on the exam. Do every drill in this book by hand. Scientific notation, fraction arithmetic, and trigonometric exact values are not side quests; they are the operating system.

## How long is “thoroughly”?

Thoroughly means: every Critical skill at 3, every High skill at 3, every Medium skill at least at 2 and preferably 3, then official timed practice at target. It does not mean “I opened every page.” The mastery gates in Part Y are not motivational posters. They are exit criteria.

## If you get stuck

Stuck on a definition: copy it, then write a tiny example that satisfies it and a tiny example that violates it.

Stuck on a computation: restart with more space. Most algebra errors are cramped writing.

Stuck on a proof-flavored item: name the objects, name the hypotheses, name the conclusion, then pick a method (direct, contrapositive, contradiction, counterexample). Lesson M-716 through M-725 exist so you do not invent a method under the clock.
'''

FRONT["notation"] = r'''# Notation and conventions

Mathematics is a written language. Ambiguous writing is how you lose points you “knew.” This book uses standard undergraduate notation. When GRE choices use a different convention, the lesson will say so.

## Sets and numbers

- $\mathbb{N}$ — positive integers $1,2,3,\ldots$ unless a lesson explicitly includes $0$. If a problem is sensitive to this, it will say so. When in doubt, check whether $0$ is needed.
- $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ — integers, rationals, reals, complexes.
- $\emptyset$ — empty set. $A\subset B$ allows $A=B$ unless we say *proper*.
- $|A|$ — cardinality, or absolute value, or determinant, or modulus: the surrounding objects decide. Never assume.

## Functions and calculus

- $f: A\to B$ — function with domain $A$ and codomain $B$.
- $f(A)$ — image of a set. $f^{-1}(B)$ — preimage, which always exists; inverse function is extra structure.
- $\ln$ — natural logarithm. $\log$ on the GRE is often natural as well in analysis contexts; in elementary contexts it may be base 10. The lesson will not be coy.
- $\exp x = e^x$.
- $f'$ and $\dfrac{dy}{dx}$ are both used. Higher derivatives: $f''$, $f^{(n)}$.
- $\int f$ means an antiderivative; $\int_a^b f$ is a definite integral (a number).

## Linear algebra

- Vectors are columns unless a lesson is doing row space on purpose.
- $I$ is an identity matrix of whatever size the surrounding text fixed.
- $\ker T$, $\operatorname{im} T$, $\operatorname{rank} A$, $\operatorname{nullity} A$.
- Eigenvalues may be complex even when the matrix is real.

## Algebra

- Groups are written multiplicatively unless clearly additive ($\mathbb{Z}$, vector spaces).
- $H\le G$ subgroup, $H\trianglelefteq G$ normal.
- $R[x]$ polynomial ring. Ideals often $(a)$ for principal ideals.

## Analysis and topology

- $\varepsilon$, $\delta$, $N$ in the usual roles.
- $\overline{A}$ closure, $A^\circ$ interior, $\partial A$ boundary.
- Compact means open-cover compact. In $\mathbb{R}^n$, Heine–Borel identifies this with closed and bounded.

## Probability

- $P(A)$, $P(A\mid B)$.
- Random variables in capitals: $X$, $E[X]$, $\operatorname{Var}(X)$.
- PMF $p_X$, PDF $f_X$, CDF $F_X$.

## Exam writing

On scratch paper, box the quantity the question asked for. Many GRE misses are correct computations of the wrong object: the radius instead of the area, the eigenvector instead of the eigenvalue, $f'(c)$ instead of $f(c)$.
'''

FRONT["study-plan"] = r'''# Ten-phase study plan

This is the spine of a perfect-score attempt. Each phase has an exit criterion. Do not enter the next phase because you are bored. Enter it because you can pass the gate.

## Phase 1 — Algebraic fluency and precalculus (Parts A–D)

**Goal.** Manipulate expressions, functions, trigonometry, and complex numbers quickly with no calculator.

**Exit.** Random drills from A–D, mixed, timed: you are accurate and you do not stare at exponents, identities, or $a+bi$.

## Phase 2 — Single-variable calculus (Parts E–G)

**Goal.** Limits, derivatives, integrals, optimization, sequences, and series — routine and unfamiliar.

**Exit.** You can justify a limit, differentiate anything built from standard functions, integrate with a plan (sub, parts, partial fractions, trig), and test series without a decision tree you have to look up.

## Phase 3 — Linear algebra and ODEs (Parts J–K)

**Goal.** Row-reduce, reason about vector spaces and eigenvalues, solve standard ODEs.

**Exit.** A $3\times 3$ eigenproblem and a second-order linear ODE are both “just work,” not adventures.

## Phase 4 — Number theory and abstract algebra (Parts L–N)

**Goal.** Congruences, finite groups, homomorphisms, ideals, fields, standard theorem recognition.

**Exit.** You can run the Euclidean algorithm, apply Lagrange and the first isomorphism theorem, and not confuse units with zero-divisors.

## Phase 5 — Analysis and topology (Parts O–P)

**Goal.** Reason from definitions: convergence, continuity, compactness, connectedness, metric spaces.

**Exit.** You can write an $\varepsilon$-$N$ argument, know why $\mathbb{R}$ is complete, and use Heine–Borel and connectedness of intervals as tools, not slogans.

## Phase 6 — Discrete math (Parts Q–S)

**Goal.** Proofs, counting, recurrences, graphs, basic algorithms.

**Exit.** Inclusion-exclusion, generating functions at a basic level, and “is there an Euler circuit?” are fast.

## Phase 7 — Probability and statistics (Parts T–U)

**Goal.** Move between counting, distributions, expectation/variance, and elementary inference.

**Exit.** Linearity of expectation is a reflex. You can finish a Bayes problem and a CLT approximation without mixing up PMF and PDF.

## Phase 8 — Geometry and complex analysis (Parts V–W)

**Goal.** Analytic/vector geometry and core complex-analysis methods (Cauchy, residues at the recognition level).

**Exit.** You can compute a residue at a simple pole and find a point-plane distance without rummaging.

## Phase 9 — Numerical methods (Part X)

**Goal.** Recognize approximation, error, root-finding, and numerical integration.

**Exit.** You know what Newton’s method is doing, what “conditioning” means, and why Simpson is more accurate than trapezoid on smooth functions.

## Phase 10 — Mixed GRE mastery (Part Y)

**Goal.** Unseen mixed questions under full-test timing, with an explanation for every miss.

**Exit.** The mastery gates: Critical and High skills at Level 3, Medium at least at Level 2, official practice at target, a second timed test that holds, an error log without repeated traps, mixed sets at 90%+ under section timing.

Then sit the exam. Not a week after you “finished reading.” After the gates.
'''

# ---------------------------------------------------------------------------
# Part introductions
# ---------------------------------------------------------------------------

PARTS: dict[str, str] = {}

PARTS["A"] = r'''# Part A — Foundations & Algebraic Fluency

If calculus is half the GRE, algebra is the ground it stands on. This part is not “review for people who forgot high school.” It is the operating system of the entire exam: integers and rationals, exponents and logs, factoring, equations, inequalities, and the structure of polynomials.

A person who “knows calculus” but cannot factor $x^3-x$, complete a square, or solve a rational inequality will leak points in limits, integrals, series, linear algebra, and probability. The GRE will not pause while you repair arithmetic.

## What you will own by the end

- Exact arithmetic with integers, rationals, absolute values, floors, and bounds.
- Exponents and logarithms as inverse languages, including inequalities.
- Factoring, division, partial fractions, and identities as reflexes.
- Linear, quadratic, polynomial, rational, radical, and absolute-value equations *and* inequalities, including parameters.
- The named inequalities (AM-GM, Cauchy–Schwarz, triangle) as tools, not posters.
- Polynomials as objects: degree, roots, Vieta, factor and remainder theorems.

## How to study this part

Do not skip a skill because it looks elementary. Elementary and *fast* are different. The GRE’s algebra is elementary and fast. Work every drill without a calculator. When a later part says “prerequisites A.3,” it means this fluency is assumed in the time budget of a two-minute item.
'''

PARTS["B"] = r'''# Part B — Precalculus & Functions

A function is the GRE’s favorite object. Limits, derivatives, integrals, linear maps, random variables, and homomorphisms are all function stories with extra structure. If “function” still means “a formula you plug into,” this part is the repair.

You will learn what a function *is*, how domain and range actually work, injectivity and surjectivity as existence/uniqueness statements, composition and inverses, the standard families, sequences as functions on $\mathbb{N}$, and the first encounter with parametric and polar language.

## The GRE motion

The exam loves: piecewise definitions, $f(f(x))$, asking for the range of a composition, and graphs implied by algebra rather than drawn. It also loves sequences written recursively with a request for a closed form.

When you finish this part you should be able to look at a formula and say, without theatrics, where it is defined, whether it is one-to-one, what its inverse does, and how it transforms when you replace $x$ by $x-2$ or $2x$.
'''

PARTS["C"] = r'''# Part C — Trigonometry & Conics

Trigonometry on the GRE is not triangle word problems from geometry class. It is the unit circle, exact values, identities as rewriting tools, inverse-trig ranges, and the algebra of sine and cosine. Conics and coordinate geometry sit here because they are the same skill: equations that mean pictures, pictures that mean equations.

You need exact values at the standard angles the way you need $7\times 8=56$. You need the Pythagorean identities the way you need $a^2-b^2=(a-b)(a+b)$. Sum-to-product is how some integrals and some GRE limits die quickly.

Coordinate geometry is also how you avoid doing vector calculus with your hands tied: distance, slope, tangency, and a line meeting a circle are undergraduate reflexes.
'''

PARTS["D"] = r'''# Part D — Complex Numbers

Complex numbers are not a side topic. They are how polynomials actually factor, how eigenvalues actually live, how De Moivre turns powers into rotation, and how later complex analysis even makes sense.

Learn $a+bi$ until division by conjugates is boring. Then learn polar form until multiplication is “multiply moduli, add arguments.” Roots of unity are a GRE favorite because they sit at the intersection of algebra, geometry, and cyclotomic intuition.

You do not need contour integrals yet. You need to be unable to fear $i$.
'''

PARTS["E"] = r'''# Part E — Calculus I: Limits & Differentiation

This is the first of the two large calculus parts, and it is the beating heart of the exam. Limits are not a ritual before derivatives. They *are* the derivative, the integral, the sum of a series, and the definition of continuity.

You will learn limits from pictures and from $\varepsilon$-$\delta$, one-sided and infinite, squeeze theorem, the standard trig and exponential limits, and L’Hôpital as a tool with hypotheses rather than a reflex that eats all quotients.

Then derivatives: definition, geometry, the algebraic rules, implicit and logarithmic differentiation, every standard function, and the applications — extrema, concavity, related rates, MVT, linear approximation, Taylor polynomials as local models.

If you only have time to make one part bulletproof after foundations, this is a candidate. But do not lie to yourself that limits are “easy intuition.” The GRE will ask a limit that is an identity in disguise, or an $\varepsilon$-$\delta$ recognition, or a Taylor comparison.
'''

PARTS["F"] = r'''# Part F — Calculus II: Integration

Integration is the inverse problem of differentiation plus geometry plus accumulation. The GRE expects a toolkit, not a single trick: antiderivatives of the standard families, substitution, parts, partial fractions, trig integrals and trig substitutions, Riemann sums, the two halves of the Fundamental Theorem, area and volume, arc length, and improper integrals.

The skill is choosing the method in thirty seconds. That choice is itself trained: “is there a function and its derivative?” (substitution), “is it a product whose derivative-table is short?” (parts), “rational and degree issues?” (partial fractions).

Improper integrals are also series in disguise. Comparison for integrals is the same idea as comparison for series. Part G will assume you already speak this language.
'''

PARTS["G"] = r'''# Part G — Infinite Series

Sequences and series are where calculus becomes analysis on the GRE. You need both the computational tests and the definitions.

Convergence of sequences, monotone convergence, subsequences, Cauchy sequences, then series as sequences of partial sums. Geometric, telescoping, $p$-series, comparison, limit comparison, integral, alternating, ratio, root, absolute versus conditional, and the rearrangement warning.

Power series: radius and interval, term-by-term calculus, Taylor series you should know in your sleep ($e^x$, $\sin$, $\cos$, $1/(1-x)$, binomial). Uniform convergence appears at awareness level: enough to not interchange limits blindly.

A GRE series question is often decided in one observation: this is geometric; this is $p$ with $p\le 1$; the terms do not go to zero; the ratio test limit is $1$ so it told you nothing. Learn to hear that observation.
'''

PARTS["H"] = r'''# Part H — Multivariable Calculus

Several variables is not “Calculus I with extra letters.” Limits in $\mathbb{R}^n$ can fail along paths. Partial derivatives can exist without the function being differentiable. The gradient points to steepest ascent and is normal to level sets. The Hessian decides min/max/saddle. Lagrange multipliers handle constraints.

Multiple integrals are geometry plus Jacobians. Polar, cylindrical, and spherical are not optional culture: they are how some GRE integrals become one-liners.

By the end you should be able to set up a double integral in either order, change variables without losing $|\det D\Phi|$, and classify a critical point of $f(x,y)$ without confusing “$f_{xx}=0$” with a full Hessian test.
'''

PARTS["I"] = r'''# Part I — Vector Calculus

Vector calculus is the GRE’s favorite way to ask whether you understand the Fundamental Theorem in higher dimensions. Gradient, divergence, and curl are operators with meanings: steepest change, source density, local rotation. Line integrals measure work. Conservative fields are gradients, and path independence is the prize.

Green, Stokes, and the divergence theorem are one idea in three costumes: integrating a derivative over a region equals integrating the original thing over the boundary, with orientation.

The exam often asks you to *choose* the theorem that makes the computation short. That choice is a skill (M-384). Learn it as a skill, not as a vibe.
'''

PARTS["J"] = r'''# Part J — Differential Equations

ODEs on the GRE are mostly first-order methods and constant-coefficient second-order linear equations, with a taste of systems and Laplace.

You should classify an ODE (order, linear or not, autonomous), solve separable and first-order linear equations, recognize exact equations, and read a phase line. For second order: characteristic polynomial, the three root cases, undetermined coefficients, variation of parameters.

Systems connect to eigenvalues — which is why this part sits next to linear algebra in the study plan even though the letters are J then K. Laplace transforms are recognition-level: enough to see $L\{y'\}=sY-y(0)$.
'''

PARTS["K"] = r'''# Part K — Linear Algebra

Linear algebra is the other backbone. It is  a large Critical block: vectors, matrices, row reduction, vector spaces, linear maps, determinants, eigenvalues, inner products.

The GRE will not only ask you to multiply matrices. It will ask whether a list is independent, what the rank-nullity theorem implies about a $4\times 6$ matrix, whether a matrix is diagonalizable, what the determinant says about invertibility, and how a projection works.

Learn to move among four languages without translation lag: geometry of vectors, matrix computations, maps $T:V\to W$, and systems of equations. They are the same subject.

Inner products, Gram–Schmidt, least squares, and the spectral theorem for symmetric matrices are the end of the part. They are also how multivariable calculus and statistics keep making sense.
'''

PARTS["L"] = r'''# Part L — Number Theory

Elementary number theory on the GRE is divisibility, the Euclidean algorithm, congruences, Euler and Fermat, and linear Diophantine equations, with awareness of quadratic residues, primitive roots, Möbius, and continued fractions.

This is computational theory. You should be able to find $\gcd(1239,168)$, invert $7$ mod $26$ when it exists, solve a system with the Chinese remainder theorem, and compute $\phi(n)$ from a factorization.

Do not study number theory as a pile of named theorems. Study it as a machine: reduce, invert, exponentiate, obstruct.
'''

PARTS["M"] = r'''# Part M — Group Theory

Groups are the GRE’s abstract-algebra workhorse. Binary operations, axioms, subgroups, cyclic groups, orders, permutations, Lagrange, homomorphisms, kernels, quotients, and the first isomorphism theorem.

A typical item: the order of an element in $S_n$, whether a subgroup is normal, the kernel of a map $\mathbb{Z}\to\mathbb{Z}_n$, or the classification of finite abelian groups as a recognition fact.

Write lots of tiny examples: $U(8)$, $S_3$, $\mathbb{Z}_6$, $D_4$. Abstraction without examples is how people confuse “abelian” with “cyclic.”
'''

PARTS["N"] = r'''# Part N — Rings, Modules & Fields

Rings add a second operation. You need domains, units, zero-divisors, ideals, quotients, and polynomial rings over fields, including irreducibility tests. Modules are “vector spaces over rings”; fields are where every nonzero element is a unit.

Finite fields $\mathbb{F}_p$ and $\mathbb{F}_{p^n}$ appear. Extension degree and minimal polynomials appear. You do not need Galois theory as a course; you need to know what a splitting field is for and why irreducible polynomials matter.

The GRE loves $\mathbb{Z}/n\mathbb{Z}$ as a ring: when it is a field, when it has zero-divisors, what its units are. That is Parts L and N talking to each other.
'''

PARTS["O"] = r'''# Part O — Real Analysis

Analysis is calculus with hypotheses and proofs. Completeness of $\mathbb{R}$, suprema, the Archimedean property, density of rationals, then sequences and series again — this time as theorems, not only tests.

Continuity from $\varepsilon$-$\delta$ and from sequences, uniform continuity, IVT and EVT as theorems with proofs you could sketch. Differentiation: MVT, Taylor with remainder, Darboux. Riemann integration: definition, who is integrable, FTC.

On the GRE this often looks like “which statement is always true?” The person who studied only computational calculus guesses. The person who studied this part eliminates.
'''

PARTS["P"] = r'''# Part P — Topology

Topology on the GRE is metric and first-course general topology: open and closed sets, interior, closure, boundary, completeness, compactness, connectedness, continuous maps, Heine–Borel.

You will not be asked to classify surfaces. You will be asked whether a set is closed, whether a continuous image of a compact set is compact, whether $\mathbb{Q}$ is a complete metric space under the usual metric (no), and whether connectedness is preserved by continuous maps (yes).

Definitions are the whole game. Learn them as if they were computational algorithms — because on a multiple-choice exam, they are.
'''

PARTS["Q"] = r'''# Part Q — Logic, Sets & Proof

This part is how you read every other part. Propositional and predicate logic, proof methods, set algebra, relations, functions again (now as set-theoretic objects), countable versus uncountable.

If you cannot negate a quantified statement, you cannot understand “for every $\varepsilon>0$ there exists $\delta>0$.” If you cannot prove by contradiction or induction, number theory and algebra become theater.

Treat this part as athletic training, even if you already “know” it. The GRE’s proof-flavored items are logic items.
'''

PARTS["R"] = r'''# Part R — Combinatorics

Counting is probability without the word probability, and it is generating functions, and it is binomial coefficients that also appear in Taylor series and $(1+x)^n$.

Addition and multiplication principles, permutations and combinations, stars and bars, inclusion-exclusion, pigeonhole, recurrences. The GRE will ask a counting problem that looks like a story and is actually “choose $k$ with repetition allowed.”

Learn to name the model before you write $n!$. Wrong model, clean arithmetic, wrong answer.
'''

PARTS["S"] = r'''# Part S — Graph Theory & Algorithms

Graphs are discrete geometry: vertices, edges, degrees, the handshaking lemma, trees, Euler versus Hamilton, coloring, planarity, adjacency matrices, BFS/DFS, Big-O.

Euler’s formula $v-e+f=2$ for connected planar graphs is a GRE-friendly fact. Trees having $n-1$ edges is another. “Hamiltonian” is harder than “Eulerian”; the exam knows that and will test whether you do.

Algorithms appear as ideas: Euclidean algorithm as complexity, growth rates, recursion versus iteration. You are not being hired as a programmer. You are being asked whether $O(n^2)$ means anything to you.
'''

PARTS["T"] = r'''# Part T — Probability

Probability is the GRE’s applied analysis: axioms, conditionals, Bayes, discrete and continuous random variables, expectation and variance, named distributions, limit theorems, MGFs.

Linearity of expectation does not need independence. Variance of a sum does. Indicator variables turn ugly counting into easy expectation. These are not cute tricks; they are how hard-looking problems collapse.

Know the named distributions as models: Bernoulli as a coin, binomial as a sum of i.i.d. coins, geometric as waiting, Poisson as rare events, exponential as memoryless waiting time, normal as the CLT’s attractor.
'''

PARTS["U"] = r'''# Part U — Mathematical Statistics

Statistics here is still mathematics: estimators, bias, likelihood, confidence intervals, tests, $t$, chi-square, $F$, and the linear model as least squares.

You will not be running SPSS. You will be asked what unbiased means, what a Type I error is, or how the normal equations look. Connect this part to Part K (least squares) and Part T (sampling distributions via CLT).
'''

PARTS["V"] = r'''# Part V — Geometry

Geometry on the GRE is Euclidean facts plus analytic and vector methods. Angles, congruence, similarity, triangle centers, circles, 3D volumes, and the vector geometry of lines and planes.

Pictures are allowed and recommended. A GRE geometry item that you try to do with pure algebra often hides a similar-triangle one-liner. Conversely, a pretty picture with no coordinates can hide a vector projection.

Own both languages. Lesson M-999 exists so you will switch on purpose.
'''

PARTS["W"] = r'''# Part W — Complex Analysis

Complex analysis is the prize for having learned Parts D and O. Holomorphic functions, Cauchy–Riemann, contour integrals, Cauchy’s theorem and formula, Laurent series, singularities, residues.

The GRE typically stays at recognition and standard computations: is $f$ holomorphic, residue at a simple pole, Cauchy formula for a derivative. You do not need a semester of isolated-singularity classification as an art. You need the definitions and the two or three computations that show up.
'''

PARTS["X"] = r'''# Part X — Numerical Analysis

Numerical analysis is what happens when analysis meets finite arithmetic: error, conditioning, stability, bisection, Newton, interpolation, trapezoid and Simpson, Euler for ODEs.

The exam asks ideas more often than long computations: what Newton is iterating, why a problem is ill-conditioned, that rounding is not truncation. Treat this part as vocabulary plus a few algorithms you could carry out for two steps by hand.
'''

PARTS["Y"] = r'''# Part Y — Mixed GRE Problem-Solving

This part is not more content. It is the exam itself: recognizing the governing concept, checking hypotheses, switching representations, avoiding traps, using multiple-choice structure, pacing, and training on hard mixed items.

You may not skip here from Part A. You also may not skip this part because you “already know the math.” Knowing the math and scoring it are different skills. The checklist puts these items at Critical because perfect-score attempts fail here: people over-solve, ignore hypotheses, or run out of time with twelve blanks.

The last lessons are gates. They are how you know you are done.
'''

GRE_WEIGHT = {
    "A": "Algebraic fluency is not a listed ETS bucket of its own, but it is the cost of every calculus and algebra item. Expect it to be invisible when you have it and fatal when you do not.",
    "B": "Functions and precalculus appear inside calculus items constantly: domains of compositions, inverses, piecewise definitions, sequences.",
    "C": "Trigonometry appears in calculus, geometry, and as standalone identity/equation items. Exact values and identities are speed.",
    "D": "Complex numbers appear in algebra, polynomials, eigenvalues, and as a bridge to Part W.",
    "E": "This is the core of the calculus half of the exam. Limits, derivatives, and applications are everywhere.",
    "F": "Integrals, FTC, and applications are first-class GRE citizens. Improper integrals feed series.",
    "G": "Series tests and Taylor series are standard GRE calculus. Do not treat this part as optional analysis.",
    "H": "Multivariable calculus is explicitly in the calculus portion: partials, gradients, multiple integrals, Jacobians.",
    "I": "Vector calculus (Green/Stokes/divergence) appears less often than single-variable calculus but is a high-leverage discriminator.",
    "J": "ODEs appear as additional or calculus-adjacent items: separable, linear first order, characteristic equations.",
    "K": "Linear algebra is a large share of the algebra portion. Rank, kernels, eigenvalues, and determinants are exam staples.",
    "L": "Number theory is additional-topics / algebra: congruences, Euler, CRT.",
    "M": "Group theory is the main abstract-algebra GRE diet: orders, Lagrange, homomorphisms.",
    "N": r"Rings and fields appear as recognition and finite examples, especially $\mathbb{Z}/n\mathbb{Z}$ and $F[x]$.",
    "O": "Real analysis items are often ‘which statement is true?’ definition checks inside additional topics.",
    "P": "Topology appears as compactness, connectedness, open/closed, Heine–Borel.",
    "Q": "Logic and proof are how other items are worded. Counting and analysis both depend on quantifiers.",
    "R": "Combinatorics is additional topics and also probability setup.",
    "S": "Graph theory is additional topics: trees, Euler, handshaking, planarity.",
    "T": "Probability is a solid additional-topics block: Bayes, expectation, named distributions, CLT.",
    "U": "Statistics is lighter than probability but bias, MLE, and tests do appear.",
    "V": "Geometry is additional topics plus analytic geometry inside calculus/algebra items.",
    "W": "Complex analysis is additional topics: Cauchy–Riemann, residues at a basic level.",
    "X": "Numerical methods are additional topics: Newton, error, quadrature recognition.",
    "Y": "This is not content weight; it is how every weighted item is actually scored under a clock.",
}

SECTION_NAMES = {s["letter"]: s["section"] for s in CATALOG}

from skill_math import TOPIC_THEORY, core_for  # noqa: E402


def prev_next(i: int):
    prev = CATALOG[i - 1] if i > 0 else None
    nxt = CATALOG[i + 1] if i + 1 < len(CATALOG) else None
    return prev, nxt


def topic_index(letter: str) -> dict[str, list]:
    out: dict[str, list] = {}
    for s in CATALOG:
        if s["letter"] == letter:
            out.setdefault(s["topic"], []).append(s)
    return out


def expand_lesson(skill: dict, i: int) -> str:
    core = core_for(skill)
    prev, nxt = prev_next(i)
    title = skill["title"]
    topic = skill["topic"]
    letter = skill["letter"]
    prereq = skill.get("prerequisites") or "none — this is ground floor"
    recon = skill.get("reconstructed")
    theory = TOPIC_THEORY.get(topic, "")
    why_p = PRIORITY_WHY.get(skill["priority"], "")
    gre = GRE_WEIGHT.get(letter, "")
    traps = "\n".join(f"- {t}" for t in core["traps"])
    idea = core.get("idea") or f"The skill **{title}** is one exact move inside *{topic}*."
    how = core.get("how") or "Write the hypotheses, apply the move, check the conclusion against the question asked."
    hook = core.get("hook") or f"This lesson isolates **{title}** and trains it until it is automatic."
    next_line = (
        f"Next lesson: [{nxt['id']}](/lesson/{nxt['id']}) — {nxt['title']}."
        if nxt
        else "You have reached the end of the checklist. Return to missed drills."
    )
    prev_line = (
        f"Previous: [{prev['id']}](/lesson/{prev['id']}) — {prev['title']}."
        if prev
        else "Previous: [Study plan](/front/study-plan)."
    )
    recon_note = (
        "\n> This skill ID sat on a page break in the source checklist; "
        "the title is reconstructed from the surrounding topic so the book stays complete.\n"
        if recon
        else ""
    )
    theory_block = (
        f"\n### Landscape of *{topic}*\n\n{theory}\n"
        if theory
        else ""
    )

    return f'''# Lesson {skill["id"]} — {md_escape_title(title)}

Part {letter}. {skill["section"]} · **{topic}** · {skill["priority"]}

Prerequisites: `{prereq}`.
{recon_note}

{hook}

{why_p} {gre}

## 1. Why this skill exists

If you cannot do **{title}**, every later item that secretly uses it becomes a two-minute panic. The GRE will not name the skill. It will drop you into a computation or a “which statement is true?” and wait.

## 2. From zero
{theory_block}
### This skill, specifically

{idea}

You are not learning the whole topic again. You are learning the exact move named in the title. Neighboring lessons exist; use them if a word here is still foreign, then come back.

## 3. Precise statement

{core["stmt"]}

Copy that statement onto paper and replace each symbol with a tiny example. A definition you cannot instantiate is a definition you do not have.

## 4. How a working mathematician uses it

{how}

On the exam, this should feel like a reflex: see the pattern, apply the move, check hypotheses, box the quantity asked for.

## 5. Worked example

**Problem.** {core["exq"]}

**Solution.** {core["exa"]}

Now cover the solution and redo it. If you cannot, you are still in Section 2.

## 6. GRE-style problem

**Problem.** {core["gq"]}

**Solution.** {core["ga"]}

Notice what was *not* done: no extra theory, no calculator, no essay. The governing idea, then the computation.

## 7. Traps that cost points

{traps}

## 8. Drills

Work these closed-book. Then check.

**Drill 1.** {core["q1"]}

**Solution.** {core["a1"]}

Cover that solution, redo the drill on paper, then continue.

**Drill 2.** {core["q2"]}

**Solution.** {core["a2"]}

## 9. Lock it in

You own this skill when you can do Drill 1 and Drill 2 tomorrow, mixed among unrelated problems, in under five minutes each, with the traps named in Section 7 avoided on purpose.

{prev_line}

{next_line}
'''


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def main() -> None:
    (CONTENT / "front").mkdir(parents=True, exist_ok=True)
    (CONTENT / "parts").mkdir(parents=True, exist_ok=True)
    (CONTENT / "lessons").mkdir(parents=True, exist_ok=True)

    for slug, body in FRONT.items():
        write_text(CONTENT / "front" / f"{slug}.md", body)

    for letter, body in PARTS.items():
        skills = [s for s in CATALOG if s["letter"] == letter]
        topics = topic_index(letter)
        toc = "\n".join(
            f"- **{topic}** — " + ", ".join(f"[{s['id']}](/lesson/{s['id']})" for s in items)
            for topic, items in topics.items()
        )
        extra = f"\n\n## Lessons in this part ({len(skills)})\n\n{toc}\n"
        write_text(CONTENT / "parts" / f"{letter}.md", body + extra)

    missing = []
    for i, skill in enumerate(CATALOG):
        try:
            md = expand_lesson(skill, i)
        except Exception as e:
            missing.append((skill["id"], str(e)))
            raise
        write_text(CONTENT / "lessons" / f"{skill['id']}.md", md)

    print(f"Wrote {len(FRONT)} front pages, {len(PARTS)} parts, {len(CATALOG)} lessons.")
    if missing:
        print("MISSING", missing)


if __name__ == "__main__":
    main()

