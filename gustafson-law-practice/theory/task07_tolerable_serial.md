# Task 07: Reverse Engineering Maximum Tolerable Serial Overhead

**Course:** Parallel & Distributed Computing Architecture  
**Topic:** Gustafson's Law & Weak Scaling

## 1. Objective

Determine the maximum allowable serial fraction for a high-performance cluster with **8,192 processing cores** that must achieve a Gustafson scaled speedup of at least **7,500**.

## 2. Given Parameters

| Parameter | Symbol | Value |
|---|---|---:|
| Number of processors | \(P\) | 8,192 |
| Minimum scaled speedup | \(S_{\min}\) | 7,500 |
| Serial fraction on parallel machine | \(\alpha\) | Unknown |

The assumed model is Gustafson's Law:

\[
S_G(P) = P - \alpha(P-1).
\]

The serial fraction satisfies \(0 \leq \alpha \leq 1\).

## 3. Algebraic Derivation

The performance requirement is

\[
S_G(P) \geq S_{\min}.
\]

Substitute Gustafson's formula:

\[
P - \alpha(P-1) \geq S_{\min}.
\]

Because \(P > 1\), rearrange to isolate \(\alpha\):

\[
\begin{aligned}
-\alpha(P-1) &\geq S_{\min}-P,\\
\alpha(P-1) &\leq P-S_{\min},\\
\alpha &\leq \frac{P-S_{\min}}{P-1}.
\end{aligned}
\]

The inequality reverses when multiplied by \(-1\). Therefore, the **maximum tolerable serial fraction** is

\[
\boxed{\alpha_{\max}=\frac{P-S_{\min}}{P-1}}.
\]

Substitute \(P=8192\) and \(S_{\min}=7500\):

\[
\begin{aligned}
\alpha_{\max}
 &= \frac{8192-7500}{8192-1}\\
 &= \frac{692}{8191}\\
 &\approx 0.08448296911244048.
\end{aligned}
\]

As a percentage:

\[
\boxed{\alpha_{\max} \approx 8.448296911\%}.
\]

The exact numerical tolerance is **692/8191**; the percentage is rounded.

## 4. Verification

At the boundary \(\alpha = 692/8191\),

\[
\begin{aligned}
S_G(8192)
 &= 8192-\frac{692}{8191}(8192-1)\\
 &= 8192-692\\
 &= \boxed{7500}.
\end{aligned}
\]

The threshold is met exactly. Any larger serial fraction produces a speedup below 7,500 because \(S_G\) decreases linearly with \(\alpha\) when \(P > 1\).

## 5. Parallel Efficiency at the Threshold

Parallel efficiency under weak scaling is

\[
E_G(P)=\frac{S_G(P)}{P}.
\]

At the minimum acceptable speedup:

\[
\begin{aligned}
E_G(8192) &= \frac{7500}{8192}\\
 &= 0.91552734375\\
 &= \boxed{91.552734375\%}.
\end{aligned}
\]

## 6. Sensitivity Table

Using \(S_G(8192)=8192-8191\alpha\):

| Serial fraction \(\alpha\) | Scaled speedup | Meets \(S \geq 7500\)? |
|---:|---:|:---:|
| 0% | 8,192.00 | Yes |
| 4% | 7,864.36 | Yes |
| 8% | 7,536.72 | Yes |
| Exact boundary, \(692/8191\) (≈ 8.4483%) | 7,500.00 | Yes |
| 9% | 7,454.81 | No |
| 10% | 7,372.90 | No |

A one-percentage-point increase in \(\alpha\) reduces scaled speedup by \(0.01(8191)=81.91\) at this processor count.

## 7. Interpretation and Assumptions

- To satisfy the target, the **serial fraction measured on the parallel machine must not exceed approximately 8.4483%**.
- The serial fraction includes time spent in operations that do not contribute to ideally parallel work, as represented by the model. Real communication, synchronization, load imbalance, and I/O costs may be larger or change with processor count.
- The guarantee holds **within the ideal Gustafson model**, assuming the expanded workload and observed serial fraction are appropriate at 8,192 processors. It is not a measured performance guarantee for a physical cluster.
- Reducing sequential overhead and improving load balance can increase the achievable scaled speedup.

## 8. Conclusion

For \(P=8192\) processors and a required scaled speedup \(S_G(P)\geq7500\), the exact maximum allowable serial fraction is

\[
\boxed{\alpha_{\max}=\frac{692}{8191}\approx 0.0844829691\; (8.4483\%)}.
\]

At that boundary, the scaled speedup is exactly **7,500**, corresponding to parallel efficiency of approximately **91.55%**. Any serial fraction greater than this bound violates the requirement under Gustafson's Law.
