# Task 03: The Serial Fraction Invariance Paradox

## 1. Introduction

Amdahl's Law and Gustafson's Law use different reference points to measure the serial fraction of a parallel program.

Amdahl's Law measures the serial fraction relative to the execution time on a single processor.

Gustafson's Law measures the serial fraction relative to the execution time on a parallel machine.

This distinction explains why Amdahl's Law predicts a speedup limit for fixed workloads, while Gustafson's Law permits nearly linear scaled speedup for growing workloads.

## 2. Serial Fraction in Amdahl's Law

Amdahl's Law assumes that the total problem size remains constant.

Its speedup formula is:

**S_A(P) = 1 / (f + (1 - f) / P)**

Where:
- P = number of processors
- f = serial fraction measured on one processor
- 1 - f = parallelizable fraction

Let the original serial and parallel execution times be t_s and t_p.

Then:

**f = t_s / (t_s + t_p)**

On P processors, assuming ideal parallel execution:

T(P) = t_s + t_p / P

The serial fraction of the actual parallel runtime becomes:

**α(P) = t_s / (t_s + t_p / P)**

Therefore, with a fixed workload, the observed serial fraction on the parallel machine generally increases as the processor count increases.

## 3. Serial Fraction in Gustafson's Law

Gustafson's Law assumes that a larger workload can be processed using additional processors while maintaining approximately constant execution time.

Its formula is:

**S_G(P) = P - α(P - 1)**

Where α is the serial fraction measured on the parallel machine.

For normalized parallel execution:

s + p = 1

Therefore:

α = s

The equivalent single-processor execution time for the scaled workload is:

T(1) = s + P × p

Thus:

S_G(P) = s + P × p

Substituting p = 1 - α:

**S_G(P) = P - α(P - 1)**

Unlike the fixed-size model, the workload expands as additional processors become available.

## 4. Analytical Resolution of the Apparent Paradox

The two models do not contradict each other because they describe different scaling conditions.

For a fixed workload, let f be the original serial fraction:

f = t_s / (t_s + t_p)

The serial fraction measured during execution on P processors is:

α(P) = t_s / (t_s + t_p / P)

Dividing numerator and denominator by the original total runtime gives:

α(P) = f / (f + (1 - f) / P)

Multiplying numerator and denominator by P:

**α(P) = Pf / (1 + (P - 1)f)**

Now substitute this fraction into Gustafson's formula:

S_G(P) = P - α(P - 1)

S_G(P) = P - [Pf(P - 1) / (1 + (P - 1)f)]

Simplifying:

**S_G(P) = P / (1 + (P - 1)f)**

This is exactly equivalent to Amdahl's formula:

**S_A(P) = 1 / (f + (1 - f) / P)**

Therefore, when both models describe the same fixed workload and use correctly converted serial fractions, they predict identical speedup.

The apparent contradiction appears when the serial fractions from different measurement conditions are treated as interchangeable.

## 5. Numerical Example

Assume:

- Serial execution time = 1 second
- Parallelizable execution time = 9 seconds
- Number of processors P = 16

### Case A: Fixed Workload (Amdahl)

Original execution time:

T(1) = 1 + 9 = 10 seconds

On 16 processors:

T(16) = 1 + 9 / 16 = 1.5625 seconds

Speedup:

S_A(16) = 10 / 1.5625

**S_A(16) = 6.4**

The observed serial fraction on the parallel machine is:

α(16) = 1 / 1.5625 = 0.64

Using Gustafson's formula with this measured fraction:

S_G(16) = 16 - 0.64(15)

**S_G(16) = 6.4**

The two results agree.

### Case B: Scaled Workload (Gustafson)

Now increase the parallelizable workload by a factor of 16 while keeping the serial work unchanged.

Equivalent serial runtime:

T(1) = 1 + 16 × 9 = 145 seconds

Parallel runtime on 16 processors:

T(16) = 1 + 144 / 16 = 10 seconds

The measured serial fraction becomes:

α = 1 / 10 = 0.10

Scaled speedup:

S_G(16) = 16 - 0.10(15)

**S_G(16) = 14.5**

The larger speedup is possible because the problem size has increased, not because the serial execution time has disappeared.

## 6. Critical Comparison

| Property | Amdahl's Law | Gustafson's Law |
|---|---|---|
| Workload | Fixed | Scaled |
| Serial fraction | Relative to single-core runtime | Relative to parallel runtime |
| Execution time | Decreases with more processors | Approximately constant |
| Main limitation | Fixed serial workload | Communication, synchronization and other overhead |
| Primary objective | Reduce execution time | Process more work in the same time |

Gustafson's Law does not eliminate serial overhead. Instead, it demonstrates that its relative impact can be managed by increasing the amount of parallel work.

If communication or synchronization overhead grows substantially with processor count, the fixed-time scaling assumption may fail.

## 7. Conclusion

The serial fraction invariance paradox is resolved by recognizing the different reference frames used by Amdahl's Law and Gustafson's Law.

Amdahl's Law evaluates speedup for a fixed workload using the serial fraction measured on one processor.

Gustafson's Law evaluates scaled speedup using the serial fraction measured on the parallel machine.

When both models are applied to the same fixed workload with consistent serial-fraction definitions, their predictions are mathematically identical.

Gustafson's higher scaled speedups arise from increasing the workload while keeping execution time approximately constant.

Therefore, both laws are valid and complementary models of parallel performance.
