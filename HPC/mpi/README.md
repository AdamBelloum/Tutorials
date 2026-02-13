# MPI Hands-on Instructions

## Prerequisites:
1. A Linux-based environment or any OS with support for MPI (e.g., OpenMPI) and OpenMP.
2. A working installation of:
    - GCC or another compiler with OpenMP support (gcc or clang).
    - MPI (mpicc for C programs).
3. Basic understanding of C programming, OpenMP, and MPI.
 
## Folder Structure:
```bash
   |--- hello_world:Contains MPI hello world code
   |--- mpi_bugs/: Contains MPI buggy codes.
   |--- doc/: Contains the presentations slides 
```

## **Objective**
Analyze, compile, and fix MPI programs that suffer from communication failures, memory misconceptions, and deadlocks.
the hands on can be done in two steps
 - step1: get some primary knowldge via the hello_world example (see instruction in hello_world/ )
 - step2: fix MPI programs (see instructions  in mpi_bugs/ )


## **HowTO**
### Step 1: Compile the Code
  - Navigate to the directory containing the buggy program (mpi_bugs/ or omp_bugs/).
  - Use the appropriate compiler to compile the code (more information see SURF documentation [1]):

### Step 2: Run the Executable Code
  - Execute the compiled program (more information see SURF documentation [1]):
  - If the program hangs, use Ctrl+C.
  - Note if the error is a crash, a hang, or an incorrect numerical result.
  - Debug: Open the source code. Trace the logic of the message passing.
  - 
### Step 3: Verify the Observations
  - Compare the program's behavior/output with the problem description in the comments.
  - Note any anomalies such as: Segmentation faults, Incorrect outputs, Deadlocks or hangs.

### Step 4: Identify the Cause
  - Analyze the problem by:
  - Checking variable scoping (e.g., shared, private, reduction).
  - Reviewing memory allocation (stack vs. heap).
  - Investigating synchronization mechanisms (e.g., barriers, locks).

### Step 5: Propose and Implement a Fix
 - Modify the source code to address the identified issue.

```bash
Note: On Cluster executing the command mpirun directly will run the mpi tasks on the head node.
      In general this is not a good practice and long jobs will be terminated by the system admin.
      it is recommanded to use a cluster resource manager such as slurm.
      we provide some scripts to help compile and execute the mpi program on the cluster using SLURM
      look at the file: mpi_bug.job and run_mpi,sh for more details. The mpi_bug.job has been written for DAS5 yo mihgt     need to adapt it when using a different cluster.
```
