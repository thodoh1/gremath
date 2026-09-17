"""Unique facts for polar, trig, conics, coordinate geometry, complex numbers."""

from __future__ import annotations


def facts() -> dict[int, dict]:
    F: dict[int, dict] = {}

    def a(n, stmt, exq, exa, gq, ga, trap, q1, a1, q2, a2):
        F[n] = dict(stmt=stmt, exq=exq, exa=exa, gq=gq, ga=ga, trap=trap, q1=q1, a1=a1, q2=q2, a2=a2)

    a(111, r"Parametric equations $x=x(t)$, $y=y(t)$ describe a curve by a parameter. The graph is the set of points $(x(t),y(t))$. Different parametrizations can trace the same set at different speeds or directions.",
      r"$x=\cos t$, $y=\sin t$, $t\in[0,2\pi]$. What curve?", r"The unit circle, traced counterclockwise once.",
      r"$x=t^2$, $y=t$ traces", r"a parabola $x=y^2$ (rightward, both ways as $t$ from $-\infty$ to $\infty$).",
      r"Eliminating $t$ and forgetting that the parametrization may only cover part of the Cartesian curve.",
      r"$x=1+t$, $y=2-3t$ is the line through", r"$(1,2)$ with direction $(1,-3)$.",
      r"Does $x=t^2$, $y=t^2$ trace $y=x$?", r"Only the ray $x\ge 0$, $y=x$.")
    a(112, r"To eliminate $t$, solve one equation for $t$ (or for a function of $t$ such as $\sin t$) and substitute. Use identities ($\sin^2+\cos^2=1$) when trig parametrizations appear.",
      r"Eliminate $t$ from $x=2t$, $y=t^2$.", r"$y=x^2/4$.",
      r"$x=3\cos t$, $y=2\sin t$ eliminates to", r"$\frac{x^2}{9}+\frac{y^2}{4}=1$.",
      r"Squaring and introducing extra branches.",
      r"$x=e^t$, $y=e^{-t}$. Relation?", r"$xy=1$, $x>0$.",
      r"$x=\sec t$, $y=\tan t$.", r"$x^2-y^2=1$, $|x|\ge 1$.")
    a(113, r"Polar coordinates: $x=r\cos\theta$, $y=r\sin\theta$, $r^2=x^2+y^2$, $\tan\theta=y/x$ with quadrant care. $r$ may be negative in some conventions, meaning a direction $\theta+\pi$.",
      r"Polar of $(0,-2)$.", r"$r=2$, $\theta=3\pi/2$ (or $r=-2$, $\theta=\pi/2$).",
      r"Cartesian of $r=2$, $\theta=\pi/3$.", r"$(1,\sqrt{3})$.",
      r"Using $\arctan(y/x)$ without the quadrant.",
      r"Convert $x^2+y^2=4$.", r"$r=2$ (or $r=-2$).",
      r"The pole is which $r$?", r"$r=0$, $\theta$ arbitrary.")
    a(114, r"Conversion: $x=r\cos\theta$, $y=r\sin\theta$; $r=\sqrt{x^2+y^2}$, $\theta=\mathrm{atan2}(y,x)$. Equations convert by substitution.",
      r"Convert $r=2\cos\theta$ to Cartesian.", r"$r^2=2r\cos\theta$, $x^2+y^2=2x$, $(x-1)^2+y^2=1$.",
      r"$x=1$ in polar is", r"$r\cos\theta=1$, $r=\sec\theta$.",
      r"Multiplying by $r$ and losing $r=0$ if it was a solution.",
      r"Convert $r\sin\theta=3$.", r"$y=3$.",
      r"Polar of $y=x$.", r"$\theta=\pi/4$ or $5\pi/4$, etc.")
    a(115, r"Standard polar graphs: $r=a\cos\theta$ circle, $r=a(1-\cos\theta)$ cardioid, $r=a\sin(n\theta)$ rose. Sketch by testing $\theta=0,\pi/2,\pi$ and symmetry.",
      r"$r=2\sin\theta$ is a circle of radius", r"$1$ centered at $(0,1)$.",
      r"$r=\cos(2\theta)$ is a rose with how many petals?", r"$4$ (even $n$ gives $2n$ petals).",
      r"Assuming $r=\sin(3\theta)$ has six petals (odd $n$ gives $n$ petals).",
      r"$r=1+\cos\theta$ at $\theta=\pi$.", r"$r=0$, the pole.",
      r"Symmetry of $r=f(\sin\theta)$ about", r"the $y$-axis typically.")
    a(116, r"Polar symmetry: if $f(\theta)=f(-\theta)$, symmetry about the polar axis. If $f(\pi-\theta)=f(\theta)$, about $\theta=\pi/2$. If $f(\theta+\pi)=f(\theta)$, symmetry about the pole (or $r\mapsto -r$).",
      r"$r=\cos(2\theta)$ has symmetry about", r"both axes and the pole.",
      r"$r=1+\sin\theta$ is symmetric about", r"the $y$-axis.",
      r"Testing only $r(\theta)=r(-\theta)$ and missing $r(\theta)=r(\pi-\theta)$.",
      r"Does $r=\theta$ (spiral) have polar-axis symmetry?", r"No.",
      r"$r^2=\sin(2\theta)$ is a lemniscate; symmetry?", r"About $y=x$ and the origin.")
    a(117, r"Polar area: $A=\dfrac12\int_{\alpha}^{\beta} r(\theta)^2\,d\theta$ over the $\theta$-interval that traces the region once.",
      r"Area of $r=2$, $\theta$ from $0$ to $\pi/2$.", r"$\frac12\int_0^{\pi/2}4\,d\theta=\pi$. A quarter disk of radius $2$ has area $\pi$, yes.",
      r"Area of one petal of $r=\sin(2\theta)$ uses $\theta$ from", r"$0$ to $\pi/2$ (where $r\ge 0$ for that petal).",
      r"Forgetting the $1/2$ or integrating a petal twice.",
      r"Area inside $r=1+\cos\theta$ (cardioid).", r"$\frac12\int_0^{2\pi}(1+2\cos\theta+\cos^2\theta)\,d\theta=\frac{3\pi}{2}$.",
      r"Why $r^2\,d\theta/2$?", r"A thin sector has area $\frac12 r^2\Delta\theta$.")

    # C trig foundations 118-127
    a(118, r"$\pi$ radians $=180^\circ$, so $\theta_{\mathrm{deg}}=\theta_{\mathrm{rad}}\cdot 180/\pi$. Calculus uses radians because $(\sin x)'=\cos x$ only then.",
      r"$150^\circ$ in radians.", r"$5\pi/6$.",
      r"$2\pi/3$ radians in degrees.", r"$120^\circ$.",
      r"Computing a derivative of $\sin x$ with $x$ in degrees without converting.",
      r"$1$ radian is about how many degrees?", r"$180/\pi\approx 57.3^\circ$.",
      r"Arc length $s=r\theta$ requires $\theta$ in", r"radians.")
    a(119, r"The unit circle is $x^2+y^2=1$. The point at angle $\theta$ from the positive $x$-axis (radians, counterclockwise) is $(\cos\theta,\sin\theta)$. Coterminal angles differ by $2\pi k$.",
      r"Coordinates at $\theta=2\pi/3$.", r"$(-1/2,\sqrt{3}/2)$.",
      r"After wrapping $\theta=9\pi/2$, equivalent standard angle", r"$9\pi/2-4\pi=\pi/2$.",
      r"Measuring from the $y$-axis, or clockwise as positive without saying so.",
      r"Point at $\theta=-\pi/6$.", r"$(\sqrt{3}/2,-1/2)$.",
      r"Does $\theta$ and $\theta+2\pi$ label the same point?", r"Yes.")
    a(120, r"$\sin\theta=y$, $\cos\theta=x$, $\tan\theta=y/x$ on the unit circle. $\csc=1/\sin$, $\sec=1/\cos$, $\cot=1/\tan$. Right-triangle definitions match in Q1: opposite/hypotenuse, etc.",
      r"$\tan\theta$ at $\theta=3\pi/4$.", r"$-1$.",
      r"$\sec\theta$ undefined when", r"$\cos\theta=0$, i.e. $\theta=\pi/2+k\pi$.",
      r"Using triangle definitions in Q2 without signs.",
      r"$\sin(0),\cos(0),\tan(0)$.", r"$0,1,0$.",
      r"Express $\cot$ in $x,y$.", r"$x/y$.")
    a(121, r"$\sin\theta\csc\theta=1$ wherever both are defined; similarly $\cos\sec=1$, $\tan\cot=1$. These are definitions of the reciprocal functions, not new facts.",
      r"Simplify $\sin\theta\cdot\csc\theta$.", r"$1$ (where $\sin\neq 0$).",
      r"$\sec\theta\cos\theta$.", r"$1$ where $\cos\neq 0$.",
      r"Writing $\csc=1/\sec$.",
      r"Is $\csc\theta$ defined at $\theta=0$?", r"No, $\sin 0=0$.",
      r"Simplify $\tan\theta\cos\theta$.", r"$\sin\theta$ where $\cos\neq 0$.")
    a(122, r"$\sin^2\theta+\cos^2\theta=1$. Divide by $\cos^2$ to get $1+\tan^2=\sec^2$; by $\sin^2$ to get $1+\cot^2=\csc^2$.",
      r"If $\cos\theta=3/5$ in Q1, $\sin\theta$.", r"$4/5$.",
      r"$\tan^2\theta+1=\sec^2\theta$ at $\theta=\pi/4$.", r"$1+1=2=(\sqrt{2})^2$.",
      r"Taking square roots and dropping $\pm$.",
      r"If $\sin\theta=-1/2$ in Q3, $\cos\theta$.", r"$-\sqrt{3}/2$.",
      r"Simplify $\dfrac{\sin^2\theta}{1-\cos\theta}$ using $1-\cos^2$.", r"$1+\cos\theta$ after multiplying by conjugate, for $\cos\neq 1$.")
    a(123, r"$\sin$ is odd, $\cos$ is even, $\tan$ is odd. Reciprocals inherit the parity of the originals (where defined).",
      r"$\sin(-\pi/6)$.", r"$-1/2$.",
      r"$\cos(-\theta)-\cos\theta$.", r"$0$.",
      r"Treating $\cos$ as odd.",
      r"$\tan(-\pi/4)$.", r"$-1$.",
      r"Is $\sec$ even or odd?", r"Even, because $\cos$ is even.")
    a(124, r"$\sin$ and $\cos$ have period $2\pi$; $\tan$ and $\cot$ have period $\pi$; $\sec$ and $\csc$ have period $2\pi$. $f(x+T)=f(x)$ for all $x$ in the domain.",
      r"Period of $\sin(x/2)$.", r"$4\pi$.",
      r"Period of $\tan(2x)$.", r"$\pi/2$.",
      r"Using $2\pi$ as the period of $\tan$.",
      r"Smallest positive period of $\cos(3x)$.", r"$2\pi/3$.",
      r"Period of $\sin x+\sin(2x)$?", r"$2\pi$ (not $\pi$).")
    a(125, r"The reference angle is the acute angle to the $x$-axis. The trig value equals $\pm$ the Q1 value of the reference angle, sign from the quadrant.",
      r"Reference angle of $5\pi/6$.", r"$\pi/6$.",
      r"$\sin(7\pi/6)$.", r"$-1/2$ (Q3, ref $\pi/6$).",
      r"Measuring the reference angle to the $y$-axis.",
      r"Reference of $300^\circ$.", r"$60^\circ$.",
      r"$\cos(4\pi/3)$.", r"$-1/2$.")
    a(126, r"Signs: Q1 all $+$; Q2 $\sin,\csc+$ ; Q3 $\tan,\cot+$ ; Q4 $\cos,\sec+$. ASTC (or CAST, depending on where you start).",
      r"Sign of $\cos$ in Q2.", r"Negative.",
      r"If $\tan\theta>0$ and $\sin\theta<0$, the quadrant is", r"Q3.",
      r"Memorizing ASTC starting from the wrong quadrant.",
      r"Can $\sin$ and $\cos$ both be negative?", r"Yes, Q3.",
      r"Sign of $\sec$ in Q4.", r"Positive.")
    a(127, r"Exact values: $0,\pi/6,\pi/4,\pi/3,\pi/2$ and symmetry. $\sin\pi/6=1/2$, $\sin\pi/4=\sqrt{2}/2$, $\sin\pi/3=\sqrt{3}/2$, $\cos$ swapped, $\tan$ as $\sin/\cos$.",
      r"$\sin(\pi/3)\cos(\pi/6)$.", r"$(\sqrt{3}/2)(\sqrt{3}/2)=3/4$.",
      r"$\tan(5\pi/4)$.", r"$1$.",
      r"$\sin\pi/3=\sqrt{2}/2$ mixup with $\pi/4$.",
      r"$\cos(2\pi/3)$.", r"$-1/2$.",
      r"$\sec(\pi/4)$.", r"$\sqrt{2}$.")

    a(128, r"$\sin(a\pm b)=\sin a\cos b\pm\cos a\sin b$, $\cos(a\pm b)=\cos a\cos b\mp\sin a\sin b$, $\tan(a\pm b)=\dfrac{\tan a\pm\tan b}{1\mp\tan a\tan b}$.",
      r"$\sin(\pi/12)=\sin(\pi/3-\pi/4)$.", r"$\dfrac{\sqrt{6}-\sqrt{2}}{4}$.",
      r"$\cos(\pi/2-x)$.", r"$\sin x$.",
      r"The $\mp$ on cosine: people keep the same sign as sine.",
      r"$\sin(x+\pi)$.", r"$-\sin x$.",
      r"$\tan(\pi/4+x)$ when $\tan x=2$.", r"$(1+2)/(1-2)=-3$.")
    a(129, r"$\sin(2a)=2\sin a\cos a$, $\cos(2a)=\cos^2 a-\sin^2 a=2\cos^2 a-1=1-2\sin^2 a$, $\tan(2a)=\dfrac{2\tan a}{1-\tan^2 a}$.",
      r"$\cos(2\theta)$ if $\cos\theta=3/5$.", r"$2(9/25)-1=-7/25$.",
      r"$\sin 2x$ if $\sin x=\cos x$.", r"$2\sin x\cos x=\sin^2 x+\cos^2 x=1$ when $\sin x=\cos x=\pm\sqrt{2}/2$.",
      r"Using $\cos 2a=2\cos a$ (missing the square).",
      r"$\sin(\pi/2)=2\sin(\pi/4)\cos(\pi/4)$.", r"$2\cdot\frac{\sqrt{2}}{2}\cdot\frac{\sqrt{2}}{2}=1$.",
      r"Express $\cos^2 x$ in double-angle.", r"$(1+\cos 2x)/2$.")
    a(130, r"Half-angle: $\sin^2(a/2)=\dfrac{1-\cos a}{2}$, $\cos^2(a/2)=\dfrac{1+\cos a}{2}$, and signed square roots for $\sin(a/2)$ itself depending on quadrant.",
      r"$\sin(\pi/8)$ using $a=\pi/4$.", r"$\sqrt{(1-\cos\pi/4)/2}=\sqrt{(2-\sqrt{2})/4}=\sqrt{2-\sqrt{2}}/2$.",
      r"$\cos^2(x/2)$ in terms of $\cos x$.", r"$(1+\cos x)/2$.",
      r"Dropping the $\pm$ when the problem asked for the signed function.",
      r"$\tan(a/2)=\sin a/(1+\cos a)$ (a Weierstrass form).", r"Useful substitution $t=\tan(a/2)$.",
      r"Evaluate $(1-\cos\theta)/\sin\theta$.", r"$\tan(\theta/2)$ in the usual range.")
    a(131, r"Power-reduction is the half-angle identities read as reducing powers: $\sin^2=\dfrac{1-\cos 2x}{2}$, $\cos^2=\dfrac{1+\cos 2x}{2}$, $\sin^3$ via $\sin\cdot\sin^2$, etc.",
      r"Rewrite $\sin^2 x\cos^2 x$.", r"$(\sin 2x/2)^2=(1-\cos 4x)/8$.",
      r"$\int\sin^2 x\,dx$ begins with", r"$\int(1-\cos 2x)/2\,dx$.",
      r"Reducing $\sin^2$ to $\sin 2x$ without the identity (that's $\sin 2x=2\sin\cos$).",
      r"$\cos^4 x$ in multiple angles.", r"$((1+\cos 2x)/2)^2=(1+2\cos 2x+\cos^2 2x)/4$ then reduce again.",
      r"Average value of $\sin^2$ over a period.", r"$1/2$.")
    a(132, r"Product-to-sum: $\sin a\sin b=\frac12(\cos(a-b)-\cos(a+b))$, $\cos a\cos b=\frac12(\cos(a-b)+\cos(a+b))$, $\sin a\cos b=\frac12(\sin(a+b)+\sin(a-b))$.",
      r"$\sin 3x\sin x$.", r"$\frac12(\cos 2x-\cos 4x)$.",
      r"Used to integrate $\sin 5x\cos 3x$.", r"$\frac12\int(\sin 8x+\sin 2x)\,dx$.",
      r"Sign errors in $\cos(a-b)-\cos(a+b)$.",
      r"$\cos x\cos x$.", r"$\frac12(1+\cos 2x)$.",
      r"Product $\sin A\cos A$.", r"$\frac12\sin 2A$.")
    a(133, r"Sum-to-product: $\sin a+\sin b=2\sin\frac{a+b}{2}\cos\frac{a-b}{2}$, $\cos a+\cos b=2\cos\frac{a+b}{2}\cos\frac{a-b}{2}$, with minus-sign variants.",
      r"$\sin 5x+\sin x$.", r"$2\sin 3x\cos 2x$.",
      r"Solve $\sin x+\sin 3x=0$.", r"$2\sin 2x\cos x=0$, so $\sin 2x=0$ or $\cos x=0$.",
      r"Mixing the cosine-sum identity's signs.",
      r"$\cos 4x-\cos 2x$.", r"$-2\sin 3x\sin x$.",
      r"Factor $\sin 7^\circ+\sin 3^\circ$.", r"$2\sin 5^\circ\cos 2^\circ$.")
    a(134, r"Multiple-angle formulas come from De Moivre or recurrence: $T_n(\cos\theta)=\cos(n\theta)$ (Chebyshev). $\sin 3\theta=3\sin\theta-4\sin^3\theta$, $\cos 3\theta=4\cos^3\theta-3\cos\theta$.",
      r"$\cos 3\theta$ if $\cos\theta=1/2$.", r"$4(1/8)-3(1/2)=-1$.",
      r"$\sin 3x$ in terms of $\sin x$.", r"$3\sin x-4\sin^3 x$.",
      r"Using $\sin 3x=3\sin x$ (small-angle leftover).",
      r"Express $\cos 4\theta$ via $\cos 2\theta$.", r"$2\cos^2 2\theta-1$.",
      r"If $z=e^{i\theta}$, $z^n+\bar z^n=2\cos(n\theta)$.", r"De Moivre.")
    a(135, r"Convert until a derivative, a standard integral, or a linear combination of $\sin,\cos$ of multiple angles appears. There is no unique ‘simplest’ form; GRE wants the form that matches a choice or an integral.",
      r"Write $3\sin x+4\cos x$ as $R\sin(x+\phi)$.", r"$R=5$, $\tan\phi=4/3$.",
      r"A GRE item asks to match $\sin 2x/(1+\cos 2x)$.", r"Equals $\tan x$ (where defined).",
      r"Simplifying into a more complicated expression because it looks more ‘trig’.",
      r"Rewrite $1-\cos 2x$.", r"$2\sin^2 x$.",
      r"$\dfrac{1-\cos x}{\sin x}$.", r"$\tan(x/2)$ or $\csc x-\cot x$.")

    a(136, r"Basic trig equations: isolate a single trig function, solve on one period, then add the period. $\sin\theta=c$ has solutions $\theta=\arcsin c+2k\pi$ or $\theta=\pi-\arcsin c+2k\pi$ for $|c|\le 1$.",
      r"Solve $\sin x=1/2$ on $[0,2\pi)$.", r"$x=\pi/6, 5\pi/6$.",
      r"$\cos x=0$ general solution", r"$x=\pi/2+k\pi$.",
      r"Missing the second family for sine/cosine.",
      r"Solve $\tan x=1$ on $(-\pi/2,\pi/2)$.", r"$x=\pi/4$.",
      r"Solve $2\cos x=1$.", r"$x=\pm\pi/3+2k\pi$.")
    a(137, r"A general solution lists all real solutions using an integer parameter $k$. Different functions have different periods and symmetries; $\tan$ uses $k\pi$, $\sin$ uses $2k\pi$ with two families.",
      r"General solution of $\sin x=0$.", r"$x=k\pi$.",
      r"$\sec x=2$ general solution", r"$x=\pm\pi/3+2k\pi$.",
      r"Writing $+2k\pi$ for $\tan x=1$ (should be $+\pi/4+k\pi$).",
      r"General solution of $\cos x=-1$.", r"$x=(2k+1)\pi$.",
      r"$\sin 2x=1$ general.", r"$2x=\pi/2+2k\pi$, $x=\pi/4+k\pi$.")
    a(138, r"On a restricted domain, take the general solution and keep those $k$ that land in the interval. Draw the unit circle or one period of the graph.",
      r"Solve $\cos x=-1/2$ for $x\in[0,\pi]$.", r"$x=2\pi/3$ only (the other standard angle $4\pi/3$ is outside).",
      r"Number of solutions of $\sin x=1/3$ in $[0,4\pi)$.", r"Four.",
      r"Including endpoints incorrectly when the function is undefined there ($\tan$ at $\pi/2$).",
      r"Solve $\tan x=\sqrt{3}$ on $(-\pi,\pi)$.", r"$x=\pi/3, -2\pi/3$.",
      r"How many $x\in[0,2\pi)$ with $\sin 2x=0$?", r"Four: $0,\pi/2,\pi,3\pi/2$.")
    a(139, r"Trig inequalities: solve the equality, then read the sign chart on a period, then expand by periodicity. Or use the unit circle arcs.",
      r"Solve $\sin x>1/2$ on $[0,2\pi)$.", r"$(\pi/6, 5\pi/6)$.",
      r"$\cos x\le 0$ on $[0,2\pi)$.", r"$[\pi/2, 3\pi/2]$.",
      r"Treating $\sin x>1/2$ as $x>\pi/6$ without the upper bound.",
      r"Solve $\tan x>0$ on $(-\pi/2,\pi/2)$.", r"$(0,\pi/2)$.",
      r"$\sin x\ge 0$ on $\mathbb{R}$.", r"$\bigcup_k [2k\pi,(2k+1)\pi]$.")
    a(140, r"Principal inverse trig: $\arcsin:[-1,1]\to[-\pi/2,\pi/2]$, $\arccos:[-1,1]\to[0,\pi]$, $\arctan:\mathbb{R}\to(-\pi/2,\pi/2)$. They are inverses of restricted sine/cosine/tangent.",
      r"$\arcsin(1/2)$.", r"$\pi/6$, not $5\pi/6$.",
      r"$\arccos(-1)$.", r"$\pi$.",
      r"Reporting $\arcsin(1/2)=150^\circ$.",
      r"$\arctan(-1)$.", r"$-\pi/4$.",
      r"Range of $\arcsin$.", r"$[-\pi/2,\pi/2]$.")
    a(141, r"Identities: $\arcsin x+\arccos x=\pi/2$, $\arctan x+\arctan(1/x)=\pi/2$ for $x>0$. $\sin(\arcsin x)=x$, but $\arcsin(\sin x)=x$ only on the principal range.",
      r"$\arcsin x+\arccos x$ for $x\in[-1,1]$.", r"$\pi/2$.",
      r"$\arcsin(\sin(3\pi/4))$.", r"$\pi/4$, not $3\pi/4$.",
      r"Canceling $\arcsin\circ\sin$ as identity on all $\mathbb{R}$.",
      r"$\tan(\arctan 10)$.", r"$10$.",
      r"$\arccos(\cos(7\pi/6))$.", r"$5\pi/6$.")
    a(142, r"Principal values are conventions: GRE and calculus textbooks use the ranges in M-140. Some older sources use $\mathrm{Arcsin}$ vs $\arcsin$ inconsistently. Always state the range.",
      r"Why is $\arccos(-1/2)=2\pi/3$ not $-2\pi/3$?", r"Because $\arccos$ lands in $[0,\pi]$.",
      r"The calculator’s $\mathrm{atan2}(y,x)$ vs $\arctan(y/x)$.", r"$\mathrm{atan2}$ knows the quadrant; $\arctan$ of a ratio does not.",
      r"Mixing two conventions in one solution.",
      r"Principal value of $\mathrm{Arg}(-1)$.", r"$\pi$, not $-\pi$, in the usual $(-\pi,\pi]$ or $[0,2\pi)$ — GRE analysis usually $(-\pi,\pi]$, so $\pi$.",
      r"Is $\arcsin$ odd?", r"Yes: $\arcsin(-x)=-\arcsin x$.")
    a(143, r"Trig substitution: $x=a\sin\theta$, $a\tan\theta$, or $a\sec\theta$ to kill $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$, $\sqrt{x^2-a^2}$. Draw the triangle to back-substitute.",
      r"For $\sqrt{4-x^2}$, set", r"$x=2\sin\theta$, $\theta\in[-\pi/2,\pi/2]$.",
      r"$\int\dfrac{dx}{\sqrt{x^2+1}}$ wants", r"$x=\tan\theta$ (or hyperbolic $x=\sinh u$).",
      r"Forgetting to change $dx$ and the limits (definite) or back-sub (indefinite).",
      r"Triangle for $x=3\sec\theta$.", r"Hyp $x$, adj $3$, opp $\sqrt{x^2-9}$.",
      r"Why $\theta=\arcsin(x/a)$ after $x=a\sin\theta$?", r"Because we chose the principal range where cosine is nonnegative.")

    a(144, r"Law of sines: $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R$ (circumdiameter). Use when you have a side and its opposite angle.",
      r"In $\triangle ABC$, $A=30^\circ$, $B=45^\circ$, $a=10$. Find $b$.", r"$\dfrac{10}{\sin 30}=\dfrac{b}{\sin 45}$, $b=10\sqrt{2}$.",
      r"$a/\sin A=2R$ with $a=5$, $A=90^\circ$ gives $R=$", r"$5/2$.",
      r"SSA ambiguous case treated as unique (see M-148).",
      r"If $A=B$, then $a=b$.", r"Yes, isosceles.",
      r"Solve for $C$ if $A=40^\circ$, $B=60^\circ$.", r"$C=80^\circ$.")
    a(145, r"Law of cosines: $c^2=a^2+b^2-2ab\cos C$. Use SAS or SSS. Obtuse $C$ makes $\cos C<0$, so $c^2>a^2+b^2$.",
      r"Sides $3,4$ included angle $60^\circ$. Opposite side?", r"$c^2=9+16-2\cdot 3\cdot 4\cdot 1/2=13$, $c=\sqrt{13}$.",
      r"When $C=90^\circ$, the law of cosines becomes", r"Pythagoras.",
      r"Using cosine law with the wrong angle (not included / not opposite the unknown side).",
      r"Find $\cos C$ if $a=5,b=6,c=7$.", r"$(a^2+b^2-c^2)/(2ab)=(25+36-49)/60=12/60=1/5$.",
      r"If $c^2>a^2+b^2$, angle $C$ is", r"obtuse.")
    a(146, r"Area $=\dfrac12 ab\sin C$. Also $\dfrac{abc}{4R}$ and $\sqrt{s(s-a)(s-b)(s-c)}$ (Heron).",
      r"Area of SAS triangle $a=5$, $b=8$, $C=30^\circ$.", r"$\frac12\cdot 5\cdot 8\cdot \frac12=10$.",
      r"Equilateral side $2$, area", r"$\frac12\cdot 2\cdot 2\cdot\sin 60=\sqrt{3}$.",
      r"Using $\sin$ of a non-included angle without law of sines first.",
      r"Area given two sides and a non-included angle — need", r"SSA first, possibly two triangles.",
      r"Max area of $ab\sin C$ with $a,b$ fixed.", r"When $C=90^\circ$.")
    a(147, r"Heron: $s=(a+b+c)/2$, area $\sqrt{s(s-a)(s-b)(s-c)}$. Use SSS.",
      r"Area of $3$-$4$-$5$ triangle.", r"$s=6$, $\sqrt{6\cdot 3\cdot 2\cdot 1}=6$.",
      r"Equilateral side $a$: Heron gives", r"$s=3a/2$, $\sqrt{\frac{3a}{2}(\frac{a}{2})^3}=\dfrac{\sqrt{3}}{4}a^2$.",
      r"Using side lengths that violate the triangle inequality (sqrt of negative).",
      r"Area of $5$-$5$-$6$.", r"$s=8$, $\sqrt{8\cdot 3\cdot 3\cdot 2}=12$.",
      r"Why Heron equals $\frac12 ab\sin C$.", r"Both compute the same area; $\sin C$ from cosine law.")
    a(148, r"SSA is ambiguous: given $a,A,b$, height $h=b\sin A$. If $A$ acute: no triangle if $a<h$; one right if $a=h$; two if $h<a<b$; one if $a\ge b$. If $A$ obtuse: one triangle iff $a>b$.",
      r"$A=30^\circ$, $a=1$, $b=2$. Then $h=1$, so", r"$a=h$: one right triangle.",
      r"$A=30^\circ$, $a=1.5$, $b=2$.", r"Two triangles ($h=1<a<b$).",
      r"Assuming SSA is as unique as SAS.",
      r"$A=120^\circ$, $a=3$, $b=2$.", r"One triangle ($a>b$).",
      r"$A=120^\circ$, $a=2$, $b=3$.", r"None ($a<b$ with obtuse $A$).")
    a(149, r"An inscribed angle is half the central angle subtending the same arc. Angle in a semicircle is $90^\circ$. Opposite angles of a cyclic quadrilateral sum to $180^\circ$.",
      r"A triangle inscribed in a diameter with vertex on the circle has", r"a right angle at that vertex.",
      r"Inscribed angle subtending a $80^\circ$ arc is", r"$40^\circ$.",
      r"Using the inscribed angle as equal to the central angle.",
      r"Two inscribed angles subtending the same arc.", r"Equal.",
      r"Angle between tangent and chord equals the inscribed angle in the alternate segment.", r"Alternate segment theorem (GRE awareness).")
    a(150, r"Larger side opposite larger angle. Triangle inequality $a+b>c$. Isosceles base angles equal. These constrain possible SSA/SSS data before computing.",
      r"If $A>B$, then $a>b$.", r"True in a Euclidean triangle.",
      r"Sides $2,3,6$ form a triangle?", r"No: $2+3<6$.",
      r"Assuming the largest side is opposite a $90^\circ$ angle without checking $a^2+b^2$ vs $c^2$.",
      r"In a triangle, can two obtuse angles occur?", r"No.",
      r"If $a=b$, then $A=B$.", r"Yes.")

    a(151, r"Circle: $(x-h)^2+(y-k)^2=r^2$. General $x^2+y^2+Dx+Ey+F=0$ completes to a circle if the radius squared is positive.",
      r"Center and radius of $x^2+y^2-4x+6y-3=0$.", r"$(x-2)^2+(y+3)^2=16$, center $(2,-3)$, $r=4$.",
      r"$x^2+y^2+2x+1=0$ is", r"$(x+1)^2+y^2=0$, a point circle.",
      r"Forgetting to complete the square on both $x$ and $y$.",
      r"Equation of circle diameter from $(0,0)$ to $(4,0)$.", r"$(x-2)^2+y^2=4$.",
      r"Does $x^2+y^2+4=0$ represent a real circle?", r"No, $r^2<0$.")
    a(152, r"Parabola: $(x-h)^2=4p(y-k)$ opens vertically, focus $(h,k+p)$, directrix $y=k-p$. Horizontal analogue $(y-k)^2=4p(x-h)$.",
      r"$y=x^2/8$ has $4p=8$, $p=2$, focus", r"$(0,2)$ if vertex at origin.",
      r"Directrix of $x^2=4y$.", r"$y=-1$.",
      r"Using $y=ax^2$ and taking focus at $(0,a)$ instead of $(0,1/(4a))$.",
      r"Vertex of $y=2(x-3)^2+1$.", r"$(3,1)$.",
      r"Opens left: $(y)^2=-8x$, $p=-2$. Focus?", r"$(-2,0)$.")
    a(153, r"Ellipse: $\dfrac{(x-h)^2}{a^2}+\dfrac{(y-k)^2}{b^2}=1$ with $a>b>0$ for horizontal major axis. $c=\sqrt{a^2-b^2}$, foci $(\pm c,0)$ translated.",
      r"Foci of $\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$.", r"$c=4$, foci $(\pm 4,0)$.",
      r"If $a=b$, the ellipse is a", r"circle.",
      r"Putting $c=\sqrt{a^2+b^2}$ (that's hyperbola).",
      r"Vertices of $\dfrac{x^2}{16}+\dfrac{y^2}{4}=1$.", r"$(\pm 4,0)$ and $(0,\pm 2)$.",
      r"Eccentricity $e=c/a$ for $a=5,b=4$.", r"$c=3$, $e=3/5$.")
    a(154, r"Hyperbola: $\dfrac{(x-h)^2}{a^2}-\dfrac{(y-k)^2}{b^2}=1$ opens horizontally. $c=\sqrt{a^2+b^2}$, foci $(\pm c,0)$. Asymptotes $y-k=\pm\frac{b}{a}(x-h)$.",
      r"Asymptotes of $\dfrac{x^2}{9}-\dfrac{y^2}{4}=1$.", r"$y=\pm\frac{2}{3}x$.",
      r"$xy=1$ is a hyperbola rotated $45^\circ$.", r"Yes (rectangular).",
      r"Using $c=\sqrt{a^2-b^2}$ as in the ellipse.",
      r"Vertices of $\dfrac{y^2}{16}-\dfrac{x^2}{9}=1$.", r"$(0,\pm 4)$.",
      r"Foci of $x^2-y^2=1$.", r"$a=b=1$, $c=\sqrt{2}$, $(\pm\sqrt{2},0)$.")
    a(155, r"Focus-directrix: a conic is the set of points with $PF=e\cdot(P$ to directrix$)$. $e<1$ ellipse, $e=1$ parabola, $e>1$ hyperbola. Circle is $e=0$ limiting.",
      r"Parabola definition with $e=1$.", r"Distance to focus equals distance to directrix.",
      r"If $e=2$ and directrix $x=1$, focus $(0,0)$, the curve is a", r"hyperbola.",
      r"Using $e=c/a$ for a parabola (undefined that way).",
      r"Circle as a conic: eccentricity", r"$0$.",
      r"A point on an ellipse is closer to the nearer focus than to the corresponding directrix because $e<1$.", r"True by definition $PF=e\cdot PD$.")
    a(156, r"Eccentricity $e=c/a$ for ellipse ($e<1$) and hyperbola ($e>1$). For parabola $e=1$. Flattening of an ellipse increases $e$ toward $1$.",
      r"$e$ for $\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$.", r"$c=3$, $e=3/5$.",
      r"As $e\to 0$ an ellipse becomes", r"circular.",
      r"Reporting $e=b/a$.",
      r"Hyperbola $e$ if $a=3,b=4$.", r"$c=5$, $e=5/3$.",
      r"Can $e=1$ for an ellipse?", r"No; that would be a parabola.")
    a(157, r"Major axis is the longer of the two axes of an ellipse ($2a$); minor is $2b$. For a hyperbola, the transverse axis is the one that intersects the curve ($2a$).",
      r"Major axis length of $\dfrac{x^2}{9}+\dfrac{y^2}{25}=1$.", r"Vertical major axis length $10$.",
      r"Transverse axis of $\dfrac{x^2}{4}-\dfrac{y^2}{9}=1$ has length", r"$4$.",
      r"Always taking the $x$-axis as major.",
      r"Minor axis of $\dfrac{x^2}{16}+\dfrac{y^2}{9}=1$.", r"Length $6$.",
      r"If $a=b$ for a hyperbola $\frac{x^2}{a^2}-\frac{y^2}{a^2}=1$, asymptotes are", r"$y=\pm x$ (rectangular).")
    a(158, r"Vertices are the intercepts of the transverse/major axis with the curve. Foci lie on that axis, distance $c$ from the center.",
      r"Vertices and foci of $\dfrac{x^2}{36}+\dfrac{y^2}{20}=1$.", r"Vertices $(\pm 6,0)$, $c=4$, foci $(\pm 4,0)$.",
      r"A hyperbola’s vertices are closer to the center than the foci because $c>a$.", r"True.",
      r"Listing co-vertices as foci.",
      r"Co-vertices of $\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$.", r"$(0,\pm 2)$.",
      r"Center of $\dfrac{(x-1)^2}{4}+\dfrac{(y+2)^2}{9}=1$.", r"$(1,-2)$.")
    a(159, r"Hyperbola asymptotes pass through the center and are the diagonals of the rectangle of sides $2a,2b$. For $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$, $y=\pm\frac{b}{a}x$ after translation.",
      r"Asymptotes of $\dfrac{(x-1)^2}{4}-\dfrac{(y+2)^2}{9}=1$.", r"$y+2=\pm\frac{3}{2}(x-1)$.",
      r"Rectangular hyperbola has asymptotes", r"perpendicular.",
      r"Using $\pm a/b$ instead of $\pm b/a$.",
      r"$xy=2$ asymptotes.", r"The axes $x=0$ and $y=0$.",
      r"Do the branches cross the asymptotes?", r"No; they approach them.")
    a(160, r"A translation $(x,y)\mapsto(x-h,y-k)$ moves the standard conic so the center/vertex is $(h,k)$. Complete the square to read $(h,k)$.",
      r"Identify $x^2+2x+y^2-4y=4$.", r"$(x+1)^2+(y-2)^2=9$, circle center $(-1,2)$, $r=3$.",
      r"$y=x^2+4x+1$ vertex.", r"Complete: $y=(x+2)^2-3$, vertex $(-2,-3)$.",
      r"Forgetting to balance the constant when completing the square.",
      r"Shift $x^2/4+y^2/9=1$ so center is $(2,-1)$.", r"$\frac{(x-2)^2}{4}+\frac{(y+1)^2}{9}=1$.",
      r"The $xy$ term means rotation, not translation.", r"True.")
    a(161, r"A rotated conic has an $xy$ term. The quadratic form $ax^2+bxy+cy^2$ is classified by $b^2-4ac$: $<0$ ellipse (or circle/point/empty), $=0$ parabola (or degenerate), $>0$ hyperbola (or degenerate). Diagonalize by rotating axes.",
      r"$xy=1$ has $b^2-4ac=1>0$, so", r"hyperbola.",
      r"$x^2+xy+y^2=1$ has $1-4=-3<0$, so", r"ellipse.",
      r"Ignoring degeneracy (the invariant only classifies the type, not existence).",
      r"$x^2+2xy+y^2=0$ is", r"$(x+y)^2=0$, a double line (degenerate parabola).",
      r"To eliminate $xy$, rotate by $\alpha$ with $\cot 2\alpha=(a-c)/b$.", r"Standard formula.")

    a(162, r"Distance in the plane: $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$. This is Pythagoras.",
      r"Distance $(0,0)$ to $(3,4)$.", r"$5$.",
      r"Equidistant from $(0,0)$ and $(2,0)$ is the line", r"$x=1$.",
      r"Forgetting to square-root (reporting the squared distance when asked for distance).",
      r"Distance $(1,-1)$ to $(4,3)$.", r"$5$.",
      r"Set of points at distance $2$ from $(1,1)$.", r"Circle $(x-1)^2+(y-1)^2=4$.")
    a(163, r"Midpoint $\left(\dfrac{x_1+x_2}{2},\dfrac{y_1+y_2}{2}\right)$. Section formula for a ratio $m:n$ is the weighted average.",
      r"Midpoint of $(2,3)$ and $(8,-1)$.", r"$(5,1)$.",
      r"Point one-third of the way from $A$ to $B$ is", r"$\frac{2}{3}A+\frac{1}{3}B$ wait: from $A$ to $B$, one-third is $\frac{2}{3}A+\frac{1}{3}B$? No: $(2A+B)/3$ is closer to $A$. One-third from $A$ to $B$ is $\frac{2}{3}A+\frac{1}{3}B$. Yes.",
      r"Averaging coordinates but subtracting instead of adding.",
      r"If midpoint of $(x,2)$ and $(4,6)$ is $(1,4)$, find $x$.", r"$(x+4)/2=1$, $x=-2$.",
      r"Diagonals of a parallelogram bisect each other, so midpoints match.", r"Vector characterization.")
    a(164, r"Slope $m=\dfrac{y_2-y_1}{x_2-x_1}$ for $x_1\neq x_2$. Vertical lines have undefined slope. $m=\tan\theta$ with inclination $\theta$.",
      r"Slope from $(1,2)$ to $(5,11)$.", r"$9/4$.",
      r"A line with inclination $120^\circ$ has slope", r"$\tan 120=-\sqrt{3}$.",
      r"Slope of a vertical line as $0$ (that's horizontal).",
      r"Slope of $y=3$.", r"$0$.",
      r"Slope of $x=3$.", r"Undefined.")
    a(165, r"Point-slope: $y-y_0=m(x-x_0)$. This is the fastest form when you have a point and a slope (or a tangent line in calculus).",
      r"Line through $(2,-1)$ with slope $3$.", r"$y+1=3(x-2)$.",
      r"Tangent to $y=x^2$ at $x=1$ has slope $2$, so", r"$y-1=2(x-1)$.",
      r"Using $y=mx+b$ and solving for $b$ when point-slope is already done.",
      r"Line through $(0,0)$ slope $-1/2$.", r"$y=-x/2$.",
      r"Rewrite $y-4=2(x+1)$ in slope-intercept.", r"$y=2x+6$.")
    a(166, r"Intercept form: $\dfrac{x}{a}+\dfrac{y}{b}=1$ meets axes at $(a,0)$ and $(0,b)$, provided $a,b\neq 0$.",
      r"Intercept form of $2x+3y=6$.", r"$x/3+y/2=1$.",
      r"A line with intercepts $4$ and $-2$ is", r"$x/4+y/(-2)=1$.",
      r"Using intercept form for a line through the origin (both intercepts $0$).",
      r"x-intercept of $x/5+y/7=1$.", r"$5$.",
      r"Does $x/2+y/3=1$ pass through $(2,0)$?", r"Yes.")
    a(167, r"Parallel lines have equal slopes (or both vertical). Perpendicular lines have slopes $m$ and $-1/m$ (or one horizontal and one vertical).",
      r"Line through $(0,0)$ perpendicular to $y=2x+1$.", r"$y=-x/2$.",
      r"Are $2x+3y=1$ and $4x+6y=7$ parallel?", r"Yes: second is twice the left of the first, different constant, parallel distinct.",
      r"Using $m_1 m_2=1$ instead of $-1$.",
      r"Slope perpendicular to $3/5$.", r"$-5/3$.",
      r"Vertical is perpendicular to", r"horizontal.")
    a(168, r"Distance from point $(x_0,y_0)$ to line $ax+by+c=0$ is $\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$.",
      r"Distance from $(0,0)$ to $3x+4y-10=0$.", r"$10/5=2$.",
      r"Distance from $(1,1)$ to $x+y=0$.", r"$\sqrt{2}$.",
      r"Forgetting the absolute value, or using $ax+by+c=1$ not $=0$.",
      r"Distance from $(2,3)$ to $y=4$.", r"$1$.",
      r"If distance from origin to $x+y+c=0$ is $1$, then $|c|=\sqrt{2}$.", r"Yes.")
    a(169, r"Distance between parallel lines $ax+by+c_1=0$ and $ax+by+c_2=0$ is $\dfrac{|c_1-c_2|}{\sqrt{a^2+b^2}}$.",
      r"Distance between $x+y=1$ and $x+y=4$.", r"$3/\sqrt{2}$.",
      r"$y=2x+1$ and $y=2x-5$ distance", r"Write $2x-y+1=0$, $2x-y-5=0$, $|1-(-5)|/\sqrt{5}=6/\sqrt{5}$.",
      r"Using the formula on non-parallel lines.",
      r"Distance between $x=0$ and $x=3$.", r"$3$.",
      r"Normalize $2x+2y-2=0$ first or not?", r"The formula already handles non-monic $a,b$; don’t double-normalize inconsistently.")
    a(170, r"A line $y=mx+k$ meets $x^2+y^2=r^2$ by substitution: a quadratic in $x$. Discriminant $>0$ two points, $=0$ tangent, $<0$ miss.",
      r"Intersection of $y=x$ with $x^2+y^2=2$.", r"$2x^2=2$, $x=\pm 1$, points $(\pm 1,\pm 1)$.",
      r"When is $y=1$ tangent to $x^2+y^2=1$?", r"$x^2+1=1$, $x=0$, one point $(0,1)$: tangent.",
      r"Solving and discarding a valid negative root.",
      r"How many intersections of $x=2$ with $x^2+y^2=1$?", r"Zero.",
      r"$x^2+y^2=25$ and $y=3x$ points.", r"$x^2+9x^2=25$, $x=\pm\sqrt{2.5}=\pm\sqrt{5/2}$.")
    a(171, r"Tangency: discriminant zero, or the radius to the contact point is perpendicular to the tangent, or distance from center to line equals radius.",
      r"Condition that $x+y+c=0$ is tangent to $x^2+y^2=1$.", r"$|c|/\sqrt{2}=1$, $|c|=\sqrt{2}$.",
      r"Tangent to $x^2+y^2=r^2$ at $(x_0,y_0)$ on the circle is", r"$x x_0+y y_0=r^2$.",
      r"Using $xx_0+yy_0=r^2$ when $(x_0,y_0)$ is not on the circle.",
      r"Horizontal tangents to $x^2+y^2=25$.", r"$y=\pm 5$.",
      r"Number of tangents from $(3,0)$ to $x^2+y^2=1$.", r"Two (external point).")
    a(172, r"A 2D coordinate argument proves a geometric claim by placing the figure conveniently: put a vertex at the origin, a side on an axis, use vectors or distances. Generality is preserved by the placement if it uses remaining symmetries.",
      r"Prove the midpoint of the hypotenuse of a right triangle is equidistant from all three vertices, by coordinates.",
      r"Place right angle at $(0,0)$, legs along axes to $(2a,0)$ and $(0,2b)$. Midpoint of hypotenuse $(a,b)$. Distances: to origin $\sqrt{a^2+b^2}$, to $(2a,0)$ $\sqrt{a^2+b^2}$, to $(0,2b)$ the same.",
      r"Centroid of a triangle with vertices $(0,0)$, $(2,0)$, $(0,2)$.", r"$\bigl(\frac23,\frac23\bigr)$.",
      r"Placing a general triangle with no remaining freedom and then claiming a special property that depended on the placement.",
      r"Show $AB=AC$ for $A=(0,0)$, $B=(1,2)$, $C=(-1,2)$ by distance.", r"Both $\sqrt{5}$.",
      r"Centroid coordinates are the averages of vertices.", r"Yes.")
    a(173, r"3D distance: $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$. The set at fixed distance from a point is a sphere.",
      r"Distance $(1,2,2)$ to origin.", r"$3$.",
      r"Sphere of radius $2$ about $(0,0,1)$.", r"$x^2+y^2+(z-1)^2=4$.",
      r"Dropping a coordinate (computing a 2D distance in a 3D problem).",
      r"Distance $(1,0,0)$ to $(0,1,0)$.", r"$\sqrt{2}$.",
      r"Does $(1,1,1)$ lie on $x^2+y^2+z^2=3$?", r"Yes.")

    return F
