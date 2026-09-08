#!/bin/bash
# Render 1280x720 exactly: oversize the window, then crop. Chromium's headless
# viewport comes up short of the requested height, leaving a white band.
set -e
cd "$(dirname "$0")"
for f in "$@"; do
  n="${f%.html}"
  /opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
    --hide-scrollbars --force-device-scale-factor=1 --window-size=1280,900 \
    --screenshot="$n.raw.png" "$f" 2>/dev/null | tail -0
  python3 -c "
from PIL import Image
im=Image.open('$n.raw.png').convert('RGB').crop((0,0,1280,720))
im.save('$n.png'); print('$n.png',im.size)"
  rm -f "$n.raw.png"
done
