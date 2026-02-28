# Welcome to the Microservices Workshop

In this session, you will evolve your standalone URL Shortener into a Microservices Architecture with multi-user support. Instead of one single application, you will split the workload into two specialized services that communicate with each other.

# The objective of the tutorial
- Build an Authentication Service: You will create a new service dedicated to managing a database of users. This service will register users, update passwords, and issue JSON Web Tokens (JWTs) upon successful login.

- Secure the URL Shortener: You will update your existing shortener to require authentication. Each URL mapping will now be associated with a specific user, ensuring that only the owner has the power to manage their own data.

- Implement Token Validation: When a user wants to shorten or delete a link, they will present their JWT to the shortener. The shortener will then communicate with the Authentication Service to validate the token and confirm the user's identity.

# Service Specifications

## 1. Authentication Service
This service acts as the gatekeeper, managing user identities.

| Method & Path | Purpose | Success Code |
| ------------- | ------- | ------------ |
| POST /users   | Register a new unique user. | 201 |
| PUT /users    | Update a password (requires old password). | 200 |
| POST /users/  | loginValidate credentials and issue a JWT. | 200 | 

## 2. URL Shortener Service

The updated shortener now includes 403 Forbidden responses for unauthorized actions.

| Method & Path  |  Purpose | Success Code | 
| -------------  |  ------- | ------------ |
| GET /:id       | Redirect to the long URL. | 301 |
| POST /Create   | a new mapping (Authenticated only).201 |
| PUT /:id       | Update a mapping (Owner only).200 |
| DELETE /:id    | Remove a mapping (Owner only).204 |

By the end of this workshop, you will understand how to manage distributed data ownership and how to use JWTs to maintain a "logged-in" state across different services while adhering to RESTful principles.

## Step 0: Environment Setup & Health Check
Open your terminal or command prompt and follow these steps to verify your installation.

- Check Python Version: Ensure you have Python 3 installed.

```bash
python --version
```

- Verify/Install Packages
We need Flask (to build the services) and Requests (to allow the services to talk to each other). Run this command to install or update them:

```bash
pip install flask requests
```
- The "Health Check" Test
Create a small file named check_env.py and paste this code to ensure everything is working:

```python
try:
    import flask
    import requests
    import hmac
    print(" Environment Ready: Flask and Requests are installed.")
except ImportError as e:
    print(f" Missing Package: {e}")
```
Run it with python check_env.py. If you see the green checkmark, you are ready to start!


## Step 1: Create the Shared Security Tool
Both services need to understand JWTs. You must construct these manually by encoding data into Base64 and adding a digital signature.

Create jwt_utils.py:

```python
import hmac, hashlib, base64, json

SECRET_KEY = "workshop-secret" # The private key used to sign tokens

def base64_url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

def create_jwt(payload):
    # 1. Header & Payload
    header = {"alg": "HS256", "typ": "JWT"}
    h_b64 = base64_url_encode(json.dumps(header).encode())
    p_b64 = base64_url_encode(json.dumps(payload).encode())
    
    # 2. Signature (Prevents tampering)
    sig_base = f"{h_b64}.{p_b64}"
    signature = hmac.new(SECRET_KEY.encode(), sig_base.encode(), hashlib.sha256).digest()
    return f"{sig_base}.{base64_url_encode(signature)}"

def verify_jwt(token):
    try:
        h_b64, p_b64, sig_prov = token.split('.')
        # Verify if the signature matches our secret key
        expected = hmac.new(SECRET_KEY.encode(), f"{h_b64}.{p_b64}".encode(), hashlib.sha256).digest()
        if base64_url_encode(expected) == sig_prov:
            return json.loads(base64.urlsafe_b64decode(p_b64 + '=='))
    except: return None
```
## Step 2: Build the Authentication Service
This service registers users and issues the JWT token.

Create auth_service.py (Port 5001):

```python
from flask import Flask, request, jsonify
from jwt_utils import create_jwt, verify_jwt

app = Flask(__name__)
users = {} # In-memory storage: {username: password}

@app.route('/users', methods=['POST'])
def register():
    data = request.json
    u = data.get('username')
    if u in users: return "duplicate", 409
    users[u] = data.get('password')
    return "Created", 201

@app.route('/users/login', methods=['POST'])
def login():
    data = request.json
    u, p = data.get('username'), data.get('password')
    if users.get(u) == p:
        return jsonify({"token": create_jwt({"user": u})}), 200
    return "forbidden", 403

@app.route('/validate', methods=['POST'])
def validate():
    token = request.json.get('token')
    payload = verify_jwt(token)
    return (jsonify(payload), 200) if payload else ("forbidden", 403)

app.run(port=5001)
```
## Step 3: Build the URL Shortener Service
This service creates links but asks the Auth Service to verify tokens first.

Create shortener_service.py (Port 5002):

```python
import requests, hashlib
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
url_db = {} # {id: {"url": long_url, "owner": username}}

def get_authorized_user():
    token = request.headers.get('Authorization')
    # Ask Auth Service to validate the "pass"
    res = requests.post("http://localhost:5001/validate", json={"token": token})
    return res.json().get('user') if res.status_code == 200 else None

@app.route('/', methods=['POST'])
def create():
    user = get_authorized_user()
    if not user: return "forbidden", 403
    
    url = request.json.get('url')
    s_id = hashlib.md5(url.encode()).hexdigest()[:6]
    url_db[s_id] = {"url": url, "owner": user}
    return jsonify({"id": s_id}), 201

@app.route('/<s_id>', methods=['DELETE'])
def delete(s_id):
    user = get_authorized_user()
    entry = url_db.get(s_id)
    if not entry: return "not found", 404
    
    # Only the owner can delete their own link
    if entry['owner'] != user: return "forbidden", 403 
    del url_db[s_id]
    return "", 204
```

app.run(port=5002)

## Step 4: Final Test
Run both services in two terminal windows.

- Register & Login at Port 5001 to get your JWT token.

- Shorten a URL at Port 5002 by sending the token in the Authorization header.

- Test Ownership: Try to delete that link without a token or with a different user's token. You should see a 403 Forbidden.

References:

1. [What are microservices?:](https://microservices.io/)
2. [Json Web Tokens (JWT):](https://jwt.io/introduction/)  
3. [A Practical Guide for JWT Authentication using Nodejs and Express](https://medium.com/swlh/a-practical-guide-for-jwt-authentication-using-nodejs-and-express-d48369e7e6d4)   
4. [Introduction to microservices:](https://www.nginx.com/blog/introduction-to-microservices/)
5. [An introduction to OAuth 2:](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)

