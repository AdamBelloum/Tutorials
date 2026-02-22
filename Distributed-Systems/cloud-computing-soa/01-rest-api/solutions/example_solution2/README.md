# REST API Example Solution

## Project Setup
### Python and FastAPI
FastAPI is a framework designed to quickly build REST APIs with easy setup and implementation.

### SQLite
In this project, we need to store mapped URLs, so we considered using a database system or CSV files. We chose a structured database for better efficiency and maintainability. Among SQLite, PostgreSQL, and MySQL, we selected SQLite because it is a lightweight database, easy to set up (no external installation needed) and still provides all necessary functions.

### Redis
For this project, we need to store global variables like URL counter that is used by shorten URL algorithm and perform rate-limiting for added security. Redis is single-threaded and can operate as a distributed cache. Its light-weightedness and low latency data access make the design scalable even with multiple read/write services and databases.

## Installation

- Python version: 3.11
- Install and start Redis as a service

    For mac users: `brew install redis` , `brew services start redis`

    For linux users: `sudo apt-get install redis`, `sudo systemctl start redis-server`

    For windows users: `sudo apt-get install redis`, `sudo service redis-server start`
- Set up venv (for MacOS):
```
    python -m venv venv
    source venv/bin/activate
```
- Install packages: `pip install -r requirements.txt`

## Run tests
- Go to `/tests` folder: `cd tests`
- Run tests: `python3 -s test_1_marking_mk2.py`

## Run our application
- Run app: `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`

**Notes**
- Use postman to test it: `http://127.0.0.1:8000`

## Authors
- Mhi Mai,
- Yunxuan Tang
- Sathya Sravya Vallabhajyosyula

From WSCBS 2025, University of Amsterdam