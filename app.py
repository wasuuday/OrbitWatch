import streamlit as st
from datetime import datetime
from utils.styles import load_css
from utils.config import TRACKED_OBJECTS
from utils.n2yo import get_satellite_position
from components.hero import render_header
from components.cards import big_number_card
from components.terminal import play_boot_terminal
from components.location_card import render_location_gate

st.set_page_config(
    page_title="OrbitWatch",
    page_icon="🛰️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

load_css()
render_header()

# --- Boot terminal (only once per session) ---
if "booted" not in st.session_state:
    play_boot_terminal()
    st.session_state.booted = True

# --- Live telemetry for ISS (default mission object) ---
iss = get_satellite_position(TRACKED_OBJECTS["ISS"])

if iss:
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:8px; margin: 4px 0 18px 2px;">
        <span class="ow-status-dot"></span>
        <span style="font-size:13px; font-weight:600; color:#111827;">ISS · Live</span>
        <span style="font-size:12px; color:#9CA3AF; margin-left:auto;">
            {datetime.utcnow().strftime('%H:%M:%S')} UTC
        </span>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        big_number_card("Altitude", iss["altitude_km"], "km")
    with c2:
        big_number_card("Speed", "27,600", "km/h")

    c3, c4 = st.columns(2)
    with c3:
        big_number_card("Latitude", round(iss["lat"], 1), "°")
    with c4:
        big_number_card("Longitude", round(iss["lng"], 1), "°")
else:
    st.markdown("""
    <div class="ow-mission-note">
        Telemetry is taking a moment. Mission Control is politely asking the satellite to speak up.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)

# --- Location gate: primes user_location for the Tracker page ---
render_location_gate()

st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

# --- CTA to full tracker ---
st.markdown("""
<div class="ow-card" style="text-align:center; padding: 20px;">
    <div style="font-size:14px; color:#374151; margin-bottom: 12px;">
        Want to see when the ISS passes over you, or track other objects like Hubble and Tiangong?
    </div>
</div>
""", unsafe_allow_html=True)

if st.button("🛰️ Open Tracker", use_container_width=True, type="primary"):
    st.switch_page("pages/1_🛰_Tracker.py")

st.markdown("""
<div class="ow-footer-tag">
    Built with real orbital data · not affiliated with NASA or your local astronaut
</div>
""", unsafe_allow_html=True)