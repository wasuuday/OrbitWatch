import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timezone, timedelta
from utils.styles import load_css
from utils.config import TRACKED_OBJECTS, SPACECRAFT_INFO
from utils.n2yo import get_satellite_position, get_visual_passes
from utils.location import reverse_geocode
from components.hero import render_header
from components.cards import big_number_card, info_card, sky_above_card, spacecraft_info_card
from components.location_card import render_location_gate

st.set_page_config(page_title="Tracker · OrbitWatch", page_icon="🛰️", layout="centered")

load_css()
render_header(status_text="Tracker online")

st.markdown("### Objects")

names = list(TRACKED_OBJECTS.keys())

if "selected_object" not in st.session_state:
    st.session_state.selected_object = "ISS"

selected = st.selectbox(
    "Tracking",
    names,
    index=names.index(st.session_state.selected_object),
    label_visibility="collapsed",
)
st.session_state.selected_object = selected

norad_id = TRACKED_OBJECTS[selected]
data = get_satellite_position(norad_id)

if not data:
    st.markdown("""
    <div class="ow-mission-note">
        Signal's a little quiet on this one right now. Try another object or check back shortly.
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# --- Live status badge ---
st.markdown(f"""
<div style="display:flex; align-items:center; gap:8px; margin: 4px 0 18px 2px;">
    <span class="ow-status-dot"></span>
    <span style="font-size:13px; font-weight:600; color:#111827;">{selected} · Live</span>
    <span style="font-size:12px; color:#9CA3AF; margin-left:auto;">
        {datetime.now(timezone.utc).astimezone(
    timezone(timedelta(hours=5, minutes=30))
).strftime('%I:%M:%S %p')} IST
    </span>
</div>
""", unsafe_allow_html=True)

# --- Telemetry cards ---
c1, c2 = st.columns(2)
with c1:
    big_number_card("Altitude", data["altitude_km"], "km")
with c2:
    big_number_card("Latitude", round(data["lat"], 2), "°")

c3, c4 = st.columns(2)
with c3:
    big_number_card("Longitude", round(data["lng"], 2), "°")
with c4:
    big_number_card("Elevation", round(data.get("elevation") or 0, 1), "°")

# --- Map ---
st.markdown("<div class='ow-card-label' style='margin: 8px 0 10px 4px;'>Live Position</div>", unsafe_allow_html=True)

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lon=[data["lng"]], lat=[data["lat"]],
    mode="markers",
    marker=dict(size=34, color="rgba(79,70,229,0.18)"),
    hoverinfo="skip", showlegend=False,
))

fig.add_trace(go.Scattergeo(
    lon=[data["lng"]], lat=[data["lat"]],
    mode="markers",
    marker=dict(size=13, color="#4F46E5", line=dict(width=2, color="#FFFFFF")),
    name=selected,
    hovertext=f"{selected}<br>{data['altitude_km']} km",
    hoverinfo="text",
))

fig.update_geos(
    projection_type="orthographic",
    showland=True, landcolor="#1F2937",
    showocean=True, oceancolor="#0B1120",
    showcountries=True, countrycolor="#374151",
    showcoastlines=False, bgcolor="rgba(0,0,0,0)",
    projection_rotation=dict(lon=data["lng"], lat=data["lat"]),
)

fig.update_layout(
    height=340, margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor="rgba(0,0,0,0)", showlegend=False,
)

st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# --- Spacecraft info ---
info = SPACECRAFT_INFO.get(selected)
if info:
    spacecraft_info_card(
        description=info["description"],
        facts=[
            ("Type", info["type"]),
            ("Launched", info["launched"]),
            ("Operator", info["operator"]),
        ],
    )

# --- Sky Above You (needs location) ---
st.markdown("<div class='ow-card-label' style='margin: 20px 0 10px 4px;'>Sky Above You</div>", unsafe_allow_html=True)

location_resolved = render_location_gate()

if location_resolved and st.session_state.get("user_location"):
    coords = st.session_state.user_location

    # Resolve + cache the human-readable place name once per session
    if "user_location_label" not in st.session_state:
        st.session_state.user_location_label = reverse_geocode(coords["lat"], coords["lng"])

    if st.session_state.user_location_label:
        st.markdown(f"""
        <div style="font-size:13px; color:#6B7280; margin: -4px 0 14px 2px;">
            📍 Showing sky data for <span style="color:#111827; font-weight:600;">{st.session_state.user_location_label}</span>
        </div>
        """, unsafe_allow_html=True)

    passes = get_visual_passes(norad_id, coords["lat"], coords["lng"])

    if passes:
        next_pass = passes[0]
        ist = timezone(timedelta(hours=5, minutes=30))

        start_time = (
            datetime.fromtimestamp(next_pass["startUTC"], tz=timezone.utc)
            .astimezone(ist)
            .strftime("%b %d, %I:%M %p IST")
        )
        duration_min = round((next_pass["endUTC"] - next_pass["startUTC"]) / 60, 1)
        mag = next_pass.get("mag", None)
        brightness = "Very bright" if mag is not None and mag < 0 else \
                     "Bright" if mag is not None and mag < 2 else "Faint"

        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        start_az = next_pass.get("startAz", 0)
        direction = directions[round(start_az / 45) % 8]

        sky_above_card(
            sat_name=selected,
            distance_km=data["altitude_km"],
            pass_time=start_time,
            duration_min=duration_min,
            direction=direction,
            brightness=brightness,
        )
        st.markdown(f"""
        <div class="ow-mission-note">
            Step outside a couple minutes before {start_time.split(',')[1].strip()},
            look toward the {direction}, and {selected} should be visible for about {duration_min} minutes —
            weather permitting.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="ow-mission-note">
            No visible passes over your location in the next 10 days. It's up there, just not swinging by your sky right now.
        </div>
        """, unsafe_allow_html=True)
elif location_resolved:
    st.markdown("""
    <div class="ow-mission-note">
        Without a location, Mission Control can't tell you when to look up — but the satellite's still up there either way.
    </div>
    """, unsafe_allow_html=True)

# --- Object info ---
info_card(
    "Object Info",
    f"""<div style="font-size:14px; line-height:1.8; color:#374151;">
NORAD ID <span style="float:right; font-weight:600; color:#111827;">{data['norad_id']}</span><br>
Name <span style="float:right; font-weight:600; color:#111827;">{data['name']}</span>
</div>"""
)