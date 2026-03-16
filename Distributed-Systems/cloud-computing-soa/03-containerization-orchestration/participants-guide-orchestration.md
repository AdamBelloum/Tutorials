# Workshop Tutorial 3.2: Orchestrating the Authentication Service and URL Shortener on Kubernetes

Note: The VM names (`student127`, `student128`, `student129`) are examples used in this guide. Replace them with your own VM names/IPs in your environment.

Welcome! In this workshop, you will adapt your Assignment 3.1 system to **Assignment 3.2** by deploying it to a 3-node Kubernetes cluster.

By the end, you will have:

- A **Kubernetes control plane** on `student127`
- Two **worker nodes** (`student128`, `student129`) joined to the cluster
- **Authentication Service** and **URL Shortener Service** deployed in namespace `websvc`
- **Persistent shared storage** using NFS + PV/PVC (`ReadWriteMany`)
- Services exposed through **NodePort** (`30081` and `30080`)
- A reliable **verification and unittest workflow**

This guide is based on the exact project layout and scripts in this repository and includes practical fixes for the issues that are most likely to appear during setup.

---

## 0. What Changes Compared to Assignment 3.1?

In Assignment 3.1, both services run with Docker Compose on a single machine.

In Assignment 3.2, you must:

1. deploy the services to Kubernetes
2. run on multiple nodes (control-plane + workers)
3. use Kubernetes resources (Namespace, Deployment, Service, ConfigMap, Secret, PV, PVC)
4. make persistent storage available across Pods
5. demonstrate the system still works end-to-end

The API behavior remains largely the same; most complexity is in cluster setup, networking, storage, and deployment correctness.

---

## 1. Assignment 3.2 Goals

### 1.1 Core Requirements

| Requirement | Meaning |
| --- | --- |
| Multi-node Kubernetes cluster | `student127` control-plane + `student128/129` workers |
| Service deployment on k8s | `auth` and `shortener` deployed via YAML manifests |
| Shared persistent storage | NFS-backed PV/PVC with RWX access |
| External reachability | NodePort services available on node IPs |
| Authenticated shortener operations | JWT minted by auth and validated by shortener |
| Demonstrable verification | `kubectl` status checks + API checks + unittest |

---

## 2. Project Structure for 3.2

~~~text
03-orchestration/
├── commands/
│   ├── student127-control-plane.sh
│   ├── student128-worker.sh
│   ├── student129-worker.sh
│   ├── push-images.sh
│   └── README.md
├── k8s/
│   ├── namespace.yaml
│   ├── shared-pv.yaml
│   ├── shared-pvc.yaml
│   ├── auth-secret.yaml
│   ├── shortener-configmap.yaml
│   ├── auth-deployment.yaml
│   ├── auth-service.yaml
│   ├── shortener-deployment.yaml
│   └── shortener-service.yaml
├── auth_service/
├── shortener_service/
└── unittest_app/
    ├── unittest_app.py
    └── read_from.csv
~~~

---

## 2.1 Step-by-Step Skeleton Implementation

The `03-orchestration-skeleton` now uses intentional TODO gaps.  
Use this checklist to fill files in a controlled order.

### A. Service code and container files

Start in:

~~~text
skeleton/03-orchestration/03-orchestration-skeleton/
~~~

Implement these files first:

1. `auth_service/auth.py`
- add absolute paths (`BASE_DIR`, `PRIVATE_KEY_FILE`, `PUBLIC_KEY_FILE`, `DATA_FILE`)
- implement persistence helpers:
  - `ensure_parent_dir(path)`
  - `load_users()`
  - `save_users()`
- ensure write endpoints persist data (`POST /users`, `PUT /users`)
- startup block should run:
  - `load_users()`
  - `ensure_keys_exist()`
  - `app.run(host="0.0.0.0", port=5001, debug=False)`

2. `shortener_service/shortener.py`
- add absolute paths (`BASE_DIR`, `PUBLIC_KEY_FILE`, `DATA_FILE`)
- implement persistence helpers:
  - `ensure_parent_dir(path)`
  - `load_urls()`
  - `save_urls()`
