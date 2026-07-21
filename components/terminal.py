import streamlit as st
import time
from utils.alerts import get_random_terminal_lines

def play_boot_terminal(placeholder=None, delay=1):
    """
    Renders an animated fake terminal boot sequence.
    Call once per page load, before showing real data.
    """
    lines = get_random_terminal_lines()
    box = placeholder if placeholder else st.empty()
    rendered = []

    for line in lines:
        rendered.append(f'<span class="dim">&gt;</span> {line} <span class="ok">✓</span>')
        html = '<div class="ow-terminal">' + "<br>".join(rendered) + "</div>"
        box.markdown(html, unsafe_allow_html=True)
        time.sleep(delay)

    time.sleep(0.4)
    box.empty()