import streamlit as st
from utils.styles import load_css
from components.hero import render_header

st.set_page_config(
    page_title="About · OrbitWatch",
    page_icon="⚙",
    layout="centered",
)

load_css()
render_header(status_text="Mission Briefing")

st.markdown("## About OrbitWatch")

# ---------------------------------------------------------
# About
# ---------------------------------------------------------

st.markdown(
    """
<div class="ow-card">

<div class="ow-card-label">Mission</div>

<div style="font-size:14px; line-height:1.85; color:#374151;">

OrbitWatch is a modern satellite tracking experience built around live space
data. Instead of presenting raw telemetry, the goal is to make orbital
activity feel approachable, interactive and just a little bit fun.

From satellites passing overhead to astronauts currently in orbit,
everything you see here comes from real-world APIs updated in real time.

</div>

</div>

<div class="ow-card">

<div class="ow-card-label">Powered By</div>

<div style="font-size:14px; line-height:2; color:#374151;">

🛰 <b>N2YO</b>
<span style="float:right;color:#111827;">Satellite Tracking</span>

<br>

👨‍🚀 <b>Open Notify</b>
<span style="float:right;color:#111827;">Astronaut Manifest</span>

<br>

🌌 <b>NASA APOD</b>
<span style="float:right;color:#111827;">Astronomy Picture of the Day</span>

</div>

</div>

<div class="ow-card">

<div class="ow-card-label">Built With</div>

<div style="font-size:14px; line-height:1.9; color:#374151;">

Python • Streamlit • Plotly • HTML • CSS

<br><br>

Designed mobile-first with inspiration from Mission Control dashboards,
Apple Weather and modern minimal interfaces.

</div>

</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# ChatGPT Review
# ---------------------------------------------------------

st.markdown(
    """
<div class="ow-card">

<div class="ow-card-label">
🤖 ChatGPT's Internal Review
</div>

<div style="font-size:14px; line-height:1.85; color:#374151;">

"Spent several days integrating NASA, N2YO and orbital mechanics APIs...

...only to dedicate twice as much effort writing 70 different ways to call the user lazy.

Priorities appear to be functioning normally."

</div>

</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Developer
# ---------------------------------------------------------

st.markdown(
    """
<div class="ow-card">

<div class="ow-card-label">
Developer
</div>

<div style="font-size:14px; line-height:1.85; color:#374151;">

Built as a passion project exploring public space APIs,
modern UI design and interactive web experiences.

Every screen was handcrafted with the goal of making
space feel a little closer—and hopefully making you smile
once or twice along the way.



</div>

</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Privacy
# ---------------------------------------------------------

st.markdown(
    """
<div class="ow-mission-note">

No ads.

No tracking cookies.

No data sold.

No mysterious analytics following you around the internet.

<br><br>

The only thing being tracked here is a few satellites...
and they were already travelling at 28,000 km/h before this website existed.

</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown(
    """
<div class="ow-footer-tag">

Made with ☕, Python and an unreasonable amount of curiosity.

<br>

OrbitWatch · v1.0

<br><br>

<small style="color:#9CA3AF;">
P.S. The Moon is still there. We checked.
</small>

</div>
""",
    unsafe_allow_html=True,
)