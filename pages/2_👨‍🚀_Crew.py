import random

import streamlit as st
import time
from utils.styles import load_css
from components.hero import render_header
from components.cards import info_card, big_number_card


st.set_page_config(
    page_title="Crew · OrbitWatch",
    page_icon="👨‍🚀",
    layout="centered",
)

load_css()
render_header(status_text="Crew Manifest")

st.markdown("### 👨‍🚀 Humans Currently Off the Planet")

# ---------------------------------------------------
# Personality
# ---------------------------------------------------
ROASTS = [
    "{} has spent hundreds of days in space. You spent three hours yesterday deciding what to watch on Netflix.",
    "{} is travelling at 27,600 km/h. You're still travelling between your bed and your desk.",
    "{} passed astronaut training. You once failed a CAPTCHA.",
    "{} has a better office view than 8 billion people. Your office plant is still judging you.",
    "{} has seen Earth from orbit. You still need Google Maps in your own city.",
    "{} works where gravity is optional. You still struggle getting out of bed.",
    "{} floated through today's work. You sat through three meetings that could've been emails.",
    "{} is conducting experiments in space. Your biggest experiment today was mixing coffee brands.",
    "{} gets paid to look at Earth. You pay to skip ads.",
    "{} has completed more orbits today than you've completed tasks.",
    "{} can literally say they're above all the drama. You still read YouTube comments.",
    "{} has touched the stars. You touched the snooze button five times.",
    "{} trained for years to get here. You watched two motivational reels and called it self-improvement.",
    "{} has a mission patch. You have 47 browser tabs open.",
    "{} has seen sixteen sunrises today. You almost missed your first one.",
    "{} left Earth. You still haven't left your comfort zone.",
    "{} is living every space nerd's dream. You're reading jokes inside a space app.",
    "{} is making history. You're making another cup of tea.",
    "{} knows how to dock a spacecraft. You still can't fold a fitted bedsheet.",
    "{} made it to space. You made it to this page.",
    "{} has been through astronaut training. You still skip software updates.",
    "{} is travelling at 27,600 km/h. You're still buffering.",
    "{} is doing science in orbit. You're doing 'just one more episode.'",
    "{} has a space suit. You have yesterday's hoodie.",
    "{} has seen Earth from above. You struggle to find your socks.",
    "{} trained for years. You watched one YouTube Short and felt inspired.",
    "{} is literally above all the drama. You're reading roast messages.",
    "{} is floating. Your motivation isn't.",
    "{} didn't become an astronaut by hitting snooze.",
    "{} is exploring the universe. You're exploring the fridge.",
    "{} has an international space mission. You have 37 unread emails.",
    "{} is orbiting Earth. You're orbiting procrastination.",
    "{} proved hard work pays off. You're still waiting for luck.",
    "{} has a mission patch. You have browser tabs.",
    "{} is closer to the stars than your life goals.",
    "{} made NASA proud. Your calculator app is proud of you too.",
    "If you'd paid attention in physics class, {}'s job could've been your LinkedIn profile.",
    "Meanwhile, your biggest achievement today was remembering your password. {} orbited Earth 16 times.",
    "{} is orbiting Earth. You're orbiting the fridge.",
    "{} trained for years. You watched one space documentary and called it research.",
    "{} is up there right now. You're refreshing this page.",
    "{}'s office has zero gravity. Yours has zero motivation.",
    "Imagine explaining to your parents that you became an astronaut instead of 'good at Excel,' like {} did.",
    "This could've been you... but you chose 'Skip Ad' over 'Study'. {} chose neither.",
    "{} is travelling at 27,600 km/h. You're still deciding what to watch tonight.",
    "{}'s morning commute is one orbit around Earth. Yours is finding your phone charger.",
    "NASA called. They were looking for someone else, not you. They found {}.",
    "The closest you've been to space is turning off airplane mode. {} lives there.",
    "{} is making history. You're making instant noodles.",
    "{} survived astronaut training. You complain when the Wi-Fi is slow.",
    "{}'s job description includes spacewalks. Yours includes 'Reply All' accidents.",
    "One small step for {}. One giant procrastination streak for you.",
    "{} is floating in orbit. You're sinking into your chair.",
    "Mission Control knows exactly where {} is. Your parents still ask what you actually do.",
    "If dreams had deadlines, this would've been awkward. {} hit theirs.",
    "The stars were within reach for {}. For you, then came Instagram Reels.",
    "Imagine being this close to greatness... by opening this app, while {} is actually up there.",
    "{} is looking down at Earth. You're looking up how to boil pasta.",
    "{} left the planet. You still haven't left your comfort zone.",
    "The only launch today was your food delivery app. {} launched into orbit.",
    "{} wears a space suit. You wear yesterday's hoodie.",
    "{} is conducting science in orbit. You're conducting quality assurance on memes.",
]

