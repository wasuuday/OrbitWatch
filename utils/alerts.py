import random

MISSION_ALERTS = [
    {
        "label": "ALERT",
        "lines": ["Large asteroid detected.", "Closest approach: 6.4 million km", "Threat level: you'll survive."],
    },
    {
        "label": "MISSION UPDATE",
        "lines": ["Moon status: still there.", "Carry on."],
    },
    {
        "label": "MISSION UPDATE",
        "lines": ["Solar activity: looking spicy today."],
    },
    {
        "label": "MISSION UPDATE",
        "lines": ["ISS is currently over the Pacific.", "Still refusing to wave."],
    },
    {
        "label": "STATUS",
        "lines": ["All 7 continents accounted for.", "Antarctica remains unbothered."],
    },
]

TERMINAL_LINE_SETS = [
    ["Initializing sensors...", "Connecting to NASA...", "Finding satellites...",
     "Ignoring Elon...", "Borrowing Hubble...", "Listening for tiny beeps...", "Signal locked."],
    ["Acquiring telemetry...", "Calculating orbital mechanics...", "Not panicking...",
     "Definitely not panicking...", "Pretending we understand relativity...",
     "Looking extremely professional...", "Signal locked."],
    ["Waking up the antenna...", "Coffee break...", "Coffee break continues...",
     "Fine, working now...", "Cross-referencing the stars...", "Signal locked."],
]

MISSION_NOTES = [
    "The ISS circles Earth every 90 minutes. Meanwhile you've probably had the same browser tab open since breakfast.",
    "Astronauts witness around sixteen sunrises each day, while you cant even see one",
    "The ISS travels at roughly 7.66 km/s. Your Wi-Fi, by comparison, is not doing great.",
    "There are currently people in space who don't have a single notification badge on their phone.",
    "Space is completely silent. Thankfully this app isn't.",
    "The ISS has traveled billions of kilometers since launch. Your package is somehow still 'out for delivery.'",
    "The crew aboard the ISS is orbiting Earth. You're orbiting your to-do list.",

]


def get_random_alert():
    return random.choice(MISSION_ALERTS)


def get_random_terminal_lines():
    return random.choice(TERMINAL_LINE_SETS)


def get_random_mission_note():
    return random.choice(MISSION_NOTES)