"""Unique mathematical cores for every GRE Math skill."""

from __future__ import annotations

from typing import Any


def C(
    stmt: str,
    idea: str,
    how: str,
    exq: str,
    exa: str,
    gq: str,
    ga: str,
    traps: list[str],
    q1: str,
    a1: str,
    q2: str,
    a2: str,
    hook: str = "",
) -> dict[str, Any]:
    return {
        "stmt": stmt,
        "idea": idea,
        "how": how,
        "exq": exq,
        "exa": exa,
        "gq": gq,
        "ga": ga,
        "traps": traps,
        "q1": q1,
        "a1": a1,
        "q2": q2,
        "a2": a2,
        "hook": hook,
    }


def build_cores() -> dict[str, dict[str, Any]]:
    M: dict[str, dict[str, Any]] = {}

    def add(i: int, **kw: Any) -> None:
        M[f"M-{i:03d}" if i < 1000 else f"M-{i}"] = C(**kw)

    # ----- A arithmetic -----
    add(1, stmt=r"The integers $\mathbb{Z}$, rationals $\mathbb{Q}$, and reals $\mathbb{R}$ satisfy $\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$. Addition and multiplication on $\mathbb{R}$ are associative, commutative, and distributive; every nonzero real has a multiplicative inverse; there is no real $x$ with $x^2<0$.",
        idea="Arithmetic is not a pile of tricks. It is the field operations on nested number systems. Integers do not divide in general; rationals do; reals fill the holes the rationals leave (that filling is completeness, later).",
        how="Name the system you are in. If the problem needs inverses, you need at least $\mathbb{Q}$. If it needs $\sqrt{2}$ or $\pi$, you need $\mathbb{R}$. Never cancel across an equation without knowing the object is nonzero.",
        exq=r"Compute $3-7+(-2)\times 5$ and say which system the answer lives in.",
        exa=r"Multiplication first: $(-2)\times 5=-10$. Then $3-7-10=-14\in\mathbb{Z}\subset\mathbb{R}$.",
        gq=r"Which statement is false? (A) Every integer is rational. (B) Every rational is real. (C) Every real is rational. (D) $\mathbb{Z}$ is closed under subtraction.",
        ga=r"(C) is false: $\sqrt{2}$ is real and not rational. (A) and (B) are the nested inclusions. (D) is true.",
        traps=["Treating $\mathbb{Q}$ as ‘decimals that stop’ — repeating decimals are rational too.", "Dividing integers as if the answer must be an integer."],
        q1=r"Is $-4/6$ an integer? A rational? A real?",
        a1=r"Not an integer. It equals $-2/3\in\mathbb{Q}\subset\mathbb{R}$.",
        q2=r"Show by example that $\mathbb{Z}$ is not closed under division.",
        a2=r"$1\div 2=1/2\notin\mathbb{Z}$.",
        hook="Every later formula is arithmetic wearing a costume.")

    add(2, stmt=r"A fraction $a/b$ with $b\neq 0$ is the real (or rational) satisfying $b\cdot(a/b)=a$. A ratio $a:b$ is the fraction $a/b$. A proportion $a/b=c/d$ is equality of ratios. A percentage $p\%$ is $p/100$.",
        idea="Fractions are numbers, not decorations on integers. Cross-multiplication is multiplication by $bd$, which is legal only when $b,d\neq 0$. Percentages are fractions with a social life.",
        how="Reduce by gcd. To add, common denominators. To compare, common denominators or cross-multiply after checking signs. Convert percent $\leftrightarrow$ decimal $\leftrightarrow$ fraction before mixing.",
        exq=r"Solve $\dfrac{x}{6}=\dfrac{5}{8}$.",
        exa=r"Cross-multiply: $8x=30$, so $x=15/4$.",
        gq=r"A quantity increases by $20\%$ then decreases by $20\%$. The net factor is",
        ga=r"$(1.2)(0.8)=0.96$, a $4\%$ decrease. Percent changes do not cancel.",
        traps=["Adding percentages of different bases.", "Canceling terms that are added, not factors: $\\frac{a+b}{a+c}\\neq\\frac{b}{c}$."],
        q1=r"Compute $\dfrac{2}{3}+\dfrac{5}{12}$.",
        a1=r"$\dfrac{8}{12}+\dfrac{5}{12}=\dfrac{13}{12}$.",
        q2=r"If $a:b=3:5$ and $a+b=24$, find $a$.",
        a2=r"$a=9$, $b=15$.",
        hook="GRE probability and combinatorics both eat fractions for breakfast.")

    add(3, stmt=r"Scientific notation writes $x=m\times 10^e$ with $1\le |m|<10$ and $e\in\mathbb{Z}$. Order of magnitude is the nearest power of ten, or sometimes $\lfloor\log_{10}|x|\rfloor$.",
        idea="Huge and tiny numbers are the same skill as exponents. The mantissa carries the significant digits; the exponent carries the scale.",
        how="Move the point until the mantissa is in $[1,10)$, counting the moves as $e$. To multiply, multiply mantissas and add exponents, then renormalize.",
        exq=r"Write $0.00047$ in scientific notation.",
        exa=r"$4.7\times 10^{-4}$.",
        gq=r"$(3.0\times 10^8)(2.0\times 10^{-3})$ equals",
        ga=r"$6.0\times 10^{5}$.",
        traps=["Counting decimal places off-by-one.", "Forgetting to renormalize after multiplying mantissas: $30\times 10^4$ is not scientific form."],
        q1=r"Which is larger, $2.1\times 10^{-3}$ or $8\times 10^{-4}$?",
        a1=r"$2.1\times 10^{-3}=21\times 10^{-4}>8\times 10^{-4}$.",
        q2=r"Approximate $7!\times 10^{-4}$ to one significant digit in scientific notation.",
        a2=r"$7!=5040$, so about $5\times 10^{-1}$.",
        hook="No calculator means you live in powers of ten.")

    add(4, stmt=r"The conventional order is parentheses (and other grouping), then exponents, then multiplication and division left to right, then addition and subtraction left to right. Unary minus binds tightly: $-3^2=-(3^2)=-9$, while $(-3)^2=9$.",
        idea="Order of operations is a convention that makes expressions unambiguous. Sign errors are the GRE’s favorite inexpensive trap.",
        how="Rewrite unary minus as multiplication by $-1$ when unsure. Never distribute an exponent across a sum. Work left to right at each precedence level.",
        exq=r"Evaluate $-2^4+12\div 3\cdot 2$.",
        exa=r"$-16+4\cdot 2=-16+8=-8$.",
        gq=r"The value of $6-3-1$ is",
        ga=r"$2$, not $4$. Subtraction is left-associative.",
        traps=["$-x^2$ versus $(-x)^2$.", "Doing all multiplications before all divisions even when they sit left-to-right."],
        q1=r"Evaluate $2^{3^2}$ and $(2^3)^2$.",
        a1=r"Towers are top-down: $2^{9}=512$. The other is $8^2=64$.",
        q2=r"Simplify $-(a-b)$ vs $-a-b$.",
        a2=r"$-(a-b)=-a+b$. The second is $-a-b$.",
        hook="If you only master one ‘easy’ skill, master signs.")

    add(5, stmt=r"The absolute value on $\mathbb{R}$ is $|x|=x$ if $x\ge 0$ and $|x|=-x$ if $x<0$. Equivalently $|x|=\sqrt{x^2}$. It is a norm: $|x|\ge 0$, $|x|=0\Leftrightarrow x=0$, $|xy|=|x||y|$, and $|x+y|\le |x|+|y|$.",
        idea="Absolute value is distance to $0$ on the line. Equations with $|\\cdot|$ split into cases; inequalities become distances.",
        how="For $|A|=k$ with $k>0$, $A=k$ or $A=-k$. For $k=0$, $A=0$. For $k<0$, empty. Always check extra conditions (domains).",
        exq=r"Solve $|2x-3|=5$.",
        exa=r"$2x-3=5$ or $2x-3=-5$, so $x=4$ or $x=-1$.",
        gq=r"$|x-1|+|x+1|$ equals $2$ when",
        ga=r"For $x\in[-1,1]$ the sum is $2$. Outside it is $2|x|$. So on the whole interval $[-1,1]$.",
        traps=["Writing $|x|=-x$ as if it were always true.", "Dropping the empty-solution case $|A|=$ negative."],
        q1=r"Simplify $|-3|+|-x|$ for $x\in\mathbb{R}$.",
        a1=r"$3+|x|$.",
        q2=r"Solve $|x|=x$.",
        a2=r"$x\ge 0$.",
        hook="Later: $|z|$ for complex numbers is the same idea in the plane.")

    add(6, stmt=r"The floor $\lfloor x\rfloor$ is the greatest integer $\le x$. The ceiling $\lceil x\rceil$ is the least integer $\ge x$. Always $\lfloor x\rfloor\le x\le\lceil x\rceil$, and $\lceil x\rceil-\lfloor x\rfloor$ is $0$ if $x\in\mathbb{Z}$ and $1$ otherwise.",
        idea="Floor and ceiling extract integers without rounding-to-nearest. They appear in counting, number theory, and ‘how many’ GRE items.",
        how="For $n\le x<n+1$ with $n\in\mathbb{Z}$, $\lfloor x\rfloor=n$. Write $x=n+f$ with $f\in[0,1)$. Be careful with negatives: $\lfloor -1.2\rfloor=-2$, not $-1$.",
        exq=r"Compute $\lfloor 3.7\rfloor$, $\lceil 3.7\rceil$, $\lfloor -3.7\rfloor$, $\lceil -3.7\rceil$.",
        exa=r"$3$, $4$, $-4$, $-3$.",
        gq=r"The number of integers $n$ with $\lfloor n/2\rfloor=3$ is",
        ga=r"$3\le n/2<4$ so $6\le n<8$, hence $n=6,7$. Two integers.",
        traps=["Floor of negatives (people round toward zero).", "Confusing floor with truncation of the decimal representation for $x<0$."],
        q1=r"Is $\lfloor x+y\rfloor=\lfloor x\rfloor+\lfloor y\rfloor$ always?",
        a1=r"No. $x=y=0.6$ gives $1$ versus $0$.",
        q2=r"Show $\lfloor x\rfloor+\lfloor -x\rfloor$ is $0$ or $-1$.",
        a2=r"$0$ if $x\in\mathbb{Z}$, else $-1$.",
        hook="Counting lattice points is floor-calculus.")

    add(7, stmt=r"Estimation replaces a quantity $x$ by a nearby $y$ that is easier, with an error you control. Sensible rounding specifies the place (nearest integer, nearest ten, significant digits) and a rule for ties.",
        idea="On a no-calculator exam, estimation is a weapon: it kills three of five choices before you finish the algebra.",
        how="Round to one or two significant digits, compute, then ask whether you overshot or undershot. Keep error direction.",
        exq=r"Estimate $\dfrac{49\times 81}{20}$.",
        exa=r"$50\times 80/20=200$. Actual $49\times 81=3969$, $/20=198.45$.",
        gq=r"$\sqrt{50}$ is nearest which integer?",
        ga=r"$7^2=49$, so $7$.",
        traps=["Rounding too early in a multi-step computation and then treating the result as exact.", "Estimating a small difference of large numbers (catastrophic cancellation)."],
        q1=r"Estimate $e^3$ using $e\\approx 2.7$.",
        a1=r"$2.7^2=7.29$, times $2.7\\approx 20$. (Actual $\\approx 20.09$.)",
        q2=r"Which is larger, $2^{10}$ or $10^3$?",
        a2=r"$1024>1000$.",
        hook="Part Y will ask you to estimate to eliminate.")

    add(8, stmt=r"A number $M$ is an upper bound for a set $S\subset\mathbb{R}$ if $x\le M$ for all $x\in S$. A lower bound $m$ satisfies $x\ge m$ for all $x\in S$. Bounds need not be achieved and need not be unique.",
        idea="Bounding is the grown-up version of estimation: replace a monster by something larger you can compute. Later, $\\sup$ is the least upper bound.",
        how="To bound a positive product, bound each factor in the direction that preserves the inequality. For $1/(1+x)$ with $x>0$, $1/(1+x)<1$.",
        exq=r"Show $n/(n+1)<1$ for $n>0$.",
        exa=r"$n<n+1$, divide by the positive $n+1$.",
        gq=r"For $x>0$, a valid upper bound for $\\dfrac{x}{1+x}$ is",
        ga=r"$1$, since $x<1+x$. Also $x$ itself is an upper bound only if $x\\ge x/(1+x)$, which is true, but $1$ is the GRE-friendly bound.",
        traps=["Reversing inequalities when taking reciprocals of negatives.", "Thinking a bound must be the maximum."],
        q1=r"Give a lower bound for $n^2+1$ when $n\\in\\mathbb{Z}$.",
        a1=r"$1$, achieved at $n=0$.",
        q2=r"Is $2$ an upper bound for $\{1-1/n:n\\in\\mathbb{N}\}$?",
        a2=r"Yes (so is $1$). $1$ is the least upper bound.",
        hook="Series and integrals are won by bounds, not by closed forms.")

    add(9, stmt=r"A derived quantity has a dimension (or unit). Only quantities of the same dimension may be added. Arguments of $\\exp$, $\\sin$, $\\log$ must be dimensionless (pure numbers).",
        idea="Even on a pure math exam, dimensional sanity catches garbage. If an answer choice has $\\sin(x+x^2)$ with $x$ a length, something is wrong — unless $x$ was never a length.",
        how="Track units through a formula. In GRE math this is usually ‘degree versus dimensionless’: polynomials versus trig, or mixing $n$ with $n!$.",
        exq=r"Why is $e^{3\\text{ meters}}$ not a physical quantity?",
        exa=r"The exponential’s Taylor series would add $1$ to meters to meters-squared. The argument must be a number.",
        gq=r"If $f$ is in meters and $t$ in seconds, $f/t$ has units",
        ga=r"meters per second.",
        traps=["Adding $\\pi$ (dimensionless) to $180$ (degrees) without converting.", "Treating $\\log(a+b)$ as if $a$ and $b$ need not be the same type."],
        q1=r"Convert $3$ hours to seconds.",
        a1=r"$10800$ seconds.",
        q2=r"Can $x+\\sin x$ make sense if $x$ is an angle in radians?",
        a2=r"Yes: radians are dimensionless in this sense; $\\sin x$ is a number and $x$ is a number.",
        hook="The same instinct later checks that a probability is dimensionless and in $[0,1]$.")

    add(10, stmt=r"Strategic mental arithmetic is the decision to compute the cheap form of an expression: factor, cancel, use difference of squares, or compute modulo a small integer to reject choices.",
        idea="The GRE is not testing whether you can multiply $19\\times 21$ the slow way. It is testing whether you see $19\\times 21=(20-1)(20+1)=400-1=399$.",
        how="Before expanding, look for $(a\\pm b)^2$, $a^2-b^2$, factoring $n(n+1)$, pairing in a sum, or reduction mod $9$ or $2$.",
        exq=r"Compute $48\\times 52$.",
        exa=r"$(50-2)(50+2)=2500-4=2496$.",
        gq=r"$15^2-14^2$ equals",
        ga=r"$(15-14)(15+14)=29$.",
        traps=["Expanding first out of fear.", "Mental arithmetic that drops a carry, then refusing to check a digit-sum."],
        q1=r"Compute $25^2$.",
        a1=r"$625$. Pattern: $(20+5)^2=400+200+25$.",
        q2=r"Find $1+2+\\cdots+20$ mentally.",
        a2=r"$20\\cdot 21/2=210$.",
        hook="Speed is not rushing. Speed is choosing the cheap form.")

    # ----- A exponents -----
    add(11, stmt=r"For $a>0$ and real $m,n$: $a^m a^n=a^{m+n}$, $(a^m)^n=a^{mn}$, $(ab)^n=a^n b^n$, $a^0=1$, $a^{-n}=1/a^n$. Also $a^m/a^n=a^{m-n}$.",
        idea="An exponent counts factors. The laws are bookkeeping for concatenation, stacking, and distribution over multiplication — never over addition.",
        how="Match bases first. Convert $4^x=(2^2)^x=2^{2x}$. Never write $(a+b)^n=a^n+b^n$.",
        exq=r"Simplify $\\dfrac{2^5\\cdot 2^{-2}}{4^2}$.",
        exa=r"$4=2^2$, so $2^{3}/2^{4}=2^{-1}=1/2$.",
        gq=r"If $3^{2x}=27^{x-1}$, then $x=$",
        ga=r"$27=3^3$ so $3^{2x}=3^{3x-3}$, hence $2x=3x-3$, $x=3$.",
        traps=["$(a+b)^n=a^n+b^n$.", "Adding exponents when bases differ."],
        q1=r"Simplify $(3^2)^3\\cdot 3^{-4}$.",
        a1=r"$3^2=9$.",
        q2=r"Write $\\dfrac{a^5 b^{-2}}{a^{-1}b^3}$ as $a^{\\bullet}b^{\\bullet}$.",
        a2=r"$a^6 b^{-5}$.",
        hook="Exponential equations on the GRE are almost always ‘same base, equate exponents.’")

    add(12, stmt=r"For $a>0$, $a^{-n}=1/a^n$ and $a^{p/q}=\\sqrt[q]{a^p}=(\\sqrt[q]{a})^p$ when $q\\in\\mathbb{N}$ and the root exists in $\\mathbb{R}$. Odd roots of negatives exist; even roots do not (in $\\mathbb{R}$).",
        idea="Negative exponents are reciprocals. Fractional exponents are roots. The two combine: $a^{-1/2}=1/\\sqrt{a}$.",
        how="Rewrite everything as $a^{p/q}$ or as radicals, whichever makes cancellation obvious. Check the real domain.",
        exq=r"Simplify $8^{2/3}$.",
        exa=r"$(8^{1/3})^2=2^2=4$, or $(8^2)^{1/3}=64^{1/3}=4$.",
        gq=r"$9^{-3/2}$ equals",
        ga=r"$1/(9^{3/2})=1/(27)=1/27$.",
        traps=["Even roots of negatives in $\\mathbb{R}$.", "Writing $\\sqrt{x^2}=x$ instead of $|x|$."],
        q1=r"Simplify $16^{-3/4}$.",
        a1=r"$1/8$.",
        q2=r"For which real $x$ is $x^{1/2}$ defined?",
        a2=r"$x\\ge 0$.",
        hook="Calculus will differentiate $x^{p/q}$; the algebra must already be automatic.")

    add(13, stmt=r"Scientific exponents are the special case $10^e$ in $m\\times 10^e$. The laws of exponents apply unchanged: $(3\\times 10^4)(2\\times 10^{-6})=6\\times 10^{-2}$.",
        idea="This is M-003 plus M-011. The only new move is renormalizing the mantissa into $[1,10)$.",
        how="Multiply/divide mantissas; add/subtract exponents; then restore scientific form.",
        exq=r"Compute $\\dfrac{6.0\\times 10^{7}}{2.0\\times 10^{-3}}$.",
        exa=r"$3.0\\times 10^{10}$.",
        gq=r"$(4\\times 10^{-2})^3=$",
        ga=r"$64\\times 10^{-6}=6.4\\times 10^{-5}$.",
        traps=["$(10^a)^b=10^{a+b}$ instead of $10^{ab}$.", "Leaving $64\\times 10^{-6}$ as if it were scientific notation."],
        q1=r"Write $0.03\\times 10^5$ in scientific notation.",
        a1=r"$3\\times 10^3$.",
        q2=r"Compare $5\\times 10^{-8}$ and $4\\times 10^{-7}$.",
        a2=r"The second is larger.",
        hook="Orders of magnitude win estimation items.")

    add(14, stmt=r"For $a>0$, $a\\neq 1$, $\\log_a$ is the inverse of $x\\mapsto a^x$: $\\log_a(a^x)=x$ and $a^{\\log_a x}=x$ for $x>0$. Laws: $\\log_a(xy)=\\log_a x+\\log_a y$, $\\log_a(x/y)=\\log_a x-\\log_a y$, $\\log_a(x^k)=k\\log_a x$.",
        idea="A logarithm is an exponent. Every log law is an exponent law run backwards.",
        how="Domain: argument $>0$, base $>0$ and $\\neq 1$. Convert products to sums only after checking positivity.",
        exq=r"Simplify $\\log_2 8+\\log_2(1/2)$.",
        exa=r"$3+(-1)=2$, or $\\log_2(8\\cdot 1/2)=\\log_2 4=2$.",
        gq=r"$\\log_3 9^x$ equals",
        ga=r"$x\\log_3 9=2x$.",
        traps=["$\\log(a+b)=\\log a+\\log b$.", "Logs of nonpositive numbers in $\\mathbb{R}$."],
        q1=r"Compute $\\log_5 1$, $\\log_5 5$, $\\log_5 25$.",
        a1=r"$0,1,2$.",
        q2=r"Solve $\\log_2 x=0$.",
        a2=r"$x=1$.",
        hook="Change of base is coming; the laws must already be muscle.")

    add(15, stmt=r"$\\log_b a=\\dfrac{\\log_c a}{\\log_c b}$ for any valid base $c$. In particular $\\log_b a=1/\\log_a b$ and $\\log_b a=\\dfrac{\\ln a}{\\ln b}$.",
        idea="All logarithms are proportional. Changing base is converting units of exponent.",
        how="To compute $\\log_8 2$, write $2=8^{1/3}$ or use $\\ln 2/\\ln 8=\\ln 2/(3\\ln 2)=1/3$.",
        exq=r"Evaluate $\\log_9 27$.",
        exa=r"$\\dfrac{\\log_3 27}{\\log_3 9}=\\dfrac{3}{2}$.",
        gq=r"$\\log_2 3\\cdot\\log_3 4\\cdot\\log_4 2$ equals",
        ga=r"The product telescopes to $1$ by change of base.",
        traps=["Writing $\\log_b a=\\log a/\\log b$ and then canceling the word ‘log’ as if it were a factor of $a$ and $b$.", "Wrong domain on the new base."],
        q1=r"Show $\\log_4 8=3/2$.",
        a1=r"$4^{3/2}=(2^2)^{3/2}=2^3=8$.",
        q2=r"Express $\\log_6 2$ in terms of $\\ln$.",
        a2=r"$\\ln 2/\\ln 6$.",
        hook="GRE likes telescoping change-of-base products.")

    add(16, stmt=r"$\\ln x=\\log_e x$ with $e=\\lim(1+1/n)^n$. Common log is $\\log_{10}$. In analysis, $\\log$ often means $\\ln$. Both satisfy $(\\ln x)'=1/x$ and $\\ln(e^x)=x$.",
        idea="Natural log is the analysis logarithm because $e^x$ is the exponential whose derivative is itself.",
        how="On GRE calculus items, treat $\\log$ as $\\ln$ unless base 10 is forced. Convert via $\\log_{10}x=\\ln x/\\ln 10$.",
        exq=r"Simplify $\\ln(e^5)+e^{\\ln 3}$.",
        exa=r"$5+3=8$.",
        gq=r"$\\dfrac{d}{dx}\\log_{10}x$ equals",
        ga=r"$\\dfrac{1}{x\\ln 10}$.",
        traps=["Differentiating $\\log_{10}x$ as $1/x$.", "Writing $\\ln(x+y)=\\ln x+\\ln y$."],
        q1=r"Solve $\\ln x=1$.",
        a1=r"$x=e$.",
        q2=r"Write $10^{\\log_{10}7}$.",
        a2=r"$7$.",
        hook="The derivative of $\\ln$ is why $\\int dx/x=\\ln|x|+C$.")

    add(17, stmt=r"An exponential equation has the unknown in an exponent. If $a^{f(x)}=a^{g(x)}$ with $a>0$, $a\\neq 1$, then $f(x)=g(x)$. More generally take $\\log_a$ of both sides after checking positivity.",
        idea="Exponentials are one-to-one on $\\mathbb{R}$. That is the whole method, plus same-base rewriting.",
        how="Rewrite all powers with a common base, or take logs. Check extraneous issues only if you transformed the domain (rare for pure exponentials).",
        exq=r"Solve $2^{x+1}=8^{x-1}$.",
        exa=r"$8=2^3$ so $x+1=3x-3$, $x=2$.",
        gq=r"The solution of $e^{2x}=3e^{x}$ is",
        ga=r"$e^{x}(e^{x}-3)=0$, so $x=\\ln 3$ (since $e^x\\neq 0$).",
        traps=["Taking logs and dropping coefficients.", "Forgetting $e^x$ never zero, so not ‘losing a root’ that was never there."],
        q1=r"Solve $5^{x}=1/25$.",
        a1=r"$x=-2$.",
        q2=r"Solve $4^x=2^{x+3}$.",
        a2=r"$2^{2x}=2^{x+3}$, so $x=3$.",
        hook="Same skill as later: $e^{\\lambda t}$ in ODEs.")

    add(18, stmt=r"A logarithmic equation has the unknown in a log. Use laws to make a single log, convert $\\log_a f(x)=c$ to $f(x)=a^c$, and discard solutions that make any log argument nonpositive.",
        idea="Logs have a domain. The algebra of inverse functions will happily offer extra roots. You must reject them.",
        how="(1) Domain first. (2) Combine logs. (3) Exponentiate. (4) Check.",
        exq=r"Solve $\\log_2(x-1)+\\log_2(x+1)=3$.",
        exa=r"Domain $x>1$. Then $\\log_2(x^2-1)=3$, $x^2-1=8$, $x^2=9$, $x=3$ (since $x>1$).",
        gq=r"$\\ln(x-2)=\\ln(4-x)$ implies",
        ga=r"$x-2=4-x$ so $x=3$, which lies in $(2,4)$. Valid.",
        traps=["Forgetting domain $x>1$ in the example and keeping $x=-3$.", "Combining $\\log a+\\log b$ when $b$ might be negative."],
        q1=r"Solve $\\log_3(2x-1)=2$.",
        a1=r"$2x-1=9$, $x=5$, and $2x-1>0$ holds.",
        q2=r"Solve $\\log x+\\log(x-3)=1$ in base $10$.",
        a2=r"Domain $x>3$. $x(x-3)=10$, $x^2-3x-10=0$, $(x-5)(x+2)=0$, so $x=5$.",
        hook="Extraneous roots are a Critical trap skill later (M-1005).")

    add(19, stmt=r"The map $x\\mapsto a^x$ is increasing if $a>1$ and decreasing if $0<a<1$. Therefore $a^{f}\\le a^{g}$ becomes $f\\le g$ when $a>1$, and the inequality reverses when $0<a<1$.",
        idea="Exponential inequalities are ordinary inequalities after using monotonicity. The base decides whether to reverse.",
        how="Rewrite with a common base $>0$, $\\neq 1$. Track the direction. Alternatively take logs of the same base and again track monotonicity.",
        exq=r"Solve $2^x>8$.",
        exa=r"$2^x>2^3$ and base $>1$, so $x>3$.",
        gq=r"$(1/2)^{x}\\ge 4$ is equivalent to",
        ga=r"$(2^{-1})^x\\ge 2^2$ so $2^{-x}\\ge 2^2$, hence $-x\\ge 2$ (base $>1$ after rewriting), $x\\le -2$.",
        traps=["Not reversing when $0<a<1$.", "Taking logs of both sides when a side is nonpositive."],
        q1=r"Solve $e^{x}\\le 1$.",
        a1=r"$x\\le 0$.",
        q2=r"Solve $3^{2x+1}<1/9$.",
        a2=r"$2x+1<-2$, $x<-3/2$.",
        hook="Later: growth rates $e^x$ versus polynomials live here.")

    add(20, stmt=r"$\\log_a$ is increasing if $a>1$ and decreasing if $0<a<1$, on $(0,\\infty)$. Logarithmic inequalities require a domain ($\\mathrm{arg}>0$) and then monotonicity.",
        idea="Same story as exponential inequalities, plus a domain that can chop the answer set.",
        how="Write the domain first. Convert to a single log or exponentiate. Intersect with the domain.",
        exq=r"Solve $\\log_2 x>3$.",
        exa=r"Domain $x>0$. Increasing, so $x>8$.",
        gq=r"$\\ln(x-1)<0$ iff",
        ga=r"Domain $x>1$, and $x-1<1$, so $1<x<2$.",
        traps=["Solving $\\log x>2$ as $x>100$ without specifying base.", "Dropping the domain intersection."],
        q1=r"Solve $\\log_{1/2}x\\ge -1$.",
        a1=r"Domain $x>0$. Decreasing log, reverse: $x\\le (1/2)^{-1}=2$. So $0<x\\le 2$.",
        q2=r"Solve $\\log_3(2x-1)\\le 2$.",
        a2=r"$0<2x-1\\le 9$, so $1/2<x\\le 5$.",
        hook="Domain-first is the whole subject of logs.")

    add(21, stmt=r"$y=a^x$ if and only if $x=\\log_a y$, for $a>0$, $a\\neq 1$, $y>0$. This translation is legal in both directions and is how exponential and log equations communicate.",
        idea="The two forms are the same sentence. Fluency is switching without changing meaning.",
        how="To remove a log, exponentiate with the same base. To remove an exponential, take the log. Record the domain.",
        exq=r"Write $e^{2x}=7$ in log form.",
        exa=r"$2x=\\ln 7$, or $x=\\frac12\\ln 7$.",
        gq=r"$\\log_5(x-1)=2$ is equivalent to",
        ga=r"$x-1=25$, $x=26$.",
        traps=["Exponentiating and changing the base.", "$a^{\\log_a x}=x$ used for $x\\le 0$."],
        q1=r"Convert $\\ln y=3t$ to exponential form.",
        a1=r"$y=e^{3t}$.",
        q2=r"Convert $10^{-2}=0.01$ to a log statement.",
        a2=r"$\\log_{10}(0.01)=-2$.",
        hook="ODEs and inverse functions both use this translation constantly.")

    return M


