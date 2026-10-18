# Module 5 — Serverless Functions with OpenFaaS

## Status

**Beginner workshop under development; not yet validated or ready for delivery.**

This module is being authored in the Tutorials repository. Integration into
`edge-ai-blueprint`, publication, and activation are separate later phases.
Authoring does not change the current infrastructure or active workshop.

The beginner material will be the complete reference implementation. An aligned
advanced TODO version will be derived later.

## Learning objectives

After completing the validated workshop, participants should be able to:

- Explain HTTP request → OpenFaaS gateway → function → response, and distinguish
  the function developer's responsibilities from the platform provider's.
- Invoke a prepared function and inspect HTTP status, headers, and JSON data.
- Implement input validation and predictable successful and error responses.
- Follow a controlled source → build → registry push → deployment workflow.
- Distinguish changing request data from changing deployed function code.
- Process deterministic weather data and handle external-service failures in an
  optional live-data extension.
- Generate bounded local traffic, interpret verified metrics, and clean up only
  their assigned exercise resources.

Serverless does not mean that servers disappear: the provider manages the runtime
infrastructure. Cold starts may occur when an instance starts; they do not occur
before every invocation. Scaling, scale-to-zero, queues, billing, and operator
behaviour depend on the platform, edition, and configuration. JavaScript
`async/await` is not queued asynchronous FaaS invocation. These features are not
required exercises in this workshop.

## Participant journey

Participants begin as developers in an organiser-prepared, isolated lab per
participant or group. They run complete guided build, push, deploy, invoke, update,
and cleanup steps themselves. Installing Kubernetes, OpenFaaS, or monitoring is
not part of the mandatory beginner path.

A shared environment may be considered in a later advanced workshop for different
learning objectives, including ownership, permissions, and collaboration.

| Planned notebook | Learning sequence |
|---|---|
| `beginner/01-explore-and-invoke.ipynb` | Check assigned configuration, invoke a prepared greeting function from Python and curl, inspect responses, and test malformed input. |
| `beginner/02-develop-and-deploy.ipynb` | Implement a participant-owned greeting function, build/push/deploy through the selected workflow, verify readiness, and update its code. |
| `beginner/03-data-and-observability.ipynb` | Process sample weather data, explore optional live data, generate bounded deterministic traffic, inspect metrics, and perform scoped cleanup. |

**These notebooks do not exist yet.** Each practical step will provide its purpose,
execution location, complete runnable action, expected result, verification
checkpoint, and focused recovery guidance. Configuration will be introduced once
and reused; secrets will never be printed.

Workshop duration is pending a timed reference rehearsal. No tested duration is
currently available.

## Existing material and planned deliverables

Existing assets:

- [Legacy participant guide](participants-guide-new.md): retained for learning-outcome
  comparison, not an approved runnable path. It includes installation, build,
  runtime, permissions, and monitoring assumptions that require correction.
- [Existing lecture slides](docs/05-serverless-DA.pdf): retained source material;
  conceptual corrections and alignment with greeting/weather exercises are pending.
- `images/`: existing illustrations, with asset provenance still to be reviewed.

Implemented authoring assets:

- `examples/greeting/handler.js`: POST greeting handler with input validation.
- `examples/greeting/handler.test.js`: 15 handler unit tests.
- `examples/greeting/package.json`: dependency-free `npm test` entry point.

Remaining planned additions, not yet available as complete deliverables:

```text
beginner/                   Three complete guided notebooks
examples/                   Greeting and weather function sources and manifests
fixtures/weather-sample.json Deterministic weather input
 tests/                     Response, failure-path, and safety verification
organizers-guide.md          Reference setup, access, preparation, and readiness
 docs/slide-corrections.md   Corrections to the retained slide narrative
 docs/validation-report.md  Exact versions, evidence, resource observations, limitations
```

Function-template, manifest, and helper filenames will be finalised with the
execution contract. There is no organiser guide or tests directory to use yet.
The legacy guide will remain during drafting until relevant outcomes are covered.

## Starting environment and responsibilities

### Participants

Participants need basic familiarity with HTTP/JSON and JavaScript, plus the ability
to run guided Python cells and Bash commands. The organiser will prepare JupyterLab
with a Python kernel, `faas-cli`, `curl`, Git, CA certificates, and the required
Python packages. Local Node.js/npm will be required only if the chosen local-test
workflow uses them. Package versions and the supported Node.js function runtime
must be pinned and tested before delivery; do not reuse an end-of-life runtime.

The planned execution environment is Linux with Bash in JupyterLab. Linux/amd64 is
the initial reference target, not a claim of tested compatibility. Other host or
image architectures require separate validation. The participant's laptop only
needs a browser compatible with the prepared JupyterLab service; native macOS or
Windows installation is not required. Exact browser versions remain to be tested.

Notebook cells and notebook terminals run on the notebook host, not on the
participant's laptop. In a notebook command, `localhost` means the notebook host;
in a laptop browser, it means the laptop. The organiser must supply reachable
notebook and browser routes instead of assuming they are interchangeable.

