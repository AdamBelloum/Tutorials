OpenFaaS Hands-On Tutorial

# Phase 1: Environment Setup (The Provider Role)
In this phase, you are acting as the Cloud Provider, setting up the infrastructure where functions will run.


## 0. Prerequisites Update
- Docker Hub Account: Required for storing function images.
- Kind & Kubectl: Installed.
- Arkade: The modern "Sway" for Kubernetes apps.

[!NOTE] if not installed see [instalation instructions ](#installing-pre-requisites)
## 1. Create a Kubernetes Cluster
We will use Kind (Kubernetes in Docker) to create a local multi-node cluster.

```Bash
# Create a simple cluster
kind create cluster --name openfaas-lab
```
## 2. Install Arkade and OpenFaaS
Arkade is a specialized installer for Kubernetes apps. We will use it to deploy OpenFaaS in Operator mode, which allows Kubernetes to manage functions as native objects.

```Bash
# Get Arkade
curl -sLS https://get.arkade.dev | sudo sh

# Install OpenFaaS CLI and the Gateway
arkade get faas-cli
arkade install openfaas --operator
```
## 3. Access the Gateway
OpenFaaS is secure by default. You need to retrieve the admin password and "port-forward" the service to access it on your local machine.

```Bash
# Forward the gateway to port 8080
kubectl port-forward -n openfaas svc/gateway 8080:8080 &

# Retrieve the auto-generated password
PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)

# Log in via CLI
echo -n $PASSWORD | faas-cli login --username admin --password-stdin
```
# Phase 2: Function Development (The User Role)
Now you are acting as the Developer, creating and deploying code.

## 4. Pull Templates and Create a New Function
OpenFaaS uses templates to wrap your code. We will use the modern Node20 HTTP template which is optimized for high performance.

```Bash
# Download the modern Node.js template
faas-cli template store pull node20-http
# Create a new function named 'hello-student'
faas-cli new hello-student --lang node20-http --prefix <YOUR_DOCKER_HUB_USER>
```
5. Write the Logic
Open the generated hello-student/handler.js. Notice the event object, which contains the HTTP request data.

```JavaScript
"use strict"

module.exports = async (event, context) => {
    const name = event.body.name || "Student";
    const result = {
        message: `Hello ${name}, your function is live!`,
        timestamp: new Date()
    };

    return context
        .status(200)
        .headers({"Content-Type": "application/json"})
        .succeed(result);
}
```
## 6. Build, Push, and Deploy
This command automates three steps: building the Docker image, pushing it to Docker Hub, and telling the Kubernetes cluster to run it.

```Bash
# Ensure you are logged into Docker (docker login)
faas-cli up -f hello-student.yml
```
# Phase 3: Testing and Monitoring
7. Invoke the Function
You can trigger your function via the CLI or using a standard curl command.

```Bash
# Via CLI
echo '{"name": "OpenFaaS User"}' | faas-cli invoke hello-student

# Via Curl
curl -d '{"name": "OpenFaaS User"}' http://127.0.0.1:8080/function/hello-student
```
## 8. Visualizing with the UI
Open your browser and navigate to http://localhost:8080. Log in with the username admin and the password you retrieved earlier. Here you can see invocation counts and manually trigger functions.



# OpenFaaS Hands-On: Real-World Data & Monitoring
# Phase 4: Handling Real-World Data (Weather API)
In this section, you learn how to make their functions "talk" to the outside world.

## 1. Function Setup
We will create a function that fetches weather data. We'll use the node20-http template because it includes the modern fetch API natively.

```Bash
faas-cli new weather-worker --lang node20-http --prefix <YOUR_DOCKER_USER>
```
2. Adding External Logic
Open weather-worker/handler.js. We will update it to call an external API.

Teacher Note: Students will need a free API key from OpenWeatherMap.

```JavaScript
"use strict"

module.exports = async (event, context) => {
    const city = event.query.city || "London";
    const apiKey = "YOUR_API_KEY_HERE"; 
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        return context.status(200).succeed({
            message: `The weather in ${city} is ${data.main.temp}°C`,
            details: data.weather[0].description
        });
    } catch (err) {
        return context.status(500).succeed({ error: "Failed to fetch weather" });
    }
}
```

3. Deploy and Test

```Bash
faas-cli up -f weather-worker.yml
```
# Test it via browser or curl
curl "http://127.0.0.1:8080/function/weather-worker?city=Paris"

# Phase 5: Detailed Monitoring (Prometheus & Grafana)
OpenFaaS tracks every execution. We will now deploy a professional monitoring stack to visualize this data.

## 4. Deploy the Monitoring Stack
Instead of manual configuration, we use arkade to install Grafana with the correct settings.

```Bash
# Install Grafana
arkade install grafana

# Get your Grafana Admin password
GRAFANA_PASS=$(kubectl get secret -n default grafana -o jsonpath="{.data.admin-password}" | base64 --decode; echo)

# Open access to Grafana
kubectl port-forward svc/grafana 3000:3000 &
```
## 5. Connecting the Dots
1. Log in: Go to http://localhost:3000 (User: admin, Password: $GRAFANA_PASS).

2. Add Data Source: * Go to Connections > Data Sources > Add Data Source.

- Select Prometheus.
- URL: http://prometheus.openfaas:9090 (This is the internal Kubernetes address).

3. Import Dashboard:
- Click the + icon > Import.
- Enter ID: 3434 and click Load.
- Select your Prometheus data source and click Import.

 ## 6. The "Load Test" Challenge
To see the graphs move, students should simulate traffic.

```Bash
# Run this loop for 30 seconds to generate "Invocations per Second" data
while true; do curl -s http://127.0.0.1:8080/function/weather-worker?city=Berlin > /dev/null; sleep 1; done
```
  
# Key Takeaways
- Serverless != No Servers: OpenFaaS abstracts the server management (Kubernetes) away so you can focus strictly on the handler.js logic.
- The Watchdog: Every function runs with a "Watchdog" inside the container. It acts as a tiny sidecar that turns HTTP requests into standard input/output for your code.
- Operator Pattern: By using the --operator flag, your functions are managed as Custom Resources in Kubernetes, making them more stable and scalable.
- Event-Driven Ready: OpenFaaS isn't just for HTTP; it uses NATS JetStream under the hood to handle asynchronous requests and queues.
- Asynchronous External Calls: Modern Node.js templates allow async/await, making it easy to call external APIs without blocking the function.
- Observability: OpenFaaS doesn't just run code; it provides Gold Standard metrics (Invocations, Errors, Duration) out of the box via Prometheus.
- Infrastructure as Code: Notice that we deployed a full monitoring suite with just a few commands—this is the power of the Kubernetes ecosystem.#

# installing pre-requisites

# 1. Install Arkade (The App Store for Kubernetes)
Arkade is the fastest way to get your Kubernetes binaries and OpenFaaS apps.

### macOS / Linux
```Bash
curl -sLS https://get.arkade.dev | sudo sh
```
### Windows (PowerShell - Run as Admin) PowerShell
```Bash
curl -sLS https://get.arkade.dev | iex
```
## 2. Install Kubectl (The Kubernetes Controller)
Kubectl is the command-line tool used to communicate with your cluster.

### macOS
```Bash
brew install kubectl
```
### Linux
```Bash
arkade get kubectl
sudo mv ~/.arkade/bin/kubectl /usr/local/bin/
```
### Windows (PowerShell)
PowerShell
```Bash 
arkade get kubectl
```
# Follow the on-screen instructions to add to your PATH if needed
## 3. Install Kind (The Local Cluster)
Kind (Kubernetes in Docker) allows you to run a full cluster as a Docker container.

### macOS
```Bash
brew install kind
```
### Linux
```Bash
# Download the binary
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
# Make it executable and move it to your path
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```
### Windows (PowerShell / Chocolatey)
PowerShell
choco install kind
# OR via Winget
winget install Kubernetes.kind

## Verification Step
Once finished, restart your terminal and run the following commands to ensure everything is set up correctly:

```Bash
arkade version
kubectl version --client
kind --version
```
Note for Windows Users: If a command is "not recognized," you may need to close and reopen your PowerShell window to refresh your Environment Variables (PATH).