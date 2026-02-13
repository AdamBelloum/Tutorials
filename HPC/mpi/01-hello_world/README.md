
#  

#     

# ggggvgg

# gasdfadfasdfasdfasdfasdfasdI have 

#  

#       

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
     |--- hello_world_1.c  - the Parallel Hello World - SPMD  programming
     |--- hello_world_2.c  - the Parallel Hello World - MIMD  programming
     |--- slurm_script.job - Slurm script exemple
```

Ensure you are in the hello_world/ directory.

## **Goal of the hands-on**

### The Parallel Hello World - SPMD programming

The purpose of this program is to demonstrate how a single source file is executed simultaneously across multiple CPU cores or nodes. This code serves as the foundational introduction to SPMD  programming..

- SPMD Basics. The code initializes the MPI environment and retrieves three key pieces of metadata:

```bash
 - The World Size: How many total processes were started by mpirun.
 - The Rank: The unique ID (0, 1, 2...) assigned to the specific process.
 - The Processor Name: The physical name of the hardware node where the process is running.
   Because there are no if (rank == 0) branches, every single process follows the exact same instructions, 
   resulting in the same block of text being printed multiple times.
```

### The Parallel Hello World - MIMD programming

The goal of this program is to demonstrate how to assign specific "roles" or "tasks" to different processes within a single parallel job. This code introduces the MIMD style of programming using conditional branching. While the same binary file is sent to all processors, each processor executes different parts of the code based on its unique identity.

- MIMD programming using conditional Branching by Rank Unlike the previous "Hello World" where every process printed the exact same thing, this code uses if-else logic to differentiate behavior:

```bash
  - Rank 0 (The Master): Identifies itself as the master process and executes a specific block of code (Line 32-39).
  - Rank 1: Prints a "Hello world" greeting and executes its own assigned work (Line 40-47).
  - Rank 2: Prints a "Bye world" message and performs a third set of tasks (Line 48-54).
  - Remaining Ranks: Any ranks higher than 2 fall into the else block (Line 55-58), where they might perform generic worker tasks or remain idle.
```

## **Instructions**

### Step 1: Compile the Code

### Step 2: Run the Executable Code (using SLURM)

- Try changing the number of tasks (--ntasks) in your .job file to see how the output scales. in your .job file to see how the output scales.

### Step 3: Analyze the Output:

- Examine the .out file. Notice the order of the ranks. Are they perfectly sequential (0, 1, 2, 3), or are they jumbled?

## **HowTo**

- Compile:

```bash
  mpicc -o hello_world hello_world.c
```

- Execute: (read the Note below)

```bash
  mpirun -np 4 ./hello_world
```

```bash
 Note: On Cluster executing the command mpirun directly will run the mpi tasks on the head node. 
     In general this is not a good practice and long jobs will be terminated by the system admin. 
     it is recommanded to use a cluster resource manager such as slurm.
     we provide some scripts to help compile and execute the mpi program on the cluster using SLURM
     look at the file: mpi_bug.job and run_mpi,sh for more details. The mpi_bug.job has been written for DAS5 yo mihgt     need to adapt it when using a different cluster.
```