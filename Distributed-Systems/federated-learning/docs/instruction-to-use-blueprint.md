


# Purpose of the BluePrint
 the Edge-AI Blueprint as a standardized template to deploy and test AI models on distributed edge nodes.

# HowTo use the BluePrint - step-by-step 

## 1. Access the Repository
- Sign In: Log in to the INRIA GitLab using your project credentials.

- Locate the Blueprint: Navigate to the digitafrica/blueprints/services/edge-ai-blueprint repository.

- Clone: Clone the repository to your local machine or the jump host of your testbed:

```bash
git clone https://gitlab.inria.fr/digitafrica/blueprints/services/edge-ai-blueprint.git
```

## 2. Configure the Inventory
The blueprint uses Infrastructure-as-Code (Ansible) to manage devices.

-  Open the `inventory/` or `hosts.ini` file.

- Add the IP addresses or hostnames of your specific edge devices (e.g., Raspberry Pi, Jetson Nano, or local servers).

- Ensure SSH access is configured between your control machine and these nodes.

## 3. Customize the AI Service

- **Model Selection**: Place your trained model (e.g., in .onnx or .tflite format) in the `models/` directory or update the download URL in the configuration file.

- **Environment Variables**: Edit the `.env` or `group_vars/all.yml` file to specify parameters like camera input paths, inference thresholds, or data destination (local vs. cloud).

## 4. Deploy the Stack
The blueprint typically uses Docker/Containerization to ensure the environment is identical across different African research sites.

Run the deployment script (usually a Makefile or Ansible playbook):

```bash
ansible-playbook -i inventory/hosts.ini deploy.yml
```
This will automatically install dependencies, pull the necessary Docker images, and start the AI inference service on your edge nodes.

## 5. Validate and Monitor
- **Check Logs**: Ensure the service is running by checking the container logs on the edge node: docker logs -f edge-ai-service.

- **Data Flow**: Verify that the inference results (e.g., metadata or telemetry) are being sent to the project’s central data lake or displayed on the local dashboard provided by the blueprint.


# Federated Learning Use Case: DIGITAfrica Blueprint
This guide demonstrates how to deploy a Federated Learning (FL) tutorial using the standardized DIGITAfrica Edge-AI Blueprint.

## 1. Preparation: Containerize the FL Code
The Blueprint requires services to be containerized to ensure consistency across different African research sites.

### Create the Dockerfiles
In your repository, create two distinct files to package the server and client logic.

For the Server (`Dockerfile.server`):

Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flwr torch torchvision  
# Add your specific dependencies
EXPOSE 8080
CMD ["python", "server.py"] 
```
For the Client (`Dockerfile.client`):

Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flwr torch torchvision
# Environment variable for the server address
ENV SERVER_ADDRESS="localhost:8080"
CMD ["python", "client.py", "--server_address", "$SERVER_ADDRESS"]
```
### Build and Push the Images
You must push these images to a registry (e.g., Docker Hub or INRIA GitLab Registry) so the distributed edge nodes can pull them.

- Build:

```bash 
docker build -t your-registry/fl-server:latest -f Dockerfile.server .
docker build -t your-registry/fl-client:latest -f Dockerfile.client .
```
- Push:

```bash
docker push your-registry/fl-server:latest
docker push your-registry/fl-client:latest
```
## 2. Configure the Blueprint
Once your images are ready, configure the Blueprint to orchestrate the deployment.

Update the Inventory
Modify `inventory/hosts.ini` to define the roles of your infrastructure nodes:

Ini, TOML

[fl_server]
```ini
server-node-01 ansible_host=10.0.x.x
```
[fl_clients]
```ini
edge-node-01 ansible_host=10.0.x.y
edge-node-02 ansible_host=10.0.x.z
```
Define Blueprint Variables
In `group_vars/all.yml`, specify the image locations and the central server IP:

```yaml
fl_image_client: "your-registry/fl-client:latest"
fl_image_server: "your-registry/fl-server:latest"
fl_server_ip: "10.0.x.x"  # The IP of your server-node-01
```
### 3. Execution
Run the deployment command. The Blueprint uses Ansible to pull your images and start the containers across the network simultaneously.

```bash
ansible-playbook -i inventory/hosts.ini deploy_federated.yml
```
