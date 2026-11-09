# Task 01: Strong Scaling vs. Weak Scaling Foundations

## 1. Introduction

Amdahl's Law and Gustafson's Law are two important models in parallel computing. Both describe how performance changes when the number of processors increases, but they use different assumptions about workload size.

## 2. Amdahl's Law (Strong Scaling)

Amdahl's Law was introduced by Gene Amdahl in 1967. It assumes that the total problem size remains constant while the number of processors increases.

The formula is:

**S(P) = 1 / (s + (1 - s) / P)**

Where:
- S(P) = speedup
- P = number of processors
- s = serial fraction of the original workload
- 1 - s = parallel fraction

As P approaches infinity, the problem size remains unchanged:

**W(P) = W(1) = constant**

The maximum speedup approaches 1/s for s > 0.

For example, if 10% of a program is serial, the maximum speedup is 10, regardless of how many processors are added.

This is called **fixed-size scaling** because the workload does not grow.

## 3. Gustafson's Law (Weak Scaling)

Gustafson's Law was introduced by John Gustafson in 1988. Unlike Amdahl's Law, it assumes that the workload can increase as more processors become available while total execution time remains approximately constant.

The formula is:

**S(P) = P - α(P - 1)**

Where:
- S(P) = scaled speedup
- P = number of processors
- α = serial fraction measured on the parallel machine

Under ideal weak scaling, the parallel workload increases proportionally with processor count.

**W(P) = Θ(P)** as P approaches infinity, assuming a fixed amount of parallel work per processor.

For example, if α = 0.04 and P = 100:

S(100) = 100 - 0.04(99) = 96.04

The theoretical scaled speedup is 96.04.

This is called **fixed-time scaling** because a larger problem can be solved in approximately the same execution time by using additional processors.

## 4. Comparison

| Feature | Amdahl's Law | Gustafson's Law |
|---|---|---|
| Scaling type | Strong scaling | Weak scaling |
| Problem size | Fixed | Increases |
| Main assumption | Constant workload | Approximately constant execution time |
| Serial fraction | Measured relative to serial execution | Measured relative to parallel execution |
| Speedup | Limited by fixed serial fraction | Can grow nearly linearly |
| Main purpose | Accelerate an existing problem | Solve larger problems with more processors |

## 5. Philosophical and Physical Differences

Amdahl's Law focuses on reducing the execution time of a fixed workload. It emphasizes that serial code creates a performance limit.

Gustafson's Law focuses on increasing the amount of useful computation performed within a fixed time. It demonstrates that additional processors can be used to solve larger problems rather than simply finishing smaller problems faster.

In real computing systems, Gustafson's assumptions may be affected by communication overhead, memory limitations, and synchronization costs.

## 6. Conclusion

Amdahl's Law and Gustafson's Law describe different approaches to parallel computing.

Amdahl's Law is appropriate when the problem size is fixed and the objective is to reduce execution time.

Gustafson's Law is appropriate when the workload can grow with the number of processors while execution time remains approximately constant.

Therefore, Gustafson's Law provides a useful model for large scientific simulations and other scalable computational workloads.
