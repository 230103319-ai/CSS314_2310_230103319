# Task 06: Parametric Speedup Across Processor Densities

## 1. Introduction

The purpose of this task is to calculate theoretical scaled speedup and parallel efficiency using Gustafson's Law for different numbers of processors.

We assume that the serial execution fraction on the parallel machine remains constant at 4%.

Given:

- Serial fraction: α = 0.04
- Parallel fraction: 1 - α = 0.96
- Processor counts: P = 16, 64, 256, 1024, 4096, 16384

## 2. Mathematical Formulas

Gustafson's scaled speedup formula:

**S(P) = P - α(P - 1)**

Substituting α = 0.04:

S(P) = P - 0.04(P - 1)

Simplifying:

**S(P) = 0.96P + 0.04**

Parallel efficiency is defined as:

**E(P) = S(P) / P**

Substituting the speedup formula:

E(P) = (0.96P + 0.04) / P

Therefore:

**E(P) = 0.96 + 0.04/P**

## 3. Step-by-Step Calculations

### Case 1: P = 16

S(16) = 16 - 0.04(16 - 1)

S(16) = 16 - 0.60

**S(16) = 15.40**

E(16) = 15.40 / 16

**E(16) = 0.9625 = 96.25%**

### Case 2: P = 64

S(64) = 64 - 0.04(64 - 1)

S(64) = 64 - 2.52

**S(64) = 61.48**

E(64) = 61.48 / 64

**E(64) = 0.960625 = 96.0625%**

### Case 3: P = 256

S(256) = 256 - 0.04(256 - 1)

S(256) = 256 - 10.20

**S(256) = 245.80**

E(256) = 245.80 / 256

**E(256) = 0.96015625 = 96.015625%**

### Case 4: P = 1024

S(1024) = 1024 - 0.04(1024 - 1)

S(1024) = 1024 - 40.92

**S(1024) = 983.08**

E(1024) = 983.08 / 1024

**E(1024) = 0.9600390625 = 96.00390625%**

### Case 5: P = 4096

S(4096) = 4096 - 0.04(4096 - 1)

S(4096) = 4096 - 163.80

**S(4096) = 3932.20**

E(4096) = 3932.20 / 4096

**E(4096) = 0.960009765625 = 96.0009765625%**

### Case 6: P = 16384

S(16384) = 16384 - 0.04(16384 - 1)

S(16384) = 16384 - 655.32

**S(16384) = 15728.68**

E(16384) = 15728.68 / 16384

**E(16384) = 0.96000244140625 = 96.000244140625%**

## 4. Complete Calculation Table

| Processors (P) | Scaled Speedup S(P) | Efficiency E(P) | Efficiency (%) |
|---:|---:|---:|---:|
| 16 | 15.40 | 0.962500 | 96.250000% |
| 64 | 61.48 | 0.960625 | 96.062500% |
| 256 | 245.80 | 0.960156 | 96.015625% |
| 1024 | 983.08 | 0.960039 | 96.003906% |
| 4096 | 3932.20 | 0.960010 | 96.000977% |
| 16384 | 15728.68 | 0.960002 | 96.000244% |

Values in the table are rounded where appropriate.

## 5. Numerical Computation Log

Input parameters:

alpha = 0.04

processors = [16, 64, 256, 1024, 4096, 16384]

Calculated results:

P = 16: Speedup = 15.40, Efficiency = 96.250000%

P = 64: Speedup = 61.48, Efficiency = 96.062500%

P = 256: Speedup = 245.80, Efficiency = 96.015625%

P = 1024: Speedup = 983.08, Efficiency = 96.003906%

P = 4096: Speedup = 3932.20, Efficiency = 96.000977%

P = 16384: Speedup = 15728.68, Efficiency = 96.000244%

## 6. Efficiency Analysis

The calculation results show that scaled speedup increases almost linearly as the number of processors grows.

When processor count increases from 16 to 16384, the theoretical scaled speedup increases from 15.40 to 15728.68.

However, parallel efficiency decreases slightly:

- At 16 processors: 96.25%
- At 64 processors: 96.0625%
- At 256 processors: 96.015625%
- At 1024 processors: 96.00390625%
- At 4096 processors: approximately 96.000977%
- At 16384 processors: approximately 96.000244%

The total efficiency reduction is approximately 0.249756 percentage points.

The efficiency approaches 96% as processor count grows.

The decline does not accelerate exponentially. Instead, the difference between efficiency and its limiting value decreases proportionally to 1/P.

For each fourfold increase in processor count, this difference becomes four times smaller.

## 7. Asymptotic Analysis

From the efficiency formula:

E(P) = 0.96 + 0.04/P

As P approaches infinity:

lim(P → ∞) 0.04/P = 0

Therefore:

**lim(P → ∞) E(P) = 0.96**

In percentage form:

**E(∞) = 96%**

This result confirms that Gustafson's ideal weak-scaling model predicts high parallel efficiency even for extremely large processor counts when the serial fraction remains constant.

## 8. Conclusion

The calculations demonstrate that Gustafson's Law predicts nearly linear scaled speedup for a workload with a constant serial fraction of 4%.

As processor count increases from 16 to 16384:

- Scaled speedup grows from 15.40 to 15728.68.
- Parallel efficiency decreases slightly from 96.25% to approximately 96.000244%.
- Efficiency approaches its theoretical limit of 96%.

These findings illustrate the potential of weak scaling for large parallel computing systems.

In practical systems, communication overhead, synchronization, memory limitations, and load imbalance may reduce actual efficiency below the theoretical prediction.
