#!/usr/bin/env bash
set -euo pipefail

# Note: VM names like student127/student128/student129 are examples for this workshop.
# Replace hostnames/IPs as needed for your own environment.

# Run on VM: student127 (145.100.130.127)
# 1) Hostname + hosts
sudo hostnamectl set-hostname student127
cat <<'HOSTS' | sudo tee /etc/hosts >/dev/null
127.0.0.1 localhost
145.100.130.127 student127
145.100.130.128 student128
145.100.130.129 student129
HOSTS

# 2) Disable swap
sudo swapoff -a
sudo sed -i.bak '/\sswap\s/s/^/#/' /etc/fstab

# 3) Kernel/network prereqs
cat <<'SYSCTL' | sudo tee /etc/sysctl.d/99-kubernetes.conf >/dev/null
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
SYSCTL
sudo modprobe br_netfilter
sudo sysctl --system

# 4) containerd
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg containerd nfs-kernel-server nfs-common
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
sudo systemctl enable --now containerd

# 5) kubeadm/kubelet/kubectl
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.35/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.35/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list >/dev/null
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable --now kubelet

# 6) Init control-plane
sudo kubeadm init --apiserver-advertise-address=145.100.130.127 --pod-network-cidr=10.244.0.0/16

mkdir -p "$HOME/.kube"
sudo cp -i /etc/kubernetes/admin.conf "$HOME/.kube/config"
sudo chown "$(id -u):$(id -g)" "$HOME/.kube/config"

kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml

# 7) Create NFS export for RWX PV
sudo mkdir -p /srv/nfs/websvc
sudo chown nobody:nogroup /srv/nfs/websvc
sudo chmod 777 /srv/nfs/websvc
cat <<'NFS' | sudo tee /etc/exports >/dev/null
/srv/nfs/websvc 145.100.130.127(rw,sync,no_subtree_check,no_root_squash) 145.100.130.128(rw,sync,no_subtree_check,no_root_squash) 145.100.130.129(rw,sync,no_subtree_check,no_root_squash)
NFS
sudo exportfs -rav
sudo systemctl enable --now nfs-kernel-server

# 8) Print join command (copy and run on worker nodes)
kubeadm token create --print-join-command

# 9) Deploy manifests (run after both workers joined)
# IMPORTANT: replace image names in k8s/auth-deployment.yaml and k8s/shortener-deployment.yaml first.
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/shared-pv.yaml
kubectl apply -f k8s/shared-pvc.yaml
kubectl apply -f k8s/auth-secret.yaml
kubectl apply -f k8s/shortener-configmap.yaml
kubectl apply -f k8s/auth-deployment.yaml
kubectl apply -f k8s/auth-service.yaml
kubectl apply -f k8s/shortener-deployment.yaml
kubectl apply -f k8s/shortener-service.yaml

kubectl get nodes -o wide
kubectl get pods -n websvc -o wide
kubectl get svc -n websvc
kubectl get pv,pvc -n websvc
