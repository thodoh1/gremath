"""Unique worked mathematics for skills M-022 through M-1036."""

from __future__ import annotations

import json
from pathlib import Path

from skill_math import C, TOPIC_HOW, TOPIC_THEORY


def _put(out: dict, n: int, stmt: str, exq: str, exa: str, gq: str, ga: str,
         trap: str, q1: str, a1: str, q2: str, a2: str, hook: str = "") -> None:
    key = f"M-{n:03d}" if n < 1000 else f"M-{n}"
    # idea/how filled later from topic
    out[key] = (stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2, hook)


def _raw() -> dict[str, tuple]:
    o: dict[str, tuple] = {}

    def p(n, stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2, hook=""):
        _put(o, n, stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2, hook)
    # A algebraic manipulation
    p(22, r"If a common factor $c$ divides every term of an expression, you may write the expression as $c$ times a simpler expression: $ca+cb=c(a+b)$. This is the distributive law read backwards.",
      r"Factor $6x^3-9x^2+12x$.", r"$3x(2x^2-3x+4)$.",
      r"$x^n-x^{n-1}$ factors as", r"$x^{n-1}(x-1)$ for integer $n\ge 1$.",
      r"Factoring $x$ out of $x-1$ and calling the rest $1$ — that is $x(1-1/x)$, which changes the domain.",
      r"Factor $15a^2b+25ab^2$.", r"$5ab(3a+5b)$.",
      r"Factor $n(n+1)+2(n+1)$.", r"$(n+1)(n+2)$.")
    p(23, r"$a^2-b^2=(a-b)(a+b)$. This is the GRE’s favorite one-step rewrite.",
      r"Factor $9x^2-16$.", r"$(3x-4)(3x+4)$.",
      r"$2^{10}-1$ equals", r"$(2^5-1)(2^5+1)=31\cdot 33=1023$, or keep factoring $2^{10}-1=(2-1)(2^9+\cdots+1)=1023$.",
      r"Writing $a^2+b^2=(a+b)(a-b)$.",
      r"Factor $x^4-16$.", r"$(x^2-4)(x^2+4)=(x-2)(x+2)(x^2+4)$.",
      r"Simplify $\dfrac{x^2-9}{x-3}$ for $x\neq 3$.", r"$x+3$.")
    p(24, r"$a^3-b^3=(a-b)(a^2+ab+b^2)$ and $a^3+b^3=(a+b)(a^2-ab+b^2)$. The quadratic factors are usually irreducible over $\mathbb{R}$.",
      r"Factor $x^3-8$.", r"$(x-2)(x^2+2x+4)$.",
      r"$8x^3+27$ factors as", r"$(2x+3)(4x^2-6x+9)$.",
      r"Stopping after $a-b$ and forgetting the quadratic, or writing $a^2-ab+b^2$ as $(a-b)^2$.",
      r"Factor $y^3+1$.", r"$(y+1)(y^2-y+1)$.",
      r"Divide $x^3-27$ by $x-3$.", r"$x^2+3x+9$.")
    p(25, r"Completing the square: $x^2+bx=(x+b/2)^2-(b/2)^2$. For $ax^2+bx+c$, factor $a$ out of the $x$ terms first. This produces vertex form and is how the quadratic formula is derived.",
      r"Write $x^2+6x+5$ as a square plus constant.", r"$(x+3)^2-4$.",
      r"The minimum of $x^2-4x+7$ is", r"$(x-2)^2+3$, minimum $3$ at $x=2$.",
      r"Forgetting to factor $a$ first when $a\neq 1$.",
      r"Complete the square for $2x^2+8x+1$.", r"$2(x+2)^2-8+1=2(x+2)^2-7$.",
      r"Solve $x^2+2x-2=0$ by completing the square.", r"$(x+1)^2=3$, $x=-1\pm\sqrt{3}$.")
    p(26, r"Polynomial long division: $f=qg+r$ with $\deg r<\deg g$ (or $r=0$). Algorithm: lead$(f)/$lead$(g)$ is the next term of $q$; subtract and repeat.",
      r"Divide $x^3+2x+1$ by $x+1$.", r"$x^2-x+3$ remainder $-2$, since $(x+1)(x^2-x+3)-2=x^3+2x+1$.",
      r"The remainder when $x^3-x$ is divided by $x-2$ is", r"By remainder theorem (next skill) $8-2=6$, matching long division.",
      r"Stopping when a remainder has degree equal to the divisor.",
      r"Divide $x^2+3x+2$ by $x+2$.", r"$x+1$ remainder $0$.",
      r"Divide $2x^3-x$ by $x^2+1$.", r"$2x$ remainder $-2x-x=-3x$. Wait: $(x^2+1)(2x)=2x^3+2x$, subtract from $2x^3-x$ gives $-3x$. Remainder $-3x$.")
    p(27, r"Synthetic division is long division by the monic linear $x-c$, compressed. The last number is $f(c)$ (remainder theorem).",
      r"Divide $x^3-2x+4$ by $x-1$ synthetically.", r"Coefficients $1,0,-2,4$. Bring down $1$; $1,1,-1,3$. Quotient $x^2+x-1$, remainder $3$.",
      r"Synthetic division by $x+2$ uses $c=$", r"$-2$, because $x+2=x-(-2)$.",
      r"Using $c=2$ when dividing by $x+2$.",
      r"Divide $x^2-9$ by $x-3$.", r"Quotient $x+3$, remainder $0$.",
      r"Find $f(2)$ for $f(x)=x^3-4x+1$ by synthetic division.", r"$8-8+1=1$.")
    p(28, r"A rational expression $p/q$ (polynomials) is defined where $q\neq 0$. Simplify by canceling common factors, never common terms. The simplified formula may have a larger apparent domain; the original domain still governs.",
      r"Simplify $\dfrac{x^2-1}{x^2-2x+1}$ and state the domain of the original.",
      r"$\dfrac{(x-1)(x+1)}{(x-1)^2}=\dfrac{x+1}{x-1}$ for $x\neq 1$. Original also needs $x\neq 1$ only (double root). Domain $\mathbb{R}\setminus\{1\}$.",
      r"$\dfrac{x^2-4}{x-2}$ at $x=2$ is", r"undefined, even though the simplified $x+2$ would be $4$. Removable discontinuity.",
      r"Canceling $x$ in $\dfrac{x+2}{x+3}$.",
      r"Domain of $\dfrac{1}{x^2-5x+6}$.", r"$x\neq 2,3$.",
      r"Simplify $\dfrac{x^3-x}{x}$.", r"$x^2-1$ for $x\neq 0$.")
    p(29, r"Partial fractions: a proper rational function decomposes into a sum of terms whose denominators are the irreducible factors of $q$. Linear factors give $A/(x-r)$; repeated $(x-r)^k$ give terms up to $A_k/(x-r)^k$; irreducible quadratics give $(Bx+C)/(x^2+\cdots)$.",
      r"Decompose $\dfrac{1}{x(x-1)}$.", r"$\dfrac{A}{x}+\dfrac{B}{x-1}$, $A=-1$, $B=1$, so $\dfrac{1}{x-1}-\dfrac{1}{x}$.",
      r"$\displaystyle\int\dfrac{1}{x^2-1}\,dx$ begins with", r"$\dfrac{1/2}{x-1}-\dfrac{1/2}{x+1}$.",
      r"Using an improper decomposition without polynomial division first.",
      r"Decompose $\dfrac{x+3}{(x+1)^2}$.", r"$\dfrac{A}{x+1}+\dfrac{B}{(x+1)^2}=\dfrac{1}{x+1}+\dfrac{2}{(x+1)^2}$.",
      r"Why is $\dfrac{x^2}{x-1}$ not ready for partial fractions?", r"Degree numerator $\ge$ degree denominator; divide first.")
    p(30, r"Algebraic identities are equalities of polynomials (or rational functions on their domains): $(a+b)^2=a^2+2ab+b^2$, $(a+b)^3$, $a^3\pm b^3$, and the difference of squares. They are rewriting licenses.",
      r"Expand $(x+2)^3$.", r"$x^3+6x^2+12x+8$.",
      r"$(x+y)^2-(x-y)^2$ simplifies to", r"$4xy$.",
      r"Expanding $(a+b)^2$ as $a^2+b^2$.",
      r"Factor $x^2+2xy+y^2-z^2$.", r"$(x+y-z)(x+y+z)$.",
      r"Show $(1+x)(1-x+x^2)=1+x^3$.", r"Direct expansion, or $a=1$, $b=x$ in $a^3+b^3$.")
    p(31, r"Substitution replaces a repeated blob by a letter. Elimination removes a variable between equations by addition or substitution. Both are changes of coordinates on the problem.",
      r"Solve $x+y=5$, $x-y=1$.", r"Add: $2x=6$, $x=3$, $y=2$.",
      r"To integrate $(2x+1)^9$, the substitution is", r"$u=2x+1$, $du=2\,dx$.",
      r"Substituting and forgetting to back-substitute.",
      r"Solve $u=x+1/x$, express $x^2+1/x^2$.", r"$u^2-2$.",
      r"Eliminate $t$ from $x=t+1$, $y=t^2$.", r"$y=(x-1)^2$.")
    p(32, r"A parameter is a letter treated as known. You may cancel a factor involving a parameter only after splitting cases where that factor is zero. “Illegal cancellation” is dividing by an expression that might be zero.",
      r"Simplify $\dfrac{(a-1)(x+2)}{a-1}$ as a function of $a$.",
      r"If $a\neq 1$, it is $x+2$. If $a=1$, the original is $0/0$ undefined (or $0$ over $0$).",
      r"The equation $(k-2)x=k-2$ has",
      r"If $k\neq 2$, $x=1$; if $k=2$, every $x$ is a solution. Cancellation would miss the all-$x$ case.",
      r"Dividing by $x$ in $x^2=x$ and losing $x=0$.",
      r"Solve $ax=a$ for $x$ in terms of $a$.", r"$x=1$ if $a\neq 0$; if $a=0$, all $x$ work.",
      r"For which $t$ is $\dfrac{t^2-1}{t-1}$ equal to $t+1$?", r"All $t\neq 1$. At $t=1$ the left is undefined.")

    # A equations 33-47
    p(33, r"A linear equation $ax+b=0$ with $a\neq 0$ has unique solution $x=-b/a$. If $a=0$ and $b\neq 0$, empty; if $a=b=0$, all $x$.",
      r"Solve $3x-7=5$.", r"$x=4$.",
      r"$kx+3=3$ has a unique solution iff", r"$k\neq 0$. If $k=0$ it is an identity.",
      r"Moving terms and flipping a sign.",
      r"Solve $\dfrac{x-1}{2}=4$.", r"$x=9$.",
      r"Solve $0\cdot x=2$.", r"No solution.")
    p(34, r"A quadratic $ax^2+bx+c=0$ with $a\neq 0$ has discriminant $\Delta=b^2-4ac$. Roots $\dfrac{-b\pm\sqrt{\Delta}}{2a}$ when $\Delta\ge 0$ in $\mathbb{R}$. Completing the square and factoring are equivalent methods.",
      r"Solve $x^2-5x+6=0$.", r"$(x-2)(x-3)=0$, $x=2,3$.",
      r"The number of real roots of $x^2+x+1=0$ is", r"$0$, because $\Delta=1-4=-3<0$.",
      r"Forgetting $\pm$, or dividing by $a$ incorrectly.",
      r"Solve $2x^2-3x-2=0$.", r"$(2x+1)(x-2)=0$, $x=-1/2$ or $2$.",
      r"For which $k$ does $x^2-kx+1=0$ have a double root?", r"$k^2=4$, $k=\pm 2$.")
    p(35, r"Polynomial equations $p(x)=0$ are solved by factoring (rational root theorem, grouping) down to linears and quadratics over $\mathbb{R}$. A degree-$n$ polynomial has at most $n$ real roots, counting multiplicity, and exactly $n$ complex roots.",
      r"Solve $x^3-x=0$.", r"$x(x-1)(x+1)=0$, $x=0,\pm 1$.",
      r"$x^3=x$ has how many real solutions?", r"Three: $-1,0,1$.",
      r"Assuming a cubic always has three distinct real roots.",
      r"Solve $x^3+x^2-x-1=0$.", r"$(x+1)(x^2-1)=0$ wait: $x^2(x+1)-(x+1)=(x+1)(x^2-1)=(x+1)^2(x-1)$. Roots $-1$ (mult 2) and $1$.",
      r"How many real roots has $x^4+1=0$?", r"Zero. (Four complex.)")
    p(36, r"A rational equation $p/q=0$ is $p=0$ and $q\neq 0$. If $p/q=r/s$, cross-multiply after noting $q,s\neq 0$, then exclude extraneous roots that zero a denominator.",
      r"Solve $\dfrac{x}{x-1}=2$.", r"$x=2(x-1)$, $x=2$. Check: denominator $1\neq 0$.",
      r"$\dfrac{1}{x}+\dfrac{1}{x-1}=0$ has solution", r"$x-1+x=0$, $x=1/2$. Both denominators nonzero.",
      r"Keeping a root that makes a denominator zero.",
      r"Solve $\dfrac{x+1}{x}=\dfrac{x}{x+1}$.", r"$(x+1)^2=x^2$, $2x+1=0$, $x=-1/2$.",
      r"Solve $\dfrac{x^2-1}{x-1}=0$.", r"$x=-1$ only ($x=1$ excluded).")
    p(37, r"A radical equation isolates a root and raises both sides to a power. This can create extraneous solutions. Always substitute back. Even roots require nonnegative radicands.",
      r"Solve $\sqrt{x+3}=x-3$.", r"Domain $x\ge -3$ and $x-3\ge 0$ so $x\ge 3$. Square: $x+3=(x-3)^2=x^2-6x+9$, $0=x^2-7x+6=(x-1)(x-6)$. Keep $x=6$.",
      r"$\sqrt{x}=-1$ has", r"no real solution.",
      r"Squaring and not checking; also $\sqrt{x^2}=x$ instead of $|x|$.",
      r"Solve $\sqrt{2x-1}=3$.", r"$2x-1=9$, $x=5$.",
      r"Solve $\sqrt{x}+\sqrt{x-1}=1$.", r"Isolate, square carefully; solution $x=1$.")
    p(38, r"$|A|=k$ with $k>0$ means $A=k$ or $A=-k$. $|A|=|B|$ means $A=B$ or $A=-B$. Always split on the expressions inside, or use cases on the real line.",
      r"Solve $|x-2|=|x+4|$.", r"$x-2=x+4$ impossible, or $x-2=-(x+4)= -x-4$, $2x=-2$, $x=-1$.",
      r"$|2x+1|=0$ has", r"one solution $x=-1/2$.",
      r"Writing $|A|=k$ as $A=\pm k$ when $k<0$ (empty).",
      r"Solve $|3x-1|=5$.", r"$x=2$ or $x=-4/3$.",
      r"Solve $|x|+|x-1|=1$.", r"The sum is $1$ on $[0,1]$.")
    p(39, r"A linear system $A\mathbf{x}=\mathbf{b}$ has either no solution, one solution, or infinitely many. Two equations in two unknowns: substitution, elimination, or matrices. Parallel lines (inconsistent) vs coincident (dependent) vs intersecting.",
      r"Solve $x+y=3$, $2x-y=0$.", r"$x=1$, $y=2$.",
      r"The system $x+y=1$, $2x+2y=3$ has", r"no solution (inconsistent).",
      r"Declaring “no solution” when the second equation is a multiple of the first.",
      r"Solve $x-2y=4$, $3x+y=1$.", r"$x=6/7$, $y=-11/7$. Wait: from first $x=4+2y$, $3(4+2y)+y=1$, $12+6y+y=1$, $7y=-11$, $y=-11/7$, $x=4-22/7=6/7$.",
      r"For which $k$ is $x+y=1$, $2x+2y=k$ consistent?", r"$k=2$.")
    p(40, r"Nonlinear systems are solved by substitution, factoring, or subtracting to factor. Circles and lines: substitute. Two circles: subtract to get the radical axis (a line).",
      r"Solve $x^2+y^2=5$, $y=x+1$.", r"$x^2+(x+1)^2=5$, $2x^2+2x-4=0$, $x^2+x-2=0$, $(x+2)(x-1)=0$, $x=-2,1$ with $y=-1,2$.",
      r"$xy=6$ and $x+y=5$ give $x,y$ as", r"roots of $t^2-5t+6=0$, so $2$ and $3$.",
      r"Losing a sign when substituting $y=\pm\sqrt{\cdot}$.",
      r"Solve $x^2+y=3$, $x+y=1$.", r"$y=1-x$, $x^2+1-x=3$, $x^2-x-2=0$, $x=2$ or $-1$.",
      r"How many real solutions has $x^2+y^2=1$, $x^2+y^2=4$?", r"Zero.")
    p(41, r"A linear inequality $ax+b>0$ reverses when multiplied by a negative. Solution is a ray (or all $\mathbb{R}$, or empty). Compound inequalities are intersections.",
      r"Solve $1-2x\ge 5$.", r"$-2x\ge 4$, reverse: $x\le -2$.",
      r"$-3x<6$ is equivalent to", r"$x>-2$.",
      r"Forgetting to reverse when multiplying by $-1$.",
      r"Solve $3(x-1)<x+5$.", r"$3x-3<x+5$, $2x<8$, $x<4$.",
      r"Solve $-1<2x+1\le 5$.", r"$-1<x\le 2$.")
    p(42, r"A quadratic inequality $ax^2+bx+c>0$ is read from a sign chart of the parabola: roots divide the line; the leading coefficient decides the outside signs.",
      r"Solve $x^2-x-6<0$.", r"$(x-3)(x+2)<0$, so $x\in(-2,3)$.",
      r"$x^2+1>0$ for", r"all real $x$.",
      r"Using the interval between roots when $a<0$ without flipping the picture.",
      r"Solve $x^2\ge 4$.", r"$x\le -2$ or $x\ge 2$.",
      r"Solve $-x^2+2x>0$.", r"$x(2-x)>0$, so $x\in(0,2)$.")
    p(43, r"Polynomial sign analysis: factor completely over $\mathbb{R}$, mark roots with multiplicity. The sign changes at a simple root and does not change at an even-multiplicity root.",
      r"Sign chart of $(x-1)^2(x+2)$.", r"Nonnegative for $x\ge -2$ except it is zero at $1$ and $-2$; strictly negative on $(-\infty,-2)$. Even multiplicity at $1$: no sign change.",
      r"$x^3-x$ is negative on", r"$(-1,0)$ wait: $x(x-1)(x+1)$. Negative on $(-1,0)$? Test $x=-0.5$: $(-0.5)(-1.5)(0.5)<0$? $(-0.5)(-1.5)>0$ times $0.5>0$. Actually negative on $(-\infty,-1)$ and $(0,1)$.",
      r"Changing sign at a double root.",
      r"Where is $x^2(x-3)$ negative?", r"$(-\infty,3)$ except $0$, i.e. $(-\infty,0)\cup(0,3)$. Wait: $x^2\ge 0$ always, so the product is negative iff $x-3<0$ and $x\neq 0$: $(-\infty,0)\cup(0,3)$.",
      r"Does $(x-1)^4(x+1)$ change sign at $x=1$?", r"No.")
    p(44, r"A rational inequality $p/q>0$ uses the same sign chart as $p\cdot q>0$ except zeros of $q$ are excluded (vertical asymptotes / holes), not solutions.",
      r"Solve $\dfrac{x-1}{x+2}>0$.", r"Critical points $-2,1$. Positive on $(-\infty,-2)\cup(1,\infty)$.",
      r"$\dfrac{x}{x-1}\ge 0$ includes", r"$x\le 0$ or $x>1$, not $x=1$. Includes $0$.",
      r"Including the pole as a closed endpoint.",
      r"Solve $\dfrac{1}{x}<1$.", r"$\dfrac{1-x}{x}<0$, so $x\in(-\infty,0)\cup(1,\infty)$.",
      r"Solve $\dfrac{x^2-1}{x}>0$.", r"$(x-1)(x+1)/x>0$; zeros $\pm 1$, pole $0$. Positive on $(-1,0)\cup(1,\infty)$.")
    p(45, r"$|A|<k$ with $k>0$ is $-k<A<k$. $|A|>k$ is $A<-k$ or $A>k$. Reduce to linear/quadratic inequalities after splitting.",
      r"Solve $|x-3|<2$.", r"$1<x<5$.",
      r"$|2x+1|\ge 5$ is", r"$x\le -3$ or $x\ge 2$.",
      r"$|A|<k$ for $k\le 0$: empty if $k<0$; only $A=0$ if $k=0$ and the inequality is $\le$.",
      r"Solve $|x|+2<5$.", r"$|x|<3$, $-3<x<3$.",
      r"Solve $|x-1|>|x+1|$.", r"This is distance to $1$ vs $-1$; true for $x<0$.")
    p(46, r"A parameter $a$ can change the number of solutions. Split on coefficients that might vanish, discriminants, and domain constraints. Report the solution set as a function of $a$.",
      r"How many real $x$ satisfy $x^2-2ax+a=0$ as $a$ varies?",
      r"$\Delta=4a^2-4a=4a(a-1)$. Two distinct real roots if $a<0$ or $a>1$; one if $a=0$ or $1$; none if $0<a<1$.",
      r"$(a-1)x=2$ has infinitely many solutions when", r"Never: if $a=1$ it is $0=2$ empty; else unique $x$. (Compare $0\cdot x=0$.)",
      r"Forgetting the case $a=0$ that drops degree.",
      r"For which $a$ does $|x-a|=a$ have two solutions?", r"$a>0$ (then $x=0$ or $x=2a$). If $a=0$, one solution; if $a<0$, empty.",
      r"Number of real solutions of $e^x=a$.", r"One if $a>0$, else zero.")
    p(47, r"Equality holds in a non-strict inequality at specified cases: AM-GM equality iff all terms equal; Cauchy iff vectors parallel; triangle iff dependent and same direction. For $f(x)\ge 0$, equality is the zero set.",
      r"When does $(x-1)^2\ge 0$ become equality?", r"Iff $x=1$.",
      r"AM-GM $ \frac{a+b}{2}\ge\sqrt{ab}$ for $a,b>0$ is equality iff", r"$a=b$.",
      r"Claiming equality never holds, or holds ‘in the limit’ when the theorem requires actual equality of terms.",
      r"Equality in $|x+y|=|x|+|y|$ holds when", r"$xy\ge 0$ (same sign, including zeros).",
      r"For $x+\dfrac{1}{x}\ge 2$ on $x>0$, equality at", r"$x=1$.")

    return o


