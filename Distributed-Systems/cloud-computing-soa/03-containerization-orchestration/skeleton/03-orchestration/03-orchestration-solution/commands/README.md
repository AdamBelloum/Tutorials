# Assignment 3.2 Minimal Runbook

Note: VM names such as `student127`, `student128`, and `student129` are examples used in this runbook. Replace them with your own VM names/IPs.

## 1) k8s YAML status

Needed files:
- `k8s/namespace.yaml`
- `k8s/shared-pv.yaml`
- `k8s/shared-pvc.yaml`
- `k8s/auth-secret.yaml`
- `k8s/shortener-configmap.yaml`
- `k8s/auth-deployment.yaml`
- `k8s/auth-service.yaml`
- `k8s/shortener-deployment.yaml`
- `k8s/shortener-service.yaml`

Updated in this cleanup:
- `shared-pv.yaml`: NFS server fixed to `145.100.130.127`
- `shared-pvc.yaml`: static bind fields added (`storageClassName`, `volumeName`)
- `shortener-configmap.yaml`: fixed public key to valid PEM body
- Deployments: image placeholder normalized to `YOUR_DOCKERHUB_USERNAME/...`

Not needed for final execution:
- `setup/control.sh`
- `setup/worker1.sh`
- `setup/worker2.sh`

## 2) Execute on VMs

1. On `student127`, run `commands/student127-control-plane.sh`.
2. On `student128`, run `commands/student128-worker.sh`, then paste join command.
3. On `student129`, run `commands/student129-worker.sh`, then paste join command.
4. On `student127`, ensure deployment section in script is executed after both workers join.

## 3) Build and push images to Docker Hub

From project root:

```bash
./commands/push-images.sh -u YOUR_DOCKERHUB_USERNAME -t 3.2 --update-k8s
```

Notes:
- Run `docker login` first.
- `--update-k8s` automatically updates:
  - `k8s/auth-deployment.yaml`
  - `k8s/shortener-deployment.yaml`
- If you skip `--update-k8s`, update image names manually in the two deployment files.
