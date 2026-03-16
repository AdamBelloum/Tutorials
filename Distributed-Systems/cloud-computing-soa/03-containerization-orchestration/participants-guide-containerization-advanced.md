# Workshop: Advanced Brief for Assignment 3.1 (Containerization)

This advanced brief defines **what you must deliver** for Assignment 3.1.
It does not prescribe implementation steps.

---

## 1. Outcome Target

By the end of this task, your system must include:

- an Authentication Service running as a container
- a URL Shortener Service running as a container
- a Compose-based multi-service runtime
- persistent data behavior across service/container restarts
- external reachability of both services

---

## 2. Required Deliverables

| Area | Required Deliverable |
| --- | --- |
| Service runtime | Two independently buildable service images |
| Service orchestration | One Compose file that manages both services together |
| Persistence | File-backed storage for user data and URL data |
| Data durability | Docker volumes used for persistent state directories |
| Key material | Correct key placement so JWT flow still works |
| Networking | Both services reachable from outside containers |

---

## 3. Scope of Changes

Your solution must cover all of the following files or equivalent structure:

- `auth_service/auth.py`
- `shortener_service/shortener.py`
- `auth_service/Dockerfile`
- `shortener_service/Dockerfile`
- `auth_service/requirements.txt`
- `shortener_service/requirements.txt`
- `docker-compose.yml`
- persistent data files under each service `data/` directory

---

## 4. Functional Expectations

### 4.1 Authentication service

You must ensure:

- user data is persisted to disk
- persisted users are loaded on startup
- user create/update operations persist data immediately
- login and JWT behavior remain consistent with Assignment 2 expectations

### 4.2 URL shortener service

You must ensure:

- URL mappings are persisted to disk
- persisted mappings are loaded for request handling
- create/update/delete operations persist data immediately
- JWT-based authorization behavior remains valid

---

## 5. Container Quality Expectations

Your containerization should demonstrate:

- clear separation of service responsibilities
- lean images and reasonable dependency scope
- reproducible builds
- correct service entrypoints
- correct service port exposure

---

## 6. Verification Requirements

You should be able to demonstrate all of the following:

- both services start together under Compose
- registration/login/shortening flow works end-to-end
- data remains available after service restarts
- data remains available after container recreation
- services are reachable from outside container network namespace

---

## 7. Submission Readiness Checklist

Before submission, confirm:

- [ ] both services are containerized and runnable
- [ ] Compose runs both services correctly
- [ ] persistence is file-based and volume-backed
- [ ] JWT integration still works between services
- [ ] externally reachable endpoints are functional
- [ ] project structure is ready for Assignment 3.2 extension

---

## 8. Architecture Reflection (Recommended)

Be prepared to explain:

- why your persistence design satisfies Assignment 3.1
- how your volume mappings preserve state
- why your network binding supports external access
- how this layout prepares migration to Kubernetes in Assignment 3.2
