# Workshop Guide: Building a Spark + Livy Cloud Sandbox
## Introduction
In this workshop, you will build a mini-cluster that mimics a real-world cloud data platform (like Databricks or AWS EMR). You will set up a `Spark Master`, a `Spark Worker`, and a `Livy Server` that acts as a bridge for remote code execution.

## Step 1: Create the Project Structure
First, we need a clean workspace. Open your terminal and run:

```bash
mkdir spark-workshop && cd spark-workshop
```
# Step 2: Define the Livy Interface (The Dockerfile)
Livy doesn't have an official Docker image for `Spark 3.5`, so we build our own. We use the `Scala 2.12` version of Livy to ensure it speaks the same language as `Spark 3.5`.

Add this to your Dockerfile:

```yaml  
 FROM apache/spark:3.5.8                                                                                                                                          
 
 USER root
 
# 1. Install dependencies
 RUN apt-get update && apt-get install -y curl unzip python3-pip && rm -rf /var/lib/apt/lists/*

 # 2. Download and extract Livy 0.9.0 (Scala 2.12 version)
 ENV LIVY_HOME /opt/livy
 RUN curl -fSL https://dlcdn.apache.org/incubator/livy/0.9.0-incubating/apache-livy-0.9.0-incubating_2.12-bin.zip -o livy.zip \
    && unzip livy.zip -d /opt \
     && mv /opt/apache-livy-0.9.0-incubating_2.12-bin /opt/livy \
     && rm livy.zip

# 3. Set environment variables
ENV SPARK_HOME /opt/spark
ENV PATH $PATH:/opt/livy/bin
 WORKDIR /opt/livy
  
 # Ensure logs directory exists
 RUN mkdir -p /opt/livy/logs
  
EXPOSE 8998

# Start Livy in the foreground
CMD ["livy-server"]
```

**What you are doing**: You are taking a base Spark image and "layering" the Livy server on top of it so they share the same environment.

# Step 3: Orchestrate the Cluster (The Docker Compose)
Now we define how the `Master`, `Worker`, and `Livy connect` to each other.

Add this to your docker-compose.yml:

```YAML
services:
  spark-master:
    image: apache/spark:3.5.8
    command: /opt/spark/bin/spark-class org.apache.spark.deploy.master.Master
    ports:
      - "9090:8080" # Spark UI moved to 9090 to avoid Mac AirPlay conflicts
      - "7077:7077"

  spark-worker:
    image: apache/spark:3.5.8
    command: /opt/spark/bin/spark-class org.apache.spark.deploy.worker.Worker spark://spark-master:7077
    depends_on:
      - spark-master

  spark-livy:
    build: .
    ports:
      - "8998:8998"
    depends_on:
      - spark-master
      - spark-worker
What you are doing: You are creating a virtual network. Note the command lines; these are critical to prevent the containers from shutting down immediately after they start.
```
# Step 4: Launch the Cluster
Build your custom image and start the services in the background.

```Bash
docker compose up -d --build
```
**Verification**: Open your browser to http://localhost:9090. You should see the Spark Master UI with 1 Worker listed as "ALIVE."

# Step 5: Start a Spark Session
Livy allows you to interact with Spark via HTTP. First, you must request a session (think of this as opening a notebook).

```Bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"kind": "pyspark"}' \
     http://localhost:8998/sessions
```
What you are doing: You are asking `Livy` to talk to the `Spark Master` and reserve resources for your Python code.

1. **The Request**: You tell Livy you want a `pyspark interpreter`.

2. **The Handshake**: `Livy` contacts the `Spark Master` (defined in our config as spark://spark-master:7077).

3. **Resource Allocation**: The `Spark Master` looks at the available Workers and tells one of them: "Hey, launch a Spark Driver process for this user."

4. **The Result**: A dedicated Python process (the REPL) starts inside the cluster. It stays alive and "idle," waiting for your commands.
**Why do we do this?** In Big Data, starting a Spark application takes time (15–30 seconds). By creating a session first, we pay that "time tax" once. All subsequent code you send will run instantly because the engine is already warm. 

# Step 6: Execute Python Code
Once the session state is idle (check via http://localhost:8998/sessions), send a snippet of code:

```Bash
curl -X POST -H "Content-Type: application/json" \
     -d '{ "code": "for i in range(1,10): print(i)" }' \
     http://localhost:8998/sessions/0/statements
```
To see the result of your calculation:

```Bash
curl http://localhost:8998/sessions/0/statements/0
```
**What you are doing**: You are sending a "Statement." `Livy` executes it on the `Spark cluster` and `holds` the output for you to collect.


**What is happening here?**
Think of this as "Giving a Command to the Driver." 
1.  **Targeting**: Notice the /sessions/0/ in the URL. This tells `Livy` exactly which "Engine" should run this code. If you had 5 participants, they would have IDs 0, 1, 2, 3, 4.
2.  **Submission**: `Livy` takes your string of Python code and pushes it into the stdin (input) of the Python process we started in Step 5.
3.  **Asynchronous Execution**: This is the most important concept for participants: 

The result is not returned immediately. `Livy` gives you a "Statement ID" (like a dry-cleaning ticket).
* The code runs in the background.
* You must use that ID later to "claim" your output.

**Why do we do it this way?** In real-world data science, a Spark job might take 2 hours to finish. You don't want your terminal (or your web browser) to stay "frozen" waiting for the result. By making it a "Statement," you can send the code, go grab a coffee, and check the results later.

# Step 7: Cleanup
In a shared workshop environment, cleaning up resources is vital.

```Bash
# Delete the Livy session
curl -X DELETE http://localhost:8998/sessions/0

# Shut down the containers
```bash
docker compose down
```