### Organisers

Organisers prepare the reference platform, registry and protected builder, deploy
initial functions, distribute configuration through an appropriate protected
channel, verify readiness, and provide monitoring access. They retain platform
administration and infrastructure-cleanup responsibilities.

Participant access must be confined to the assigned disposable lab and registry
repositories. Participants must not receive shared-platform administrator
credentials, infrastructure-host Docker socket access, platform-admin kubeconfigs,
or unrestricted registry credentials. Any administrative capability within the
isolated lab must be documented explicitly.

The isolation boundary, image-building capability, registry permissions, and scoped
cleanup must be validated. Function-name prefixes alone are not authorisation.

## Indicative infrastructure recommendation

**The beginner workshop uses isolated labs. The shared profile below is retained
only as an indicative alternative; it is not a sizing recommendation for the
selected beginner model.** Per-lab resources, concurrency, and total cohort capacity
must be estimated separately and validated through rehearsal.

The following is an **unmeasured planning profile** for a dedicated small shared
pilot with **two simultaneous participant/group sessions**, small functions,
lightweight monitoring, and serial image builds. It is not a vendor minimum,
benchmark result, or guarantee of cohort capacity.

| Component | Initial planning recommendation | Assumptions |
|---|---|---|
| Shared lab budget | 8 vCPUs, 16 GiB RAM, 80 GiB available disk | Kubernetes/OpenFaaS, small functions, monitoring, and one build at a time; budget unrelated workloads separately. |
| Notebook session | 1 vCPU and 2 GiB RAM per session | Included in the shared total if colocated; not a dedicated image-building budget. |
| Image builder | One concurrent build initially | Protected build submission; explicit CPU, memory, and ephemeral-storage limits; measure peaks before increasing concurrency. |
| Function execution | One replica per exercise function initially | Use tested requests/limits and supported configuration; do not assume scale-to-zero or unrestricted scaling. |
| Registry | Reachable compatible image registry | Verify edition-specific access support; account for retained images and build-cache growth. |
| Monitoring | Prometheus; Grafana optional initially | Expose only the access needed for the exercises; verify metric names and dashboard compatibility. |

A multi-node topology is optional. Physical placement does not determine the
learning sequence. Isolated labs per participant and larger cohorts require their
own provisioning, security model, and sizing. Pilot observations will refine this
profile after the reference rehearsal.

The reference setup must document and verify:

- Kubernetes distribution/version, OpenFaaS edition/release/chart settings,
  CLI version, template revision, Node.js runtime, and image architecture.
- A protected build mechanism and registry reachable by both builder and runtime.
- Notebook/browser access to gateway and monitoring, DNS resolution, trusted TLS
  where applicable, and appropriate network restrictions.
- Image/template download routes during preparation; optional outbound access to
  the selected weather provider only for the live-data extension.
- Safe credential storage outside Git, notebooks, function images, and fixtures.
  Build/deployment credentials must not be disclosed in outputs or diagnostics.

The deterministic core weather exercise must work without an external weather API.

## Execution contract — pending S2

The selected teaching model is an isolated lab per participant or group, with
participants executing build, push, and deploy commands themselves. The isolation
mechanism, build implementation, and access controls have not yet been selected.
Executable deployment cells cannot be finalised until one complete path is
documented and validated.

S2 must resolve:

1. Exact platform edition, versions, CLI, template, runtime, and handler contract.
2. Participant identity, assigned function names, allowed operations, and enforced
   ownership boundaries, including negative cross-participant tests.
3. Protected source submission, build, push, deploy, readiness, update, and cleanup.
4. Matching manifests, registry repository names, and versioned image tags.
5. Configuration distribution, invocation access, monitoring routes, and verified
   invocation/error/duration metrics.

Organiser-mediated build/deployment is not the selected beginner workflow.
Organisers prepare the isolated labs; participants perform the function lifecycle.
The selected implementation must support this distinction without granting access
to the shared infrastructure.

## Inspected reference candidates — not yet validated

The following candidates have been inspected upstream. They are not an approved
or platform-validated version set. The standalone Node.js authoring runtime
and direct HTTP wrapper described below have been executed. The template image
build, watchdog, and OpenFaaS platform have not been validated.

| Component | Candidate | Evidence and limitations |
|---|---|---|
| OpenFaaS CLI | `0.18.16` | Release metadata and build/push/deploy command sources inspected; binary not verified or executed. |
| Node.js template | `node22` from `openfaas/templates`, commit `262e6a608a3f987bcbe3322d1543b44e0e4282dc` | Template inspected; base-image tags and dependency ranges remain mutable; default tests are placeholders. |
| OpenFaaS chart | `15.0.13` from `openfaas/faas-netes`, commit `f97de9fc1314bad45848f7e0bfaadb69710615a6` | CE selection and monitoring templates inspected; chart not rendered or deployed. |

Published SHA-256 for the CLI release asset named `faas-cli`:
`16f82d999d92ada11c3abb5ab4be32207fc99b83463672227a9ea57c0cf36299`.
This is the upstream checksum, not evidence of local binary verification.

