# Task 04: Asymptotic Analysis of Parallel Efficiency

## 1. Introduction

Parallel efficiency measures how effectively processors are utilized in a parallel computing system.

The efficiency formula is:

E(P) = S(P) / P

Where:
- E(P) = parallel efficiency
- S(P) = speedup
- P = number of processors
- α = serial fraction measured on the parallel machine

The objective is to determine the asymptotic efficiency of Gustafson's Law and compare it with Amdahl's Law as P approaches infinity.

## 2. Gustafson's Law Efficiency

Gustafson's scaled speedup formula is:

**S_G(P) = P - α(P - 1)**

Parallel efficiency is defined as:

E_G(P) = S_G(P) / P

Substituting Gustafson's formula:

E_G(P) = [P - α(P - 1)] / P

Expanding:

E_G(P) = [P - αP + α] / P

Dividing each term by P:

**E_G(P) = 1 - α + α/P**

This can also be written as:

**E_G(P) = 1 - α(1 - 1/P)**

## 3. Asymptotic Limit of Gustafson's Efficiency

We calculate:

lim(P → ∞) E_G(P)

Substituting the efficiency expression:

lim(P → ∞) [1 - α + α/P]

Assuming α remains constant as P increases:

lim(P → ∞) α/P = 0

Therefore:

**lim(P → ∞) E_G(P) = 1 - α**

This proves that Gustafson's parallel efficiency approaches a positive constant when 0 ≤ α < 1.

For example, if α = 0.04:

lim(P → ∞) E_G(P) = 1 - 0.04

**E_G(∞) = 0.96 = 96%**

Under the ideal weak-scaling assumptions, efficiency approaches 96%, even as the number of processors becomes very large.

## 4. Amdahl's Law Efficiency

Amdahl's fixed-size speedup formula is:

**S_A(P) = 1 / [s + (1 - s)/P]**

Where s is the serial fraction of the original single-processor workload.

Parallel efficiency is:

E_A(P) = S_A(P) / P

Substituting:

E_A(P) = 1 / [P(s + (1 - s)/P)]

Simplifying:

**E_A(P) = 1 / [Ps + (1 - s)]**

## 5. Asymptotic Limit of Amdahl's Efficiency

We calculate:

lim(P → ∞) E_A(P)

Substituting:

lim(P → ∞) 1 / [Ps + (1 - s)]

For a constant s > 0:

Ps → ∞ as P → ∞

Therefore:

**lim(P → ∞) E_A(P) = 0**

This means that, under fixed-size scaling with a nonzero serial fraction, adding processors eventually produces diminishing efficiency.

Special case:

If s = 0, the workload is fully parallelizable.

Then:

E_A(P) = 1

Therefore:

**lim(P → ∞) E_A(P) = 1 when s = 0**

## 6. Numerical Comparison

Assume the numerical parameters α = s = 0.04 for illustration.

| Processors P | Gustafson Efficiency | Amdahl Efficiency |
|---|---|---|
| 1 | 100% | 100% |
| 16 | 96.25% | 62.50% |
| 64 | 96.06% | 28.09% |
| 256 | 96.02% | 8.95% |
| 1024 | 96.00% | 2.38% |
| Infinity | 96% | 0% |

These efficiency values illustrate two different workload-scaling assumptions.

Although the same numerical parameter 0.04 is used, α and s represent serial fractions measured under different execution conditions.

## 7. Interpretation

### Gustafson's Law

Gustafson's Law assumes the parallel workload increases with processor count while parallel execution time remains approximately constant.

Its asymptotic efficiency is:

**E_G(∞) = 1 - α**

Thus, efficiency can remain high if the serial fraction stays small and communication overhead does not increase significantly.

### Amdahl's Law

Amdahl's Law assumes the total workload remains fixed.

Its asymptotic efficiency is:

**E_A(∞) = 0 for s > 0**

The fixed serial portion eventually dominates the reduced parallel runtime, limiting effective processor utilization.

## 8. Important Assumptions and Limitations

The theoretical results depend on the following assumptions:

1. The serial fractions remain constant in their respective models.
2. The parallel workload can be expanded under weak scaling.
3. Communication and synchronization overheads are negligible or sufficiently controlled.
4. Processor performance remains consistent.
5. Memory bandwidth and resource contention do not create additional bottlenecks.

In real distributed systems, increased communication, load imbalance, and synchronization may cause measured efficiency to decline below Gustafson's ideal prediction.

## 9. Conclusion

The asymptotic efficiency of Gustafson's Law is:

**lim(P → ∞) E_G(P) = 1 - α**

For Amdahl's Law:

**lim(P → ∞) E_A(P) = 0, if s > 0**

These results demonstrate the distinction between weak scaling and strong scaling.

Gustafson's Law indicates that high parallel efficiency can theoretically be maintained by increasing the workload with processor count.

Amdahl's Law demonstrates that fixed-size applications with nonzero serial work experience diminishing efficiency as processor count increases.

Both laws are useful for understanding performance limitations and designing scalable parallel computing systems.
