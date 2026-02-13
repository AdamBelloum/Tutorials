# OpenMP Hands-on Instructions

## Prerequisites:
1. A Linux-based environment or any OS with support for OpenMP.
2. A working installation of:
    - GCC or another compiler with OpenMP support (gcc or clang).
3. Basic understanding of C programming, OpenMP
 
## Folder Structure:
```bash   
   |--- hello_world:Contains MPI hello world code
     |--- hello_world.c  - Shared Memory programming
     |--- slurm_script.job - Slurm script exemple
```
Ensure you are in the hello_world/ directory.

## **Goal of the hands-on**
### The Parallel Hello World - SPMD  programming
The purpose of this program is to demonstrate how a single process forks into multiple threads that execute concurrently on a single multi-core node. This code serves as the foundational introduction to the Fork-Join model.

- OpenMP Basics: The code uses a parallel region to create a team of threads. It retrieves two key pieces of metadata using library routines:
 ```bash
  - The Thread ID (tid): A unique integer assigned to each thread in the team (Master is always 0).
  - The Number of Threads: The total count of threads currently executing in the parallel region.
```

- The Logic: Unlike the MPI version, threads share the same memory space. The private(nthreads, tid) clause ensures each thread has its own local instance of these variables to prevent them from overwriting each other.

## **Instructions**

### Step 1: Compile the Code
To compile an OpenMP program, you must explicitly tell the compiler to recognize the #pragma directives using a specific flag (usually -fopenmp).

### Step 2: Run the Executable Code (using SLURM)
OpenMP behavior is often controlled by Environment Variables. Before running, you can decide how many threads to spawn by setting OMP_NUM_THREADS.

### Step 3: Analyze the Output: 
Observe the "Hello World" messages.

- Does the Master thread (ID 0) always print its message first?
- Run the program 5 times. Does the order of the Thread IDs change?
- The Race for Stdout: Even though the threads execute in parallel, they must all share the same terminal output.

## **HowTo**
 - Compile: 
 ```bash 
   gcc -fopenmp -o omp_hello omp_hello.c
 ``` 
 - Execute: (read the Note below)
 ```bash 
   export OMP_NUM_THREADS=4
   ./omp_hello
 ```
```bash
 Note: On a Cluster, while you can run small OpenMP tests on the head node, 
       production runs should use SLURM. 
       
       In your SLURM script (.job file), for OpenMP you typically request:
       #SBATCH --nodes=1            (OpenMP is for shared memory/single node)
       #SBATCH --cpus-per-task=4    (This matches your OMP_NUM_THREADS)
       
       Use 'sbatch slurm_script.job' to submit.
