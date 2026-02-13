# OpenMP Hands-on Instructions


## Prerequisites:
1. A Linux-based environment or any OS with support for MPI (e.g., OpenMPI) and OpenMP.
2. A working installation of:
   - GCC or another compiler with OpenMP support (gcc or clang).
   - MPI (mpicc for C programs).
3. Basic understanding of C programming, OpenMP, and MPI.

Folder Structure:
----------------
```bash  
    |--- omp_bugs/: Contains OpenMP code
       |--- omp_bug1.c  - The Syntax Barrier - Combined Construct Rules
       |--- omp_bug2.c  - The Data Race - Shared Memory Summation
       |--- omp_bug3.c  - The Orphaned Barrier - Nested Sync Deadlock
       |--- omp_bug4.c  - The Stack Limit - Private Array SegFault
       |--- omp_bug5.c  - The Deadly Embrace - Circular Lock Dependency
       |--- omp_bug6.c  - The Scoping Trap - Orphaned Directive Reductions
       |--- slurm_script.job - Slurm script example
```
### **Objective**
Identify and fix data races, synchronization issues, and memory management errors in shared memory parallel programming.

### **The Syntax Barrier** (omp_bug1.c)
This program is designed to demonstrate the strict relationship between OpenMP directives and the code blocks they control.

 - The Logic: It attempts to use the parallel for combined construct to distribute loop iterations.
 - The Process: The code initializes a team of threads to update an array. It tries to capture the thread ID (tid) immediately before the loop starts.
  - The Symptom: The program will fail to compile. This serves as a lesson on "canonical loop form" and the constraints of combined directives.

### **The Data Race** - Shared Memory Summation (omp_bug2.c)
This program calculates a large mathematical sum across multiple threads to demonstrate how shared memory conflicts occur.

 - The Logic: The program spawns a parallel region where every thread contributes to a global variable total.

 - The Process: Threads work through a loop of 1 million iterations using a dynamic schedule.

 - The Symptom: The code compiles and runs, but the "Final Total" is non-deterministic. If you run it multiple times, you will get different, incorrect answers because threads are overwriting each other's updates.

### **The Orphaned Barrier**- Nested Sync Deadlock (omp_bug3.c)
This program uses sections to perform different tasks in parallel and uses barriers to ensure clean console output.

 - The Logic: The code divides work into two sections. Inside each section, it calls a subroutine (print_results) to display data.

 - The Problem: The subroutine contains an omp barrier. By definition, a barrier must be encountered by all threads in the team.

 -  The Symptom: The program will hang (deadlock). Because only one thread enters a specific section, that thread waits at the barrier for a team that is not coming.

#### **The Stack Limit** - Private Array SegFault (omp_bug4.c)
This program demonstrates the physical memory limits of thread-local storage (the Stack).

 - The Logic: A large 2D array (1048x1048 doubles) is declared. The code attempts to make this array private so each thread has its own workspace.

 - The Problem: Private variables are allocated on the thread stack. Most systems have a stack limit (e.g., 8MB) that is smaller than the requested array.

 - The Symptom: The program will crash immediately with a Segmentation Fault before performing any calculations.

### **The Deadly Embrace** - Circular Lock Dependency (omp_bug5.c)
This program uses low-level locks (omp_lock_t) to protect two different arrays while threads perform cross-array updates.

 - The Logic: Thread A tries to update Array B using data from Array A (locking A then B). Thread B tries to update Array A using data from Array B (locking B then A).

 - The Problem: If Thread A grabs Lock A and Thread B grabs Lock B at the same time, neither can acquire the second lock they need.

 - The Symptom: The program hangs indefinitely. This is a classic "Deadlock" or "Deadly Embrace."

### **The Scoping Trap** - Orphaned Directive Reductions (omp_bug6.c)
This program calculates a vector dot product using a function called from within a parallel region.

 - The Logic: The main function defines a parallel region and calls dotprod(). The function uses a #pragma omp for with a reduction.

 - The Problem: Because the sum variable inside the function is not correctly scoped or linked back to the main variable, the partial results are lost.

 - The Symptom: The program runs fine but consistently produces a result of 0.0 or a random incorrect value.


### **HowTo**

- **Environmental Setup**
OpenMP relies on the stack for private variables. OpenMP threads often require more stack space than standard serial programs, especially when using private arrays. 

```bash
Before starting, it is highly recommended to remove stack limits in your current terminal session: To avoid crashes with large arrays, and to set your thread count, run:
``` 
```bash
ulimit -s unlimited
export OMP_NUM_THREADS=4
```
Ensure you are in the omp_bugs/ directory and that your compiler supports OpenMP (e.g., gcc or clang).

- **Compile:**
```bash  
gcc -fopenmp -o bug_exe omp_bugX.c
```
- **Execute:**
```bash
./bug_exe 
```
- **Observe**: Run the program multiple times. If the result changes between runs, you have a data race.
   Note if the error is a segmentation fault (crash), a deadlock (hang), or an inconsistent numerical result.
- **Identify the Cause**: Open the source code. Check pragmas, variable scoping (shared vs. private), and synchronization points.
     - Variable Scoping: Are variables correctly marked as shared, private, or firstprivate?
     - Reductions: Are global sums protected, or are threads overwriting each other?
     - Memory Allocation: Is a large array trying to fit on the thread stack?
     - Synchronization: Are barriers or locks used in a way that causes threads to wait forever?
     - Propose and Implement a Fix
     - Re-compile and re-run to verify the fix is stable across multiple executions.

### The Challenges
Try to solve these by looking at the code logic first:
 - omp_bug1.c: Fix the compilation or logic error in the parallel loop structure.
 - omp_bug2.c: Fix the inconsistent "Total" result caused by multiple threads updating one variable.
 - omp_bug3.c: Resolve the runtime error occurring due to improper synchronization placement.
 - omp_bug4.c: Fix the Segmentation Fault caused by stack size limits and incorrect variable scoping.
 - omp_bug5.c: Resolve the Deadlock where threads are stuck waiting for each other's locks.
 - omp_bug6.c: Fix the logic error where the final sum is not correctly updated from a function call.
