# Task 10: Memory Growth Rate vs. Scaled Speedup

## 1. Introduction

The purpose of this task is to analyze how memory capacity and maximum problem dimension change under weak scaling in a parallel computing system.

Under Gustafson's weak-scaling model, the total workload increases proportionally with the number of processors while the amount of work per processor remains approximately constant.

We investigate a three-dimensional grid-based numerical solver with a maximum memory capacity of 32 GB per computing node.

The analysis considers systems containing 64 and 512 nodes.

## 2. Given Information

- Scaling model: Weak scaling
- Memory per node: 32 GB
- Processor configurations: P = 64 and P = 512
- Workload model: W(P) = P × W(1)
- Aggregate memory model: M(P) = c × P
- Grid dimensions: N × N × N
- Grid memory complexity: O(N³)

The task does not specify the memory consumed by each grid element.

Therefore, we first derive a general formula using b bytes per element and then calculate numerical examples assuming 8 bytes per element (double-precision floating-point storage).

For consistency, 1 GB is treated as 10^9 bytes. The examples assume that all memory is available for grid data, without additional storage overhead.

## 3. Weak Scaling and Memory Growth

Under ideal weak scaling:

**W(P) = P × W(1)**

This means that increasing the processor count allows the total workload to increase proportionally.

The total memory capacity follows:

**M(P) = c × P**

Where:

- M(P) = total aggregate memory capacity
- c = available memory per node
- P = number of nodes

Since each node has 32 GB:

**M(P) = 32P GB**

The total memory capacity grows linearly with the number of computing nodes.

## 4. Total Memory for 64 Nodes

Given:

P = 64

Memory per node = 32 GB

Total memory:

M(64) = 32 × 64

**M(64) = 2048 GB**

Converting to decimal terabytes:

M(64) = 2048 / 1000

**M(64) = 2.048 TB**

Therefore, a 64-node system provides a theoretical aggregate memory capacity of 2048 GB.

## 5. Total Memory for 512 Nodes

Given:

P = 512

Memory per node = 32 GB

Total memory:

M(512) = 32 × 512

**M(512) = 16384 GB**

Converting to decimal terabytes:

M(512) = 16384 / 1000

**M(512) = 16.384 TB**

Therefore, a 512-node system provides a theoretical aggregate memory capacity of 16384 GB.

## 6. Three-Dimensional Grid Memory Model

A cubic three-dimensional grid has dimensions:

N × N × N

The total number of elements is:

**Number of elements = N³**

If each element requires b bytes, the memory requirement is:

**M_grid(N) = b × N³ bytes**

The grid must fit within the total available memory:

b × N³ ≤ 32 × 10^9 × P

Divide both sides by b:

N³ ≤ (32 × 10^9 × P
