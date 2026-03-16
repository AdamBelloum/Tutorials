# Workshop Tutorial 3.1: Containerizing the Authentication Service and URL Shortener with Docker Compose

Welcome! In this workshop, you will adapt your Assignment 2 microservice system to **Assignment 3.1** by containerizing both services and making their data persistent.

By the end, you will have:

- An **Authentication Service** running inside Docker
- A **URL Shortener Service** running inside Docker
- A **Docker Compose** setup that starts both services together
- **Persistent storage** using files plus Docker volumes
- Services that are reachable **from outside the containers**
- A project layout that is ready to extend toward Assignment 3.2

Assignment 3.1 explicitly asks you to containerize your services with Docker and Docker Compose, make the service persistent by writing data to files and using Docker volumes, keep containers efficient, and ensure the services are accessible from outside the machine. It also expects you to demonstrate that the services still work and that the data survives service restarts and even `docker compose down`. 

---

## 0. What Changes Compared to Assignment 2?

In Assignment 2, your services could still store everything **in memory only**. 

In Assignment 3.1, that is no longer enough. You now need to:

1. package both services inside Docker containers
2. start them together using Docker Compose
3. store service data in files
4. mount those files or folders using Docker volumes so the data survives container recreation
5. make the services reachable from outside the Docker container

That means the biggest changes are not in the API specification itself, but in:

- file persistence
- network binding
- Dockerfiles
- Docker Compose
- project structure

---

## 1. Assignment 3.1 Goals

### 1.1 Core Requirements

For Assignment 3.1, your implementation should satisfy the following:

| Requirement | Meaning |
| --- | --- |
| Containerize both services | Each service should run inside its own Docker container |
| Use Docker Compose | Both services should be managed together |
| Persist service data | Data should be written to files and survive restarts |
| Use Docker volumes | Data should remain even after `docker compose down` |
| Keep containers efficient | Keep images compact and avoid unnecessary files/dependencies |
| Make services externally reachable | They must be accessible from outside the container |

These points are directly aligned with the 3.1 assignment description and grading criteria. 

---

## 2. Project Structure

A clean structure for 3.1 is:

~~~text
project/
├── auth_service/
│   ├── auth.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── data/
│   │   └── users.json
│   └── keys/
│       ├── private_key.pem
│       └── public_key.pem
├── shortener_service/
│   ├── shortener.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── data/
│   │   └── urls.json
│   └── keys/
│       └── public_key.pem
├── docker-compose.yml
└── README.md
~~~

### Why this structure?

- `auth.py` and `shortener.py` remain your main service files
- `data/` stores persistent JSON files
- `keys/` stores the key materials already used in Assignment 2
- each service gets its own `Dockerfile`
- `docker-compose.yml` starts everything together

This structure also helps you later explain in your README which files belong to 3.1 and which will belong to 3.2, as required in the submission instructions. 

---

## 3. Step 1: Add File Persistence to Both Services

Assignment 3.1 requires that the service storing data writes its contents to a file, and that Docker volumes are then used to make that data persistent. 

Because your system has two services with state, a practical solution is:

- `auth_service/data/users.json` for user data
- `shortener_service/data/urls.json` for URL mappings

This is fully reasonable for the assignment, especially because the assignment explicitly says you may assume your chosen storage implementation does not create race conflicts. 

---

## 4. Step 2: Modify `auth.py`

### 4.1 Add path handling based on the file location

You should not rely on paths like:

~~~python
PRIVATE_KEY_FILE = "keys/private_key.pem"
~~~

because Docker may run your program from a different working directory.

Instead, compute paths relative to the script itself:

~~~python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "users.json")
PRIVATE_KEY_FILE = os.path.join(BASE_DIR, "keys", "private_key.pem")
PUBLIC_KEY_FILE = os.path.join(BASE_DIR, "keys", "public_key.pem")
~~~

### Why this change?

This makes the code reliable both:

- when run locally
- when run inside Docker

---

### 4.2 Add file persistence functions

You should add helper functions like:

~~~python
def ensure_parent_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def load_users():
    ...

def save_users():
    ...
~~~

#### Expected behavior

- `load_users()` should:
  - create the data directory if needed
  - create `users.json` if missing
  - load user data from the file into `users_dict`

- `save_users()` should:
  - write `users_dict` back to `users.json`

### Why this change?

