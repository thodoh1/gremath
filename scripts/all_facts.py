"""Unique facts for remaining GRE math skills, keyed by n."""

from __future__ import annotations


def facts() -> dict[int, dict]:
    F: dict[int, dict] = {}

    def a(n, stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2):
        F[n] = dict(stmt=stmt, exq=exq, exa=exa, gq=gq, ga=ga, trap=trap, q1=q1, a1=a1, q2=q2, a2=a2)

    # A inequality techniques 48-55
    a(48, r"AM-GM: for $x_i\ge 0$, $\frac{x_1+\cdots+x_n}{n}\ge\sqrt[n]{x_1\cdots x_n}$, equality iff all $x_i$ equal (or a zero in a way that both sides vanish when $n\ge 1$ with zeros).",
      r"Minimize $x+1/x$ for $x>0$.", r"AM-GM: $x+1/x\ge 2\sqrt{x\cdot 1/x}=2$, equality at $x=1$.",
      r"For $a,b>0$, $\frac{a}{b}+\frac{b}{a}$ is at least", r"$2$, equality $a=b$.",
      r"Applying AM-GM to negative numbers.",
      r"Show $x^2+y^2\ge 2xy$.", r"$(x-y)^2\ge 0$, or AM-GM on $x^2,y^2$ if nonnegative — actually $x^2+y^2-2xy=(x-y)^2$ is better and works for all reals.",
      r"Equality case of AM-GM on $3$ positive numbers.", r"All three equal.")
    a(49, r"Cauchy–Schwarz: $(\sum a_i b_i)^2\le(\sum a_i^2)(\sum b_i^2)$, equality iff the vectors are parallel. Engel form: $\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$ for $b_i>0$.",
      r"Prove $(a^2+b^2)(c^2+d^2)\ge(ac+bd)^2$.", r"This is Cauchy on $(a,b)$ and $(c,d)$.",
      r"$(1^2+1^2)(x^2+y^2)\ge(x+y)^2$ says", r"$x^2+y^2\ge\frac{(x+y)^2}{2}$, i.e. QM-AM on two terms.",
      r"Forgetting equality is parallel vectors, including the zero vector.",
      r"Apply Cauchy to $(1,1,1)$ and $(x,y,z)$.", r"$(x+y+z)^2\le 3(x^2+y^2+z^2)$.",
      r"When does equality hold in Cauchy for $(1,2)$ and $(3,6)$?", r"They are parallel, so yes.")
    a(50, r"Triangle inequality: $|x+y|\le|x|+|y|$ on $\mathbb{R}$ or $\mathbb{C}$ or in a normed space. Reverse: $|\,|x|-|y|\,|\le|x-y|$.",
      r"Show $|x-3|\ge|x|-3$.", r"Reverse triangle.",
      r"The set of $z\in\mathbb{C}$ with $|z-1|+|z+1|=2$ is", r"the segment $[-1,1]$ on the real axis (equality in triangle).",
      r"Using $|x+y|=|x|+|y|$ as if it were always true.",
      r"Prove $|a-b|\le|a|+|b|$.", r"Replace $y$ by $-b$.",
      r"Can $|x+y+z|=|x|+|y|+|z|$ if $x,y,z$ are not all same sign?", r"Only if the ones that break same-direction are zero.")
    a(51, r"Jensen: if $\phi$ is convex on an interval, $\phi(\sum \lambda_i x_i)\le\sum\lambda_i\phi(x_i)$ for $\lambda_i\ge 0$, $\sum\lambda_i=1$. Concave reverses. Intuition: the graph lies above tangents / below chords for convex $\phi$.",
      r"Why is $\frac{e^a+e^b}{2}\ge e^{(a+b)/2}$?", r"$e^x$ is convex, Jensen with equal weights.",
      r"$\ln$ is concave, so $\ln(\frac{x+y}{2})\ge$", r"$\frac{\ln x+\ln y}{2}$ for $x,y>0$, which is AM-GM in log form.",
      r"Applying Jensen to a function that is neither convex nor concave on the interval used.",
      r"Is $x^2$ convex on $\mathbb{R}$?", r"Yes, $f''=2>0$.",
      r"Jensen for $1/x$ on $(0,\infty)$: compare $\frac12(1/x+1/y)$ to $1/\frac{x+y}{2}$.", r"$1/x$ is convex, so the first is larger: harmonic-AM.")
    a(52, r"Bounding by squares: $2|ab|\le a^2+b^2$, or $0\le(a-b)^2$. Many GRE bounds are this identity in costume.",
      r"Show $x^2+y^2+z^2\ge xy+yz+zx$.", r"Multiply by 2: $(x-y)^2+(y-z)^2+(z-x)^2\ge 0$.",
      r"A cheap upper bound for $2xy$ when $x^2+y^2=1$ is", r"$1$, because $2|xy|\le x^2+y^2=1$.",
      r"Using $2xy\le x^2+y^2$ without absolute values when $xy$ may be negative (still true!).",
      r"Maximize $xy$ on $x^2+y^2=4$.", r"$xy\le 2$ by AM-GM on $x^2,y^2$ or Cauchy.",
      r"Prove $n^2+1\ge n$ for $n\in\mathbb{Z}$.", r"$(n-1/2)^2\ge 0$ is overkill; $(n-1)n+1\ge 1$ or just cases.")
    a(53, r"Completing-square bounds turn a quadratic into a visible square plus constant, hence a min/max without calculus.",
      r"Bound $x^2-4x+9$.", r"$(x-2)^2+5\ge 5$.",
      r"The range of $x+\frac{4}{x}$ for $x>0$ via completing/AM-GM is", r"$[4,\infty)$.",
      r"Completing the square but dropping the remaining constant.",
      r"Min of $2x^2+12x+20$.", r"$2(x+3)^2+2$, min $2$.",
      r"Show $x^2+2x+2$ never zero over $\mathbb{R}$.", r"$(x+1)^2+1\ge 1$.")
    a(54, r"Symmetric inequalities often reduce by setting $s=x+y$, $p=xy$, or assuming $xyz=1$, or WLOG $x\ge y\ge z$ after homogenizing.",
      r"If $x,y>0$ and $xy=1$, minimize $x+y$.", r"$x+1/x\ge 2$.",
      r"For $x+y+z=3$, $xyz=1$, $x,y,z>0$, AM-GM says", r"$1\ge 1$ with equality at $x=y=z=1$; the constraint is the equality case.",
      r"Substituting and changing the feasible region (losing $x,y>0$).",
      r"Reduce $x^3+y^3$ given $x+y=2$.", r"$x^3+y^3=(x+y)(x^2-xy+y^2)=2((x+y)^2-3xy)=2(4-3xy)$.",
      r"Why set $t=x+1/x$ for recursive inequalities?", r"Because $x^2+1/x^2=t^2-2$, etc.")
    a(55, r"Always track equality: it tells you whether a bound is achieved (so a max exists) or is only approached (so a sup, not a max).",
      r"Does $x+\frac{1}{x}$ for $x>0$ achieve $2$?", r"Yes, at $x=1$.",
      r"Does $\frac{x}{1+x}$ for $x>0$ achieve $1$?", r"No: it approaches $1$ but never reaches it. Max does not exist; sup is $1$.",
      r"Reporting a bound as a maximum when equality is impossible in the domain.",
      r"Equality in Cauchy for $(1,0)$ and $(2,0)$.", r"Parallel, equality holds.",
      r"Can $e^{-x}$ for $x\ge 0$ equal $0$?", r"No. Infimum $0$, not a minimum.")

    # A polynomials 56-65
    a(56, r"Degree of a nonzero polynomial is the largest exponent with nonzero coefficient. Leading coefficient is that coefficient. $\deg(fg)=\deg f+\deg g$, $\deg(f+g)\le\max(\deg f,\deg g)$.",
      r"Degree of $3x^5-x+7$.", r"$5$, leading coefficient $3$.",
      r"$\deg(x^2+1)+\deg(x^3-x)$ vs $\deg((x^2+1)(x^3-x))$", r"$2+3=5$, and the product has degree $5$.",
      r"Calling the zero polynomial degree $0$ (it is often $-\infty$ or undefined).",
      r"Degree of $(x^2+1)^3$.", r"$6$.",
      r"Can $\deg(f+g)<\max(\deg f,\deg g)$?", r"Yes, if leading terms cancel.")
    a(57, r"$r$ is a zero of multiplicity $k$ if $(x-r)^k$ divides $p$ but $(x-r)^{k+1}$ does not. The graph of a real polynomial touches and turns back at even multiplicity, crosses at odd.",
      r"Multiplicity of $x=1$ in $(x-1)^3(x+2)$.", r"$3$.",
      r"If $p$ has a double root at $0$ and $p(x)=x^4+ax^3+bx^2+c$, then", r"$c=0$ and the $x$ coefficient is $0$, so $p(x)=x^2(x^2+ax+b)$ already from $c=0$; double root also needs $p'(0)=0$ which kills a possible $x$ term — here there is none, so $c=0$ is the constant; wait $p(0)=c=0$ and $p'(0)=0$ automatic if no $x$ term. The given form has no $x$ term, so double root at $0$ iff $c=0$.",
      r"Confusing multiplicity with the number of distinct roots.",
      r"Write a cubic with a double root at $2$ and a simple root at $0$.", r"$x(x-2)^2$.",
      r"Does $p(x)=(x-1)^2(x-1)$ have a root of multiplicity $2$ or $3$?", r"$3$.")
    a(58, r"Factor theorem: $p(r)=0$ iff $(x-r)$ divides $p(x)$.",
      r"Show $x-1$ divides $x^3-1$.", r"$p(1)=0$.",
      r"If $p(2)=0$ and $\deg p=3$, then $p(x)=(x-2)q(x)$ with", r"$\deg q=2$.",
      r"Concluding $p$ has no real roots from $p(0)\neq 0$.",
      r"Does $x+2$ divide $x^3+8$?", r"Yes, $p(-2)=0$.",
      r"If $p(a)=p(b)=0$ and $a\neq b$, then $(x-a)(x-b)$ divides $p$.", r"True.")
    a(59, r"Remainder theorem: the remainder of $p$ divided by $x-c$ is $p(c)$, a constant.",
      r"Remainder of $x^{10}-3$ divided by $x-1$.", r"$1-3=-2$.",
      r"Remainder of $x^2+x+1$ divided by $x+1$.", r"$p(-1)=1-1+1=1$.",
      r"Using $p(-c)$ when dividing by $x+c$ incorrectly (for $x+c=x-(-c)$, it is $p(-c)$ — that one is correct; the trap is $p(c)$).",
      r"Remainder of $2x^3-4$ by $x-2$.", r"$16-4=12$.",
      r"If $p(x)=(x-3)q(x)+7$, then $p(3)=$?", r"$7$.")
    a(60, r"Fundamental theorem of algebra: a nonconstant polynomial of degree $n$ with complex coefficients has exactly $n$ roots in $\mathbb{C}$, counting multiplicity. Equivalently, it factors as $c(x-r_1)\cdots(x-r_n)$.",
      r"How many complex roots has $x^4+1$?", r"Four.",
      r"A real cubic always has", r"at least one real root (odd degree), and three complex roots counting multiplicity.",
      r"Reading FTA as ‘$n$ distinct real roots’.",
      r"Write $x^2+1$ as a product of complex linears.", r"$(x-i)(x+i)$.",
      r"Can a degree $4$ real polynomial have no real roots?", r"Yes: $(x^2+1)^2$.")
    a(61, r"If $p$ has real coefficients and $p(z)=0$, then $p(\bar z)=0$. Nonreal roots come in conjugate pairs. Hence odd-degree real polynomials have at least one real root.",
      r"If $1+i$ is a root of a real polynomial, so is", r"$1-i$.",
      r"A real cubic with roots $i$ and $-i$ must also have", r"a real root (the third); actually $i$ forces $-i$, the third is real. Example $x(x^2+1)$.",
      r"Assuming conjugate pairs for complex coefficients.",
      r"Can a real quartic have exactly one nonreal root?", r"No: nonreal roots come in pairs, so the count of nonreal roots is even.",
      r"Minimal real polynomial with root $i$.", r"$x^2+1$.")
    a(62, r"Vieta: for $a_n x^n+\cdots+a_0=a_n(x-r_1)\cdots(x-r_n)$, the sum of roots is $-a_{n-1}/a_n$, product is $(-1)^n a_0/a_n$. For $x^2-sx+p=(x-r)(x-t)$, $s=r+t$, $p=rt$.",
      r"Sum and product of roots of $2x^2-6x+4=0$.", r"Sum $3$, product $2$.",
      r"If roots of $x^3+ax^2+bx+c=0$ are $1,2,3$ then $c=$", r"$-6$ (product $1\cdot 2\cdot 3=6=(-1)^3 c$, so $c=-6$), and $a=-6$.",
      r"Forgetting the sign $(-1)^n$ on the product.",
      r"Roots sum to $0$ for which monic quadratics?", r"$x^2+k$ form, no $x$ term? Sum $0$ means no $x$ term: $x^2+c$.",
      r"For $x^2+x+1=0$, product of roots.", r"$1$.")
    a(63, r"Rational root theorem: any rational root $p/q$ in lowest terms of $a_n x^n+\cdots+a_0$ has $p\mid a_0$ and $q\mid a_n$.",
      r"Possible rational roots of $2x^3-x+3=0$.", r"$\pm 1,3,\pm 1/2,3/2$.",
      r"Does $x^3-x-1=0$ have a rational root?", r"Candidates $\pm 1$; $p(1)=-1\neq 0$, $p(-1)=-1\neq 0$. No rational root.",
      r"Treating the list as guaranteed roots rather than candidates.",
      r"Test whether $3/2$ is a root of $2x^3-3x^2-3x+2$.", r"$p(3/2)=2\cdot 27/8-3\cdot 9/4-3\cdot 3/2+2=27/4-27/4-9/2+2\neq 0$. Compute carefully: actually $2(27/8)=27/4$, $3(9/4)=27/4$, so they cancel; $-9/2+2=-0.5\neq 0$. Not a root.",
      r"Possible rational roots of $x^3+2x+2$.", r"$\pm 1,\pm 2$. None work, so no rational roots.")
    a(64, r"Descartes’ rule of signs: the number of positive real roots is equal to the number of sign changes in $p(x)$, or less by an even integer. For negatives, use $p(-x)$. This bounds, it does not count exactly.",
      r"Sign changes of $x^3-x^2+x-1$.", r"Three sign changes, so $3$ or $1$ positive real roots. (Actually $(x-1)(x^2+1)$, one positive.)",
      r"$p(-x)$ for $x^2+x+1$ has how many sign changes?", r"$p(-x)=x^2-x+1$, one sign change, so $1$ or $0$ negative roots; actually none.",
      r"Reading Descartes as an exact count.",
      r"How many negative real roots can $x^3+x+1$ have?", r"$p(-x)=-x^3-x+1$, one sign change: one negative root. (And no positive.)",
      r"Can Descartes allow $2$ positive roots when there is $1$ sign change?", r"No: $1$ or fewer by even, so $1$ only.")
    a(65, r"There is a unique polynomial of degree $<n$ interpolating $n$ points with distinct $x$-coordinates. Lagrange/Newton forms construct it. Degree can drop if the points happen to lie on a lower-degree graph.",
      r"The unique linear polynomial through $(0,1)$ and $(2,5)$.", r"$y=2x+1$.",
      r"Three non-collinear points determine a quadratic interpolant of degree", r"$2$ (exactly $2$, not less).",
      r"Interpolating two points with a quadratic and thinking it is unique.",
      r"Find $p$ of degree $\le 1$ with $p(1)=3$, $p(3)=7$.", r"$p(x)=2x+1$.",
      r"Can $n$ points with distinct $x$ fail to have an interpolant of degree $<n$?", r"No: existence and uniqueness hold.")

    return F
