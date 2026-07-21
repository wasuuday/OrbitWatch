import requests
from utils.config import N2YO_API_KEY, N2YO_BASE_URL, TRACKED_OBJECTS

def get_satellite_position(norad_id, lat=0, lng=0, alt=0):
    """Get current position + basic telemetry for a satellite."""
    url = f"{N2YO_BASE_URL}/positions/{norad_id}/{lat}/{lng}/{alt}/1/"
    params = {"apiKey": N2YO_API_KEY}
    try:
        resp = requests.get(url, params=params, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        if "positions" not in data or not data["positions"]:
            return None
        pos = data["positions"][0]
        info = data.get("info", {})
        return {
            "name": info.get("satname", "Unknown"),
            "norad_id": info.get("satid", norad_id),
            "lat": pos.get("satlatitude"),
            "lng": pos.get("satlongitude"),
            "altitude_km": round(pos.get("sataltitude", 0), 1),
            "azimuth": pos.get("azimuth"),
            "elevation": pos.get("elevation"),
            "timestamp": pos.get("timestamp"),
        }
    except requests.exceptions.RequestException:
        return None


def get_visual_passes(norad_id, lat, lng, alt=0, days=10, min_visibility=300):
    """Get upcoming visible passes for a satellite over a given location."""
    url = f"{N2YO_BASE_URL}/visualpasses/{norad_id}/{lat}/{lng}/{alt}/{days}/{min_visibility}/"
    params = {"apiKey": N2YO_API_KEY}
    try:
        resp = requests.get(url, params=params, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        return data.get("passes", [])
    except requests.exceptions.RequestException:
        return []


def get_tle(norad_id):
    """Get raw TLE data for a satellite (useful for orbit period calc)."""
    url = f"{N2YO_BASE_URL}/tle/{norad_id}/"
    params = {"apiKey": N2YO_API_KEY}
    try:
        resp = requests.get(url, params=params, timeout=8)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException:
        return None


def list_tracked_objects():
    return TRACKED_OBJECTS