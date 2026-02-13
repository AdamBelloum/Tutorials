
# Moderator Solution Guide: URL Shortener Workshop

This document contains the step-by-step solutions and logic for the **Architecting a RESTful URL Shortener** workshop. Use this to assist students who are stuck and to verify their implementation.

## NOTE : for wokrshop orgwanisers

**Workshop Title:** Build-a-Shortener: Architecting RESTful APIs  
**Target Audience:** Students/Developers familiar with basic Python.  
**Goal:** Transition from theoretical REST knowledge to a functional, validated URL shortening service.

### Phase 1: The "Mental Model" (30 Minutes)
1.  **REST vs. SOAP Lightning Talk (10 mins):** Quick refresher on why REST won the web (statelessness, resource-based).
2.  **Mapping the Specs (20 mins):** * **Group Activity:** Define the "Request Body" for `POST /` and `PUT /:id`.
    * **Whiteboarding:** Draw the lifecycle of a URL being shortened.

### Phase 2: Scaffolding & Hello World (45 Minutes)
1.  **Environment Setup:** Provide a `requirements.txt` and a `starter_app.py`.
2.  **Live Coding Demo:** Facilitator codes the `GET /` (list all keys) route live.
    * *Note:* Explain the use of an in-memory dictionary $urls = \{\}$ to store data.
3.  **Hands-on Lab 1:** Participants implement `POST /` to return a hard-coded ID.

### Phase 3: The "Shortener" Logic & Regex (60 Minutes)
1.  **The ID Algorithm Challenge:** Discuss why `random.randint()` or incremental IDs are bad for scaling/security.
    * **Task:** Implement Base62 encoding or hashing-and-slicing.
2.  **The Regex Shield:** Provide "trap" URLs (e.g., `ftp://site`, `http://---`).
    * **Task:** Write logic to ensure only valid `http/https` URLs are stored.

### Phase 4: Peer Testing & "Chaos" Demo (45 Minutes)
1.  **The Postman Gauntlet:** Students pair up and try to "break" each other's APIs.
2.  **Bonus "Sprint":** Add **expiration dates** to URLs.

---

##  Table of Contents
* [Step 1: The Flask Skeleton](#step-1-the-flask-skeleton)
* [Step 2: The Shortener Logic](#step-2-the-shortener-logic)
* [Step 3: Validation & Regex](#step-3-validation--regex)
* [Step 4: The Redirect](#step-4-the-redirect)
* [Full Implementation Code](#full-implementation-code)

---

## Step 1: The Flask Skeleton
**Objective:** Verify Flask is installed and the basic route works.

* **Moderator Check:** Ensure the student has `flask` installed (`pip install flask`).
* **The Code:**
```python
from flask import Flask, jsonify, request

app = Flask(__name__)
url_db = {} # The in-memory database

@app.route('/', methods=['GET'])
def list_urls():
    return jsonify(url_db), 200

if __name__ == '__main__':
    app.run(debug=True)
```

## Step 2: The Shortener Logic
Objective: Create a unique ID from a long URL.
Moderator Check: Students should not use random.randint.
Logic: Suggest using hashlib to create a hash of the URL and taking the first 6 characters.
```python
import hashlib

def generate_short_id(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]
```

## Step 3: Validation & Regex
Objective: Block malformed or dangerous URLs.
Moderator Check: Does the regex handle http:// and https://? Does it return a 400 status code for fails?
The Regex:
Python
```python
import re

def is_valid_url(url):
    # Matches http:// or https:// followed by domain logic
    regex = re.compile(
        r'^https?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|' # domain
        r'localhost|' # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None
```
## Step 4: The Redirect
Objective: Ensure the browser actually moves to the destination.
Moderator Check: Ensure they imported redirect from Flask.
Common Error: Returning the URL as a string instead of using the redirect() function.
Python
```python
from flask import redirect

@app.route('/<short_id>', methods=['GET'])
def go_to_url(short_id):
    long_url = url_db.get(short_id)
    if long_url:
        return redirect(long_url, code=301)
    return jsonify({"error": "URL not found"}), 404
```

Full Implementation Code
This is the complete app.py for your reference.

Python
```python
from flask import Flask, request, jsonify, redirect
import hashlib
import re

app = Flask(__name__)
url_db = {}

def is_valid_url(url):
    regex = re.compile(r'^https?://\S+')
    return re.match(regex, url)

@app.route('/', methods=['GET'])
def list_all():
    return jsonify(url_db), 200

@app.route('/', methods=['POST'])
def create_short():
    data = request.get_json()
    long_url = data.get('url')
    
    if not long_url or not is_valid_url(long_url):
        return jsonify({"error": "Invalid URL"}), 400
    
    short_id = hashlib.md5(long_url.encode()).hexdigest()[:6]
    url_db[short_id] = long_url
    
    return jsonify({"short_url": f"http://localhost:5000/{short_id}"}), 201

@app.route('/<id>', methods=['GET'])
def do_redirect(id):
    url = url_db.get(id)
    return redirect(url, code=301) if url else (jsonify({"error": "Not Found"}), 404)

@app.route('/<id>', methods=['DELETE'])
def delete_url(id):
    if id in url_db:
        del url_db[id]
        return '', 204
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
```
## FacilitatorÕs Toolkit: Cheat Sheet

| Component | Recommendation |
| :--- | :--- |
| **Language** | Python 3.x |
| **Framework** | Flask (Lightweight) |
| **Testing Tool** | Postman or `curl` |
| **Data Storage** | Python Dictionary (Global variable) |

> **Common Pitfalls:**
> * **The 301 Redirect:** Ensure students return a header, not just text.
> * **Method Confusion:** `PUT` (Update) vs `POST` (Create).
> * **Trailing Slashes:** Flask is sensitive to `/route` vs `/route/`.

**Closing:** Have students write a `README.md` explaining their algorithm and scaling strategy to mirror real-world engineering practices.

## Troubleshooting for Moderators

- 415 Unsupported Media Type
Ensure the student is sending the request in Postman as Body -> raw -> JSON.

- Infinite Redirects: If a student tries to shorten the short URL itself.
- Port already in use: Tell them to run app.run(port=5001) or another number.
