#!/bin/bash
# Display faces for the Pinnacle thumbnail system. All SIL Open Font License 1.1
# (Archivo Black, Archivo, Anton, Inter) — fetched rather than vendored so the
# licences stay with upstream.
set -e
cd "$(dirname "$0")"
mkdir -p fonts
base="https://fonts.gstatic.com/s"
curl -sSLf -o fonts/ArchivoBlack.ttf "$base/archivoblack/v21/HTxqL289NzCGg4MzN6KJ7eW6OYuP_x7yx3A.ttf"
curl -sSLf -o fonts/Anton.ttf        "$base/anton/v27/1Ptgg87LROyAm0K0.ttf"
curl -sSLf -o fonts/Archivo900.ttf   "$base/archivo/v25/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTnTRp8A.ttf"
curl -sSLf -o fonts/Inter900.ttf     "$base/inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuFuYMZg.ttf"
echo "fonts ready:"; ls -1 fonts
