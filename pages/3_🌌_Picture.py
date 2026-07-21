import streamlit as st

from utils.styles import load_css
from utils.nasa import get_apod
from components.hero import render_header

st.set_page_config(
    page_title="Picture · OrbitWatch",
    page_icon="🌌",
    layout="centered",
)

load_css()

render_header(status_text="Daily transmission")

st.markdown("## 🌌 Picture of the Day")

try:

    apod = get_apod()

except Exception as e:

    st.error(f"NASA API Error\n\n{e}")

    st.stop()

# --------------------------
# IMAGE
# --------------------------

if apod["media_type"] == "image":

    st.image(
        apod["url"],
        use_container_width=True,
    )

elif apod["media_type"] == "video":

    st.video(apod["url"])

else:

    st.warning("NASA returned an unsupported media type.")

# --------------------------
# DETAILS
# --------------------------

st.markdown(
    f"""
<div class="ow-card">

<div class="ow-card-label">
{apod['date']}
</div>

<div style="font-size:26px;
font-weight:700;
margin-top:6px;
margin-bottom:18px;">

{apod['title']}

</div>

<div style="font-size:15px;
line-height:1.9;
color:#4B5563;">

{apod['explanation']}

<br><br>

<hr style="border:none;border-top:1px solid #E5E7EB;margin:24px 0;">

<span style="font-size:13px;color:#9CA3AF;">

You made it all the way down here.

Whether you understood every word is now strictly between you and astrophysics.

</span>

</div>

</div>
""",
    unsafe_allow_html=True,
)

if apod.get("copyright"):

    st.caption(f"© {apod['copyright']}")