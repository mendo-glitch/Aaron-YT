from plate import page, subject

# PROOF FRAME — validates the extracted system: badge pill + stacked caps headline
# + subject overlap. Headline copy is a placeholder until the script lands.
body = (
    subject(left=96)
    + '<div class="badge" style="left:640px;top:126px;">Retirement</div>'
    + '<div class="head" style="left:636px;top:196px;font-size:152px;">5<br>SIGNS</div>'
    + '<div class="bar" style="left:636px;top:494px;width:452px;height:22px;"></div>'
    + '<div class="head title-case" style="left:636px;top:512px;font-size:64px;'
      'letter-spacing:-.01em;">it’s time</div>'
)
open("proof.html", "w").write(page(body))
