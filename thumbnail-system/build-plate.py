"""Turn a frame from the episode into the 1280x720 thumbnail background.

Pan/scans the 16:9 frame so Aaron sits left-of-centre — the blocking every
live thumbnail on the channel uses — then grades the rough footage: the
ungraded frame is too flat for white type to hold against the cream wall.
"""
import sys
import cv2
import numpy as np

SRC = sys.argv[1] if len(sys.argv) > 1 else "frame.png"
W, X0, Y0 = 1400, 520, 0          # Y0=0: his hair sits high, so headroom is tight

src = cv2.imread(SRC)
H = round(W * 9 / 16)
plate = cv2.resize(src[Y0:Y0 + H, X0:X0 + W], (1280, 720), interpolation=cv2.INTER_AREA)

lab = cv2.cvtColor(plate, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
l = cv2.createCLAHE(clipLimit=1.1, tileGridSize=(8, 8)).apply(l)

# Match the channel's airy look. The live thumbnails sit well off black, and a
# straight CLAHE pass leaves shadows too deep — which reads as "too dark" even
# when mean brightness looks right. Calibrate the lift from this frame's own
# percentiles rather than hardcoding, so any frame lands in the same place.
# P90 targets 200, not the reference's measured 205: that figure is inflated by
# the big white headline baked into the reference, which the bare plate lacks.
SHADOW_TARGET, HIGHLIGHT_TARGET = 60.0, 200.0
p10, p90 = np.percentile(l, 10), np.percentile(l, 90)
slope = (HIGHLIGHT_TARGET - SHADOW_TARGET) / max(p90 - p10, 1e-6)
l = np.clip(l.astype(np.float32) * slope + (SHADOW_TARGET - slope * p10), 0, 255).astype(np.uint8)
plate = cv2.cvtColor(cv2.merge([l, a, b]), cv2.COLOR_LAB2BGR)

hsv = cv2.cvtColor(plate, cv2.COLOR_BGR2HSV).astype(np.float32)
hsv[:, :, 1] *= 1.10
plate = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR)

# Vignette only in the far corners. Anything stronger dims the right-hand type
# zone, which is the half that has to stay bright.
yy, xx = np.mgrid[0:720, 0:1280]
vignette = 1 - 0.07 * np.clip(((xx - 640) / 900) ** 4 + ((yy - 360) / 520) ** 4, 0, 1)
cv2.imwrite("plate-photo.png", np.clip(plate * vignette[:, :, None], 0, 255).astype(np.uint8))
print("wrote plate-photo.png")
