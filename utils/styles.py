import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .stApp {
            background-color: #F8F8F6;
        }

 #MainMenu, footer { visibility: hidden; }

header {
    background: transparent;
}

header [data-testid="stHeader"] {
    background: transparent;
}

        .block-container {
            padding-top: 6rem;
            padding-bottom: 3rem;
            max-width: 480px;
        }

        /* Sticky glass header */
        .ow-header {
            position: sticky;
            top: 0;
            z-index: 999;
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            background: rgba(248, 248, 246, 0.72);
            padding: 20px 4px 16px 4px;
            margin: -1rem -1rem 20px -1rem;
            border-bottom: 1px solid rgba(0,0,0,0.04);
        }

        .ow-header-icon { font-size: 28px; margin-bottom: 4px; }

        .ow-header-title {
            font-size: 22px;
            font-weight: 800;
            color: #111827;
            letter-spacing: -0.02em;
            margin: 0;
        }

        .ow-header-sub {
            font-size: 13px;
            color: #6B7280;
            margin-top: 2px;
        }

        .ow-status-dot {
            display: inline-block;
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #16A34A;
            margin-right: 6px;
            box-shadow: 0 0 0 0 rgba(22,163,74, 0.6);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(22,163,74, 0.5); }
            70% { box-shadow: 0 0 0 8px rgba(22,163,74, 0); }
            100% { box-shadow: 0 0 0 0 rgba(22,163,74, 0); }
        }

        /* Card */
        .ow-card {
            background: #FFFFFF;
            border: none;
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .ow-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 50px rgba(0,0,0,0.08);
        }

        .ow-card-label {
            font-size: 12px;
            font-weight: 600;
            color: #6B7280;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 6px;
        }

        .ow-big-number {
            font-size: 52px;
            font-weight: 800;
            color: #111827;
            letter-spacing: -0.03em;
            line-height: 1;
        }

        .ow-big-number-unit {
            font-size: 18px;
            font-weight: 600;
            color: #6B7280;
            margin-left: 6px;
        }

        .ow-mission-note {
            background: #FFFFFF;
            border-radius: 20px;
            padding: 22px 24px;
            border-left: 3px solid #4F46E5;
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            margin-bottom: 16px;
            line-height: 1.7;
            color: #374151;
            font-size: 14px;
        }

        .ow-mission-note-label {
            font-size: 11px;
            font-weight: 700;
            color: #4F46E5;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 8px;
        }

        .ow-alert {
            background: #111827;
            color: #F8F8F6;
            border-radius: 18px;
            padding: 18px 22px;
            margin-bottom: 16px;
            font-size: 13px;
            line-height: 1.6;
        }

        .ow-alert-label {
            font-size: 11px;
            font-weight: 700;
            color: #9CA3AF;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 6px;
        }

        /* Terminal */
        .ow-terminal {
            background: #111827;
            border-radius: 16px;
            padding: 20px;
            font-family: 'SF Mono', 'Fira Code', monospace;
            font-size: 12.5px;
            color: #A3E635;
            line-height: 1.9;
            margin-bottom: 16px;
        }

        .ow-terminal .ok { color: #4ADE80; }
        .ow-terminal .dim { color: #6B7280; }

        /* Nav pills (radio as segmented control) */
        div[role="radiogroup"] {
            display: flex;
            gap: 6px;
            background: #EFEFEC;
            padding: 4px;
            border-radius: 14px;
            margin-bottom: 20px;
        }

        div[role="radiogroup"] label {
            flex: 1;
            text-align: center;
            border-radius: 10px;
            padding: 8px 0;
            margin: 0 !important;
            transition: all 0.2s ease;
        }

        /* Buttons */
        .stButton button {
            border-radius: 14px;
            font-weight: 600;
            padding: 10px 20px;
            border: none;
            transition: transform 0.15s ease;
        }

        .stButton button:hover {
            transform: translateY(-2px);
        }

        div.stButton > button[kind="primary"] {
            background: #111827;
            color: white;
        }

        .ow-footer-tag {
            text-align: center;
            font-size: 11px;
            color: #9CA3AF;
            margin-top: 32px;
            letter-spacing: 0.02em;
        }
    </style>
    """, unsafe_allow_html=True)