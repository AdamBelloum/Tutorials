# Setup Guide for Distributed Systems Workshops

This file summarizes setup requirements based on the workshop guides in:
- `Distributed-Systems/cloud-computing-soa/01-rest-api/participants-guide.md`
- `Distributed-Systems/cloud-computing-soa/02-microservices/participants-guide.md`
- `Distributed-Systems/cloud-computing-soa/03-containerization-orchestration/participants-guide.md`
- `Distributed-Systems/cloud-computing-soa/05-openfaas/participants-guide-new.md`
- `Distributed-Systems/federated-learning/docs/participant-guide.md`

## 1. Global Setup (Used Across Multiple Tutorials)

### Required
- **Python 3** (recommended: Python 3.9+)
- **pip** (Python package manager)
- **Terminal/Command Line** basics
- **Basic HTTP + JSON understanding** (GET/POST/PUT/DELETE, status codes, JSON request/response)

### Strongly Recommended
- **VS Code** as editor/IDE
- **curl** for API testing

### Optional (but useful)
- **Git** for version control (not mandatory)

## 2. Tutorial-Specific Setup

## 2.1 `01-rest-api` (RESTful URL Shortener with Flask)

### Required for this tutorial
- Python 3 + pip
- Flask
  - Install: `pip install flask`

### Knowledge prerequisites
- Python basics (functions, dictionaries)
- REST API concepts
- HTTP status codes

## 2.2 `02-microservices` (Auth + Shortener with JWT)

### Required for this tutorial
- Everything from `01-rest-api`
- `cryptography` library (RSA signing/verification)
  - Install: `pip install flask cryptography`

### Required project structure awareness
- Two services: auth service and shortener service
- RSA key files (`private_key.pem`, `public_key.pem`) and public-key sharing to shortener service

### Knowledge prerequisites
- JWT basics (`header.payload.signature`, `sub`, `exp`)
- Auth flow (register, login, bearer token)
- Basic password hashing concepts

## 2.3 `03-containerization-orchestration`

### Part 3.1 (Docker + Docker Compose)

#### Required for this part
- Docker
- Docker Compose (usually included with Docker Desktop)

#### Knowledge prerequisites
- Image vs container
- Dockerfile basics
- Port mapping and Docker volumes for persistence

### Part 3.2 (Kubernetes on provided VMs)

#### Required for this part
- Access to provided Debian VMs (1 control plane + 2 workers)
- Kubernetes tools:
  - `kubeadm`
  - `kubectl`
  - `kubelet`

#### Knowledge prerequisites
- Kubernetes `Deployment`, `Service`, `Replica`
- Control plane vs worker roles

## 2.4 `openfaas` (Serverless with OpenFaaS)

### Required for this tutorial
- Docker (and Docker Hub account)
- Kubernetes local cluster tool: `kind`
- `kubectl`
- `arkade`
- OpenFaaS CLI (`faas-cli`)

### Common commands/install hints from guide
- `kind create cluster --name openfaas-lab`
- `arkade get faas-cli`
- `arkade install openfaas-ce`
- `kubectl port-forward -n openfaas svc/gateway 8080:8080`

### Recommended for this tutorial
- Basic JavaScript/Node.js understanding for function handlers
- Browser access for OpenFaaS UI (`http://localhost:8080`)

### Knowledge prerequisites
- Serverless concept (function-based deployment)
- Container image build/push/deploy flow
- Basic Kubernetes service access and port-forwarding

## 2.5 `federated-learning` (Flower-based FL Workshop)

### Required for this tutorial
- Python 3 + pip
- Dependencies from `Distributed-Systems/federated-learning/requirements.txt`:
  - `flwr`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `Pillow`
- Install: `pip install -r Distributed-Systems/federated-learning/requirements.txt`

### Environment requirements from participant guide
- Laptop
- Stable Wi-Fi
- Chrome or Firefox
- JupyterHub login credentials (for workshop environment)
- Assigned Group ID

### Knowledge prerequisites
- Basic Python (loops, functions, running scripts)
- Basic ML concepts (training vs testing)
- Federated Learning basics (local training, aggregation, rounds)

### If running multi-VM setup (from project docs)
- One server node + at least two client nodes
- Port `8080` reachable from clients to server
- Environment variables such as `FLOWER_SERVER_ADDRESS`, `GROUP_ID`, and optional `DATA_PATH`

## 3. Suggested Installation Order

1. Install Python 3 and pip.
2. Install VS Code (recommended).
3. Install Flask and cryptography for `01/02`.
4. Install Docker + Docker Compose for `03` and `05`.
5. Install Kubernetes tooling (`kubectl`, `kubeadm`, `kubelet`) for `03.2`.
6. Install OpenFaaS prerequisites (`kind`, `arkade`, `faas-cli`) for `05-openfaas`.
7. Install Federated Learning dependencies from `requirements.txt`.
8. Optionally install Git anytime.

## 4. Quick Checklist

- [ ] Python 3 installed
- [ ] pip working
- [ ] VS Code installed (recommended)
- [ ] Flask installed
- [ ] cryptography installed
- [ ] curl available
- [ ] Docker + Compose installed (for `03`/`05`)
- [ ] Kubernetes tools installed (for `03.2`)
- [ ] Kind + Arkade + faas-cli installed (for `05-openfaas`)
- [ ] Docker Hub account ready (for `05-openfaas`)
- [ ] Federated Learning dependencies installed (`flwr`, `pandas`, `numpy`, `scikit-learn`, `Pillow`)
- [ ] JupyterHub access + Group ID ready (for `federated-learning` workshop mode)
- [ ] Git installed (optional)