FOOTER_NOTES = [
    "They're orbiting Earth. You're orbiting your deadlines.",
    "They've watched around sixteen sunrises today. You probably snoozed through one.",
    "Some people dream of space. These people forgot where they parked Earth.",
    "The view is spectacular. The commute home is slightly inconvenient.",
    "Meanwhile, gravity continues to overachieve down here.",
    "Some meetings really could have been emails. These ones happen in orbit.",
]
PROFILE_TYPES = [

    "mission",

    "fact",

    "telemetry",

    "achievement",

    "comparison",

    "orbitlog",

    "briefing",

    "ground",

    "field",

]
MISSION_STATUS = [

    "Conducting orbital research.",

    "Keeping humanity slightly above average.",

    "Doing actual rocket science.",

    "Probably enjoying the best office view on Earth.",

    "Busy making gravity look optional.",

    "Currently travelling faster than your Monday.",

    "Science in progress. Please do not disturb.",

    "Floating with professional confidence.",

]

TODAY_FACTS = [

    "This crew will witness around sixteen sunrises today.",

    "Every orbit takes roughly ninety minutes.",

    "The station travels close to 28,000 km/h.",

    "Everything on board is constantly falling around Earth.",

    "A normal workday includes seeing continents drift beneath you.",

    "Their commute circles an entire planet.",

]

TELEMETRY = [

    ("Crew Morale", "██████████"),

    ("Coffee Levels", "███████░░░"),

    ("Gravity", "Unavailable"),

    ("Orbit Stability", "Nominal"),

    ("Mission Status", "Operational"),

]
ACHIEVEMENTS = [

    "✓ Left Earth",

    "✓ Saw Earth from orbit",

    "✓ Floated in microgravity",

    "✓ Earned astronaut wings",

    "□ Replied to every email",

]
COMPARISONS = [

    ("Earth Meetings", "██████████", "ISS Meetings", "██░░░░░░░"),

    ("Traffic", "██████████", "Orbital Traffic", "█░░░░░░░░"),

    ("Coffee Refills", "████████", "Space Coffee", "█████░░░"),

]
ORBIT_LOG = [

    "Orbit 8 complete. Systems nominal.",

    "Crew continuing scheduled science operations.",

    "Earth still looking spectacular.",

    "Mission proceeding exactly as planned.",

]
GROUND_CONTROL = [

    "All systems responding normally.",

    "Mission Control reports everything is nominal.",

    "No anomalies detected.",

    "Communications link stable.",

]
FIELD_NOTES = [

    "Zero gravity never really gets old.",

    "Another ordinary day... in orbit.",

    "Today's office has excellent views.",

    "Somewhere below is your hometown.",

]


SECTION_TITLES = [
    "Mission Note",
    "Crew Update",
    "Telemetry",
    "Mission Control",
    "Status Report",
    "Orbit Log",
    "Daily Briefing",
    "Ground Control",
    "Field Notes",
]