The planned beginner sequence uses separate `faas-cli build`, `faas-cli push`,
and `faas-cli deploy` commands against the same manifest, followed by readiness
checks and invocation. Explicit image versions will distinguish code updates.
`--shrinkwrap` prepares a build context; it does not build an image.

Before adopting these candidates, resolve CE distribution terms for the intended
institution-run workshop, registry access restrictions, VM and network isolation,
notebook/browser routes, supported Kubernetes and Docker versions, image digests,
dependency locking, and meaningful tests. Then rehearse the complete lifecycle
in a disposable reference lab. No installation is required on the authoring host.

## Validation and release gate

### Local greeting-handler baseline

Implementation checkpoint: `95bbd65a2a5c74f5e0b7acc6626fa8648b5ae22a`.

On the Linux/x86_64 authoring host, `npm test` passed all 15 tests with no failures,
skips, or TODOs using Apptainer `1.4.0-1.el8`, Node.js `v22.23.3`, and npm `10.9.9`.
The runtime was executed with a read-only source bind and required neither a
host Node.js installation nor Docker.

Source image: `docker.io/library/node:22-alpine`, resolved to the verified
Linux/amd64 OCI manifest digest:
`sha256:2c752226d477b4a886378baa95b9af252be59301b725fdb0b7e15208131505a8`.

Local converted SIF SHA-256:
`aa8a5e9435fa2ae5c1c837f626a5fd2b1300029cfdb250aedd912a117871dadf`.
This identifies the recorded local file; independent conversions may produce
different SIF checksums.

Tests cover successful greetings, trimming, the 80-unit JavaScript string-length
boundary, invalid bodies/names, and GET rejection with an Allow header. They use a
context stub, not the actual OpenFaaS HTTP wrapper. Separate direct-wrapper
observations are recorded below. Container builds, watchdog/gateway invocation,
and participant isolation remain unvalidated. The test-image pin does not pin the template's build images or
dependency ranges. Apptainer is an authoring test method, not a selected
participant runtime or function-image builder.

### Direct HTTP-wrapper observations

The unmodified `node22/index.js` from template revision
`262e6a608a3f987bcbe3322d1543b44e0e4282dc` was executed with the greeting handler
in an external scratch directory using the recorded Apptainer/Node.js runtime.
Dependencies resolved to Express `5.3.0` and body-parser `2.3.0`.

The scratch dependency lockfile SHA-256 was
`86c9d89afa68de7e64c5408caf2808656d452c5ce6b5236d62925cab10feb5ee`.
This lockfile is not committed or integrated into the function-image build.

A test-only interception bound the server to loopback on an automatically
assigned port without modifying the wrapper source. Seven HTTP observations
matched expectations in both default mode and explicit `NODE_ENV=production`:

- Valid JSON returned 200 with the expected JSON greeting.
- An invalid name returned 400 with `invalid_name`.
- A JSON array and plain text returned 400 with `expected_json_object`.
- GET returned 405 with JSON and `Allow: POST`.
- A URL-encoded form containing `name=Ada` was accepted with 200.
- Malformed JSON returned 400 with HTML before the handler ran.

In default mode, the malformed-JSON response included parser stack details.
Production mode replaced those client-facing details with `Bad Request`, but the
parser diagnostic and submitted malformed body still appeared in server logs.

These are observations, not approval of a JSON-only request contract or uniformly
JSON error responses. Request media-type policy and parser-error handling remain
execution-contract decisions. Production mode alone does not resolve those gaps.
The stale `node20` startup label does not identify the runtime, and the logged
port was not the actual port used by this test.

The scratch probe does not exercise the watchdog, gateway, image build, deployment,
or participant isolation. Its files remain outside Git; durable automated
integration tests are still pending.

### Delivery gate

Before delivery, a fresh reference rehearsal must complete all three notebooks and
check response semantics, invalid inputs, external-failure handling, bounded load,
scoped cleanup, and participant capability boundaries. Record exact versions,
commands, results, resource observations, and unresolved issues. Static notebook
checks alone do not establish live platform compatibility.

No live OpenFaaS execution or end-to-end workshop validation has been performed in
this authoring sprint. No current platform deployment or activation is implied.
Advanced notebooks, production integration, required autoscaling/scale-to-zero,
queued invocation, and URL-shortener exercises are outside this sprint.

## Licensing and provenance — unresolved

The repository [LICENSE](../../../LICENSE) contains Apache License 2.0, while the
[root README](../../../README.md) states MIT for code and CC BY 4.0 for documentation.
This discrepancy must be resolved with the repository maintainer before publication;
this module does not infer or introduce a licence assignment for individual assets.
Review slide/image provenance and retain applicable attribution and licence notices.

Modification notice: this README has been revised for the beginner-first OpenFaaS
workshop authoring sprint, replacing the previous incomplete navigation and
prerequisites. The legacy guide, slides, and images are unchanged.
