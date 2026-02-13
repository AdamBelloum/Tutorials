
# OpenMP Workshop (Alpine Linux Edition)


## Pre-requisites
- install docker in your lab/top/descktop/ follow instruction https://www.docker.com 

```sh
docker run --rm -it -v $(pwd):/project  mfisherman/openmpi
```

## Overview

This 4-hour workshop introduces **parallel programming with OpenMP**, using a lightweight
**Alpine Linux container** environment.

Participants will learn:

- Core OpenMP concepts
- How to compile and run parallel programs
- How to measure performance
- How scheduling affects scalability

Hands-on exercises are available at two levels:
- **Beginners** (minimal C knowledge)
- **Intermediates** (some programming experience)

---

## 1. Environment

You will work inside an Alpine Linux container with:

- `gcc`, `make`, musl libc
- Support for OpenMP via `libgomp`
- Basic shell utilities

### Install Required Packages (if needed)

```sh
apk update
apk add build-base libgomp
````

Check compiler:

```sh
gcc --version
```

---

## 2. Repository Structure

```
 README-instruction.md
 README.md
 makefile
 solution_beginner/
 |-- 01_hello_par.c
 |-- 02_parallel_for.c
 |-- 03_reduction.c
 |-- 04_critical.c
 solution_intermidiate/
 |-- 01_schedule.c
 |-- 02_data_scoping.c
 |-- 03_sync_vs_reduction.c
 |-- 04_tasks.c
 |-- pi_parallel.c
```

---
## 3. Compiling Code in Alpine

### Serial programs

```sh
gcc <PATH-TO-C-FILE>/pi_serial.c -o pi_serial -lm
./pi_serial
```

### OpenMP programs

```sh
gcc -fopenmp <PATH-TO-C-FILE>/program.c -o program -lgomp -lm
./program
```

---

## 4. Running with Different Numbers of Threads

```sh
export OMP_NUM_THREADS=4
./pi_parallel
```

---

## 5. Absolute Beginner Track

### Learning Goals

* Understand what parallelism is
* Compile and run OpenMP code
* Measure speedup

### Exercise 1  -   Compile the serial baseline

```sh
gcc <PATH-TO-C-FILE>/pi_serial.c -o pi_serial -lm
./pi_serial
```

Record runtime.

### Exercise 2  -   Parallelize the loop

Add:

```c
#pragma omp parallel for reduction(+:sum)
```

### Exercise 3 -  Test scaling

Run:

```
1, 2, 4, and 8 threads
```

Fill benchmark table below.

---

## 6. Beginner Track

### Learning Goals

* Improve parallel performance
* Understand scheduling strategies
* Analyze scaling behavior

### Exercise 1 -  Compile base version

```sh
cd advanced
gcc -fopenmp pi_parallel.c -o pi_parallel -lgomp -lm
./pi_parallel
```

### Exercise 2  -  Scaling experiment

```sh
export OMP_NUM_THREADS=1; ./pi_parallel
export OMP_NUM_THREADS=2; ./pi_parallel
export OMP_NUM_THREADS=4; ./pi_parallel
export OMP_NUM_THREADS=8; ./pi_parallel
```

### Exercise 3  -  Scheduling

Modify:

```c
#pragma omp parallel for schedule(static) reduction(+:sum)
```

Try:

* `static`
* `dynamic,4`
* `guided`

---

## 7. Benchmark Templates

### A. Basic Performance

| Threads | Runtime (s) | Speedup |
| ------: | ----------: | ------: |
|       1 |             |     1.0 |
|       2 |             |         |
|       4 |             |         |
|       8 |             |         |

---

### B. Speedup + Efficiency

| Threads | Runtime (s) | Speedup | Efficiency |
| ------: | ----------: | ------: | ---------: |
|       1 |             |     1.0 |        1.0 |
|       2 |             |         |            |
|       4 |             |         |            |
|       8 |             |         |            |

---

### C. Scheduling Comparison

| Threads | Schedule | Chunk | Runtime | Notes |
| ------: | -------- | ----: | ------: | ----- |
|       4 | static   |     1 |         |       |
|       4 | dynamic  |     4 |         |       |
|       8 | static   |     1 |         |       |
|       8 | guided   |       |         |       |

---

## 8. Measuring Execution Time

Inside code:

```c
double start = omp_get_wtime();
/* compute */
double end = omp_get_wtime();
printf("Time: %f\n", end - start);
```

Shell timer:

```sh
time ./pi_parallel
```

---

## 9. Expected Learning Outcomes

### Beginner

* Understand basic OpenMP directives
* Write a simple parallel loop
* Measure runtime and speedup

### Intermediate

* Tune thread counts
* Apply scheduling policies
* Evaluate performance results

---

## 10. Suggested Schedule (4 Hours)

| Phase | Topic           |   Time |
| ----: | --------------- | -----: |
|     1 | OpenMP basics   | 30 min |
|     2 | Serial baseline | 15 min |
|     3 | Parallel loop   | 20 min |
|     4 | Scaling         | 30 min |
|     5 | Scheduling      | 30 min |
|     6 | Reporting       | 15 min |
|     7 | Q&A             | 10 min |
|     8 | Breaks          | 30 min |

---

## 11. Known Alpine Limitations

* Must link `-lgomp`
* `time` output is simplified
* No `perf` or advanced profiling

---

<!-- 
## 12. Submission Requirements

Submit:

1. Completed tables
2. Parallel code
3. Short conclusion (3Ð5 sentences) covering:

   * Speedup
   * Bottlenecks
   * Scheduling performance

---
add example later -->

## 13. Key Takeaways

* OpenMP makes parallelization accessible
* Performance depends on:

  * Thread count
  * Loop structure
  * Scheduling
* Alpine has everything needed to explore speedup and scalability

---

## 14. Useful References

* OpenMP Specification: [https://www.openmp.org](https://www.openmp.org)
* GCC OpenMP Guide: [https://gcc.gnu.org/wiki/openmp](https://gcc.gnu.org/wiki/openmp)

---

Happy coding!

```

---