- call `load_urls()` before route logic that reads/writes shared state
- call `save_urls()` after mutating operations:
  - `POST /`
  - `PUT /<id>`
  - `DELETE /<id>`
  - `DELETE /`
- startup block should run:
  - `load_urls()`
  - `app.run(host="0.0.0.0", port=5000, debug=False)`

3. `auth_service/requirements.txt` and `shortener_service/requirements.txt`
- include:
  - `flask`
  - `cryptography`

4. `auth_service/Dockerfile` and `shortener_service/Dockerfile`
- base image: `python:3.11-slim`
- `WORKDIR /app`
- install dependencies from `requirements.txt`
- copy app file + `keys/` + `data/`
- expose ports (`5001` for auth, `5000` for shortener)
- run correct entrypoints (`python auth.py`, `python shortener.py`)

5. `docker-compose.yml` (local parity check before k8s)
- define `auth` and `shortener` services
- map ports:
  - `5001:5001`
  - `5000:5000`
- keep persistent data volumes mounted to `/app/data`
- mount keys to `/app/keys`

### B. Kubernetes manifest files (`k8s/`)

Fill these YAML files in this order:

1. `namespace.yaml`
- create namespace `websvc`

2. `shared-pv.yaml`
- PV name: `websvc-shared-pv`
- RWX + 1Gi + `Retain`
- NFS:
  - server `145.100.130.127`
  - path `/srv/nfs/websvc`

3. `shared-pvc.yaml`
- PVC name: `websvc-shared-pvc`
- namespace `websvc`
- bind to `websvc-shared-pv`
- request `1Gi`, access mode `ReadWriteMany`

4. `auth-secret.yaml`
- either:
  - generate secret from key files using `kubectl create secret ... --from-file ...`
  - or fill base64 fields manually
- expected secret name: `auth-keys`

5. `shortener-configmap.yaml`
- create ConfigMap `shortener-public-key`
- data key must be `public_key.pem`
- content must match auth service public key

6. `auth-deployment.yaml`
- deployment `auth`, namespace `websvc`, replicas `1`
- image: `YOUR_DOCKERHUB_USERNAME/auth-service:3.2`
- mount:
  - PVC to `/app/data`
  - secret `auth-keys` to `/app/keys` (readOnly)
- container port `5001`

7. `auth-service.yaml`
- NodePort service `auth`
- selector `app: auth`
- service port/targetPort `5001`
- nodePort `30081`

8. `shortener-deployment.yaml`
- deployment `shortener`, namespace `websvc`, replicas `3`
- image: `YOUR_DOCKERHUB_USERNAME/shortener-service:3.2`
- mount:
  - same PVC to `/app/data`
  - ConfigMap `shortener-public-key` to `/app/keys` (readOnly)
- container port `5000`

9. `shortener-service.yaml`
- NodePort service `shortener`
- selector `app: shortener`
- service port/targetPort `5000`
- nodePort `30080`

### C. Suggested fill-and-verify workflow

Use this quick loop:

1. fill one file
2. run syntax/format check (Python/YAML)
3. move to next file
4. after all files are done, deploy in Section 9 order
5. run smoke + unittest checks in Sections 12 and 13

---

## 3. Preflight Checklist

Before touching Kubernetes:

1. Ensure Docker images exist on Docker Hub.
2. Ensure images are built for **linux/amd64** (your VMs are amd64).
3. Ensure keys are consistent:
- `auth_service/keys/private_key.pem` signs JWT
- `auth_service/keys/public_key.pem` verifies JWT
- `shortener` must mount the same public key

Quick architecture check (on each VM):

~~~bash
uname -m
# expected: x86_64
~~~

---

## 4. Build and Push Images

### 4.1 Use provided script

From project root on your local machine:

~~~bash
docker login
./commands/push-images.sh -u YOUR_DOCKERHUB_USERNAME -t 3.2 --update-k8s
~~~

This script:

- builds `auth-service` and `shortener-service`
- pushes both to Docker Hub
- optionally updates image references in deployment YAMLs

