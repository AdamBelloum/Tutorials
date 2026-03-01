
# Workshop Part 2: 

This part of the wowkshop focuses on `Kubernetes` (K8s) Orchestration. In this stage, you move from running containers on your own laptop to running them on a Cluster of multiple servers (Nodes).

In this workshop scenario, you have 3 Virtual Machines (VMs):

1. Control Plane (Master Node): The "Brain" that manages the cluster.
2. Worker Nodes: The "Muscle" that actually runs your code.

# Step 1: Cluster Initialization
You must install the K8s tools (kubeadm, kubectl, kubelet) on all three VMs.

On the Master Node: Initialize the cluster.

```Bash
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```
- On **Worker Nodes**: Use the "join" command provided by the Master's output to link them to the cluster.

```Bash
sudo kubeadm join <master-ip>:<port> --token <token> ...
```
[!TIP] How to test: Run kubectl get nodes on the Master. You should see all 3 VMs listed as Ready.

# Step 2: Create Deployments (Scaling)
A Deployment defines how many copies (replicas) of your service should run. The assignment requires one service to have 3 replicas. We will scale the Shortener Service to handle more traffic.

Create shortener-deployment.yaml:

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: shortener-deployment
spec:
  replicas: 3  # Requirement: 3 instances running across your nodes
  selector:
    matchLabels:
      app: shortener
  template:
    metadata:
      labels:
        app: shortener
    spec:
      containers:
      - name: shortener
        image: <your-registry-username>/shortener-service:latest
        ports:
        - containerPort: 5002
Create auth-deployment.yaml:
(Set replicas: 1 for the Authentication service).
```

# Step 3: Create Services (External Access)
Kubernetes "Services" act as a stable entry point. Since your VMs are in a lab network, you need a way to reach them from your personal computer.

- Internal Communication: Use `ClusterIP`.
- External Access: Use `NodePort` or `LoadBalancer`.
- Create shortener-service.yaml:

```YAML
apiVersion: v1
kind: Service
metadata:
  name: shortener-external
spec:
  type: NodePort # This makes the service accessible from outside the VM
  selector:
    app: shortener
  ports:
    - port: 80         # Port inside the cluster
      targetPort: 5002 # Port on the container
      nodePort: 30002  # Port you will use in your browser (30000-32767)
```
# Step 4: Applying and Testing

- Apply the configurations:

```Bash
kubectl apply -f auth-deployment.yaml
kubectl apply -f shortener-deployment.yaml
kubectl apply -f shortener-service.yaml
```

- Verify the Replicas:

```Bash
kubectl get pods -o wide
```
**Success**: You should see 3 "Shortener" pods spread across your 2 Worker Nodes.

The "Kill" Test: Delete one of the 3 Shortener pods manually: 

```Bash
kubectl delete pod <pod-name>.
```

**Success**: Observe Kubernetes automatically starting a new pod to replace it. This is the "Automated Management" mentioned in the background.

**Final Access**:
From your laptop, visit `http://<VM-IP-ADDRESS>:30002`. Your URL shortener is now live on a production-style cluster!