"""Turn a frame from the episode into the 1280x720 thumbnail background.

Pan/scans the frame so Aaron sits left-of-centre — the blocking every live
thumbnail on the channel uses — then lifts the wall to the channel's bright,
airy level.

Grade note: anchor on the WHITE POINT, never on shadow percentiles. Episode 1
was shot in a cream shirt (p10=45); episode 2 in black (p10=2). A shadow-
anchored lift reads that wardrobe change as "the frame got darker" and washes
the black shirt out to grey. The wall lives in the upper percentiles, so p90
is the stable anchor across wardrobe.
"""
import sys
import cv2
import numpy as np

SRC = sys.argv[1] if len(sys.argv) > 1 else "frame.png"
OUT = sys.argv[2] if len(sys.argv) > 2 else "plate-photo.png"
W, X0, Y0 = (int(v) for v in (sys.argv[3:6] or (1400, 520, 0)))

HIGHLIGHT_TARGET = 204.0     # where the wall should land; the reference sits ~205

src = cv2.imread(SRC)
H = round(W * 9 / 16)
plate = cv2.resize(src[Y0:Y0 + H, X0:X0 + W], (1280, 720), interpolation=cv2.INTER_AREA)

lab = cv2.cvtColor(plate, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
l = cv2.createCLAHE(clipLimit=1.1, tileGridSize=(8, 8)).apply(l)

# Pull the white point down so the wall brightens; black point stays at 0 so a
# dark shirt stays dark instead of turning muddy grey.
white = np.percentile(l, 90) * (255.0 / HIGHLIGHT_TARGET)
l = np.clip(l.astype(np.float32) * (255.0 / white), 0, 255).astype(np.uint8)
plate = cv2.cvtColor(cv2.merge([l, a, b]), cv2.COLOR_LAB2BGR)

hsv = cv2.cvtColor(plate, cv2.COLOR_BGR2HSV).astype(np.float32)
hsv[:, :, 1] *= 1.08
plate = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR)

# No vignette. Two rounds of "too dark" traced back to it dimming the type side.
cv2.imwrite(OUT, plate)
l2 = cv2.cvtColor(plate, cv2.COLOR_BGR2LAB)[:, :, 0].astype(np.float32)
print(f"{OUT}  meanL={l2.mean():.1f} p10={np.percentile(l2,10):.1f} "
      f"p75={np.percentile(l2,75):.1f} p90={np.percentile(l2,90):.1f}")
