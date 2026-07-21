import streamlit as st
from streamlit_js_eval import get_geolocation

def request_browser_location():
    """
    Triggers the browser geolocation prompt and returns
    {'lat': .., 'lng': ..} or None if denied/unavailable.
    """
    loc = get_geolocation()
    if loc and "coords" in loc:
        return {
            "lat": loc["coords"]["latitude"],
            "lng": loc["coords"]["longitude"],
        }
    return None


def init_location_state():
    if "location_status" not in st.session_state:
        # values: "unset" | "asked" | "granted" | "denied" | "mystery"
        st.session_state.location_status = "unset"
    if "user_location" not in st.session_state:
        st.session_state.user_location = None


def set_location_granted(coords):
    st.session_state.user_location = coords
    st.session_state.location_status = "granted"


def set_location_mystery():
    st.session_state.location_status = "mystery"
    st.session_state.user_location = None


def set_location_denied():
    st.session_state.location_status = "denied"
    st.session_state.user_location = None

import requests

def reverse_geocode(lat, lng):
    """
    Free reverse geocoding, no API key required.
    Returns a short human-readable label like 'Pune, Maharashtra, India'.
    """
    try:
        resp = requests.get(
            "https://api.bigdatacloud.net/data/reverse-geocode-client",
            params={"latitude": lat, "longitude": lng, "localityLanguage": "en"},
            timeout=6,
        )
        resp.raise_for_status()
        data = resp.json()
        city = data.get("city") or data.get("locality") or ""
        region = data.get("principalSubdivision", "")
        country = data.get("countryName", "")
        parts = [p for p in [city, region, country] if p]
        return ", ".join(parts) if parts else None
    except requests.exceptions.RequestException:
        return None