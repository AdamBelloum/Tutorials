# MPI Hands-on Instructions

## Prerequisites:
1. A Linux-based environment or any OS with support for MPI (e.g., OpenMPI) and OpenMP.
2. A working installation of:
    - GCC or another compiler with OpenMP support (gcc or clang).
    - MPI (mpicc for C programs).
3. Basic understanding of C programming, OpenMP, and MPI.
 
## Folder Structure:
```bash   
   |--- mpi_bugs/:Contains MPI code
     |--- mpi_bug1.c  - The "Ping-Pong" communication 
     |--- mpi_bug2.c  - The "Mismatch" Mystery 
     |--- mpi_bug3.c  - The Collective Calculation Crash - Distributed Array Processing 
     |--- mpi_bug4.c  - The Incomplete Reduction - Distributed Summation
     |--- mpi_bug5.c  - The "Unsafe" Buffer Overflow - Asynchronous Speed Mismatch
     |--- mpi_bug6.c  - The Request Handle Hazard - Non-Blocking Performance Test
     |--- mpi_bug7.c  - The Broadcast Breakdown - One-to-All Communication
     |--- slurm_script.job - slurm script example
```
Ensure you are in the hello_world/ directory.

## **Goal of the hands-on**
### The "Ping-Pong" communication (mpi_bug1.c) 
 This program is designed to simulate a basic Ping-Pong data exchange between two parallel processes. The Goal: Rank 0 sends a large "ball" (a 2MB data buffer) to Rank 1. Rank 1 catches it and immediately throws back a small "ball" (a 1-byte message) to Rank 0. The Execution: Both processes use blocking communication (MPI_Send and MPI_Recv). In a perfect scenario, the messages cross paths, both tasks confirm receipt, and the program terminates gracefully.

### The "Mismatch" Mystery (mpi_bug2.c) 
This program attempts to send a sequence of 10 integers from Rank 0 to Rank 1.
 - The Logic: Instead of using standard blocking communication, this code uses Non-blocking calls (MPI_Isendand MPI_Irecv).
 - The Process: Rank 0 calculates a value (alpha), starts a send, and immediately waits for it to finish using MPI_Wait. Rank 1 prepares to receive a value into a variable (beta), and waits for the data to arrive before printing it.
 - The Expectation: The output should show Task 0 sending 0, 10, 20... and Task 1 receiving 0.0, 10.0, 20.0...
 
### The Collective Calculation Crash - Distributed Array Processing  (mpi_bug3.c)
This program distributes a massive array of 16 million floating-point numbers across multiple processes.
 - The Workflow: 1.  The Master (Rank 0) initializes the array and sends "chunks" of it to all other worker tasks. 2.  The Workers (Ranks > 0) receive their specific chunk, perform a calculation using the update function, and send the modified data back to the Master. 3.  The Final Step: The program uses MPI_Reduce to collect the partial sums from every task and combine them into one global total at the Master.
 - The Expectation: The Master should collect all modified array segments and print a final sum that reflects the work done by every process.

### The Incomplete Reduction - Distributed Summation (mpi_bug4.c)
This program distributes a large array of 20 million double-precision numbers across several tasks.
 - The Workflow: The Master (Rank 0) splits the array, handles any "leftover" elements that don't divide evenly, and sends chunks to the Worker tasks. Each task updates its portion of the data and calculates a local sum (mysum).
 - The Goal: The program intends to use MPI_Reduce to aggregate all these local sums into one final global sum on the Master.
 - The Symptom: The program runs to completion, but the "Final sum" printed at the end is wrong—specifically, it doesn't match the sum of the processed data.


### The "Unsafe" Buffer Overflow - Asynchronous Speed Mismatch (mpi_bug5.c)
This program sets up a continuous stream of data between two processes.
 - The Logic: Rank 0 is a "fast sender"—it sits in a loop, sending 2,000-byte messages as fast as possible. Rank 1 is a "slow receiver"—it receives a message and then performs a massive, time-consuming calculation before it is ready to receive the next one.
 - The Problem: In a perfect world, MPI would just wait. However, many MPI implementations try to be helpful by buffering outgoing messages so the sender can keep working.
 - The Symptom: The program might run fine for a few iterations, but eventually, it will crash or hang indefinitely. The behavior is "unsafe" because it depends entirely on how much system memory the MPI library is allowed to use for its internal buffers.

### The Request Handle Hazard - Non-Blocking Performance Test (mpi_bug6.c)
This program is designed to compare two different communication styles across 4 tasks:
 - Tasks 0 & 1: Perform a "Pure Non-blocking" test using MPI_Isend and MPI_Irecv.
 - Tasks 2 & 3: Perform a "Mixed" test where Task 2 uses blocking MPI_Send and Task 3 uses non-blocking MPI_Irecv.
The program uses MPI_Waitall at the very end to ensure all non-blocking operations have finished before calculating the total elapsed time.

### The Broadcast Breakdown - One-to-All Communication (mpi_bug7.c)
This program uses MPI_Bcast (Broadcast). The goal is for the Root process (Task 0) to share the value of a single integer (buffer) with every other task in the communicator.
 - The Logic: Every task initializes its own buffer and defines Task 0 as the root. They then call the broadcast function to synchronize the data.
 - The Problem: While the code looks simple, it violates a fundamental rule of collective operations regarding the count argument.
 - The Symptom: The program will hang (deadlock). Some tasks may finish the call, while others wait forever, preventing the program from ever reaching MPI_Finalize.


## **Instructions**

### Step 1: Compile the Code
### Step 2: Run the Executable Code (using SLURM)
  - Try changing the number of tasks (--ntasks) in your .job file to see how the output scales.
    in your .job file to see how the output scales.
### Step 3: Analyze the Output: 
  - Examine the .out file. Notice the order of the ranks. Are they perfectly sequential (0, 1, 2, 3), or are they jumbled?

## **HowTo**
 - Compile: 
```bash 
   mpicc -o mpi_bug<X> bug<X>.c
``` 
 - Execute: (read the Note below)
```bash 
   mpirun -np 4 ./bug<X>
```
```bash
 Note: On Cluster executing the command mpirun directly will run the mpi tasks on the head node. 
     In general this is not a good practice and long jobs will be terminated by the system admin. 
     it is recommanded to use a cluster resource manager such as slurm.
     we provide some scripts to help compile and execute the mpi program on the cluster using SLURM
     look at the file: mpi_bug.job and run_mpi,sh for more details. The mpi_bug.job has been written for DAS5 yo mihgt     need to adapt it when using a different cluster.
```
