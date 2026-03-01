# Workshop Part 1: Containerizing Microservices with Docker

In this part of the tutorial, you will move your `Authentication` and `URL Shortener` services from your local machine into Docker Containers. This ensures your software runs exactly the same way regardless of the environment.

# The Goals
- **Containerization**: Wrap each service in a Docker image.
- **Orchestration**: Use Docker Compose to manage both containers as a single system.
- **Persistence**: Use Docker Volumes so your data survives even if the container is deleted.

# Step 0: Environment Check
Before starting, ensure Docker is installed on your machine.

Command: 
```bash 
docker --version and docker-compose --version
```

- **Success**: You should see version numbers. If not, install Docker Desktop (Windows/macOS) or use your package manager (Linux).

# Step 1: Prepare for Persistence
Your services must write data to a file (like data.json) rather than just keeping it in memory.

- Update your Python code (both services):
- Ensure your `url_db` and `users` dictionaries are saved to a file whenever they change.

- **Success**: Run your app locally, add a user, stop the app, and restart it. The user should still exist.

# Step 2: Create the Dockerfiles
A Dockerfile is a recipe for building a container image. You need one for each service. To keep images efficient, we copy only the necessary files.

Create `Dockerfile.auth` (for Authentication Service):

```yaml
# 1. Use a slim version of Python for efficiency
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the source code
COPY auth_service.py jwt_utils.py .

# 5. Run the service
CMD ["python", "auth_service.py"]
Repeat this for the Shortener service as Dockerfile.shortener.
```

Test Command: 

```bash
docker build -t auth-service -f Dockerfile.auth .
```

- **Success**: Docker builds the image without errors.

# Step 3: Orchestrate with Docker Compose
Instead of starting containers manually, use a docker-compose.yml file to manage the network and volumes.

Create docker-compose.yml:

```yaml
version: '3.8'
services:
  auth-service:
    build:
      context: .
      dockerfile: Dockerfile.auth
    ports:
      - "5001:5001" # Accessible from outside the container
    volumes:
      - auth_data:/app/data # Persistent storage

  shortener-service:
    build:
      context: .
      dockerfile: Dockerfile.shortener
    ports:
      - "5002:5002"
    volumes:
      - short_data:/app/data
    depends_on:
      - auth-service

volumes:
  auth_data:
  short_data:
Step 4: Deploy and Test
```

Now, launch the entire microservice architecture with one command.

Command: 

```bash
docker-compose up --build
```
- **Success**: Both services start, and you see their logs in the terminal.

# Verification Steps:
Connectivity: Use curl to register a user at `http://localhost:5001/users`.

Persistence Test: * Stop the containers: 

```bash
docker-compose down.
```

Start them again: 

```bash
docker-compose up.
```

Try to login: The user you created should still exist because of the Docker Volume.

# Important Efficiency Reminders
- **Order Matters**: Always copy `requirements.txt` and `install` dependencies before copying your source code. This prevents Docker from re-downloading packages every time you change a single line of Python code.

- **Slim Base**: Use -slim or -alpine versions of Python to keep the container file system small.