### 4.2 Important platform warning (very common)

If Pods fail with:

~~~text
no match for platform in manifest
~~~

your pushed image is not compatible with VM architecture.

Fix by pushing amd64 images explicitly:

~~~bash
docker buildx create --use --name multiarch-builder 2>/dev/null || docker buildx use multiarch-builder
docker buildx build --platform linux/amd64 -t YOUR_DOCKERHUB_USERNAME/auth-service:3.2 --push auth_service
docker buildx build --platform linux/amd64 -t YOUR_DOCKERHUB_USERNAME/shortener-service:3.2 --push shortener_service
~~~

---

## 5. Bring Up the Cluster

### 5.1 Control-plane (`student127`)

Run:

~~~bash
./commands/student127-control-plane.sh
~~~

### 5.2 Worker setup (`student128`, `student129`)

Run on each worker:

~~~bash
./commands/student128-worker.sh
# and
./commands/student129-worker.sh
~~~

Then on `student127` generate join command:

~~~bash
kubeadm token create --print-join-command
~~~

Run generated `kubeadm join ...` on both workers.

---

## 6. Known Script Pitfall You Must Fix

In `commands/student127-control-plane.sh`, there is an accidental injected command line after `sysctl --system`:

~~~bash
kubectl delete pod -n websvc shortener-766945b597-n92bz --force --grace-period=0
~~~

This line should **not** be part of bootstrap. Remove it before reuse.

Why: it can break idempotency and introduce random errors during first-time cluster setup.

---

## 7. CNI and containerd Configuration (Critical)

A common failure is:

~~~text
failed to find plugin "flannel" in path [/usr/lib/cni]
failed to find plugin "loopback" in path [/usr/lib/cni]
~~~

Fix on **all nodes** (`student127/128/129`):

~~~bash
sudo sed -i 's|bin_dir = "/usr/lib/cni"|bin_dir = "/opt/cni/bin"|g' /etc/containerd/config.toml
sudo systemctl restart containerd
sudo systemctl restart kubelet
~~~

Then re-apply flannel on `student127`:

~~~bash
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
kubectl -n kube-flannel get pods -o wide
~~~

---

## 8. NFS Shared Storage Setup

Your `PV/PVC` expects:

- NFS server: `145.100.130.127`
- export path: `/srv/nfs/websvc`
- access mode: `ReadWriteMany`

### 8.1 On `student127` (NFS server)

~~~bash
sudo mkdir -p /srv/nfs/websvc
sudo chown nobody:nogroup /srv/nfs/websvc
sudo chmod 777 /srv/nfs/websvc

cat <<'NFS' | sudo tee /etc/exports
/srv/nfs/websvc 145.100.130.127(rw,sync,no_subtree_check,no_root_squash) 145.100.130.128(rw,sync,no_subtree_check,no_root_squash) 145.100.130.129(rw,sync,no_subtree_check,no_root_squash)
NFS

sudo exportfs -rav
sudo systemctl enable --now nfs-kernel-server
~~~

### 8.2 On all nodes (including workers)

~~~bash
sudo apt-get update
sudo apt-get install -y nfs-common
~~~

If Pods show `FailedMount ... exit status 32`, check NFS first.

---

## 9. Deploy Kubernetes Resources in Correct Order

Do not rely on `kubectl apply -f k8s/` initially, because namespace-dependent resources can race.

Use explicit order:

~~~bash
cd ~/03-orchestration

kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/shared-pv.yaml
kubectl apply -f k8s/shared-pvc.yaml
~~~

Check binding:

~~~bash
kubectl get pv,pvc -n websvc
# expected: PVC Bound
~~~

Then apply auth key material and shortener public key:

~~~bash
# recommended: build secret from files (safer than handwritten base64)
kubectl -n websvc delete secret auth-keys --ignore-not-found
kubectl -n websvc create secret generic auth-keys \
  --from-file=private_key.pem=auth_service/keys/private_key.pem \
  --from-file=public_key.pem=auth_service/keys/public_key.pem

