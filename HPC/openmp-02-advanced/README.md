TODO
# openmp  Hands-on Instructions

## Prerequisites:
1. A Linux-based environment or any OS with support for MPI (e.g., OpenMPI) and OpenMP.
2. A working installation of:
    - GCC or another compiler with OpenMP support (gcc or clang).
3. Basic understanding of C programming, Ond penMP.
 
## Folder Structure:
```bash
   |--- hello_world:Contains OpenMP hello world code
   |--- openmp_bugs/: Contains OpenMP buggy codes (omp_bug1.c to omp_bug6.c)
   |--- doc/: Contains the presentations slides 
```

## **Objective**
Identify and fix common parallel programming errors in OpenMP, including syntax violations, data races, deadlocks, and memory management issues. The hands-on session is divided into two steps:

  - Step 1: verify that  environment is setup correctlyusing the hello_world example.
  - Step 2: Analyze and fix 6 buggy OpenMP programs in the omp_bugs/ directory.

## **HowTO**

### Step 0: Environmental Setup
OpenMP threads often require more stack space than standard serial programs, especially when using private arrays. Before starting, it is highly recommended to remove stack limits in your current terminal session:
```bash
ulimit -s unlimited
export OMP_NUM_THREADS=4
```

### Step 1: Compile the Code
  - Navigate to the omp_bugs/ directory.
  - Compile using the -fopenmp flag to enable OpenMP directives:
 ```bash
./bug_exe
```
### Step 2: Run the Executable Code
  - Execute the compiled program:
 ```bash
gcc -fopenmp -o bug_exe omp_bugX.c
```
  - Observe: Does the program crash (Segmentation Fault), hang (Deadlock), or finish with a "wrong" result
  - Repeat: For OpenMP, it is crucial to run the code multiple times. If the output changes every time, you have a Data Race.

### Step 3: Identify the Cause
  - Analyze the source code and look for:
    - Variable Scoping: Are variables correctly marked as shared, private, or firstprivate?
    - Reductions: Are global sums protected, or are threads overwriting each other?
    - Memory Allocation: Is a large array trying to fit on the thread stack?
    - Synchronization: Are barriers or locks used in a way that causes threads to wait forever?

### Step 4: Propose and Implement a Fix
  - Modify the source code to address the identified issue.
  - Re-compile and re-run to verify the fix is stable across multiple executions.

```bash
Note on Performance:
      Unlike MPI, OpenMP is a Shared Memory model. This means all threads 
      run on a single node and share the same memory address space.

Note on Slurm:
      If you are running these exercises on a cluster, ensure your 
      Slurm script requests a single node with multiple CPUs:
      #SBATCH --nodes=1
      #SBATCH --cpus-per-task=4
      
      Using more threads than physical CPU cores available can lead 
      to significant performance degradation (oversubscription).
  ```
