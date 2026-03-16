# Workshop: Advanced Brief for Assignment 3.2 (Orchestration)

Note: The VM names (`student127`, `student128`, `student129`) are examples used in this brief. Replace them with your own VM names/IPs in your environment.

This advanced brief defines **what you must deliver** for Assignment 3.2.
It does not prescribe implementation steps.

---

## 1. Outcome Target

By the end of this task, your system must include:

- a working 3-node Kubernetes cluster
- authentication and shortener workloads deployed in Kubernetes
- persistent shared storage available to Pods
- externally reachable application services
- a repeatable verification workflow

---

## 2. Cluster-Level Requirements

| Requirement | Expected State |
| --- | --- |
| Control plane | `student127` initialized and operational |
| Workers | `student128` and `student129` joined and Ready |
| CNI networking | Pod networking functional across all nodes |
| Runtime health | Kubernetes system components healthy |

---

## 3. Workload-Level Requirements

| Component | Required State |
| --- | --- |
| Namespace | Dedicated namespace `websvc` |
| Auth deployment | Running with expected replica policy |
| Shortener deployment | Running with expected replica policy |
| Auth service | Exposed for external access via Kubernetes Service |
| Shortener service | Exposed for external access via Kubernetes Service |
| Endpoints | Backing endpoints available (not empty) |

---

## 4. Storage Requirements

You must provide Kubernetes storage resources that achieve:

- persistent data beyond Pod lifecycle
- shared access model compatible with your deployment design
- correct claim-to-volume binding
- usable mounted storage inside both services

Deliverables must include:

- PersistentVolume manifest
- PersistentVolumeClaim manifest
- valid storage backend configuration aligned with cluster environment

---

## 5. Security and Configuration Requirements

You must provide resource definitions for:

- auth private/public key distribution to auth workload
- public key distribution to shortener workload
- consistent key material so JWT validation succeeds

Deliverables must include:

- Secret resource for auth keys
- ConfigMap (or equivalent) for shortener public key

---

## 6. Image and Deployment Requirements

You must ensure:

- container images are available from your registry namespace
- Kubernetes deployments reference the intended image tags
- image architecture is compatible with target VM architecture
- rollout reaches healthy state for both services

---

## 7. Manifest Coverage

Your `k8s/` set should include, at minimum:

- namespace manifest
- storage manifests (PV + PVC)
- secret/config manifests
- deployment manifests for auth and shortener
- service manifests for auth and shortener

---

## 8. Verification Expectations

You should be able to demonstrate all of the following:

- all nodes report Ready
- application Pods report Running and stable
- services are externally reachable on expected exposed ports
- persistence behaves correctly across Pod restarts/rescheduling
- end-to-end user flow works (register, login, authenticated shortener actions)
- unittest workflow can validate functional behavior against Kubernetes deployment

---

## 9. Submission Readiness Checklist

Before submission, confirm:

- [ ] cluster is healthy and multi-node
- [ ] manifests deploy cleanly in correct namespace
- [ ] storage resources are bound and mounted
- [ ] auth and shortener services are reachable externally
- [ ] JWT auth/authorization behavior is correct
- [ ] tests and smoke checks pass consistently

---

## 10. Architecture Reflection (Recommended)

Be prepared to explain:

- why your orchestration design satisfies Assignment 3.2 goals
- how storage and service exposure decisions support reliability
- how key/config distribution supports secure JWT validation
- what operational risks remain and how you monitor them