# recommended: build configmap from actual public key file
kubectl -n websvc create configmap shortener-public-key \
  --from-file=public_key.pem=auth_service/keys/public_key.pem \
  -o yaml --dry-run=client | kubectl apply -f -
~~~

Then deploy workloads/services:

~~~bash
kubectl apply -f k8s/auth-deployment.yaml
kubectl apply -f k8s/auth-service.yaml
kubectl apply -f k8s/shortener-deployment.yaml
kubectl apply -f k8s/shortener-service.yaml
~~~

---

## 10. Two High-Risk Configuration Issues

### 10.1 `auth-secret.yaml` can fail with illegal base64

If you see:

~~~text
Secret ... illegal base64 data at input byte ...
~~~

Do not debug long inline base64 manually. Recreate Secret from files (commands shown above).

### 10.2 Public key mismatch causes all protected calls to return 403

Symptom in unittest:

- login works
- but `POST /` on shortener returns `403` instead of `201`

Cause:

- `shortener-public-key` content does not match auth private key pair.

Fix:

- regenerate ConfigMap from `auth_service/keys/public_key.pem`
- restart shortener deployment

~~~bash
kubectl rollout restart deployment/shortener -n websvc
kubectl rollout status deployment/shortener -n websvc
~~~

---

## 11. Health Verification Commands (Must Run)

### 11.1 Cluster-level

~~~bash
kubectl get nodes -o wide
kubectl get pods -A
~~~

Expected: all 3 nodes `Ready`; core system Pods healthy.

### 11.2 Application-level

~~~bash
kubectl get all -n websvc -o wide
kubectl get svc -n websvc
kubectl get endpoints -n websvc
kubectl get pv,pvc -n websvc
~~~

Expected:

- `auth` and `shortener` Pods `Running`
- `auth` service exposes `5001:30081`
- `shortener` service exposes `5000:30080`
- endpoints are not `<none>`
- PVC is `Bound`

### 11.3 Rollout status

~~~bash
kubectl rollout status deployment/auth -n websvc
kubectl rollout status deployment/shortener -n websvc
~~~

---

## 12. API Smoke Tests

From `student127`:

~~~bash
# register
curl -i -X POST http://127.0.0.1:30081/users \
  -H 'Content-Type: application/json' \
  -d '{"username":"smoke_user","password":"test"}'

# login
curl -i -X POST http://127.0.0.1:30081/users/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"smoke_user","password":"test"}'
~~~

Then use the returned token against shortener:

~~~bash
curl -i -X POST http://127.0.0.1:30080/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"value":"https://example.com"}'
~~~

---

## 13. Unittest Strategy (Recommended)

The most stable strategy is to run unittest on `student127` with local port-forward.

### 13.1 Keep test URLs as localhost

In `unittest_app/unittest_app.py`:

~~~python
base_url = "http://127.0.0.1:5000"
auth_url = "http://127.0.0.1:5001"
~~~

### 13.2 Start two forwards (two terminals)

Terminal A:

~~~bash
kubectl -n websvc port-forward svc/shortener 5000:5000 --address 127.0.0.1
~~~

Terminal B:

~~~bash
kubectl -n websvc port-forward svc/auth 5001:5001 --address 127.0.0.1
~~~

### 13.3 Run tests (third terminal)

~~~bash
cd ~/03-orchestration/unittest_app
python3 unittest_app.py
~~~

If you prefer direct NodePort testing from another machine, set:

~~~python
base_url = "http://145.100.130.127:30080"
auth_url = "http://145.100.130.127:30081"
~~~

But this mode is more sensitive to external network/firewall restrictions.

---

## 14. Troubleshooting Matrix

### Problem 1: `kubectl` tries `localhost:8080` and fails

Symptom:

~~~text
The connection to the server localhost:8080 was refused
~~~

Cause: `admin.conf` missing or not copied to `$HOME/.kube/config`.

Fix:

~~~bash
mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
~~~

If `/etc/kubernetes/admin.conf` does not exist, control-plane init did not complete.

---

