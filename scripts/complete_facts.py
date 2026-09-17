"""Unique facts M-066 through later skills."""

from __future__ import annotations


def facts() -> dict[int, dict]:
    F: dict[int, dict] = {}

    def a(n, stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2):
        F[n] = dict(stmt=stmt, exq=exq, exa=exa, gq=gq, ga=ga, trap=trap, q1=q1, a1=a1, q2=q2, a2=a2)

    # B functions 66-83
    a(66, r"A function $f:A\to B$ is a rule assigning to each $x\in A$ exactly one $f(x)\in B$. $A$ is the domain, $B$ the codomain. Two functions are equal when they have the same domain and agree pointwise.",
      r"Is $f(x)=\sqrt{x}$ a function $\mathbb{R}\to\mathbb{R}$?", r"No: domain cannot be all of $\mathbb{R}$. As $[0,\infty)\to\mathbb{R}$ it is a function.",
      r"Which graph fails the vertical line test?", r"A side-opening parabola $x=y^2$.",
      r"Calling a relation a function because it is given by a formula that is sometimes two-valued ($\pm\sqrt{\,}$).",
      r"Domain of $f(x)=1/(x-2)$ as a real function given by that formula.", r"$\mathbb{R}\setminus\{2\}$.",
      r"Are $f(x)=x$ on $\mathbb{R}$ and $g(x)=x$ on $[0,1]$ the same function?", r"No: different domains.")
    a(67, r"The natural domain of a formula is the largest subset of $\mathbb{R}$ (or $\mathbb{C}$) on which the formula makes sense. The range (image of the domain) is $\{f(x):x\in\mathrm{dom}f\}$. Codomain may be larger than the range.",
      r"Domain and range of $f(x)=\sqrt{1-x^2}$.", r"Domain $[-1,1]$, range $[0,1]$.",
      r"Range of $f(x)=e^x$ on $\mathbb{R}$.", r"$(0,\infty)$.",
      r"Confusing codomain with range; claiming $\arcsin$ has range $\mathbb{R}$.",
      r"Domain of $\ln(x-3)+\sqrt{5-x}$.", r"$(3,5]$.",
      r"Range of $x^2$ on $[-2,1]$.", r"$[0,4]$.")
    a(68, r"For $S\subset A$, the image $f(S)=\{f(x):x\in S\}$. For $T\subset B$, the preimage $f^{-1}(T)=\{x\in A:f(x)\in T\}$. Preimages always exist; inverse functions need extra hypotheses.",
      r"For $f(x)=x^2$ on $\mathbb{R}$, $f(\{-2,2\})$ and $f^{-1}(\{4\})$.", r"Image $\{4\}$; preimage $\{-2,2\}$.",
      r"$f^{-1}(\emptyset)$ is", r"$\emptyset$.",
      r"Thinking $f^{-1}(T)$ requires $f$ to be invertible.",
      r"Image of $[0,2]$ under $f(x)=x^2$.", r"$[0,4]$.",
      r"Preimage of $(0,\infty)$ under $f(x)=x^2$.", r"$\mathbb{R}\setminus\{0\}$.")
    a(69, r"$f(x)$ means the value of $f$ at $x$, not $f$ times $x$. $f(a+h)$ is evaluation at $a+h$. Parentheses are application.",
      r"If $f(x)=x^2-1$, compute $f(x+1)-f(x)$.", r"$(x^2+2x+1-1)-(x^2-1)=2x+1$.",
      r"$f(2x)$ vs $2f(x)$ for $f(x)=x^2$.", r"$4x^2$ vs $2x^2$.",
      r"Writing $f(x+y)=f(x)+f(y)$ as if it were notation rather than a property.",
      r"If $f(x)=1/x$, $f(f(x))$ for $x\neq 0$.", r"$x$.",
      r"Difference quotient $\frac{f(x+h)-f(x)}{h}$ for $f(x)=3x+2$.", r"$3$.")
    a(70, r"A piecewise function is defined by different formulas on different parts of the domain. Continuity/differentiability at junctions must be checked separately. Evaluate by identifying the piece.",
      r"$f(x)=x^2$ for $x<0$ and $2x$ for $x\ge 0$. Compute $f(-2)$ and $f(2)$.", r"$4$ and $4$.",
      r"At $x=0$ in that example, the left and right limits of $f$ are", r"$0$ and $0$, so $f$ is continuous there. Left derivative $0$, right derivative $2$, so not differentiable.",
      r"Using the wrong piece; also assuming smoothness at the joint.",
      r"$|x|$ as piecewise.", r"$-x$ for $x<0$, $x$ for $x\ge 0$.",
      r"$f(x)=1$ if $x\in\mathbb{Q}$ else $0$. Range?", r"$\{0,1\}$.")
    a(71, r"$f$ is even if $f(-x)=f(x)$ (reflection symmetry through the $y$-axis). Odd if $f(-x)=-f(x)$ (rotational symmetry $180^\circ$). Even$\cdot$even is even; odd$\cdot$odd is even; even$\cdot$odd is odd.",
      r"Is $x^3-x$ even, odd, or neither?", r"Odd.",
      r"$e^x+e^{-x}$ is", r"even (a multiple of $\cosh$).",
      r"Checking only $f(-1)=f(1)$ and declaring even.",
      r"Is $\sin x+\cos x$ odd?", r"Neither.",
      r"Product of two odd functions.", r"Even.")
    a(72, r"$f$ is periodic with period $T\neq 0$ if $f(x+T)=f(x)$ for all $x$ in the domain (suitably shifted). The fundamental period is the smallest positive $T$ if it exists. $\sin$ and $\cos$ have $2\pi$; $\tan$ has $\pi$.",
      r"Fundamental period of $\sin(2x)$.", r"$\pi$.",
      r"Period of $|\sin x|$.", r"$\pi$, not $2\pi$.",
      r"Adding periods of $\sin x$ and $\sin(\sqrt{2}x)$ and claiming a period — the sum need not be periodic.",
      r"Period of $\tan(3x)$.", r"$\pi/3$.",
      r"Is a constant function periodic?", r"Yes, every $T$ is a period; no fundamental period.")
    a(73, r"$f$ is increasing on $I$ if $x_1<x_2$ in $I$ implies $f(x_1)\le f(x_2)$ (some authors require $<$ and say strictly increasing). For differentiable $f$, $f'\ge 0$ implies increasing; the converse needs care at isolated zeros of $f'$.",
      r"Is $x^3$ strictly increasing on $\mathbb{R}$?", r"Yes, even though $f'(0)=0$.",
      r"$e^{-x}$ on $\mathbb{R}$ is", r"strictly decreasing.",
      r"Concluding not increasing because $f'$ is zero at a point.",
      r"Where is $f(x)=x^2$ increasing?", r"$[0,\infty)$.",
      r"If $f'=2x$, where is $f$ decreasing?", r"$(-\infty,0]$.")
    a(74, r"$f$ is bounded above on $S$ if some $M$ has $f(x)\le M$ for all $x\in S$. Bounded means bounded above and below. $e^{-x^2}$ is bounded on $\mathbb{R}$; $x^3$ is not.",
      r"Is $\arctan$ bounded on $\mathbb{R}$?", r"Yes: range $(-\pi/2,\pi/2)$.",
      r"Is $\tan$ bounded on $(-\pi/2,\pi/2)$?", r"No.",
      r"Confusing bounded function with bounded derivative.",
      r"Bound for $\sin x+\cos x$.", r"$\sqrt{2}$ by rewriting $R\sin(x+\phi)$.",
      r"Is $1/x$ bounded on $(0,1]$?", r"No: unbounded above.")
    a(75, r"$f:A\to B$ is injective if $f(x)=f(y)$ implies $x=y$. Equivalent: distinct inputs give distinct outputs. Horizontal line test for functions $\mathbb{R}\to\mathbb{R}$. Strict monotonicity implies injective.",
      r"Is $x^2$ injective on $\mathbb{R}$? On $[0,\infty)$?", r"No; yes.",
      r"$e^x$ is injective on $\mathbb{R}$ because", r"it is strictly increasing (or $e^x=e^y\Rightarrow x=y$).",
      r"Horizontal vs vertical line test mixup.",
      r"Is $f(x)=x^3-x$ injective on $\mathbb{R}$?", r"No: $f(0)=f(1)=f(-1)=0$.",
      r"Prove $2x+1$ is injective.", r"$2x+1=2y+1\Rightarrow x=y$.")
    a(76, r"$f:A\to B$ is surjective if for every $b\in B$ there is $a\in A$ with $f(a)=b$, i.e. the range equals the codomain. Changing the codomain can make a function surjective without changing the formula.",
      r"Is $e^x:\mathbb{R}\to\mathbb{R}$ surjective? $\mathbb{R}\to(0,\infty)$?", r"No; yes.",
      r"$x^3:\mathbb{R}\to\mathbb{R}$ is", r"bijective, hence surjective.",
      r"Claiming $x^2:\mathbb{R}\to[0,\infty)$ is not onto.",
      r"Is $\sin:\mathbb{R}\to[-1,1]$ onto?", r"Yes.",
      r"Is $\sin:\mathbb{R}\to\mathbb{R}$ onto?", r"No.")
    a(77, r"A bijection is injective and surjective. Then an inverse function $f^{-1}:B\to A$ exists and $f^{-1}\circ f=\mathrm{id}_A$, $f\circ f^{-1}=\mathrm{id}_B$. Finite sets: $|A|=|B|$ is required.",
      r"Inverse of $f(x)=2x+3$.", r"$f^{-1}(y)=(y-3)/2$.",
      r"$f(x)=x^3$ is a bijection $\mathbb{R}\to\mathbb{R}$ with inverse", r"$\sqrt[3]{x}$.",
      r"Writing inverse as $1/f(x)$.",
      r"Is $f(x)=e^x$ a bijection $\mathbb{R}\to\mathbb{R}$?", r"No. As $\mathbb{R}\to(0,\infty)$ yes, inverse $\ln$.",
      r"If $f$ is bijective, so is $f^{-1}$.", r"True.")
    a(78, r"$(g\circ f)(x)=g(f(x))$. Domain: $x$ in $\mathrm{dom} f$ and $f(x)$ in $\mathrm{dom} g$. Composition is associative, not commutative. Identity function is a two-sided identity for $\circ$.",
      r"If $f(x)=x+1$, $g(x)=x^2$, then $(g\circ f)(x)$ and $(f\circ g)(x)$.", r"$(x+1)^2$ vs $x^2+1$.",
      r"$(f\circ f)(x)$ for $f(x)=1-x$.", r"$x$. Order $2$.",
      r"Computing $g(f(x))$ as $g(x)f(x)$.",
      r"$f(x)=\sqrt{x}$, $g(x)=x-3$, domain of $g\circ f$.", r"$[0,\infty)$, but $f\circ g$ has domain $[3,\infty)$.",
      r"Is composition of injections an injection?", r"Yes.")
    a(79, r"If $f:A\to B$ is bijective, $f^{-1}$ is the unique function $B\to A$ with $f(f^{-1}(y))=y$ and $f^{-1}(f(x))=x$. Graph of $f^{-1}$ is the reflection of the graph of $f$ across $y=x$. To compute: set $y=f(x)$, solve for $x$.",
      r"Inverse of $f(x)=\ln(x-1)$ on $(1,\infty)$.", r"$f^{-1}(y)=e^y+1$.",
      r"If $f(2)=5$ and $f$ is invertible, $f^{-1}(5)=$", r"$2$.",
      r"Inverting $y=x^2$ on $\mathbb{R}$ without restricting domain.",
      r"Inverse of $f(x)=\dfrac{x}{x-1}$ for $x\neq 1$.", r"$f^{-1}(y)=\dfrac{y}{y-1}$ (same formula), domain $y\neq 1$.",
      r"Does every injection $\mathbb{R}\to\mathbb{R}$ have an inverse onto $\mathbb{R}$?", r"No: it has an inverse onto its range, which may be smaller.")
    a(80, r"$\mathrm{dom}(g\circ f)=\{x\in\mathrm{dom}f: f(x)\in\mathrm{dom}g\}$. Range of $g\circ f$ is $g(f(\mathrm{dom}(g\circ f)))\subset\mathrm{range}(g)$.",
      r"Domain of $\ln(\sin x)$.", r"$\sin x>0$, so $(2k\pi,(2k+1)\pi)$ wait: $\sin>0$ on $(2k\pi, (2k+1)\pi)$. Yes.",
      r"Range of $\sin(\ln x)$ for $x>0$.", r"$[-1,1]$, because $\ln$ hits all reals.",
      r"Taking domain of $g\circ f$ as $\mathrm{dom}g\cap\mathrm{dom}f$.",
      r"Domain of $\sqrt{1-e^x}$.", r"$e^x\le 1$, $x\le 0$.",
      r"Domain of $1/\ln(x-2)$.", r"$x>2$ and $x\neq 3$.")
    a(81, r"A functional equation is an equation whose unknown is a function. GRE typical: $f(x)+f(1-x)=x$, Cauchy $f(x+y)=f(x)+f(y)$ with extra regularity, or $f(f(x))=x$. Solve by substitution, assuming forms, or plugging special values.",
      r"If $f(x)+f(1-x)=x^2$ and $f$ is a polynomial of degree $2$, find $f(1/2)$.", r"Set $x=1/2$: $2f(1/2)=1/4$, $f(1/2)=1/8$.",
      r"$f(f(x))=x$ means $f$ is", r"an involution: a bijection equal to its inverse.",
      r"Assuming $f$ is linear without justification when infinitely many solutions exist.",
      r"Solve $f(x)+f(-x)=2x^2$ if $f$ is even.", r"Even implies $f(-x)=f(x)$, so $2f(x)=2x^2$, $f(x)=x^2$.",
      r"If $f(x+1)=f(x)+2$ and $f(0)=3$, $f(n)$ for $n\in\mathbb{N}$.", r"$f(n)=3+2n$ if we assume this on $\mathbb{N}$.")
    a(82, r"Nested evaluation: compute inside-out. $f(f(x))$ uses the same rule twice. Watch piecewise: the inner value determines which piece the outer uses.",
      r"If $f(x)=2x+1$, $f(f(f(0)))$.", r"$f(0)=1$, $f(1)=3$, $f(3)=7$.",
      r"$f(x)=1-x$, $f^{\circ 100}(x)$ (100-fold composition).", r"$x$, because $f\circ f=\mathrm{id}$.",
      r"Applying the outer piece based on $x$ instead of $f(x)$.",
      r"$f(x)=x^2-2$, $f(f(2))$.", r"$f(2)=2$, $f(2)=2$.",
      r"If $f(n)=n/2$ for even $n$ and $3n+1$ for odd, $f(f(3))$.", r"$f(3)=10$, $f(10)=5$.")
    a(83, r"From algebra read geometry: degree, leading coefficient (end behavior), roots (x-intercepts), $f(0)$ (y-intercept), sign of $f'$, even/odd, asymptotes of rationals. Conversely, a graph constrains possible formulas.",
      r"End behavior of $-2x^3+x$.", r"As $x\to\infty$, $f\to-\infty$; as $x\to-\infty$, $f\to+\infty$.",
      r"A graph symmetric about the origin is", r"odd (if it is a function).",
      r"Reading a horizontal asymptote as a value the function never crosses (it can).",
      r"Possible formula for a parabola through origin opening down.", r"$-ax^2$ with $a>0$, or $-a(x-h)^2+k$ if not vertex at origin — through origin opening down: e.g. $-x^2+x$.",
      r"If $f$ has a vertical asymptote at $x=2$ and $f(x)\to 3$ as $x\to\infty$, what kind of function?", r"Rational with factor $x-2$ in the denominator and degree numerator $\le$ degree denominator, horizontal asymptote $y=3$.")

    # B transformations 84-90
    a(84, r"$y=f(x-h)+k$ shifts the graph of $f$ right by $h$ and up by $k$. Inside the function does the opposite of the sign you feel: $f(x-2)$ is right, not left.",
      r"Shift $y=\sqrt{x}$ right $3$ and down $1$.", r"$y=\sqrt{x-3}-1$.",
      r"$y=(x+4)^2$ vs $y=x^2$ is a shift", r"left by $4$.",
      r"Shifting $f(x+h)$ to the right.",
      r"Vertex of $y=(x-2)^2+5$.", r"$(2,5)$.",
      r"$y=\ln(x+e)$ shifts $\ln x$ how?", r"Left by $e$.")
    a(85, r"$y=-f(x)$ reflects through the $x$-axis. $y=f(-x)$ reflects through the $y$-axis. $y=-f(-x)$ is $180^\circ$ rotation about the origin (odd-type flip).",
      r"Reflect $y=e^x$ through the $y$-axis.", r"$y=e^{-x}$.",
      r"The graph of $y=-|x|$ is", r"$|x|$ flipped over the $x$-axis (a downward V).",
      r"Mixing $f(-x)$ and $-f(x)$.",
      r"Reflection of $y=\sqrt{x}$ across $y$-axis.", r"$y=\sqrt{-x}$, domain $x\le 0$.",
      r"If $f$ is even, $f(-x)$ vs $f(x)$.", r"The same graph.")
    a(86, r"$y=cf(x)$ with $|c|>1$ stretches vertically; $0<|c|<1$ compresses. $y=f(ax)$: $|a|>1$ compresses horizontally toward the $y$-axis; $0<|a|<1$ stretches horizontally. $a<0$ includes a $y$-axis reflection.",
      r"$y=\sin(2x)$ compared to $\sin x$.", r"Horizontal compression by $1/2$ (period $\pi$).",
      r"$y=3\sin x$ has amplitude", r"$3$.",
      r"Thinking $f(2x)$ stretches horizontally.",
      r"$y=(2x)^2$ vs $4x^2$.", r"They are the same: horizontal compress by $1/2$ equals vertical stretch by $4$ for this parabola.",
      r"$f(x/2)$ vs $f(x)$.", r"Horizontal stretch by $2$.")
    a(87, r"A general transformation $y=c\,f(a(x-h))+k$ is done in a consistent order: horizontal shift/scale inside, then vertical scale/reflect, then vertical shift. Drawing reference points is safer than memorizing a slogan.",
      r"Describe $y=2\sqrt{x-1}+3$.", r"Start from $\sqrt{x}$, shift right $1$, stretch vertically by $2$, shift up $3$.",
      r"$y=-\sin(x-\pi/2)$ equals", r"$-\cos x$, or a shift of sine then flip.",
      r"Doing vertical shift before vertical stretch when the formula is $c f+k$ — actually stretch first then shift is correct for $cf+k$. Doing shift first is wrong.",
      r"Sequence for $y=-(x+2)^2-1$.", r"Shift left $2$, reflect $x$-axis, down $1$.",
      r"A point $(1,1)$ on $y=f(x)$ goes where on $y=2f(x-3)$?", r"$(4,2)$.")
    a(88, r"Even $\Leftrightarrow$ symmetry about $y$-axis. Odd $\Leftrightarrow$ symmetry about the origin. $f(a+x)=f(a-x)$ is symmetry about the line $x=a$. Periodic symmetry repeats.",
      r"Symmetry of $y=\cos x$.", r"Even: $y$-axis. Also periodic.",
      r"$y=(x-1)^3$ is symmetric about", r"the point $(1,0)$, not the origin.",
      r"Calling a graph even because it looks balanced left-right after a shift — evenness is specifically $y$-axis.",
      r"Is $x^4-x^2$ even?", r"Yes.",
      r"A graph symmetric about $x=2$ corresponds to evenness of", r"$g(t)=f(t+2)$ in the variable $t$.")
    a(89, r"The graph of $y=f^{-1}(x)$ is the reflection of $y=f(x)$ across $y=x$. Domain and range swap. Tangents: if $f'(a)=m\neq 0$, then $(f^{-1})'(f(a))=1/m$.",
      r"Reflect $y=e^x$ across $y=x$.", r"$y=\ln x$.",
      r"If $f(3)=8$ and $f'(3)=4$, then $(f^{-1})'(8)=$", r"$1/4$.",
      r"Reflecting across $y=0$ or $x=0$ instead of $y=x$.",
      r"The inverse of $y=\sqrt{x}$ (domain $[0,\infty)$) graphs as", r"$y=x^2$ restricted to $x\ge 0$.",
      r"Why must $f'$ be nonzero to invert locally?", r"Horizontal tangent $\Rightarrow$ not locally injective.")
    a(90, r"Combine transformations by composing the corresponding maps on the $x$ and $y$ coordinates. Factor constants: $f(2x-6)=f(2(x-3))$ is compress by $1/2$ then shift right $3$ (or shift first by $6$ then compress — order matters unless you rewrite).",
      r"Rewrite $f(2x-6)$ to see the shift.", r"$f(2(x-3))$: shift right $3$, horizontal compress $1/2$.",
      r"$2f(x-1)+4$ applied to point $(1,5)$ on $y=f(x)$ goes to", r"$(2,14)$.",
      r"Shifting by $6$ after compressing by $2$ without rewriting $2x-6=2(x-3)$.",
      r"Simplify $-(2(x+1))^2$.", r"$-4(x+1)^2$: left $1$, vertical stretch $4$, $x$-axis flip.",
      r"Two routes for $f(ax-b)$ that agree.", r"Factor $a(x-b/a)$: shift $b/a$ then scale $a$, versus scale then shift $b$.")

    # B families 91-100
    a(91, r"A polynomial function is $p(x)=a_n x^n+\cdots+a_0$. Continuous everywhere, differentiable everywhere, end behavior ruled by $a_n x^n$, at most $n$ roots unless identically zero.",
      r"End behavior of $p(x)=-x^4+3x$.", r"Both ends $\to-\infty$.",
      r"A cubic always has how many real roots counting multiplicity?", r"At least one real; three real counting multiplicity only if the other two are real — always three complex. Real count: 1 or 3.",
      r"Treating a polynomial as having vertical asymptotes.",
      r"How many turning points can a degree $4$ polynomial have?", r"At most $3$.",
      r"$p(x)=x^2+1$ roots over $\mathbb{R}$?", r"None.")
    a(92, r"A rational function $p/q$ in lowest terms has vertical asymptotes (or holes) at zeros of $q$, and a horizontal or oblique asymptote from comparing degrees.",
      r"Asymptotes of $f(x)=\dfrac{x^2-1}{x-1}$.", r"Hole at $x=1$, no vertical asymptote; $f(x)=x+1$ for $x\neq 1$, so oblique $y=x+1$.",
      r"$y=\dfrac{2x}{x-3}$ has horizontal asymptote", r"$y=2$ and vertical $x=3$.",
      r"Canceling first and forgetting a hole vs an asymptote.",
      r"End behavior of $\dfrac{x^3}{x^2+1}$.", r"Like $x$, oblique/slant $y=x$.",
      r"Domain of $\dfrac{x}{x^2-4}$.", r"$\mathbb{R}\setminus\{\pm 2\}$.")
    a(93, r"Power functions $x^a$ for real $a$: domain depends on $a$ (even/odd integers vs rationals vs irrationals). $x^{-1}$ is $1/x$; $x^{1/2}$ is $\sqrt{x}$.",
      r"Domain of $x^{1/2}$ vs $x^{1/3}$ vs $x^{-2}$.", r"$[0,\infty)$; $\mathbb{R}$; $\mathbb{R}\setminus\{0\}$.",
      r"$x^{2/3}$ at $x=-8$.", r"$(x^2)^{1/3}=4$ or $(x^{1/3})^2=4$.",
      r"Writing $(-8)^{1/2}$ as real.",
      r"Compare $x^2$ and $x^4$ on $(0,1)$.", r"$x^2>x^4$.",
      r"Derivative of $x^a$ for $x>0$.", r"$a x^{a-1}$.")
    a(94, r"Root functions $\sqrt[n]{x}$: even $n$ need $x\ge 0$; odd $n$ allow all reals. $\sqrt{x^2}=|x|$. Compositions like $\sqrt{1-x^2}$ are semicircle graphs.",
      r"Graph of $y=\sqrt{x+4}$.", r"$\sqrt{x}$ shifted left $4$, domain $[-4,\infty)$.",
      r"$\sqrt[3]{-8}$.", r"$-2$.",
      r"Simplifying $\sqrt{x^2}$ to $x$.",
      r"Domain of $\sqrt{x^2-9}$.", r"$(-\infty,-3]\cup[3,\infty)$.",
      r"Solve $\sqrt{x}=x-2$.", r"$x=4$ (check; $x=1$ extraneous).")
    a(95, r"$y=|x|$ is even, V-shaped, derivative $\mathrm{sgn}(x)$ for $x\neq 0$, not differentiable at $0$. $|f|$ folds the negative part of $f$ above the $x$-axis.",
      r"Graph $y=|x-2|-1$.", r"V with vertex $(2,-1)$.",
      r"$|x|+|x-1|$ is linear on", r"$(-\infty,0]$, $[0,1]$, $[1,\infty)$ with kinks at $0,1$.",
      r"Differentiating $|x|$ at $0$.",
      r"Solve $|2x-4|=6$.", r"$x=5$ or $x=-1$.",
      r"Range of $|x^2-1|$.", r"$[0,\infty)$.")
    a(96, r"$f(x)=a^x$ for $a>0$, $a\neq 1$: domain $\mathbb{R}$, range $(0,\infty)$, $y$-intercept $1$, horizontal asymptote $y=0$. Increasing iff $a>1$. $e^x$ is the calculus exponential.",
      r"Solve $2^x=1/8$.", r"$x=-3$.",
      r"$y=(1/2)^x$ as $x\to\infty$.", r"$\to 0$.",
      r"Thinking $a^x$ is defined for $a<0$ as a real function of a real variable in general.",
      r"Intercept of $y=3^{x}-1$.", r"$x$-intercept $0$, $y$-intercept $0$ wait: $3^0-1=0$, so through origin. $y$-intercept $0$.",
      r"$e^{x}+e^{-x}$ is always at least", r"$2$.")
    a(97, r"$y=\log_a x$: domain $(0,\infty)$, range $\mathbb{R}$, $x$-intercept $1$, vertical asymptote $x=0$. Inverse of $a^x$. Increasing iff $a>1$.",
      r"Domain of $y=\ln(2-x)$.", r"$x<2$.",
      r"Asymptote of $y=\log_2(x+3)$.", r"$x=-3$ vertical.",
      r"Including $x=0$ in the domain of $\log$.",
      r"Solve $\log_3 x=-2$.", r"$x=1/9$.",
      r"Range of $\ln(x^2+1)$.", r"$[0,\infty)$.")
    a(98, r"Step functions (Heaviside, floor as a staircase, GRE piecewise constants) jump. They are discontinuous at jumps and constant on open intervals between jumps.",
      r"Sketch $f(x)=\lfloor x\rfloor$ on $[-2,2)$.", r"Steps at integers, left-closed/right-open if using $\lfloor x\rfloor=n$ on $[n,n+1)$.",
      r"The Heaviside step $H(x)=0$ for $x<0$ and $1$ for $x\ge 0$ has a jump of size", r"$1$ at $0$.",
      r"Calling a step function differentiable at the jump.",
      r"$u(x-2)$ turns on at", r"$x=2$.",
      r"Integral of a unit step from $-1$ to $1$.", r"$1$ if $H(0)=1$ includes half? From $-1$ to $1$: length $1$ on the positive side, so $1$.")
    a(99, r"Composition of families: $\ln(\sin x)$ needs $\sin x>0$; $e^{\cos x}$ is entire and even in a periodic way; polynomials of exponentials stay positive, etc. Track domain first, then range.",
      r"Range of $e^{-x^2}$.", r"$(0,1]$.",
      r"Domain of $\arcsin(2x)$.", r"$x\in[-1/2,1/2]$.",
      r"Composing without restricting to the inner range inside the outer domain.",
      r"Range of $\sin(e^x)$.", r"$[-1,1]$ because $e^x$ covers $(0,\infty)$, which is more than a full period infinitely often.",
      r"Domain of $\sqrt{\ln x}$.", r"$x\ge 1$.")
    a(100, r"Qualitative graphing checklist: domain, intercepts, symmetries, asymptotes, critical points, concavity, end behavior. Zeros of numerator vs denominator decide intercepts vs asymptotes.",
      r"Intercepts of $y=\dfrac{x-2}{x+1}$.", r"$x$-intercept $2$, $y$-intercept $-2$.",
      r"A rational function with a hole at $x=1$ and no other denominator zeros has how many vertical asymptotes?", r"Zero.",
      r"Plotting a hole as an asymptote.",
      r"End behavior of $\dfrac{3x^2}{x^2+1}$.", r"$y\to 3$.",
      r"How many real zeros can $\dfrac{x^2+1}{x}$ have?", r"None.")

    # B sequences 101-110
    a(101, r"An arithmetic sequence has constant difference $d$: $a_n=a_1+(n-1)d$.",
      r"$a_1=3$, $d=5$, $a_{10}$.", r"$3+9\cdot 5=48$.",
      r"The $n$th term of $7,3,-1,\ldots$ is", r"$7+(n-1)(-4)=11-4n$.",
      r"Using $a_n=a_1+nd$ off-by-one.",
      r"Is $2,3,5,8$ arithmetic?", r"No.",
      r"Find $d$ if $a_3=10$, $a_7=22$.", r"$d=3$.")
    a(102, r"A geometric sequence has constant ratio $r$: $a_n=a_1 r^{n-1}$.",
      r"$a_1=3$, $r=2$, $a_6$.", r"$3\cdot 2^5=96$.",
      r"$2, -6, 18, -54$ has $r=$", r"$-3$.",
      r"Ratio $a_{n+1}/a_n$ when terms can be zero.",
      r"Geometric with $a_2=6$, $a_4=54$, find possible $r$.", r"$r^2=9$, $r=\pm 3$.",
      r"$a_n=5\cdot (1/2)^{n-1}$, $a_5$.", r"$5/16$.")
    a(103, r"An explicit formula gives $a_n$ directly. A recursive formula gives $a_{n}$ from previous terms plus initial conditions. Closed forms solve recurrences.",
      r"$a_1=1$, $a_{n+1}=a_n+2$. Explicit?", r"$a_n=2n-1$.",
      r"Fibonacci $F_1=F_2=1$, $F_{n}=F_{n-1}+F_{n-2}$ is", r"recursive, not explicit (Binet is explicit).",
      r"A recurrence without enough initial conditions.",
      r"$a_n=n^2$ recursively?", r"$a_1=1$, $a_{n+1}=a_n+2n+1$.",
      r"Which is explicit: $a_n=3^n$ or $a_{n+1}=3a_n$?", r"The first.")
    a(104, r"The sum of an arithmetic series $a_1+\cdots+a_n=n(a_1+a_n)/2=n(2a_1+(n-1)d)/2$.",
      r"$1+2+\cdots+100$.", r"$5050$.",
      r"$5+9+13+\cdots$ (20 terms).", r"$20/2\cdot(5+81)=860$. $a_{20}=5+19\cdot 4=81$.",
      r"Using $n$ terms when the last index is not $n$.",
      r"Sum of first $n$ odd numbers.", r"$n^2$.",
      r"$10+20+\cdots+100$.", r"$10(1+\cdots+10)=550$.")
    a(105, r"Finite geometric sum $a+ar+\cdots+ar^{n-1}=a\dfrac{1-r^n}{1-r}$ for $r\neq 1$, and $na$ if $r=1$.",
      r"$1+2+4+\cdots+2^{9}$.", r"$2^{10}-1=1023$.",
      r"Sum of $3+3\cdot\frac12+\cdots+3\cdot(\frac12)^{5}$.", r"$3\dfrac{1-(1/2)^6}{1/2}=6(1-1/64)=6\cdot 63/64$.",
      r"Using the infinite-sum formula on a finite sum.",
      r"$1-1+1-1$ (10 terms).", r"$0$.",
      r"Sum $x+x^2+\cdots+x^n$.", r"$x\dfrac{1-x^n}{1-x}$ for $x\neq 1$.")
    a(106, r"Infinite geometric series $\sum_{n=0}^\infty ar^n=\dfrac{a}{1-r}$ iff $|r|<1$. Diverges if $|r|\ge 1$ (except $a=0$).",
      r"$1+1/2+1/4+\cdots$.", r"$2$.",
      r"$\sum_{n=1}^\infty (2/3)^n$.", r"First term $2/3$, ratio $2/3$, sum $2$.",
      r"Using $1/(1-r)$ when $|r|\ge 1$.",
      r"$0.999\ldots$ as a geometric series.", r"$9/10+9/100+\cdots=1$.",
      r"Does $\sum (-1/2)^n$ from $n=0$ converge?", r"Yes, to $2/3$.")
    a(107, r"$\sum_{k=1}^n a_k$ is a compact loop. Index shifts: $\sum_{k=0}^n a_{k+1}=\sum_{j=1}^{n+1}a_j$. Linearity of summation is free.",
      r"Write $1^2+2^2+3^2$ in sigma notation.", r"$\sum_{k=1}^3 k^2$.",
      r"$\sum_{k=1}^n 1$.", r"$n$.",
      r"Off-by-one in changing indices.",
      r"$\sum_{k=1}^5 (2k-1)$.", r"$25$.",
      r"Split $\sum (a_k+b_k)$.", r"$\sum a_k+\sum b_k$.")
    a(108, r"A telescoping sum cancels internally: $\sum (b_k-b_{k+1})=b_1-b_{n+1}$. Partial fractions often create telescopes.",
      r"$\sum_{k=1}^n \left(\dfrac{1}{k}-\dfrac{1}{k+1}\right)$.", r"$1-\dfrac{1}{n+1}$.",
      r"$\sum_{k=1}^\infty \dfrac{1}{k(k+1)}$.", r"$1$.",
      r"Forgetting the leftover first and last terms.",
      r"Evaluate $\sum_{k=2}^5 (k^2-(k+1)^2)$.", r"$2^2-6^2=-32$.",
      r"Partial fractions for $1/(k(k+2))$.", r"$(1/2)(1/k-1/(k+2))$, telescope in two streams.")
    a(109, r"A simple linear recurrence $a_{n+1}=pa_n+q$. If $p\neq 1$, equilibrium $q/(1-p)$; homogeneous solution $A p^n$; particular constant. Solve with initial $a_0$.",
      r"$a_{n+1}=3a_n$, $a_0=2$.", r"$a_n=2\cdot 3^n$.",
      r"$a_{n+1}=a_n+4$, $a_0=1$.", r"$a_n=1+4n$.",
      r"Solving as geometric when there is a constant term without finding equilibrium.",
      r"$a_{n+1}=2a_n+1$, $a_0=0$.", r"$a_n=2^n-1$.",
      r"Closed form of $a_{n+1}=a_n/2$, $a_0=5$.", r"$5\cdot 2^{-n}$.")
    a(110, r"Guess-and-verify: conjecture a closed form from the first terms, then prove by induction using the recurrence. Polynomial guess for arithmetic-like, exponential for geometric-like.",
      r"$a_1=1$, $a_{n+1}=a_n+n$. Guess $a_n$.", r"$a_n=1+\sum_{k=1}^{n-1}k=1+\dfrac{(n-1)n}{2}$. Verify.",
      r"If $a_n=n\cdot a_{n-1}$, $a_1=1$, then $a_n=$", r"$n!$.",
      r"Guessing from three terms a degree that is too low.",
      r"$a_{n}=a_{n-1}+2n-1$, $a_1=1$. Closed form?", r"$n^2$ (odd numbers).",
      r"Verify $a_n=2^n-1$ satisfies $a_{n}=2a_{n-1}+1$, $a_1=1$.", r"$2(2^{n-1}-1)+1=2^n-1$, and $a_1=1$.")

    return F
