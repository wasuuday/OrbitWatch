import os
from dotenv import load_dotenv

load_dotenv()

N2YO_API_KEY = os.getenv("N2YO_API_KEY", "")
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

N2YO_BASE_URL = "https://api.n2yo.com/rest/v1/satellite"
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"

# NORAD IDs for trackable objects
TRACKED_OBJECTS = {
    "ISS": 25544,
    "Hubble": 20580,
    "Tiangong": 48274,
    "NOAA 15": 25338,
    "GPS IIR-2": 24876,
}

COLORS = {
    "background": "#F8F8F6",
    "surface": "#FFFFFF",
    "primary": "#111827",
    "accent": "#4F46E5",
    "success": "#16A34A",
    "muted": "#6B7280",
    "danger": "#EF4444",
}

SPACECRAFT_INFO = {
    "ISS": {
        "description": "A habitable space station in low Earth orbit, jointly run by NASA, Roscosmos, ESA, JAXA, and CSA. Continuously crewed since November 2000.",
        "launched": "1998",
        "type": "Space Station",
        "operator": "NASA / Roscosmos / ESA / JAXA / CSA",
    },
    "Hubble": {
        "description": "A space telescope launched aboard the Space Shuttle Discovery, still capturing deep-space imagery decades later.",
        "launched": "1990",
        "type": "Space Telescope",
        "operator": "NASA / ESA",
    },
    "Tiangong": {
        "description": "China's modular space station, operational since 2021, crewed on a rotating basis by Chinese astronauts (taikonauts).",
        "launched": "2021",
        "type": "Space Station",
        "operator": "CNSA",
    },
    "NOAA 15": {
        "description": "A polar-orbiting weather satellite used for atmospheric and sea-surface monitoring.",
        "launched": "1998",
        "type": "Weather Satellite",
        "operator": "NOAA",
    },
    "GPS IIR-2": {
        "description": "Part of the GPS satellite constellation providing global positioning and timing signals.",
        "launched": "1997",
        "type": "Navigation Satellite",
        "operator": "US Space Force",
    },
}