ABSURD_NOTES = [
    "Mission Control confirms the Moon is still there. We checked.",
    "Gravity is currently unavailable on board. Expected behaviour.",
    "The astronauts have requested more snacks. Science continues.",
    "Ground Control has once again confirmed that space is, in fact, very big.",
    "No aliens have returned our emails today.",
    "Coffee levels aboard the station remain classified.",
    "The ISS is still refusing to accept parking reservations.",
    "Breaking News: Earth continues to orbit the Sun successfully.",
    "Nobody panic. Everything appears to be exactly where it should be.",
    "One rubber duck is statistically closer to space than expected.",
]
# Manually verified snapshot — last checked around July 23, 2026.
# Refresh this occasionally by checking NASA's ISS blog and Wikipedia's
# "Expedition" / "Tiangong space station" pages for the current crew.
CURRENT_CREW = [
    {"craft": "ISS", "name": "Jessica Meir"},
    {"craft": "ISS", "name": "Jack Hathaway"},
    {"craft": "ISS", "name": "Sophie Adenot"},
    {"craft": "ISS", "name": "Andrey Fedyaev"},
    {"craft": "ISS", "name": "Pyotr Dubrov"},
    {"craft": "ISS", "name": "Anna Kikina"},
    {"craft": "ISS", "name": "Anil Menon"},
    {"craft": "Tiangong", "name": "Zhu Yangzhu"},
    {"craft": "Tiangong", "name": "Zhang Zhiyuan"},
    {"craft": "Tiangong", "name": "Lai Ka-ying"},
]

CREW_NOTE = (
    "This list was last verified by an actual human checking actual sources. "
    "By the time you're reading this, a couple of these folks might already be back on Earth, "
    "sipping tea and re-learning what gravity feels like. Crew rotations happen every few months — "
    "consider this 'recently true' rather than 'true this second.'"
)

import hashlib


def profile_for(name):

    profiles = PROFILE_TYPES

    idx = int(
        hashlib.md5(name.encode()).hexdigest(),
        16,
    )

    return profiles[idx % len(profiles)]
def visible_panel(profile):

    if profile == "mission":

        return (
            "MISSION CONTROL",
            f"""
<b>Status</b><br>
{random.choice(MISSION_STATUS)}
""",
        )

    if profile == "fact":

        return (
            "TODAY'S FACT",
            random.choice(TODAY_FACTS),
        )

    if profile == "telemetry":

        rows = ""

        for k, v in TELEMETRY:

            rows += f"<b>{k}</b><br>{v}<br><br>"

        return ("TELEMETRY", rows)

    if profile == "achievement":

        return (
            "UNLOCKED",
            "<br>".join(ACHIEVEMENTS),
        )

    if profile == "comparison":

        c = random.choice(COMPARISONS)

        return (
            "EARTH vs ORBIT",
            f"""
<b>{c[0]}</b><br>
{c[1]}
<br><br>

<b>{c[2]}</b><br>
{c[3]}
""",
        )

    if profile == "orbitlog":

        return (
            "ORBIT LOG",
            random.choice(ORBIT_LOG),
        )

    if profile == "briefing":

        return (
            "DAILY BRIEFING",
            random.choice(TODAY_FACTS),
        )

    if profile == "ground":

        return (
            "GROUND CONTROL",
            random.choice(GROUND_CONTROL),
        )

    return (

        "FIELD NOTES",

        random.choice(FIELD_NOTES),

    )
# ---------------------------------------------------
# API
# ---------------------------------------------------

crew = CURRENT_CREW

