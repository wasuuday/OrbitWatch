import textwrap
import streamlit as st
from utils.location import (
    init_location_state,
    set_location_granted,
    set_location_mystery,
    request_browser_location,
)

def render_location_gate():
    """
    Shows the custom permission card BEFORE the real browser prompt fires.
    Returns True once we have a resolved status (granted/mystery/denied),
    False if still waiting on the user's choice.
    """
    init_location_state()
    status = st.session_state.location_status

    if status == "unset":
        st.markdown(textwrap.dedent("""
        <div class="ow-card">
            <div class="ow-card-label">📍 Sky Above You</div>
            <div style="font-size:15px; font-weight:700; color:#111827; margin-bottom:10px;">
                Want a more accurate mission?
            </div>
            <div style="font-size:13.5px; color:#374151; line-height:1.7;">
                If you let OrbitWatch know roughly where you are, it can tell you things like:
                <br>• how far the ISS is from you
                <br>• when it'll pass overhead
                <br>• which direction to look
                <br><br>
                Don't worry. I'm not coming over for dinner.
                <br>I just need a tiny patch of Earth to point at.
            </div>
        </div>
        """), unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔭 Sounds good", use_container_width=True, type="primary"):
                st.session_state.location_status = "asked"
                st.session_state._geo_attempts = 0
                st.rerun()
        with c2:
            if st.button("🕶️ I'd rather stay mysterious", use_container_width=True):
                set_location_mystery()
                st.rerun()
        return False

    if status == "asked":
        coords = request_browser_location()

        if coords:
            set_location_granted(coords)
            st.markdown(textwrap.dedent("""
            <div class="ow-mission-note">
                <div class="ow-mission-note-label">📍 Signal Locked</div>
                Mission Control now knows roughly which bit of Earth you're standing on.
                <br><br>No addresses. No doorbells. No surprise visits.
            </div>
            """), unsafe_allow_html=True)
            return True

        # Not resolved yet — give the browser a few reruns before giving up.
        attempts = st.session_state.get("_geo_attempts", 0)
        if attempts < 4:
            st.session_state._geo_attempts = attempts + 1
            st.markdown(textwrap.dedent("""
            <div class="ow-mission-note">
                Waiting for your approval...
            </div>
            """), unsafe_allow_html=True)
            st.rerun()
        else:
            st.session_state.location_status = "denied"
            st.rerun()
        return False

    if status == "mystery":
        st.markdown(textwrap.dedent("""
        <div class="ow-mission-note">
            🕶️ Staying mysterious. Fair enough.
            <br><br>Mission Control will pretend you're somewhere vaguely on Earth.
            Honestly, that's where most astronauts start too.
        </div>
        """), unsafe_allow_html=True)
        return True

    if status == "denied":
        st.markdown(textwrap.dedent("""
        <div class="ow-mission-note">
            Looks like your browser didn't confirm a location in time.
            <br><br>Privacy level: maximum. Even the satellites are guessing now.
        </div>
        """), unsafe_allow_html=True)
        if st.button("Try again", use_container_width=True):
            st.session_state.location_status = "asked"
            st.session_state._geo_attempts = 0
            st.rerun()
        return True

    if status == "granted":
        return True

    return True