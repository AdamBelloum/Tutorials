#!/usr/bin/env bash
set -euo pipefail

# Build and push project images to Docker Hub.
# Usage:
#   docker login
#   ./commands/push-images.sh -u <dockerhub_username> [-t <tag>] [--update-k8s]
# Example:
#   ./commands/push-images.sh -u zhihengyang -t 3.2 --update-k8s

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

DOCKERHUB_USER=""
IMAGE_TAG="3.2"
UPDATE_K8S="false"

usage() {
  cat <<'EOF'
Usage:
  ./commands/push-images.sh -u <dockerhub_username> [-t <tag>] [--update-k8s]

Options:
  -u, --user         Docker Hub username (required)
  -t, --tag          Image tag (default: 3.2)
      --update-k8s   Replace image lines in k8s deployment YAMLs
  -h, --help         Show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -u|--user)
      DOCKERHUB_USER="${2:-}"
      shift 2
      ;;
    -t|--tag)
      IMAGE_TAG="${2:-}"
      shift 2
      ;;
    --update-k8s)
      UPDATE_K8S="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ -z "${DOCKERHUB_USER}" ]]; then
  echo "Error: Docker Hub username is required." >&2
  usage
  exit 1
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "Error: docker is not installed or not in PATH." >&2
  exit 1
fi

if ! docker info >/dev/null 2>&1; then
  echo "Error: docker daemon is not running or not reachable." >&2
  exit 1
fi

# Web-based Docker login may not expose "Username" in `docker info`.
# Do not hard-fail here; `docker push` will return an auth error if login is missing.
if ! docker info 2>/dev/null | grep -q '^ Username:'; then
  echo "Warning: could not confirm Docker Hub login from docker info output."
  echo "Continuing anyway; push step will fail if authentication is missing."
fi

AUTH_IMAGE="${DOCKERHUB_USER}/auth-service:${IMAGE_TAG}"
SHORTENER_IMAGE="${DOCKERHUB_USER}/shortener-service:${IMAGE_TAG}"

echo "Building ${AUTH_IMAGE}"
docker build -t "${AUTH_IMAGE}" "${REPO_ROOT}/auth_service"

echo "Building ${SHORTENER_IMAGE}"
docker build -t "${SHORTENER_IMAGE}" "${REPO_ROOT}/shortener_service"

echo "Pushing ${AUTH_IMAGE}"
docker push "${AUTH_IMAGE}"

echo "Pushing ${SHORTENER_IMAGE}"
docker push "${SHORTENER_IMAGE}"

if [[ "${UPDATE_K8S}" == "true" ]]; then
  AUTH_DEPLOY="${REPO_ROOT}/k8s/auth-deployment.yaml"
  SHORTENER_DEPLOY="${REPO_ROOT}/k8s/shortener-deployment.yaml"
  sed -i.bak -E "s|image: .*/auth-service:[^[:space:]]+|image: ${AUTH_IMAGE}|" "${AUTH_DEPLOY}"
  sed -i.bak -E "s|image: .*/shortener-service:[^[:space:]]+|image: ${SHORTENER_IMAGE}|" "${SHORTENER_DEPLOY}"
  rm -f "${AUTH_DEPLOY}.bak" "${SHORTENER_DEPLOY}.bak"
  echo "Updated image tags in k8s deployment files."
fi

echo
echo "Done."
echo "Auth image:      ${AUTH_IMAGE}"
echo "Shortener image: ${SHORTENER_IMAGE}"
