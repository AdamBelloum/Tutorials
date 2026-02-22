# Workshop 3: Containerization & Orchestration

This workshop has two parts:
1. **Workshop 3.1 — Container Containerization**: containerize your existing multi-user URL shortener (from  & 2) using **Docker**, and manage all containers using **Docker Compose**.  
2. **Workshop 3.2 — Container Orchestration**: set up a **Kubernetes cluster** on provided UvA VMs and deploy your containers on it.  

> Note: The workshop explicitly states that you must continue your previous URL shortener + authentication services, and make your system **persistent across restarts** using a **Docker volume**. 

---

## What you are building (high level)

You will deliver:
- Dockerized versions of your existing services (URL shortener + authentication service).
- A `docker-compose.yml` that deploys and connects all containers.
- Persistence: data must survive:
  - service restarts, and
  - `docker compose down` (i.e., container destruction).
- A Kubernetes deployment of the same services on your own cluster on UvA-provided VMs, with at least one service running **3 replicas**, externally accessible. 

---

# Part 3.1 — Container Virtualization (Docker + Docker Compose)

## Goals (what to demonstrate)
During the demo, you should be able to show:
- You deploy your services using **Docker** and they still work (show a few example paths for both services).
- Your system is **persistent across restarts** and survives `docker compose down`.
- What you did to minimize container size / improve build efficiency.
- (Bonus) Anything extra you implemented, clearly explained.

## Constraints / tips to keep in mind
- Make containers **efficient**: order Dockerfile commands carefully, and include the minimum dependencies and source files.  
- Services must be accessible from **outside** your machine (not only inside Docker).
- You may assume storage layer does not create race conflicts if multiple services access it concurrently (to keep things simple).  
- Bonus idea mentioned: implement an **nginx proxy** to expose everything under one port.  

---

## Installation / Setup

### Install Docker and Docker Compose
- On Linux: typically via your distribution package manager.
- On Windows/macOS: use Docker Desktop (includes CLI tools). 

### Recommended testing tools
The assignment recommends using the **same tools as previous assignments** for testing your services. 

---

## Deliverables for Part 3.1
You will typically end up with:
- A `Dockerfile` per service (or however you structure it).
- A `docker-compose.yml` that starts all services together.
- A persistent storage mechanism:
  - ensure your storage service writes contents to a file, and
  - use a Docker **volume** to persist it across restarts.

---

## Usage (hands-on checklist)

### 1) Build and run with Docker Compose
Your README must include the exact commands to deploy the service.
At minimum, your workflow should include:
- Build images
- Start containers
- Verify services are reachable externally

> Add the exact commands you use here (e.g., `docker compose up --build`), matching your implementation.

### 2) Verify external accessibility
You must ensure the services are reachable from outside the containers.
Hands-on checks to do (and to show in demo):
- Call a few endpoints of your URL shortener service
- Call a few endpoints of your authentication service
- Confirm ports are exposed and reachable from your host machine

### 3) Verify persistence (required demo item)
You must show persistence across:
- service restarts, and
- `docker compose down`. 

Suggested demo script:
1. Start the stack with Docker Compose.
2. Create some data (e.g., create a user / create a shortened URL).
3. Restart services and confirm the data remains.
4. Run `docker compose down` (destroy containers).
5. Start again and confirm the data is still there.

### 4) Efficiency / container size (required discussion)
You must be able to explain what you did for:
- minimizing container size
- improving build efficiency (ordering of steps, minimal dependencies, minimal source files).

---

## Report requirements for Part 3.1
Include in the report (same report file also includes Part 3.2): 
- Implementation overview (max 1 page):
  - focus on key design decisions (persistence approach, compactness decisions, etc.)
  - do not describe Dockerfile line-by-line
- Bonus description (succinct; no strict page limit but keep it short)

---

# Part 3.2 — Container Orchestration (Kubernetes)

## Goals (what you are building)
You must: 
1. Deploy a Kubernetes cluster on UvA-provided VMs (OpenLab infrastructure).
2. Use 3 VMs:
   - 1 VM as **control plane**
   - 2 VMs as **worker nodes**
3. Deploy your services:
   - create a **Deployment** for each service
   - at least one service must run with **3 replicas**
4. Create Kubernetes **Services** so your services are externally accessible.
5. Decide which Service type is best for external access.

A tutorial to set up the nodes is provided on the assignment page in Canvas.

---

## Installation / Setup (Kubernetes on provided VMs)

### VM environment
- You will receive **3 VMs per group**, running **Debian**.
- Debian can matter for installation steps (e.g., Docker uses different keys).

### Tools to install
The tutorial document specifies the required tools; it mentions: 
- `kubeadm`
- `kubectl`
- `kubelet`

### Cluster roles (suggested)
- VM #1: control plane (manages the cluster)
- VM #2–#3: worker nodes (run the containers) 

---

## Deployment (hands-on checklist)

### 1) Confirm the cluster is running (required demo item)
You must show your cluster is up and running.

### 2) Deploy services via Kubernetes Deployments
You must create deployments for each service.
One deployment must be configured with **3 replicas**.

### 3) Ensure external accessibility (required demo item)
Create Kubernetes Services to expose your services externally, and show they are reachable from your local machine.

### 4) Replica consistency (required demo item)
You must show:
- 3 replicas of a particular service are running, and
- they all offer a consistent view of the database.

### 5) Troubleshooting hint (from assignment tips)
Common errors relate to using the wrong network plugin or forgetting to apply it.

---

## Report requirements for Part 3.2
Add to the same report document:
- Experience report (max 1/2 page):
  - describe your experience working with Kubernetes
  - major challenges encountered
- Answer (max 1/2 page):
  - Based on observations only, deduce Kubernetes’ load balancing algorithm for your replicated service
  - Provide examples that support your deductions
- Bonus description (succinct)
