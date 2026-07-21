import textwrap
import streamlit as st

def big_number_card(label, value, unit=""):
    st.markdown(textwrap.dedent(f"""
    <div class="ow-card">
        <div class="ow-card-label">{label}</div>
        <div>
            <span class="ow-big-number">{value}</span>
            <span class="ow-big-number-unit">{unit}</span>
        </div>
    </div>
    """), unsafe_allow_html=True)


def info_card(label, body_html):
    """Generic card for anything that isn't a single big number."""
    # dedent the caller's body_html too, since callers pass indented f-strings
    clean_body = textwrap.dedent(body_html)
    st.markdown(textwrap.dedent(f"""
    <div class="ow-card">
        <div class="ow-card-label">{label}</div>
        {clean_body}
    </div>
    """), unsafe_allow_html=True)


def mission_note_card(text):
    st.markdown(textwrap.dedent(f"""
    <div class="ow-mission-note">
        <div class="ow-mission-note-label">Mission Note</div>
        {text}
    </div>
    """), unsafe_allow_html=True)


def alert_card(label, lines):
    lines_html = "<br>".join(lines)
    st.markdown(textwrap.dedent(f"""
    <div class="ow-alert">
        <div class="ow-alert-label">{label}</div>
        {lines_html}
    </div>
    """), unsafe_allow_html=True)


def sky_above_card(sat_name, distance_km, pass_time, duration_min, direction, brightness):
    st.markdown(textwrap.dedent(f"""
    <div class="ow-card">
        <div class="ow-card-label">Above You</div>
        <div class="ow-big-number" style="font-size: 32px;">{sat_name}</div>
        <div style="margin-top: 14px; line-height: 2;">
            <div style="color:#6B7280; font-size:13px;">Distance right now
                <span style="float:right; color:#111827; font-weight:600;">{distance_km} km</span>
            </div>
            <div style="color:#6B7280; font-size:13px;">Next visible pass
                <span style="float:right; color:#111827; font-weight:600;">{pass_time}</span>
            </div>
            <div style="color:#6B7280; font-size:13px;">Visible for
                <span style="float:right; color:#111827; font-weight:600;">{duration_min} min</span>
            </div>
            <div style="color:#6B7280; font-size:13px;">Direction
                <span style="float:right; color:#111827; font-weight:600;">{direction}</span>
            </div>
            <div style="color:#6B7280; font-size:13px;">Brightness
                <span style="float:right; color:#111827; font-weight:600;">{brightness}</span>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)


def spacecraft_info_card(description, facts):
    """facts: list of (label, value) tuples"""
    facts_html = "".join(
        f"""<div style="color:#6B7280; font-size:13px; margin-top:6px;">{label}
            <span style="float:right; color:#111827; font-weight:600;">{value}</span>
        </div>"""
        for label, value in facts
    )
    st.markdown(textwrap.dedent(f"""
    <div class="ow-card">
        <div class="ow-card-label">About This Object</div>
        <div style="font-size:14px; line-height:1.7; color:#374151; margin-bottom:10px;">
            {description}
        </div>
        {facts_html}
    </div>
    """), unsafe_allow_html=True)