In Assignment 2, the user table could remain in memory. In Assignment 3.1, this would be lost when the container restarts. Writing users to `users.json` solves that. 

---

### 4.3 Save data after user changes

You should call `save_users()` after every successful write operation:

- after `POST /users`
- after `PUT /users`

This ensures the file is always updated when the user database changes.

---

### 4.4 Load users before starting the service

In the main block, make sure the users are loaded before running Flask:

~~~python
if __name__ == "__main__":
    load_users()
    ensure_keys_exist()
    app.run(host="0.0.0.0", port=5001, debug=False)
~~~

### Important change: use `0.0.0.0`

Do **not** use:

~~~python
app.run(host="127.0.0.1", port=5001, debug=True)
~~~

Inside Docker, `127.0.0.1` means “listen only inside the container itself”.  
If you do that, Docker can expose the port, but the service will still not be reachable from your host machine.

Instead, use:

~~~python
app.run(host="0.0.0.0", port=5001, debug=False)
~~~

### Why this change is required

Assignment 3.1 explicitly says the services must be accessible from outside the machine/container, not just from within Docker. Binding to `0.0.0.0` allows Docker port mappings to work correctly. :contentReference[oaicite:7]{index=7}

---

## 5. Step 3: Modify `shortener.py`

### 5.1 Add path handling based on the file location

Just like in `auth.py`, you should replace simple relative strings with paths based on `__file__`:

~~~python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "urls.json")
PUBLIC_KEY_FILE = os.path.join(BASE_DIR, "keys", "public_key.pem")
~~~

---

### 5.2 Add file persistence functions

You should add:

~~~python
def ensure_parent_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def load_urls():
    ...

def save_urls():
    ...
~~~

#### Expected behavior

- `load_urls()` loads `urls.json` into `shared_dict`
- `save_urls()` writes `shared_dict` back to `urls.json`

---

### 5.3 Save mappings after each change

You should call `save_urls()` after every operation that modifies the shortener data:

- after `POST /`
- after `PUT /<id>`
- after `DELETE /<id>`
- after `DELETE /`

That way, the URL mappings survive container recreation.

---

### 5.4 Load URLs before use

A simple and robust pattern is:

- call `load_urls()` once at startup
- also call `load_urls()` at the start of each route that reads or modifies the data

This is especially useful because it keeps the in-memory dictionary synchronized with the file contents.

---

### 5.5 Run Flask on `0.0.0.0`

The final block should look like:

~~~python
if __name__ == "__main__":
    load_urls()
    app.run(host="0.0.0.0", port=5000, debug=False)
~~~

### Why this matters

Exactly like for the authentication service, this makes the shortener reachable from outside the container. Without this, your local test scripts will fail even though the container appears to be running.

---

## 6. Step 4: Create the Data Files

Create these two files manually before building:

### `auth_service/data/users.json`

~~~json
{}
~~~

### `shortener_service/data/urls.json`

~~~json
{}
~~~

### Why start with empty JSON objects?

Because your Python code expects a dictionary-like structure:

- `users_dict` for user records
- `shared_dict` for URL mappings

This is the cleanest initial state.

---

## 7. Step 5: Create `requirements.txt` for Each Service

### `auth_service/requirements.txt`

~~~text
flask
cryptography
~~~

### `shortener_service/requirements.txt`

~~~text
flask
cryptography
~~~

### Why separate requirements files?

Each Docker image is built independently from its own service directory.  
So each service should carry the dependencies it needs to install itself.

---

## 8. Step 6: Create the Dockerfiles

Assignment 3.1 asks you to pay attention to efficiency and compactness of containers. In practice, that means:

- use a small base image
- copy only what is needed
- install dependencies before copying the full source tree where possible
- avoid large unnecessary build contexts

This is also something you should mention in the demo/report. 

---

### 8.1 `auth_service/Dockerfile`

~~~dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY auth.py .
COPY keys ./keys
COPY data ./data

EXPOSE 5001

CMD ["python", "auth.py"]
~~~

### Why this order?

- `COPY requirements.txt .` and `RUN pip install ...` come before copying the app files
- that allows Docker to reuse cached dependency layers if only your Python code changes
- `python:3.11-slim` keeps the image smaller than a full Python image

---

### 8.2 `shortener_service/Dockerfile`

