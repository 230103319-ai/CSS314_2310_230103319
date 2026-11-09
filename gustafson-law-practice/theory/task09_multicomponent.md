# Task 09: Multi-Component Workload Partitioning

## 1. Introduction

The purpose of this task is to analyze a scientific simulation consisting of three computational phases and calculate its theoretical scaled speedup using Gustafson's Law.

The simulation contains serial operations, synchronization overhead, and parallel computation.

We evaluate performance for two processor configurations:

- P = 512
- P = 2048

## 2. Given Information

The scientific simulation consists of three phases.

| Phase | Description | Execution Time |
|---|---|---|
| A | Initial disk I/O and parameter broadcast | 2% |
| B | Boundary message-passing synchronization | 6% |
| C | Core domain flux computation | 92% |
| Total | Complete simulation | 100% |

Phase A involves initialization and data distribution.

Phase B represents synchronization between processors.

Phase C performs the main parallel scientific calculations.

For this exercise, phases A and B are treated as serial-equivalent overhead, while phase C is assumed to be perfectly parallelizable.

## 3. Calculate the Aggregate Serial Fraction

The aggregate serial fraction is the sum of the serial-equivalent components.

The formula is:

**α = α_A + α_B**

Substitute the given values:

α = 0.02 + 0.06

Therefore:

**α = 0.08 = 8%**

The parallel fraction is:

p = 1 - α

p = 1 - 0.08

**p = 0.92 = 92%**

Verification:

0.02 + 0.06 + 0.92 = 1.00

Thus, the workload consists of:

- Serial-equivalent fraction: 8%
- Parallel fraction: 92%

## 4. Gustafson's Law

Gustafson's scaled speedup formula is:

**S(P) = P - α(P - 1)**

Where:

- S(P) = scaled speedup
- P = number of processors
- α = aggregate serial fraction

Substitute α = 0.08:

S(P) = P - 0.08(P - 1)

Expand:

S(P) = P - 0.08P + 0.08

Simplify:

**S(P) = 0.92P + 0.08**

This formula will be used for both processor configurations.

## 5. Calculation for P = 512

### Step 1: Apply Gustafson's Law

S(512) = 512 - 0.08(512 - 1)

S(512) = 512 - 0.08(511)

S(512) = 512 - 40.88

Therefore:

**S(512) = 471.12**

### Step 2: Verify Using Phase Contributions

Phase A:

S_A contribution = 0.02

Phase B:

S_B contribution = 0.06

Phase C:

S_C contribution = 0.92 × 512

S_C contribution = 471.04

Total scaled speedup:

S(512) = 0.02 + 0.06 + 471.04

**S(512) = 471.12**

### Step 3: Calculate Parallel Efficiency

Parallel efficiency is:

E(P) = S(P) / P

Substitute:

E(512) = 471.12 / 512

E(512) = 0.92015625

Therefore:

**E(512) = 92.015625%**

The simulation achieves a theoretical scaled speedup of 471.12 with approximately 92.02% parallel efficiency.

## 6. Calculation for P = 2048

###
