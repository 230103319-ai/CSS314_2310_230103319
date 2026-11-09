# Task 08: Cross-Over Point Determination (Amdahl vs. Gustafson)

## 1. Introduction

The purpose of this task is to compare the theoretical speedup predicted by Amdahl's Law and Gustafson's Law for 128 processors.

Both calculations use a numerical serial fraction of 0.08 (8%), but each model assumes a different workload-scaling approach.

Amdahl's Law describes fixed-size scaling, while Gustafson's Law describes scaled workloads with approximately constant parallel execution time.

## 2. Given Information

- Number of processors: P = 128
- Amdahl serial fraction: s = 0.08
- Gustafson serial fraction: α = 0.08
- Parallel fraction: 1 - 0.08 = 0.92

Objectives:

1. Calculate Amdahl's speedup.
2. Calculate Gustafson's scaled speedup.
3. Determine the percentage discrepancy.
4. Explain why the two predictions differ.

## 3. Amdahl's Law Calculation

Amdahl's Law is:

**S_A(P) = 1 / [s + (1 - s)/P]**

Substitute the given values:

S_A(128) = 1 / [0.08 + (1 - 0.08)/128]

Simplify:

S_A(128) = 1 / [0.08 + 0.92/128]

S_A(128) = 1 / [0.08 + 0.0071875]

S_A(128) = 1 / 0.0871875

Therefore:

**S_A(128) ≈ 11.4695**

According to Amdahl's Law, the fixed-size workload can be accelerated approximately 11.47 times using 128 processors.

## 4. Gustafson's Law Calculation

Gustafson's scaled speedup formula is:

**S_G(P) = P - α(P - 1)**

Substitute the given values:

S_G(128) = 128 - 0.08(128 - 1)

S_G(128) = 128 - 0.08(127)

S_G(128) = 128 - 10.16

Therefore:

**S_G(128) = 117.84**

According to Gustafson's Law, the scaled workload achieves a theoretical speedup of 117.84.

## 5. Percentage Discrepancy

We calculate the percentage discrepancy using Amdahl's prediction as the reference value.

The formula is:

**Discrepancy (%) = [(S_G - S_A) / S_A] × 100**

Substitute the calculated values:

Discrepancy = [(117.84 - 11.46953405) / 11.46953405] × 100

Discrepancy = (106.37046595 / 11.46953405) × 100

Therefore:

**Percentage Discrepancy ≈ 927.42%**

The ratio between the predictions is:

S_G / S_A = 117.84 / 11.46953405

**S_G / S_A ≈ 10.2742**

Thus, Gustafson's predicted scaled speedup is approximately 10.27 times Amdahl's predicted fixed-size speedup for these numerical parameters.

## 6. Comparison Table

| Metric | Amdahl's Law | Gustafson's Law |
|---|---:|---:|
| Processors | 128 | 128 |
| Numerical serial fraction | 8% | 8% |
| Speedup | 11.4695 | 117.8400 |
| Parallel efficiency | 8.96% | 92.06% |
| Scaling model | Strong scaling | Weak scaling |
| Workload assumption | Fixed size | Increasing size |

The absolute speedup difference is:

117.84 - 11.46953405 = 106.37046595

**Absolute Difference ≈ 106.37**

**Percentage Discrepancy ≈ 927.42%**

## 7. Why the Models Diverge

### 7.1 Amdahl's Law

Amdahl's Law assumes that the total problem size remains fixed.

The serial portion cannot be distributed across multiple processors.

As more processors are added, the parallel execution time decreases, but the serial portion remains unchanged.

For a nonzero serial fraction, maximum speedup is limited by:

S_max = 1/s

With s = 0.08:

S_max = 1/0.08 = 12.5

Therefore, the maximum theoretical speedup for this fixed-size workload is 12.5.

The result of 11.4695 on 128 processors is already approaching this limit.

### 7.2 Gustafson's Law

Gustafson's Law assumes that the problem size grows as the number of processors increases.

The objective is to perform more useful computation within approximately the same execution time.

With α = 0.08:

S_G(P) = P - 0.08(P - 1)

Simplifying:

**S_G(P) = 0.92P + 0.08**

This expression grows almost linearly with processor count.

At P = 128:

S_G(128) = 117.84

This is close to the ideal linear speedup of 128.

### 7.3 Different Serial-Fraction Reference Frames

It is important that s and α are not automatically interchangeable for the same workload.

In Amdahl's Law, s is measured relative to the execution time on one processor.

In Gustafson's Law, α is measured relative to execution time on the parallel machine.

For the same fixed workload, their relationship is:

**α = Ps / [1 + (P - 1)s]**

For P = 128 and s = 0.08:

α = 128(0.08) / [1 + 127(0.08)]

α = 10.24 / 11.16

**α ≈ 0.91756**

Using this correctly converted serial fraction in Gustafson's formula gives the same speedup as Amdahl's Law, approximately 11.4695.

Therefore, the large discrepancy calculated earlier arises because the task uses the same numerical value of 0.08 under different scaling assumptions.

It does not mean that either mathematical law is incorrect.

## 8. Cross-Over Interpretation

At P = 1, both models predict:

S_A(1) = 1

S_G(1) = 1

When 0 < s = α < 1 and P > 1, Gustafson's scaled speedup is greater than Amdahl's fixed-size speedup under the task's numerical comparison.

This
