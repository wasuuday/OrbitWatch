import streamlit as st

def render_header(status_text="Tracking orbital activity", updated_text="Updated just now"):
    st.markdown(f"""
    <div class="ow-header">
        <div class="ow-header-icon">🛰️</div>
        <p class="ow-header-title">OrbitWatch</p>
        <p class="ow-header-sub">
            <span class="ow-status-dot"></span>{status_text} · {updated_text}
        </p>
    </div>
    """, unsafe_allow_html=True)