### Problem 2: `kubeadm init` preflight errors (ports in use, manifests exist)

Cause: node was already initialized.

Fix:

~~~bash
sudo kubeadm reset -f
sudo rm -rf /etc/kubernetes /var/lib/etcd /etc/cni/net.d
sudo systemctl restart containerd
sudo systemctl restart kubelet
sudo kubeadm init --apiserver-advertise-address=145.100.130.127 --pod-network-cidr=10.244.0.0/16
~~~

---

### Problem 3: Pods stuck `ContainerCreating`

Run:

~~~bash
kubectl describe pod -n websvc <pod-name>
kubectl get events -n websvc --sort-by=.lastTimestamp | tail -n 50
~~~

Interpret quickly:

- `failed to find plugin flannel/loopback`: CNI path issue (Section 7)
- `FailedMount ... nfs ... exit status 32`: NFS issue (Section 8)
- `ErrImagePull`/`ImagePullBackOff`: image/tag/platform/permission issue (Section 4)

---

### Problem 4: `ErrImagePull` with `no match for platform in manifest`

Fix: rebuild and push with `--platform linux/amd64` (Section 4.2).

---

### Problem 5: All unittest cases fail with `403 != 201`

Cause: shortener cannot verify JWT because mounted public key is wrong/mismatched.

Fix:

- recreate `shortener-public-key` ConfigMap from `auth_service/keys/public_key.pem`
- rollout restart shortener

---

### Problem 6: `No resources found in websvc namespace`

Cause: manifests not applied or namespace ordering issue.

Fix:

- apply `namespace.yaml` first
- apply the rest in explicit order (Section 9)

---

## 15. Commands Recap (End-to-End)

### 15.1 Build/push images

~~~bash
docker login
./commands/push-images.sh -u YOUR_DOCKERHUB_USERNAME -t 3.2 --update-k8s
~~~

### 15.2 Initialize nodes

~~~bash
# student127
./commands/student127-control-plane.sh

# student128
./commands/student128-worker.sh

# student129
./commands/student129-worker.sh

# student127 -> generate join
kubeadm token create --print-join-command
~~~

### 15.3 Apply manifests safely

~~~bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/shared-pv.yaml
kubectl apply -f k8s/shared-pvc.yaml
kubectl -n websvc create secret generic auth-keys \
  --from-file=private_key.pem=auth_service/keys/private_key.pem \
  --from-file=public_key.pem=auth_service/keys/public_key.pem \
  -o yaml --dry-run=client | kubectl apply -f -
kubectl -n websvc create configmap shortener-public-key \
  --from-file=public_key.pem=auth_service/keys/public_key.pem \
  -o yaml --dry-run=client | kubectl apply -f -
kubectl apply -f k8s/auth-deployment.yaml
kubectl apply -f k8s/auth-service.yaml
kubectl apply -f k8s/shortener-deployment.yaml
kubectl apply -f k8s/shortener-service.yaml
~~~

### 15.4 Verify

~~~bash
kubectl get nodes -o wide
kubectl get all -n websvc -o wide
kubectl get pv,pvc -n websvc
kubectl get endpoints -n websvc
~~~

### 15.5 Run unittest

~~~bash
# terminal A
kubectl -n websvc port-forward svc/shortener 5000:5000 --address 127.0.0.1

# terminal B
kubectl -n websvc port-forward svc/auth 5001:5001 --address 127.0.0.1

# terminal C
cd unittest_app
python3 unittest_app.py
~~~

---

## 16. Final Checklist

Before submission, ensure all are true:

- [ ] all 3 nodes are `Ready`
- [ ] `auth` (1 replica) and `shortener` (3 replicas) are `Running`
- [ ] `websvc-shared-pvc` is `Bound`
- [ ] NodePort services expose `30081` and `30080`
- [ ] JWT login works and shortener accepts authenticated requests
- [ ] unittest runs against Kubernetes deployment
- [ ] image tags and architectures match cluster (`linux/amd64`)
- [ ] key material is consistent between auth and shortener

If all items pass, your Assignment 3.2 environment is in good shape.