st.markdown(
    f"""
<div class="ow-mission-note">
<div class="ow-mission-note-label">📋 Crew Manifest</div>

{CREW_NOTE}
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# Hero Card
# ---------------------------------------------------

big_number_card(
    "Humans in Space",
    len(crew),
    "people",
)

# ---------------------------------------------------
# Group By Spacecraft
# ---------------------------------------------------

by_craft = {}

for astronaut in crew:
    craft = astronaut.get("craft", "Unknown")
    by_craft.setdefault(craft, []).append(astronaut.get("name"))

# ---------------------------------------------------
# Crew Cards
# ---------------------------------------------------

import time
import hashlib
# ---------------------------------------------------
# Build stable crew profiles for this session
# ---------------------------------------------------

if "crew_profiles" not in st.session_state:
    st.session_state.crew_profiles = {}

def transmission():
    if random.random() < 0.10:
        return random.choice(ABSURD_NOTES)
    return random.choice(ROASTS)


def profile_for(name):
    profiles = PROFILE_TYPES
    idx = int(hashlib.md5(name.encode()).hexdigest(), 16)
    return profiles[idx % len(profiles)]


def visible_panel(profile):

    if profile == "mission":
        return (
            "🚀 Mission Control",
            random.choice(MISSION_STATUS),
        )

    if profile == "fact":
        return (
            "🌍 Today's Fact",
            random.choice(TODAY_FACTS),
        )

    if profile == "telemetry":

        body = f"""
<b>Crew Morale</b><br>██████████<br><br>
<b>Coffee Level</b><br>███████░░░<br><br>
<b>Gravity</b><br>Unavailable
"""
        return ("📡 Telemetry", body)

    if profile == "achievement":

        return (
            "🏆 Unlocked",
            """
✓ Left Earth<br>
✓ Saw Earth from Orbit<br>
✓ Floated in Microgravity<br>
□ Replied to Emails
""",
        )

    if profile == "comparison":

        return (
            "🌎 Earth vs Orbit",
            """
<b>Earth Meetings</b><br>
██████████

<br><br>

<b>ISS Meetings</b><br>
██░░░░░░░░
""",
        )

    if profile == "orbitlog":
        return (
            "🛰 Orbit Log",
            random.choice(ORBIT_LOG),
        )

    if profile == "briefing":
        return (
            "📋 Daily Briefing",
            random.choice(TODAY_FACTS),
        )

    if profile == "ground":
        return (
            "🎧 Ground Control",
            random.choice(GROUND_CONTROL),
        )

    return (
        "📝 Field Notes",
        random.choice(FIELD_NOTES),
    )

def get_profile(name):

    if name not in st.session_state.crew_profiles:

        profile = profile_for(name)

        heading, body = visible_panel(profile)

        roast = transmission()

        if "{}" in roast:
            roast = roast.format(name)

        st.session_state.crew_profiles[name] = {
            "heading": heading,
            "body": body,
            "roast": roast,
            "decoded": False,
        }

    return st.session_state.crew_profiles[name]


for craft, astronauts in by_craft.items():

    st.markdown(f"## 🛰 {craft}")

    for astronaut in astronauts:

        astronaut_profile = get_profile(astronaut)

        heading = astronaut_profile["heading"]

        body = astronaut_profile["body"]

        roast = astronaut_profile["roast"]

        with st.container(border=False):

            st.markdown(
                f"""
<div class="ow-card">

<div style="font-size:34px;">👨‍🚀</div>

<div style="font-size:23px;font-weight:700;margin-top:8px;">
{astronaut}
</div>

<div style="font-size:12px;
letter-spacing:2px;
text-transform:uppercase;
margin-top:18px;
color:#6B7280;">
Current Ride
</div>

<div style="font-size:16px;font-weight:600;margin-top:4px;">
{craft}
</div>

<hr style="margin:20px 0;border:none;border-top:1px solid #ECECEC;">

<div style="
font-size:12px;
letter-spacing:2px;
text-transform:uppercase;
color:#6B7280;
margin-bottom:10px;">
{heading}
</div>

<div style="
font-size:15px;
line-height:1.8;
color:#4B5563;
margin-bottom:18px;">
{body}
</div>
""",
                unsafe_allow_html=True,
            )



            if not astronaut_profile["decoded"]:
                key = astronaut.replace(" ", "_")

                if st.button(
                    "📡 Decode Transmission",
                    key=f"btn_{key}",
                    use_container_width=True,
                ):

                    placeholder = st.empty()

                    placeholder.info("Decrypting...")

                    time.sleep(0.35)

                    placeholder.success("Transmission received ✓")

                    time.sleep(0.25)

                    placeholder.empty()

                    astronaut_profile["decoded"] = True

                    st.rerun()

            elif astronaut_profile["decoded"]:

                st.markdown(
                    f"""
<div style="
background:#F8FAFC;
border-radius:14px;
padding:18px;
margin-top:12px;
">

<div style="
font-size:12px;
letter-spacing:2px;
text-transform:uppercase;
color:#6B7280;
margin-bottom:10px;">
📡 Incoming Transmission
</div>

<div style="
font-size:15px;
line-height:1.8;
color:#374151;">
💬 {roast}
</div>

</div>
""",
                    unsafe_allow_html=True,
                )

            st.markdown("</div>", unsafe_allow_html=True)
# ---------------------------------------------------
# Bottom Mission Note
# ---------------------------------------------------

st.markdown(
    f"""
<div class="ow-mission-note">
{random.choice(FOOTER_NOTES)}
</div>
""",
    unsafe_allow_html=True,
)
