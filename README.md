# 🛰 OrbitWatch

> **Live orbital activity. Beautifully presented. Occasionally sarcastic.**

OrbitWatch is a modern, mobile-first satellite tracking web application built with **Streamlit**, powered by **live space APIs**, and designed to make orbital data feel approachable rather than overwhelming.

Instead of looking like another API dashboard, OrbitWatch delivers a clean Mission Control experience with live telemetry, astronaut information, satellite tracking, and a touch of personality throughout.

---

## ✨ Features

### 🛰 Live Satellite Tracking

Track multiple satellites in real time including:

- International Space Station (ISS)
- Hubble Space Telescope
- Tiangong Space Station
- Additional satellites via N2YO

View:

- Live latitude & longitude
- Altitude
- Velocity
- Ground track
- Interactive world map

---

### 👨‍🚀 Astronaut Dashboard

See everyone currently living off the planet.

Each astronaut gets their own interactive mission card featuring:

- Current spacecraft
- Mission updates
- Telemetry panels
- Crew facts
- Hidden transmissions
- The occasional sarcastic comment

No two refreshes are exactly the same.

---

### 🌌 NASA Astronomy Picture of the Day

Every day OrbitWatch fetches NASA's Astronomy Picture of the Day along with its official description.

If you read the entire explanation...

...the app quietly judges your commitment.

---

### 📡 Mission Control Experience

OrbitWatch includes lots of small details that make it feel alive.

- Live mission status
- Fake terminal logs
- Rotating telemetry
- Mission notes
- Easter eggs
- Ambient humor
- Carefully crafted loading messages

The goal is personality—not distraction.

---

## 🎨 Design Philosophy

OrbitWatch was designed to feel closer to modern mobile applications than traditional dashboards.

Inspired by:

- 🍎 Apple Weather
- ✈️ Flighty
- ⚫ Nothing OS
- 🛰 Mission Control interfaces

Design principles:

- Typography first
- Minimal UI
- Spacious layouts
- Soft shadows
- Mobile-first responsiveness
- Personality through writing instead of flashy animations

---

## 🛠 Tech Stack

- Python
- Streamlit
- Plotly
- HTML/CSS
- Requests
- Python Dotenv

---

## 🌍 APIs Used

| API | Purpose |
|------|---------|
| NASA APOD | Astronomy Picture of the Day |
| Open Notify | Current astronauts in space |
| N2YO | Live satellite tracking |

---

## 📂 Project Structure

```text
orbitwatch/
│
├── app.py
├── pages/
│   ├── Home
│   ├── Live Tracker
│   ├── Crew
│   ├── Picture of the Day
│   └── About
│
├── components/
│
├── utils/
│
├── assets/
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🚀 Running Locally

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/orbitwatch.git
```

Move into the project

```bash
cd orbitwatch
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
NASA_API_KEY=YOUR_API_KEY
N2YO_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

> Add screenshots here after deployment.

Suggested:

- Home
- Live Tracker
- Astronaut Dashboard
- Picture of the Day
- Mobile View

---

## 🎯 Why I Built This

I wanted to explore public space APIs while building something that **didn't feel like another API demo**.

Most satellite trackers focus on displaying data.

OrbitWatch focuses on creating an experience.

It combines real-time orbital information with thoughtful UI, subtle animations, and a little humor to make space feel just a bit closer.

---

## 🤖 Fun Fact

The project started as:

> "A simple ISS tracker."

Several conversations later it somehow contained:

- encrypted astronaut transmissions
- fake Mission Control logs
- rotating telemetry
- easter eggs
- personality-driven UI
- and far more CSS than originally intended.

Apparently "just one more feature" isn't a measurable unit.

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/YOUR_USERNAME

If you enjoyed the project, consider giving it a ⭐.

---

## 📜 License

This project is licensed under the MIT License.
