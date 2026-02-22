# Microservices Example Solution

## Run without Docker

### Python version: 3.11

### Install and start Redis as a service

- For mac users: `brew install redis` , `brew services start redis`
- For linux users: `sudo apt-get install redis`, `sudo systemctl start redis-server`
- For windows users: `sudo apt-get install redis`, `sudo service redis-server start`
### Set up venv (for MacOS):
- For url_shortener_service:
```
    cd url_shortener_service
    python -m venv url_venv
    source url_venv/bin/activate
    pip install -r requirements.txt
```
- For auth_service:
```
    cd auth_service
    python -m venv auth_venv
    source auth_venv/bin/activate
    pip install -r requirements.txt
```

### Run our application and experience round robin style load balancing
- Back to `example_solution2` folder

Run 2 servers for url_shortener service:
- `uvicorn url_shortener_service.main:app --host 0.0.0.0 --port 8000 --reload`
- `uvicorn url_shortener_service.main:app --host 0.0.0.0 --port 8002 --reload`

Run 2 servers for auth service:
- `uvicorn auth_service.main:app --host 0.0.0.0 --port 8001 --reload`
- `uvicorn auth_service.main:app --host 0.0.0.0 --port 8003 --reload`

### Run gateway
- Create venv (MacOS):
```
    cd gateway
    python -m venv gateway_venv
    source gateway_venv/bin/activate
    pip install -r requirements.txt
```
- Back to `example_solution2` folder
- Run app: `uvicorn gateway.main:app --host 0.0.0.0 --port 10000 --reload`
- You can make requests to gateway and internally requests will be forwarded to respective microservices. Also, while sending requests to each service, the load is balanced in round robin style.


## Run tests
- Install requests: `pip install requests`
- After starting all five servers on different ports locally, following the steps above, you can run tests using the below commands. 
- Run tests: `python3 -s test_app.py`
- Use postman to test: You can test gateway directly at `http://127.0.0.1:10000` ( Recommended since API gateway can forward requests to individual services).


## Using Docker:
<!-- **Note**: If you use docker, do not do above steps -->
- Update docker compose file: Using `bridge` network instead of `overlay` (see in the file)
- Build: `docker-compose build`
- Run all: `docker-compose up -d`
- Stop all: `docker-compose down`
- You can test all endpoints using Postman

## Using Docker Swarm (scaling & docker based in-built load balancing)
- Update docker compose file: Using `overlay` network instead of `bridge` (see in the file)
- Init Swarm: `docker swarm init` (once)
- Build images:
```
docker build -t url_shortener_service_image:latest url_shortener_service/
docker build -t auth_service_image:latest auth_service/
docker build -t gateway_image:latest gateway/
```

- Create stack: `docker stack deploy -c docker-compose.yml app_stack`

- Scale:
```
docker service scale app_stack_url_shortener_service=<num_of_instances>
docker service scale app_stack_auth_service=<num_of_instances>
docker service scale app_stack_gateway=<num_of_instances>

```

- Get all services (optional): `docker service ls`

- Remove stack (if you want to stop): `docker stack rm app_stack`


## Authors
- Mhi Mai,
- Yunxuan Tang
- Sathya Sravya Vallabhajyosyula

From WSCBS 2025, University of Amsterdam