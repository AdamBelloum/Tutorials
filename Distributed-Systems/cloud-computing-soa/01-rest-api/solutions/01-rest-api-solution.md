# This guide provides a complete walkthrough and solution for the RESTful URL Shortener workshop.

# 1. Understanding the Problem & Architecture
## The Problem
A long URL (like a 200-character Amazon link) is difficult to share. URL Shortening solves this by mapping a `Short ID` to a `Long URL` in a database. When someone visits the short ID, we redirect them to the long one.

## The API Interface (Endpoints)
We use different HTTP Methods to tell the server exactly what we want to do:

| HTTP method | Description |
| ----------- | ----------  |
| `POST` / (Create): | Used to send new data. Since we are creating a new mapping, POST is the standard.| 
|  `GET` / (List): | Used to retrieve data without changing it. It returns all current mappings.| 
| `GET` /:id (Redirect): | Used to "fetch" the long URL. We use a 301 Redirect so the browser automatically jumps to the destination.| 
| `PUT` /:id (Update): | Used when you want to change where an existing ID points.| 
| `DELETE` /:id (Remove): | Used to destroy a mapping.| 

## Error Handling
We use Status Codes to tell the client if they messed up:

| Error code | Description |
| ---------- | ----------  |
| `400` Bad Request: | Used if the user sends a "fake" URL or missing |data.
| `404` Not Found: | Used if the user tries to access/delete an ID that doesn't exist. |

# 2. Flask 101: Setup & First Code
## What is Flask?
Flask is a "micro-framework" for Python. It handles the networking (listening for requests) so you can focus on the logic.

- Check Installation: Open your terminal and type:

```bash
python3 -m flask --version
```
If it says "command not found," run: pip install flask

The First Code (The Skeleton)
Create app.py:

Python
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

if __name__ == '__main__':
    app.run(debug=True)

```
- Test: Run python3 app.py and visit `http://127.0.0.1:5000`. You should see

```text
 "Server is running!"
```

# 3. Step-by-Step Implementation
## Step 1: Data Storage & Hashing
We need a place to store data and a way to make IDs.
Code:
```bash
import hashlib
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
url_db = {} # Our temporary database

def generate_short_id(url):
    # Create a unique 6-character hash of the URL
    return hashlib.md5(url.encode()).hexdigest()[:6]
```
## Step 2: The POST & GET Endpoints

Explanation: POST accepts a JSON URL, validates it, hashes it, and saves it. GET shows the list.
Code:
```python
import re

def is_valid_url(url):
    # Regex to check if it starts with http/https
    return re.match(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)

@app.route('/', methods=['POST'])
def create_short_url():
    data = request.get_json()
    long_url = data.get('url')
    
    if not long_url or not is_valid_url(long_url):
        return jsonify({"error": "Invalid URL"}), 400
        
    short_id = generate_short_id(long_url)
    url_db[short_id] = long_url
    return jsonify({"short_id": short_id}), 201

@app.route('/', methods=['GET'])
def list_urls():
    return jsonify(url_db), 200
```

- How to Test:

```bash
curl -X POST http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{"url":"https://google.com"}'
```
## Step 3: The Redirect (GET /:id)
Explanation: When someone visits the ID, look it up. If found, use 301 to send them away.
Code:
```python
@app.route('/<short_id>', methods=['GET'])
def do_redirect(short_id):
    long_url = url_db.get(short_id)
    if long_url:
        return redirect(long_url, code=301)
    return jsonify({"error": "Not Found"}), 404
```

- How to Test: Paste `http://127.0.0.1:5000/YOUR_ID` into your browser.

## Step 4: Update & Delete (PUT/DELETE)
Explanation: PUT overwrites the destination. DELETE removes the entry entirely.

Code:
```python
@app.route('/<short_id>', methods=['PUT'])
def update_url(short_id):
    if short_id not in url_db:
        return jsonify({"error": "Not Found"}), 404
    
    new_url = request.get_json().get('url')
    if not is_valid_url(new_url):
        return jsonify({"error": "Invalid URL"}), 400
        
    url_db[short_id] = new_url
    return jsonify({"message": "Updated"}), 200

@app.route('/<short_id>', methods=['DELETE'])
def delete_url(short_id):
    if short_id in url_db:
        del url_db[short_id]
        return '', 204
    return jsonify({"error": "Not Found"}), 404
```
- How to Test (Delete):

```bash
curl -X DELETE http://127.0.0.1:5000/YOUR_ID
```

# References

1. [Flask quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
2. [Flask Cheat Sheet](https://realpython.com/flask-blueprint/)
3. [Regular expresssion 101](https://regex101.com/)
4. [Learn RegEx](https://github.com/ziishaned/learn-regex/blob/master/README.md)
5. [iHateRegEx](https://ihateregex.io/expr/url/)
6. [HTTP status code](https://www.restapitutorial.com/httpstatuscodes)
7. [HTTP response status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)