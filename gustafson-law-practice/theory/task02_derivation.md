# Task 02: Formal Derivation of Scaled Speedup

## 1. Introduction

Gustafson's Law describes the theoretical speedup achieved when the workload increases with the number of processors while parallel execution time remains constant.

The goal is to derive the formula:

**S(P) = s + p × P**

and prove its equivalent form:

**S(P) = P - α(P - 1)**

## 2. Initial Assumptions

Let:

- P = number of processors
- s = serial execution time on the parallel machine
- p = parallel execution time on the parallel machine
- α = serial fraction of the normalized parallel execution time
- S(P) = scaled speedup

We assume that:

1. The serial portion cannot be parallelized.
2. The parallel portion is perfectly distributed among P processors.
3. Communication and synchronization overheads are negligible.
4. Total execution time on P processors is normalized to 1.

Therefore:

**T(P) = s + p = 1**

## 3. Step-by-Step Mathematical Derivation

### Step 1: Determine Parallel Execution Time

On P processors, the normalized execution time is:

T(P) = s + p = 1

The serial part takes time s, and the parallel part takes time p.

### Step 2: Calculate Equivalent Serial Execution Time

If the same scaled workload were executed on only one processor, the parallel portion would require P times more time.

Therefore:

**T(1) = s + P × p**

This represents the time needed to complete the same workload on a single processor.

### Step 3: Define Scaled Speedup

Speedup is the ratio between the equivalent serial execution time and the parallel execution time:

S(P) = T(1) / T(P)

Substituting the expressions:

S(P) = (s + P × p) / (s + p)

Since s + p = 1:

**S(P) = s + P × p**

This is the first form of Gustafson's Law.

### Step 4: Express the Formula Using the Serial Fraction

From the normalization condition:

s + p = 1

We obtain:

p = 1 - s

Substitute this into the speedup formula:

S(P) = s + P(1 - s)

Expand:

S(P) = s + P - Ps

Rearrange:

S(P) = P - Ps + s

Factor out s:

**S(P) = P - s(P - 1)**

### Step 5: Introduce Alpha

The serial fraction measured on the parallel machine is:

α = s / (s + p)

Since s + p = 1:

α = s

Therefore:

**S(P) = P - α(P - 1)**

This is Gustafson's scaled speedup formula.

## 4. Numerical Example

Assume:

- P = 16 processors
- α = 0.05 (5% serial execution time)
- p = 0.95

Using Gustafson's Law:

S(16) = 16 - 0.05(16 - 1)

S(16) = 16 - 0.05 × 15

S(16) = 16 - 0.75

**S(16) = 15.25**

Therefore, the theoretical scaled speedup is 15.25.

The same result can be verified using the first formula:

S(16) = 0.05 + 16 × 0.95

S(16) = 0.05 + 15.20

**S(16) = 15.25**

Both formulas produce identical results.

## 5. Boundary Case Verification

Case 1: P = 1

S(1) = 1 - α(1 - 1) = 1

There is no speedup when only one processor is used.

Case 2: α = 0

S(P) = P

A fully parallel workload achieves ideal linear scaled speedup.

Case 3: α = 1

S(P) = P - (P - 1) = 1

A completely serial workload cannot benefit from additional processors.

## 6. Conclusion

Starting from the normalized execution time s + p = 1, we derived the equivalent serial execution time:

T(1) = s + P × p

This gives:

**S(P) = s + P × p**

By substituting p = 1 - s and α = s, we proved:

**S(P) = P - α(P - 1)**

Gustafson's Law demonstrates that scaled speedup can increase nearly linearly with processor count when the serial fraction is small and the workload grows appropriately.

The result depends on ideal parallel execution assumptions, including negligible additional communication and synchronization overhead.