~~~dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shortener.py .
COPY keys ./keys
COPY data ./data

EXPOSE 5000

CMD ["python", "shortener.py"]
~~~

### Important note

Make sure the shortener Dockerfile copies `shortener.py`, not `auth.py`.

---

## 9. Step 7: Create `docker-compose.yml`

A simple 3.1 Compose file is:

~~~yaml
services:
  auth:
    build:
      context: ./auth_service
    container_name: auth_service
    ports:
      - "5001:5001"
    volumes:
      - auth_data:/app/data
      - ./auth_service/keys:/app/keys
    restart: unless-stopped

  shortener:
    build:
      context: ./shortener_service
    container_name: shortener_service
    ports:
      - "5000:5000"
    volumes:
      - shortener_data:/app/data
      - ./shortener_service/keys:/app/keys
    depends_on:
      - auth
    restart: unless-stopped

volumes:
  auth_data:
  shortener_data:
~~~

---

## 10. Why These Compose Settings Matter

### 10.1 `ports`
The lines:

~~~yaml
ports:
  - "5001:5001"
~~~

and

~~~yaml
ports:
  - "5000:5000"
~~~

map the container ports to your local machine.

This is required so you can access:

- `http://127.0.0.1:5001`
- `http://127.0.0.1:5000`

from outside Docker, including through your test scripts.

---

### 10.2 `volumes`
The lines:

~~~yaml
- auth_data:/app/data
- shortener_data:/app/data
~~~

make the data directories persistent even if the containers are removed.

This is exactly what Assignment 3.1 asks you to demonstrate: the data should survive restarts and even survive `docker compose down`. 

---

### 10.3 key mounts
The lines:

~~~yaml
- ./auth_service/keys:/app/keys
- ./shortener_service/keys:/app/keys
~~~

make sure the services see the expected key files.

For the shortener, this means it can still load `public_key.pem` and validate JWTs locally, just as in Assignment 2.

---

### 10.4 `depends_on`
This ensures Docker Compose starts the auth container before the shortener container.

It does not guarantee the auth service is fully ready, but for this simple setup it is a sensible dependency declaration.

---

## 11. Step 8: Update the Key Setup

Make sure:

- `auth_service/keys/private_key.pem` exists
- `auth_service/keys/public_key.pem` exists
- `shortener_service/keys/public_key.pem` exists

The shortener should only need the **public key**, not the private key, consistent with the Assignment 2 design.

---

## 12. Step 9: Run the System

In the project root, run:

~~~bash
docker compose up --build
~~~

If you want it in the background:

~~~bash
docker compose up --build -d
~~~

### Why `--build`?

Because this forces Docker Compose to build the images based on your latest changes before starting the containers.

---

## 13. Step 10: Verify That the Services Are Reachable

Once the containers are up, open a new terminal and test the services.

### 13.1 Authentication service

This endpoint only supports `POST` and `PUT`, so a plain GET should at least show that the service is reachable:

~~~bash
curl -i http://127.0.0.1:5001/users
~~~

You should get something like `405 Method Not Allowed`, which is good enough to show the service is running.

---

### 13.2 Shortener service

Without a token, `GET /` should return `403`, which also proves the service is reachable:

~~~bash
curl -i http://127.0.0.1:5000/
~~~

If you get a valid HTTP response, your container is reachable from outside Docker, which is a key 3.1 requirement. :contentReference[oaicite:10]{index=10}

---

## 14. Step 11: Test the Full Workflow

### 14.1 Register a user

~~~bash
curl -X POST http://127.0.0.1:5001/users \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"test123"}'
~~~

### 14.2 Login and get a token

~~~bash
curl -X POST http://127.0.0.1:5001/users/login \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"test123"}'
~~~

Suppose the response contains:

~~~json
{
  "token": "YOUR_JWT_TOKEN"
}
~~~

### 14.3 Create a short URL

~~~bash
curl -X POST http://127.0.0.1:5000/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"value":"https://example.com"}'
~~~

### 14.4 List your keys

~~~bash
curl http://127.0.0.1:5000/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
~~~

### 14.5 Resolve the short URL

~~~bash
curl -i http://127.0.0.1:5000/<id>
~~~

This confirms that the application behavior from Assignment 2 still works after containerization.

---

## 15. Step 12: Demonstrate Persistence

This is a required demo point for Assignment 3.1. 

