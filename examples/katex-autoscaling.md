---
theme: default
math: katex
---

# KaTeX Block Auto-Scaling

This demonstrates how KaTeX math blocks are automatically scaled.

---

## Traditional Rendering

Long formulas would overflow:

$$
\begin{align}
x &= 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 \\
  &= \frac{n(n+1)}{2}
\end{align}
$$

---

## Auto-Scaling

With auto-scaling enabled, long formulas shrink to fit:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi} \quad \text{and} \quad \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6} \quad \text{and} \quad \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e
$$
