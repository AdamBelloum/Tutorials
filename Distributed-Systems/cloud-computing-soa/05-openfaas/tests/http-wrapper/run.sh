#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  printf 'Usage: %s /absolute/path/to/node22.sif\n' "$0" >&2
  exit 2
fi

command -v apptainer >/dev/null
image="$(realpath -- "$1")"
test -f "$image"

here="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
module="$(cd -- "$here/../.." && pwd)"

# Apptainer bind syntax cannot safely represent these path characters.
case "$image$here${TMPDIR:-/tmp}" in
  *:*|*,*)
    printf 'STOP: Paths must not contain colons or commas.\n' >&2
    exit 1
    ;;
esac

work="$(mktemp -d "${TMPDIR:-/tmp}/openfaas-wrapper.XXXXXX")"
trap 'rm -rf -- "$work"' EXIT

for file in index.js package.json package-lock.json probe.cjs LICENSE; do
  cp -- "$here/$file" "$work/"
done
mkdir "$work/function"
cp -- "$module/examples/greeting/handler.js" "$work/function/handler.js"

printf '\n--- Test runtime ---\n'
apptainer --version
sha256sum "$image"
apptainer exec --cleanenv --containall --no-home --pwd /work \
  --bind "$work:/work:ro" "$image" node -e '
console.log(process.version, process.platform, process.arch);
if (process.version !== "v22.23.3" ||
    process.platform !== "linux" || process.arch !== "x64") {
  console.error("STOP: Runtime differs from the recorded reference.");
  process.exit(1);
}
'

printf '\n--- Install locked wrapper dependencies ---\n'
apptainer exec --cleanenv --containall --no-home --pwd /work \
  --bind "$work:/work" "$image" npm ci \
  --ignore-scripts --no-audit --no-fund --cache /work/.npm-cache

for mode in development production; do
  printf '\n--- HTTP-wrapper probe: NODE_ENV=%s ---\n' "$mode"
  apptainer exec --cleanenv --containall --no-home --pwd /work \
    --env "NODE_ENV=$mode" \
    --bind "$work:/work:ro" "$image" node /work/probe.cjs
done