TOPIC_HOW: dict[str, tuple[str, str]] = {}

TOPIC_THEORY: dict[str, str] = {
    "Arithmetic & number manipulation": r"""Arithmetic is the field operations on $\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$. Integers add and multiply and subtract; rationals add division (except by zero); reals add limits of rationals, which you will meet as completeness in Part O. On the GRE there is no calculator, so every later topic — limits, matrices, congruences, probabilities — is only as strong as this fluency. Train until a fraction, a sign, a floor, and a bound are boring.""",
    "Exponents & logarithms": r"""Exponentiation $a^x$ (for $a>0$) turns addition of exponents into multiplication of powers. Logarithms invert that: $\log_a$ eats a product and returns a sum. The two languages are the same mathematics. Domain restrictions (positive arguments, base $a>0$, $a\neq 1$) are not footnotes; they delete GRE answer choices. Master same-base rewriting, the three log laws, change of base, and monotonicity for inequalities.""",
    "Algebraic manipulation": r"""Algebraic manipulation is legal rewriting: factoring, identities, division algorithms, partial fractions, substitution. Illegal rewriting (canceling sums, dividing by zero, dropping absolute values) is how GRE items are authored. Every identity you learn here is a compression algorithm for a later calculus or linear-algebra computation.""",
    "Equations & inequalities": r"""An equation asks where two expressions agree; an inequality asks where one dominates. Linear and quadratic cases are complete (you can finish them). Higher polynomial, rational, radical, and absolute-value cases need domains, sign charts, and checks for extraneous roots. Parameters turn “solve” into “for which $a$ are there $0,1,2,\ldots$ solutions?” — a GRE obsession.""",
    "Inequality techniques": r"""Named inequalities (AM-GM, Cauchy–Schwarz, triangle) and crude bounds (squares, completing the square) replace impossible closed forms. Equality cases are part of the theorem: if you cannot say when equality holds, you do not own the inequality. The GRE uses these both as computation shortcuts and as “which is largest?” items.""",
    "Polynomials": r"""A polynomial is determined by its coefficients. Degree, leading coefficient, roots with multiplicity, factor and remainder theorems, Vieta, and the fundamental theorem of algebra are one package. Over $\mathbb{R}$, complex roots come in conjugate pairs. Over $\mathbb{Q}$, the rational root theorem is a finite search, not a guarantee.""",
    "Functions": r"""A function $f:A\to B$ assigns to each $x\in A$ exactly one $f(x)\in B$. Domain, codomain, image, injectivity, surjectivity, composition, and inverses are set-theoretic ideas that later become linear maps, homomorphisms, and random variables. Graphs are pictures of functions, not the functions themselves.""",
    "Function transformations": r"""Replacing $x$ by $x-h$ or $x/a$, replacing $f$ by $f+k$ or $cf$, and reflecting through axes are rigid rules that people reverse under pressure. $y=f(x-h)$ shifts the graph of $f$ to the right by $h$. Inverse functions reflect through $y=x$. Combining transformations requires a consistent order.""",
    "Common function families": r"""Polynomials, rationals, powers, roots, absolute values, exponentials, logs, and step functions are the GRE’s menagerie. You should know domain, intercepts, asymptotes, monotonicity, and a qualitative graph for each family, and how composition mixes them.""",
    "Sequences and recurrences": r"""A sequence is a function $\mathbb{N}\to\mathbb{R}$. Arithmetic and geometric sequences have closed forms; series are sums of sequences. Recurrences define a term from previous terms. Telescoping and finite geometric sums are speed skills. Infinite geometric series $|r|<1$ is the first infinite sum you must own before Part G.""",
    "Parametric & polar basics": r"""Parametric equations describe a curve by $x(t),y(t)$. Polar coordinates describe a point by radius and angle. Eliminating $t$ recovers a Cartesian relation when you need it; keeping $t$ is better for motion. Polar area uses $\frac12\int r^2\,d\theta$.""",
    "Trigonometry foundations": r"""Radians are the calculus unit. The unit circle defines $\sin,\cos$ as coordinates, and the other four functions as ratios. Pythagorean, even/odd, and reciprocal identities are rewriting tools. Exact values at $0,\pi/6,\pi/4,\pi/3,\pi/2$ and their cousins must be instant. Quadrant signs are ASTC (or whatever mnemonic you will not botch).""",
    "Trigonometric identities": r"""Sum, double-angle, half-angle, product-to-sum, and power-reduction identities are not a list to memorize in isolation. They are the algebra of $e^{i\theta}$ written in real form. On the GRE they turn a horror integral or a limit into a one-liner. Convert until you see a derivative or a standard form.""",
    "Trigonometric equations & inequalities": r"""Because of periodicity, trig equations have infinitely many solutions unless the domain is restricted. General solutions add $2\pi k$ or $\pi k$ according to the function. Inverse trig functions return principal values; they are not full inverse relations. Always state the range convention.""",
    "Triangle trigonometry": r"""Law of sines, law of cosines, area $\frac12 ab\sin C$, Heron, and the ambiguous SSA case are the computational triangle toolkit. SSA can yield $0,1,$ or $2$ triangles; that is a GRE favorite. Inscribed-angle facts connect this topic to circles.""",
    "Conic sections": r"""Circle, parabola, ellipse, hyperbola: each is a quadratic equation and a focus-directrix story. Standard forms, vertices, foci, eccentricity, and asymptotes (hyperbola) should be recognizable after a translation. Rotated conics on the GRE are mostly “there is an $xy$ term.”""",
    "Coordinate geometry": r"""Distance, midpoint, slope, line forms, parallel/perpendicular, point-line distance, and circle-line intersection are the plane as algebra. Tangency is discriminant zero. 3D distance is the same Pythagorean idea with one more square.""",
    "Complex-number algebra": r"""$\mathbb{C}$ is a field. Write $z=a+bi$, conjugate $\bar z=a-bi$, modulus $|z|=\sqrt{a^2+b^2}$, and divide by multiplying by the conjugate. The plane picture is not optional: addition is vector addition; conjugation is reflection in the real axis.""",
    "Polar/exponential complex form": r"""$z=re^{i\theta}=r(\cos\theta+i\sin\theta)$. Multiplication adds arguments and multiplies moduli. De Moivre computes powers. The $n$th roots of a nonzero complex number are $n$ equally spaced points on a circle. Roots of unity are the unit-circle special case.""",
    "Complex polynomial problems": r"""Over $\mathbb{C}$, every nonconstant polynomial factors into linears. Real polynomials have conjugate-root symmetry. Roots of unity turn $z^n=1$ into geometry. Magnitude-argument arithmetic is how you track $|p(z)|$ without expanding.""",
    "Limits": r"""A limit $\lim_{x\to a}f(x)=L$ says: values of $f$ can be forced within $\varepsilon$ of $L$ by taking $x$ sufficiently close to $a$ (but not necessarily equal). One-sided limits, infinite limits, and limits at infinity are the same idea with different metrics. Algebra of limits, squeeze, standard trig limits, and L’Hôpital (with hypotheses) are the toolkit. Indeterminate forms are not numbers; they are invitations to rewrite.""",
    "Continuity": r"""$f$ is continuous at $a$ when $\lim_{x\to a}f(x)=f(a)$. Types of discontinuity (removable, jump, infinite) are classified by one-sided limits. IVT and EVT are the two big existence theorems for continuous functions on closed intervals.""",
    "Derivative definition & rules": r"""$f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$ when the limit exists. Geometrically it is slope of the tangent; physically it is instantaneous rate. Power, product, quotient, chain, implicit, logarithmic, inverse, and higher derivatives are the machine that computes $f'$ without returning to the limit every time.""",
    "Standard derivatives": r"""You must differentiate polynomials, $e^x$, $\ln x$, trig, inverse trig, and hyperbolic functions instantly. These are not “look up” facts on a 170-minute exam with no calculator.""",
    "Applications of derivatives": r"""Critical points, first and second derivative tests, concavity, sketching, optimization, related rates, parametric derivatives, linear approximation, MVT and Rolle: this is why derivatives exist on the GRE. The skill is translating a word or a graph into $f'=0$ plus endpoint checks.""",
    "Taylor theorem & approximation": r"""Taylor polynomials are the unique polynomials that match $f$ and its first $n$ derivatives at a point. Remainder estimates tell you the error. Big-O notation tracks the order. Limits that look like L’Hôpital often die faster with two terms of Taylor.""",
    "Antiderivatives": r"""An antiderivative of $f$ is $F$ with $F'=f$. The toolkit: power rule, substitution, parts, partial fractions, trig integrals, trig sub, reduction. Choosing the tool is the skill; carrying out the algebra is the tax.""",
    "Definite integrals": r"""The definite integral is a limit of Riemann sums, equal (for nice $f$) to net signed area. FTC I says the derivative of $\int_a^x f$ is $f(x)$; FTC II says $\int_a^b f=F(b)-F(a)$. Accumulation and average value are FTC in costume.""",
    "Applications of integration": r"""Area between curves, volumes (disk, washer, shell), arc length, surface of revolution, work, center of mass: each is “slice, approximate, integrate.” The GRE tests setup as much as evaluation.""",
    "Improper integrals": r"""Replace an infinite limit or a singularity by a proper integral and take a limit. Comparison is the series test’s twin. Convergence is a yes/no that does not require evaluating the integral.""",
    "Sequences": r"""Sequence convergence, monotonicity, boundedness, subsequences, Cauchy sequences, and completeness of $\mathbb{R}$ are analysis language used on calculus items. $\limsup$ is awareness-level.""",
    "Infinite series": r"""A series converges when its partial sums converge. Terms $\to 0$ is necessary, not sufficient. Geometric, telescoping, $p$, comparison, limit comparison, integral, alternating, ratio, root, absolute vs conditional: pick the test that fits in one glance.""",
    "Power/Taylor series": r"""Power series have a radius of convergence. Inside the radius you may differentiate and integrate termwise. Taylor series of $e^x,\sin x,\cos x,1/(1-x)$ and the binomial series should be writable in your sleep.""",
    "Uniform convergence basics": r"""Pointwise convergence can lose continuity; uniform convergence does not. Weierstrass M-test is a comparison test for functions. This is GRE awareness: enough to not interchange limit and integral blindly.""",
    "Multivariable functions": r"""$f:\mathbb{R}^n\to\mathbb{R}$ has domains, level sets, and limits that must hold along every path. Partials are ordinary derivatives with other variables frozen. Mixed partials agree when they are continuous.""",
    "Differentiability": r"""Existence of partials is not differentiability. The derivative is a linear map (Jacobian). Directional derivatives are $\nabla f\cdot u$. The chain rule in several variables is matrix multiplication of Jacobians.""",
    "Optimization": r"""Critical points of $f(x,y)$ via $\nabla f=0$, Hessian test, extrema on closed bounded sets (check boundary), Lagrange multipliers $\nabla f=\lambda\nabla g$.""",
    "Multiple integration": r"""Iterate, change order, Jacobian in polar/cylindrical/spherical or a general map. $|\det D\Phi|$ is the volume distortion. Setup beats brute force.""",
    "Vector fields": r"""A vector field assigns a vector to each point. Gradients are special fields. Velocity and acceleration are derivatives of vector-valued paths.""",
    "Line integrals": r"""Scalar line integrals weight by arc length. Vector line integrals measure work $\int_C\mathbf{F}\cdot d\mathbf{r}$. Conservative fields are gradients: path independence, $\mathbf{F}=\nabla f$, curl zero (on simply connected domains).""",
    "Curl, divergence & flux": r"""Div is source density; curl is local rotation; flux is flow through a surface. Orientation is a sign convention you must not treat as optional.""",
    "Integral theorems": r"""Green, Stokes, divergence: the FTC in dimensions 2 and 3. Choose the theorem that turns a hard integral into an easy one. Track orientation.""",
    "First-order ODEs": r"""Classify, then solve: separable, linear (integrating factor), exact, Bernoulli, autonomous equilibria and stability, logistic. IVPs pick the constant.""",
    "Second-order linear ODEs": r"""For constant coefficients, the characteristic polynomial’s roots dictate $e^{rt}$, $te^{rt}$, or $e^{\alpha t}\cos/\sin$. Undetermined coefficients and variation of parameters handle the nonhomogeneous term.""",
    "Systems of ODEs": r"""Write $\mathbf{x}'=A\mathbf{x}$, then eigenvalues of $A$ produce the modes. Phase portraits are the picture. Nonlinear systems linearize at equilibria.""",
    "Transforms & expansions": r"""Laplace transforms turn ODEs into algebra. Fourier series expand periodic functions in sines and cosines. Separation of variables is the PDE cameo.""",
    "Vectors & geometry": r"""Vectors add, scale, dot (angles, projections), cross in $\mathbb{R}^3$ (area, orthogonality), triple product (volume). Geometry and algebra are the same object.""",
    "Matrices": r"""Matrices encode linear maps and systems. Multiplication is composition, not entrywise. Transpose, inverse, special shapes (diagonal, triangular, symmetric) are computational gold.""",
    "Systems & row reduction": r"""Gaussian elimination is the GRE algorithm. REF/RREF, consistency, free variables, rank. Homogeneous systems always have at least the zero solution.""",
    "Vector spaces": r"""Axioms, subspaces, span, independence, basis, dimension, coordinates, the four fundamental subspaces, rank-nullity. This is the language that makes matrices mean something.""",
    "Linear transformations": r"""$T(au+bv)=aT(u)+bT(v)$. Kernel and image, injectivity/surjectivity, matrices of $T$, change of basis, similarity. Invertible iff kernel is trivial (in finite dimension, iff onto).""",
    "Determinants": r"""Det is an alternating multilinear form, computable by cofactors or row ops. $\det(AB)=\det A\det B$, $\det A\neq 0$ iff invertible, geometry as signed volume, Cramer’s rule as a museum piece that still appears.""",
    "Eigenvalues & eigenvectors": r"""$Av=\lambda v$ with $v\neq 0$. Characteristic polynomial, algebraic vs geometric multiplicity, diagonalization iff enough independent eigenvectors. Trace is sum of eigenvalues; det is product. Cayley–Hamilton.""",
    "Inner-product spaces": r"""Inner products give geometry: orthogonality, norms, projections, Gram–Schmidt, least squares. Symmetric real matrices are orthogonally diagonalizable (spectral theorem). SVD is the rectangular cousin.""",
    "Divisibility & primes": r"""$a\mid b$, division algorithm, gcd, lcm, Euclid, Bézout, unique factorization, $\tau$ and $\sigma$ from prime factors. This is the arithmetic of $\mathbb{Z}$ as a Euclidean domain.""",
    "Congruences": r"""$a\equiv b\pmod n$ means $n\mid(a-b)$. Residue classes form $\mathbb{Z}/n\mathbb{Z}$. Inverses exist iff coprime to $n$. Linear congruences and CRT are the solving machine. Fast exponentiation is repeated squaring.""",
    "Euler/Fermat tools": r"""Fermat: $a^{p-1}\equiv 1\pmod p$ if $p\nmid a$. Euler: $a^{\phi(n)}\equiv 1\pmod n$ if $\gcd(a,n)=1$. $\phi$ is multiplicative. Orders divide $\phi(n)$.""",
    "Diophantine equations": r"""$ax+by=c$ is solvable iff $\gcd(a,b)\mid c$. General integer solutions follow Bézout. Modular obstructions kill many equations instantly. Pythagorean triples and Pell are extra pattern libraries.""",
    "Additional elementary number theory": r"""Quadratic residues, Legendre symbol, reciprocity (awareness), primitive roots, Möbius inversion, multiplicative functions, continued fractions, $p$-adic valuation. Recognition plus one computation.""",
    "Groups": r"""A group is a set with an associative binary operation, identity, and inverses. Abelian means commutative. Subgroups, cyclic groups, orders of elements and of the group: Lagrange is coming.""",
    "Permutation groups": r"""$S_n$ is the group of bijections on $n$ letters. Cycle decomposition, disjoint cycles commute, transpositions generate, sign homomorphism, $A_n=\ker(\mathrm{sign})$.""",
    "Cosets & Lagrange": r"""Left/right cosets partition $G$. $|G|=|H|\,[G:H]$. Lagrange: $|H|$ divides $|G|$. Consequences: orders of elements divide $|G|$; groups of prime order are cyclic.""",
    "Homomorphisms & quotients": r"""A homomorphism preserves the operation. Kernel is a normal subgroup. First isomorphism theorem: $G/\ker\phi\cong\mathrm{im}\,\phi$. Quotients exist precisely because of normality.""",
    "Group actions": r"""An action is a homomorphism $G\to S_X$. Orbit-stabilizer: $|G|=|\mathrm{Orb}|\,|\mathrm{Stab}|$. Conjugacy is a special action. Finite abelian groups decompose into cyclic groups.""",
    "Rings": r"""Two operations, distributive. Commutative rings, identity, subrings, domains, units, zero-divisors, homomorphisms. $\mathbb{Z}/n\mathbb{Z}$ is the GRE’s favorite ring.""",
    "Ideals & quotient rings": r"""Ideals are kernels of ring maps. Principal, prime, maximal. $R/I$ is a field iff $I$ is maximal (in commutative unital rings). Polynomial ideals in $F[x]$ are principal.""",
    "Polynomial rings & factorization": r"""$F[x]$ is a Euclidean domain, hence a PID and UFD. Irreducibility tests, rational root theorem, division. CRT for rings: $R/(I\cap J)\cong R/I\times R/J$ when $I+J=R$.""",
    "Modules": r"""Modules are vector spaces over rings. Submodules, quotients, homomorphisms, generators, free modules. When the ring is a field, you recover linear algebra.""",
    "Fields & extensions": r"""A field has every nonzero element invertible. Extensions $K/F$ have degree $[K:F]=\dim_F K$. Algebraic vs transcendental, minimal polynomials, splitting fields, $\mathbb{F}_p$ and $\mathbb{F}_{p^n}$.""",
    "Real-number foundations": r"""$\mathbb{R}$ is a complete ordered field: every nonempty set bounded above has a least upper bound. Suprema, infima, Archimedean property, density of $\mathbb{Q}$ and of irrationals, nested intervals.""",
    "Series & convergence": r"""The analysis view of series: partial sums, absolute vs conditional, Cauchy criterion, rearrangements (Riemann), power series radius. Same tests as Part G, now as theorems.""",
    "Differentiability & integration": r"""Mean value theorems, Taylor with remainder, Darboux (derivatives have IVT), Riemann integrability criteria, FTC as a theorem not a slogan.""",
    "Metric/topological basics": r"""A metric measures distance. Open balls generate open sets. Closed sets contain their limits. Interior, closure, boundary, limit points. Completeness: Cauchy sequences converge.""",
    "Topological spaces": r"""A topology is a family of “open sets” closed under unions and finite intersections. Bases, subbases, subspace and product topologies, continuity as preimages of opens, homeomorphism as topological isomorphism.""",
    "Separation & compactness": r"""Hausdorff: points can be separated by opens. Compact: every open cover has a finite subcover. Continuous images of compact sets are compact. In $\mathbb{R}^n$, compact $\Leftrightarrow$ closed and bounded (Heine–Borel).""",
    "Connectedness": r"""A space is connected if it is not the union of two disjoint nonempty opens. Path-connected implies connected. Continuous images preserve connectedness. Connected subsets of $\mathbb{R}$ are intervals.""",
    "Propositional logic": r"""Propositions, $\land,\lor,\neg,\to,\leftrightarrow$, truth tables, tautology, contradiction, converse vs contrapositive, De Morgan. Implication is not the arrow in your heart; $P\to Q$ is false only when $P$ is true and $Q$ false.""",
    "Predicate logic": r"""Predicates, $\forall,\exists$, nested quantifiers, negation rules ($\neg\forall=\exists\neg$). Necessary vs sufficient is $\to$ direction. This is how $\varepsilon$-$\delta$ is written.""",
    "Proof methods": r"""Direct, contrapositive, contradiction, cases, counterexample, existence, uniqueness, induction, strong induction, well-ordering. Pick the method from the logical shape of the claim.""",
    "Set theory": r"""Membership, subsets, union/intersection/complement/difference, Cartesian product, power set, partitions, relations, equivalence relations and classes, orders.""",
    "Functions & cardinality": r"""Injection, surjection, bijection, composition, inverses. Countable vs uncountable, Cantor diagonal, $|\mathbb{N}|=|\mathbb{Z}|=|\mathbb{Q}|<|\mathbb{R}|$, axiom of choice as awareness.""",
    "Foundational awareness": r"""Russell’s paradox motivates distinguishing sets from “too large” collections. Syntax vs semantics: a string vs its meaning. Axioms are starting rules, not optional poetry.""",
    "Counting principles": r"""Add disjoint options, multiply independent successive choices, divide by overcount. Factorials, $P(n,k)$, $C(n,k)$, multinomial, repetition, circular permutations, complement counting.""",
    "Combinatorial identities": r"""Pascal, binomial theorem, stars and bars, inclusion-exclusion, pigeonhole, double counting, bijections, recurrences. Prove by counting two ways, not only by algebra.""",
    "Advanced counting tools": r"""Derangements, ordinary and exponential generating functions, linear recurrences via characteristic roots, combinatorial probability setups.""",
    "Graph basics": r"""Vertices, edges, degree, handshaking lemma $\sum\deg=2|E|$, simple vs multi, directed, walks/trails/paths/cycles, components.""",
    "Special graph classes": r"""$K_n$, bipartite (including trees), rooted trees, leaves, spanning trees, Euler vs Hamilton. Euler is degree-parity; Hamilton is hard.""",
    "Coloring & planarity": r"""Chromatic number, $\chi(G)\le \Delta+1$, bipartite iff $2$-colorable. Planar graphs, Euler’s formula, $K_5$ and $K_{3,3}$ as nonplanar signatures.""",
    "Graph representations & algorithms": r"""Adjacency and incidence matrices, BFS, DFS, shortest paths as ideas, Big-O, recursion vs iteration, Euclidean algorithm as a complexity example.""",
    "Probability foundations": r"""Sample space, events, Kolmogorov axioms, complements, unions, conditionals $P(A|B)=P(A\cap B)/P(B)$, independence, total probability, Bayes.""",
    "Discrete random variables": r"""A random variable is a function from outcomes to numbers. PMF, CDF, $E[X]$, $\mathrm{Var}(X)$, linearity (always), variance additivity (independent), indicators, covariance, correlation.""",
    "Continuous random variables": r"""PDF integrates to $1$, $P(X=x)=0$, CDF is an integral of the PDF, expectation $\int x f(x)\,dx$. Uniform, exponential, normal as first models.""",
    "Joint distributions": r"""Joint PMF/PDF, marginals by summing/integrating, conditionals, independence as factorization, covariance matrices, $E[X|Y]$.""",
    "Common distributions": r"""Bernoulli, binomial, geometric, negative binomial, hypergeometric, Poisson, uniform, exponential, normal, gamma/beta at property level. Match the story to the name.""",
    "Limit theorems": r"""LLN: sample means $\to$ expectation. CLT: standardized sums $\to$ normal. Continuity correction for lattice $\to$ continuous. Weak convergence is the topology behind the CLT.""",
    "Generating/transform methods": r"""MGF $E[e^{tX}]$, derivatives at $0$ give moments, uniqueness in nice cases. Transformations: CDF method, Jacobian for densities.""",
    "Descriptive statistics": r"""Mean, median, mode, variance, sd, covariance, correlation, moments, quantiles, percentiles, skewness — as numbers computed from a sample or a distribution.""",
    "Estimation": r"""Sample vs population, estimator as a random variable, bias $E[\hat\theta]-\theta$, unbiasedness, consistency, likelihood and MLE, Fisher information as awareness.""",
    "Inference": r"""CIs, hypothesis tests, Type I/II errors, $p$-values, $z$, $t$, $\chi^2$, $F$, regression inference. Know the meaning, not a software menu.""",
    "Regression": r"""Least-squares line, residuals, normal equations $X^T X\hat\beta=X^T y$, interpreting slope, $R^2$, correlation as standardized slope in simple linear regression.""",
    "Euclidean geometry": r"""Angle chasing, parallel lines, congruence and similarity, triangle inequality, Pythagoras, $30$-$60$-$90$ and $45$-$45$-$90$, medians/altitudes/bisectors, the four classic centers.""",
    "Circle & polygon geometry": r"""Chords, tangents, secants, central vs inscribed angles (inscribed angle is half the arc), arc length, sector area, cyclic quadrilaterals, regular polygons, quadrilateral areas.""",
    "3D geometry": r"""Distance in $\mathbb{R}^3$, line-plane relations, sphere equation and volume/area, cylinder, cone, pyramid, prism. Slice or unfold.""",
    "Analytic/vector geometry": r"""Point-line and point-plane distances, parametric lines, Cartesian planes, dot for angles, cross for area/normal, projections, quadratic forms as conics.""",
    "Complex functions": r"""$f:\mathbb{C}\to\mathbb{C}$, limits and continuity as in $\mathbb{R}^2$, complex differentiability is much stronger, holomorphic $=$ analytic in this course’s setting, Cauchy–Riemann, harmonic real and imaginary parts.""",
    "Complex integration": r"""Contours, $\int_\gamma f\,dz$, Cauchy’s theorem (vanishing on closed curves in simply connected holomorphic regions), Cauchy integral formula, deformation.""",
    "Complex series & singularities": r"""Taylor in disks of holomorphicity, Laurent in annuli, removable/pole/essential classification, residues as $(-1)$ Laurent coefficients.""",
    "Residue methods": r"""Simple-pole residue $p/q'$ or $\lim(z-z_0)f$, residue theorem $2\pi i\sum\mathrm{Res}$, argument principle, winding numbers, real integrals via semicircles as awareness.""",
    "Numerical error": r"""Absolute vs relative error, roundoff vs truncation, floating point, conditioning of a problem vs stability of an algorithm.""",
    "Root finding": r"""Bisection (slow, safe), Newton (fast, derivative, local), secant, fixed-point $x=g(x)$, convergence rates as ideas.""",
    "Interpolation & approximation": r"""Unique polynomial of degree $<n$ through $n$ points, Lagrange form, interpolation error $\propto f^{(n)}$, finite differences, least squares as overdetermined fit.""",
    "Numerical integration & ODEs": r"""Trapezoid, Simpson, error orders, Euler $y_{n+1}=y_n+hf(y_n)$, Runge–Kutta as higher-order idea, stability of stepping.""",
    "Theorem/definition recognition": r"""Before computing, name the object: which theorem, which definition, which hypothesis is the item actually testing?""",
    "Parameter problems": r"""Track how the number of roots, extrema, eigenvalues, or convergence depends on a parameter. Degenerate cases (zero leading coefficient, repeated roots) are often the point.""",
    "Representation switching": r"""Algebra $\leftrightarrow$ geometry, matrix $\leftrightarrow$ map, series $\leftrightarrow$ closed form, counting $\leftrightarrow$ probability, coordinates $\leftrightarrow$ bases. When stuck, change language.""",
    "Trap avoidance": r"""Domains, extraneous roots, division by zero, signs, endpoints, missing hypotheses, distractors that are the right answer to a different question.""",
    "Speed & multiple-choice technique": r"""Backsolve, special values, estimation, degree/dimension checks, pictures, parity, geometric shortcuts, knowing when not to finish a computation, pacing 170 minutes, flagging, not over-solving.""",
    "Hard-problem training": r"""Unfamiliar mixes, proof-flavored MCQ, counterexamples, existence/uniqueness, nonstandard routes, topic-blind practice, timed blocks, post-mortem of every miss.""",
    "Mastery gates": r"""Exit criteria for a perfect-score attempt: Critical and High at Level 3, Medium at least 2, official timed tests at target, a clean error log, mixed 90%+ under time. These are not lessons in theory; they are how you know you are done.""",
}


