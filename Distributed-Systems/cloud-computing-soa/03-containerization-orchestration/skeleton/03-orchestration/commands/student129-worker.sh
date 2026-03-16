#!/usr/bin/env bash
set -euo pipefail

# Run on VM: student129 (145.100.130.129)
sudo hostnamectl set-hostname student129
cat <<'HOSTS' | sudo tee /etc/hosts >/dev/null
127.0.0.1 localhost
145.100.130.127 student127
145.100.130.128 student128
145.100.130.129 student129
HOSTS

sudo swapoff -a
sudo sed -i.bak '/\sswap\s/s/^/#/' /etc/fstab

cat <<'SYSCTL' | sudo tee /etc/sysctl.d/99-kubernetes.conf >/dev/null
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
SYSCTL
sudo modprobe br_netfilter
sudo sysctl --system

sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg containerd nfs-common
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
sudo systemctl enable --now containerd

sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.35/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.35/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list >/dev/null
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable --now kubelet

# Paste the join command printed on student127, for example:
# sudo kubeadm join 145.100.130.127:6443 --token <TOKEN> --discovery-token-ca-cert-hash sha256:<HASH>
