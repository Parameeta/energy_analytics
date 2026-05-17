import sys
from pathlib import Path
import pandas as pd
import streamlit as st

# --- Streamlit page config MUST be first Streamlit command ---
st.set_page_config(page_title="Internship Guide", page_icon="📘", layout="wide")

from utils import eon_branding

# --- E.ON logo and theme ---
eon_branding()

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.agenda import AGENDA, SUMMARY  # noqa: E402

detailed_days = [d for d in AGENDA if not d.get("skip_details")]
day_labels = [f"{d['date']} — {d['theme']}" for d in detailed_days]
selected = st.sidebar.radio("Jump to a working day", day_labels, index=0)
sel = detailed_days[day_labels.index(selected)]

st.header(f"{sel['date']} · {sel['theme']}")
m1, m2, m3 = st.columns(3)
m1.metric("Mode", sel["mode"])
m2.metric("Total hours", f"{sel['hours']} h")
m3.metric("Daily check-in", f"{sel['checkin']} h")

st.subheader("👨‍🏫 Supervisor session")
st.markdown(sel["supervisor"])

c1, c2 = st.columns(2)
with c1:
    st.subheader("🛠️ Student tasks")
    for t in sel["student_tasks"]:
        st.checkbox(t, key=f"task_{sel['date']}_{t[:40]}")

    st.subheader("📦 Deliverables (end of day)")
    for d in sel["deliverables"]:
        st.markdown(f"- {d}")