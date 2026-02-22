# Example Solution

## 3.1 Run docker & docker compose (run on your machine locally)
- Files used: `compose.yml, .env, services/`
- Build: `docker compose build`
- Run services: `docker compose up -d`
- Test services:
```
cd tests
python3 test_app.py
```

## 3. 2 App deployment on Kubernetes
- Files used: ` k8s/ , certs/ , services/, calico.yml, deploy_services.sh, check_k8status.sh`
- We chose master node with user, IP `student024@145.100.130.24` and worker nodes `student023@145.100.130.23`,`student025@145.100.130.25`.

### Setup on Master we followed [Note: Don't run these steps. We already did]

#### Cluster Master node setup  - docker, containerd, kubeadm init, kube config, calico apply
1. Follow steps in readme provided on canvas

#### Setup certification, key for TLS verification
2. Setup using secure https protocol using `443` port on server ( master node with IP address `145.100.130.24`)

```
mkdir -p ~/example_solution/certs
cd ~/example_solution/certs
openssl genrsa -out ca.key 4096
openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 -out ca.crt   -subj "/C=NL/ST=Noord-Brabant/L=Den Bosch/O=WebCloud/OU=IT/CN=145.100.130.24"
openssl req -newkey rsa:4096 -nodes -sha256 -keyout domain.key -out domain.csr   -subj "/C=NL/ST=Noord-Brabant/L=Den Bosch/O=WebCloud/OU=IT/CN=145.100.130.24"
```

Create and use extfile conf,
```
cat > extfile.cnf <<EOF
[req]
distinguished_name=req_distinguished_name
[req_distinguished_name]
[v3_ext]
subjectAltName = @alt_names
[alt_names]
IP.1 = 145.100.130.24
EOF
```

```
openssl x509 -req -in domain.csr -CA ca.crt -CAkey ca.key -CAcreateserial     -out domain.crt -days 365 -sha256 -extfile extfile.cnf -extensions v3_ext
```

#### Copy certification, key for TLS verification
3. Copy certificates to docker, local
```
sudo cp ~/example_solution/certs/ca.crt /etc/docker/certs.d/145.100.130.24:443/ca.crt
sudo cp ~/example_solution/certs/ca.crt /usr/local/share/ca-certificates/145.100.130.24.crt
sudo update-ca-certificates --fresh
sudo systemctl restart docker
sudo systemctl restart kubelet
openssl x509 -in ~/example_solution/certs/domain.crt -text -noout | grep -A 2 "Subject Alternative Name" # check feilds
```

Copy certificates to containerd and add host on containerd
```
sudo mkdir -p /etc/containerd/certs.d/145.100.130.24:443
sudo nano /etc/containerd/certs.d/145.100.130.24:443/hosts.toml
```
Insert in the file opened,
```
server = "https://145.100.130.24:443"

[host."https://145.100.130.24:443"]
  capabilities = ["pull", "resolve"]
  ca = "/etc/docker/certs.d/145.100.130.24:443/ca.crt"
```

#### Setup docker registry, kube deployments
4. Restart docker, containerd, kubelet, to apply TLS certification changes
```
sudo systemctl restart docker
sudo systemctl restart containerd
sudo systemctl restart kubelet
```

5. Start private registry on docker

```
docker run -d   --restart=always   --name private-registry   -p 443:443   -v ~/example_solution/certs:/certs   -e REGISTRY_HTTP_ADDR=0.0.0.0:443   -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt   -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key   registry:2
docker ps | grep registry
```

6. Build docker images of our app
```
docker compose build
```

7. Tag and push container images
```
docker tag postgres:15 145.100.130.24:443/example-solution-db:v1
docker tag redis:7.2 145.100.130.24:443/example-solution-redis:v1
docker tag example-solution-auth-service:latest 145.100.130.24:443/example-solution-auth-service:v1
docker tag example-solution-url-shortener-service:latest 145.100.130.24:443/example-solution-url-shortener-service:v1
docker tag example-solution-gateway:latest 145.100.130.24:443/example-solution-gateway:v1
```
```
docker push 145.100.130.24:443/example-solution-db:v1
docker push 145.100.130.24:443/example-solution-redis:v1
docker push 145.100.130.24:443/example-solution-auth-service:v1
docker push 145.100.130.24:443/example-solution-url-shortener-service:v1
docker push 145.100.130.24:443/example-solution-gateway:v1
```

8. Check the catalog for published repositories
```
curl https://localhost:443/v2/_catalog
curl http://145.100.130.24:443/v2/example-solution-auth_service/tags/list
```

9. Once you see all repos, deploy kubernetes deployments and services and check status
```
./deploy_services.sh
./check_k8status.sh
```


### Setup and Steps to run on Worker Nodes [Note: Don't run these steps. We already did]

1. Join the cluster as per instructions on canvas, using
```
kubeadm join 145.100.130.24:6443 --token dfh5fs.5t2lezup5p7a3526 --discovery-token-ca-cert-hash sha256:5fb407a0f14695e3028feeccb5245f83812267507f7e61f4436af1f6bdc2ff2d
```
**Note**: the token and sha key can be expired, if `[preflight] Running pre-flight checks` takes so long, please go to master node: `kubeadm token list` to check if there is any token, or `kubeadm token create --print-join-command` to create a new token

2. Copy CA certificates to docker, containerd steps below,
```
sudo mkdir -p /etc/docker/certs.d/145.100.130.<>:443/
sudo cp ~/example_solution/certs/ca.crt /etc/docker/certs.d/145.100.130.<>:443/ca.crt
sudo cp ~/example_solution/certs/ca.crt /usr/local/share/ca-certificates/145.100.130.<>.crt
sudo update-ca-certificates --fresh
sudo systemctl restart docker
sudo systemctl restart kubelet
openssl x509 -in ~/example_solution/certs/domain.crt -text -noout | grep -A 2 "Subject Alternative Name" # check field
```

```
sudo mkdir -p /etc/containerd/certs.d/145.100.130.<>:443
sudo nano /etc/containerd/certs.d/145.100.130.<>:443/hosts.toml
```

In the file opened, 
```
server = "https://145.100.130.<>:443"
[host."https://145.100.130.<>:443"]
  capabilities = ["pull", "resolve"]
  ca = "/etc/docker/certs.d/145.100.130.<>:443/ca.crt"
```


3. Pull docker images using
```
docker pull 145.100.130.24:443/example-solution-db:v1
docker pull 145.100.130.24:443/example-solution-redis:v1
docker pull 145.100.130.24:443/example-solution-gateway:v1
docker pull 145.100.130.24:443/example-solution-auth-service:v1
docker pull 145.100.130.24:443/example-solution-url-shortener-service:v1
```
4. Test services that are running

Since we are using NodePort, the port would be export in range 30000-32767.
Currently, url-shortener-service uses 30000, auth-service uses 30001 and gateway uses 30002.
Before testing locally, please make sure you change `base_url` and `auth_url` to the correct host (145.100.130.23-25) and 30003, 30001, 30002 port. Then, executing the tests:
```
cd tests
python3 test_app.py
```

## Authors
- Mhi Mai,
- Yunxuan Tang
- Sathya Sravya Vallabhajyosyula

From WSCBS 2025, University of Amsterdam