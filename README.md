# Parallel & Distributed Computing Learning Hub

Welcome to the central repository for tutorials on High-Performance Computing (HPC), Cloud Architectures, and Distributed AI. This resource is designed to provide hands-on experience with modern computational frameworks, from shared-memory programming to large-scale cloud orchestration.

## Curriculum Overview
  The tutorials are organized into multiple tracks:

### 1. High-Performance Computing (HPC)
Focuses on maximizing performance on local nodes and distributed clusters.

- OpenMP Basics: Introduction to shared-memory parallelism and the Fork-Join model.
- OpenMP Advanced: Advanced data sharing, tasking, and performance optimization.
- MPI (Message Passing Interface): Distributed-memory programming for cluster environments and supercomputers.

### 2. Distributed Systems & Cloud
Focuses on scalable architectures, service-oriented design, and privacy-preserving AI.

- Cloud & SOA Workshop: * REST API Design & Implementation.
- Microservices Architecture.
- Virtualization & Orchestration (Docker & Kubernetes).
- OpenStack Cloud Management.
- Federated Learning: Decentralized machine learning techniques.

### 3. BigData and AI

### Getting Started
#### Prerequisites
Most tutorials require a Linux-based environment. Specific requirements for each module (e.g., gcc, openmpi-dev, python3, docker) are listed within their respective directories.

#### Common Compilation (HPC)
For OpenMP and MPI exercises, a central Makefile is often provided. General usage:

```Bash
# To compile the beginner OpenMP exercises
cd HPC/openmp-01-basics
make
```
Environment Setup
If you are working on a cluster using a workload manager, sample Slurm scripts (.job or .sh) are included in the exercise folders.

#### License & Usage
- This content is developed for educational purposes.
- Code: Licensed under the MIT License.
- Documentation: Licensed under CC BY 4.0.

#### Acknowledgments
These tutorials were originally developed and refined through various international workshops and educational projects in the fields of Cloud Computing and HPC.