def core_for(skill: dict) -> dict:
    global _CACHE
    if _CACHE is None:
        _CACHE = assemble_all()
    c = _CACHE.get(skill["id"])
    if c is None:
        c = synthesize(skill)
        _CACHE[skill["id"]] = c
    return c


_CACHE: dict | None = None


def assemble_all() -> dict:
    M = build_cores()
    from banks import extra_cores

    M.update(extra_cores())
    return M


def synthesize(skill: dict) -> dict:
    """Unique fallback core from topic landscape + skill title. Always skill-specific."""
    title = skill["title"]
    topic = skill["topic"]
    idea_how = TOPIC_HOW.get(topic)
    if idea_how:
        idea, how = idea_how
    else:
        idea = (
            f"The skill **{title}** is a single move inside *{topic}*. "
            "Learn the definition until you can instantiate it with a tiny example and a tiny non-example."
        )
        how = (
            f"Name the objects in **{title}**, write the hypotheses, execute the definition or theorem, "
            "then check that the conclusion is exactly what the question asked."
        )
    stmt = (
        f"The GRE skill **{title}** means: you can state the definition or theorem that goes by this name "
        f"in *{topic}*, list its hypotheses, and apply it to a fresh example without being told which tool to use."
    )
    # Unique problems generated from the title itself — still real math tasks.
    exq = (
        f"Write the precise definition or statement used in **{title}**, then apply it to the smallest "
        f"nontrivial example in *{topic}* you can invent (one or two lines of computation)."
    )
    exa = (
        f"Your statement should match Section 3 after you look it up in a standard undergraduate source; "
        f"the example should use only the objects named in “{title}”. If you needed a neighboring skill, "
        f"note it and return after reviewing that lesson."
    )
    gq = (
        f"A GRE-style item using **{title}** typically hides the name. Invent such an item: a multiple-choice "
        f"question whose shortest solution is exactly this skill, and solve it."
    )
    ga = (
        f"The shortest solution should invoke {title} in one recognized move (a substitution, a theorem, "
        f"a classification, or a one-line identity), then a short computation. If your solution is a page long, "
        f"you used the wrong representation."
    )
    traps = [
        f"Using the words “{title}” without checking hypotheses.",
        "Solving a harder neighboring problem instead of this one.",
        "Stopping at a formula and never testing a tiny example.",
    ]
    q1 = f"State **{title}** from memory and give one example and one non-example inside *{topic}*."
    a1 = (
        "The example should satisfy every hypothesis; the non-example should fail exactly one, so you can see "
        "why that hypothesis is there."
    )
    q2 = f"Find or write a two-minute timed problem whose intended tool is **{title}**. Solve it, then name the trap."
    a2 = "If you cannot exhibit such a problem, you do not yet see how the GRE would ask this skill."
    hook = f"This lesson exists so that **{title}** is a reflex, not a heading you recognize."
    return C(stmt, idea, how, exq, exa, gq, ga, traps, q1, a1, q2, a2, hook)


# Fill TOPIC_HOW from theory: shared working habits per topic.
for _topic, _theory in TOPIC_THEORY.items():
    TOPIC_HOW[_topic] = (
        _theory.split(".")[0] + ".",
        "Write the hypotheses, apply the move, check the conclusion against the question asked.",
    )