def _pack(sk: dict, stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2, hook="") -> dict:
    idea_how = TOPIC_HOW.get(sk["topic"])
    if idea_how:
        idea, how = idea_how
    else:
        theory = TOPIC_THEORY.get(sk["topic"], "")
        idea = theory.split(".")[0] + "." if theory else sk["title"]
        how = "Apply the definition, then check hypotheses and the quantity asked for."
    return C(
        stmt,
        idea,
        how,
        exq,
        exa,
        gq,
        ga,
        [trap, "Skip checking a candidate in the original equation."],
        q1,
        a1,
        q2,
        a2,
        hook,
    )


def extra_cores() -> dict:
    catalog = json.loads(
        (Path(__file__).resolve().parents[1] / "content" / "catalog.json").read_text()
    )
    by_id = {s["id"]: s for s in catalog}
    by_n = {s["n"]: s for s in catalog}
    out: dict = {}
    for key, tup in _raw().items():
        stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2, hook = tup
        out[key] = _pack(by_id[key], stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2, hook)
    from all_facts import facts as facts_a
    from complete_facts import facts as facts_b
    from rest_c import facts as facts_c
    from rest_more import facts as facts_m

    for loader in (facts_a, facts_b, facts_c, facts_m):
        for n, f in loader().items():
            sk = by_n[n]
            out[sk["id"]] = _pack(
                sk, f["stmt"], f["exq"], f["exa"], f["gq"], f["ga"], f["trap"], f["q1"], f["a1"], f["q2"], f["a2"]
            )
    return out