### 15.1 Test persistence across restart

1. Create a user and a short URL
2. Run:

~~~bash
docker compose restart
~~~

3. Query the services again

If the user and URLs are still there, persistence across restart works.

---

### 15.2 Test persistence across `docker compose down`

1. Create a user and a short URL
2. Run:

~~~bash
docker compose down
~~~

3. Start everything again:

~~~bash
docker compose up -d
~~~

4. Query the data again

If the data is still present, then the named Docker volumes are correctly preserving the files, which is exactly what 3.1 asks you to show. 

---

## 16. Common Problems and Fixes

### Problem 1: The service starts, but tests cannot connect
If Docker logs show:

~~~text
Running on http://127.0.0.1:5000
~~~

or

~~~text
Running on http://127.0.0.1:5001
~~~

inside the container, then the app is probably still bound to `127.0.0.1`.

#### Fix
Change:

~~~python
app.run(host="127.0.0.1", ...)
~~~

to:

~~~python
app.run(host="0.0.0.0", ...)
~~~

### Why this happens
Inside a container, `127.0.0.1` means “inside this container only”.  
To expose the service properly through Docker, Flask must bind to all interfaces using `0.0.0.0`.

---

### Problem 2: Port 5000 is already in use on macOS
On macOS, port `5000` may be occupied by Control Center / AirPlay Receiver.

#### Fix
Disable AirPlay Receiver in system settings and retry.

---

### Problem 3: The shortener cannot validate JWTs
Usually this means the public key is missing in:

~~~text
shortener_service/keys/public_key.pem
~~~

#### Fix
Make sure the file exists and matches the auth service’s public key.

---

### Problem 4: Data disappears after containers are removed
This usually means:

- you forgot to write the in-memory data to JSON
- or you forgot to mount a Docker volume for `/app/data`

#### Fix
Make sure:
- your code calls `save_users()` / `save_urls()`
- your Compose file mounts named volumes to `/app/data`

---

## 17. What You Should Mention in the Demo and Report

Assignment 3.1 grading explicitly asks you to highlight several things. 

### In the demo, show:

1. that both services are deployed using Docker
2. that both services still work
3. that data survives service restarts
4. that data survives `docker compose down`
5. what you did to keep the containers compact and efficient

### In the report, focus on design decisions such as:

- why you chose JSON files for persistence
- how Docker volumes provide persistence
- why `0.0.0.0` was necessary
- how you kept the images small and efficient
- any bonus design decisions you want to highlight

The assignment explicitly says the report should emphasize important design decisions rather than explaining the Dockerfile line by line. 

---

## 18. Summary of Required File Changes

### Files to create or update for Assignment 3.1

| File | Purpose |
| --- | --- |
| `auth_service/auth.py` | add JSON persistence and Docker-safe path handling |
| `shortener_service/shortener.py` | add JSON persistence and Docker-safe path handling |
| `auth_service/requirements.txt` | Python dependencies |
| `shortener_service/requirements.txt` | Python dependencies |
| `auth_service/Dockerfile` | build auth image |
| `shortener_service/Dockerfile` | build shortener image |
| `auth_service/data/users.json` | persistent user storage |
| `shortener_service/data/urls.json` | persistent URL storage |
| `docker-compose.yml` | run both services together with volumes and ports |

---

## 19. Final Checklist

Before you continue to Assignment 3.2, make sure all of these work:

- [ ] both services build with Docker
- [ ] both services start with Docker Compose
- [ ] both services are reachable from `127.0.0.1`
- [ ] users are saved in `users.json`
- [ ] mappings are saved in `urls.json`
- [ ] data survives `docker compose restart`
- [ ] data survives `docker compose down` and re-creation
- [ ] both images are built from compact Dockerfiles
- [ ] your README can explain how to run 3.1

If all of these are working, your Assignment 3.1 implementation is in good shape and your project is ready to move toward Kubernetes for Assignment 3.2.

---

## 20. Run Commands Recap

### Start everything
~~~bash
docker compose up --build
~~~

### Start in background
~~~bash
docker compose up --build -d
~~~

### Stop and remove containers
~~~bash
docker compose down
~~~

### Restart services
~~~bash
docker compose restart
~~~

### Show running containers
~~~bash
docker compose ps
~~~

### View logs
~~~bash
docker compose logs -f
~~~