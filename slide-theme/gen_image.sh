#!/usr/bin/env bash
# gen_image.sh — generate an image for course slides via the image generation API.
#
# Usage:
#   ./gen_image.sh <output.png> <size, e.g. 1024x512> <seed> <<'EOF'
#   your prompt here
#   EOF
#
# Or with a prompt file:
#   ./gen_image.sh assets/hero.png 1024x512 42 prompt.txt
#
# Style guardrails (see session-creation-guide.md §9.3):
#   - prompts MUST include the course art-style keywords so all 32 sessions
#     share one visual identity:
#     "kid-friendly flat illustration, deep indigo background, neon cyan and
#     pink accents, soft glow, clean vector shapes, no text"
#   - always pin a seed for reproducibility; record seed + prompt next to the
#     image in images-manifest.md
set -e
OUT="$1"; SIZE="${2:-1024x512}"; SEED="${3:-42}"
if [ "$4" ]; then PROMPT="$(cat "$4")"; else PROMPT="$(cat)"; fi

[ -z "$PROMPT" ] && { echo "ERROR: empty prompt" >&2; exit 1; }

curl -s --max-time 180 http://192.168.1.153:30083/v1/images/generations \
  -H 'Content-Type: application/json' \
  -d "$(python3 - "$PROMPT" "$SIZE" "$SEED" <<'PYEOF'
import json, sys
print(json.dumps({
    "model": "flux2-dev",
    "prompt": sys.argv[1],
    "size": sys.argv[2],
    "num_inference_steps": 14,
    "guidance_scale": 4.0,
    "seed": int(sys.argv[3]),
    "response_format": "b64_json",
}))
PYEOF
)" | python3 -c "
import sys, json, base64
d = json.load(sys.stdin)
img = base64.b64decode(d['data'][0]['b64_json'])
open('$OUT','wb').write(img)
print('wrote $OUT (' + str(len(img)) + ' bytes)')
"
