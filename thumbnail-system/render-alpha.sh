#!/bin/bash
# Render graphics layers to transparent PNG at 1920x1080 for compositing.
# --default-background-color=00000000 is what makes the backdrop transparent;
# device-scale 1.5 takes the 1280x720 layout up to 1920x1080.
set -e
cd "$(dirname "$0")"
for f in "$@"; do
  n="${f%.html}"
  /opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
    --hide-scrollbars --force-device-scale-factor=1.5 --window-size=1280,900 \
    --default-background-color=00000000 \
    --screenshot="$n.raw.png" "$f" 2>/dev/null | tail -0
  python3 -c "
from PIL import Image
im=Image.open('$n.raw.png').convert('RGBA').crop((0,0,1920,1080))
im.save('$n.png')
a=im.getchannel('A')
print('$n.png', im.size, 'opaque px %.1f%%' % (100*sum(1 for p in a.getdata() if p>250)/(im.width*im.height)))"
  rm -f "$n.raw.png"
done
