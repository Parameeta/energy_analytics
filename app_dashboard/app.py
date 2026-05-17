"""E.ON Energy Markets Learning Dashboard – Internship Blueprint.

Run with:  streamlit run app.py
"""
from __future__ import annotations

import sys

import pandas as pd
import streamlit as st

# --- E.ON branding helper ---

from pathlib import Path
from utils import eon_branding


# --- Streamlit page config MUST be first Streamlit command ---
st.set_page_config(
    page_title="E.ON Energy Markets GmbH – Internship Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- E.ON logo and theme ---
eon_branding()

sys.path.append(str(Path(__file__).resolve().parent))
from utils.agenda import AGENDA, SUMMARY, WEEK_FOCUS  # noqa: E402


st.title("⚡ E.ON Energy Markets GmbH – Internship Dashboard")
st.caption("10-day school internship · 18 May – 29 May 2026 · Educational use only · Public data sources only · Powered by E.ON Energy Markets GmbH")

st.markdown(

    """
    Welcome! This interactive **learning cockpit** is your companion for a
    **10-day school internship** at **E.ON Energy Markets GmbH** focused on how
    modern energy systems work.

    Use the sidebar ⬅️ to navigate between pages. The 📘 **Internship Guide**
    is your day-by-day plan; the other pages are interactive learning tools.
    """
)

# ---------------- Public Energy Information ----------------
st.subheader("🌍 Public Energy Market Information")
st.warning(
    "🛡️ **Governance reminder** — Avoid: internal screenshots, internal architecture, "
    "internal dashboards, sensitive operational details. Use **public websites only**.",
    icon="🛡️",
)
st.markdown("""
E.ON Energy Markets GmbH is part of E.ON, a European energy company focused on **energy networks** and **customer solutions**. Public materials describe activities such as operating distribution grids, supplying electricity and gas to customers, and developing services around energy efficiency and electrification (heat pumps, EV charging, etc.).

*Always check the official corporate site for the latest, authoritative description.*
""")
st.subheader("Suggested topics to explore")
topics = [
    ("Energy trading overview", "How electricity is bought and sold (day-ahead, intraday)."),
    ("Forecasting concepts", "Why forecasts of demand and renewables are essential inputs."),
    ("Renewable integration", "How solar and wind are integrated into the grid."),
    ("Flexibility & balancing", "How grids stay stable second by second."),
    ("Role of data", "Why modern energy systems rely heavily on data & analytics."),
]
for title, desc in topics:
    with st.expander(f"📖 {title}"):
        st.write(desc)
st.subheader("🔗 Suggested public links")
links = [
    ("E.ON Corporate website", "https://www.eon.com/"),
    ("SMARD – German market data", "https://www.smard.de/"),
    ("ENTSO-E Transparency Platform", "https://transparency.entsoe.eu/"),
    ("Agora Energiewende", "https://www.agora-energiewende.org/"),
]
for label, url in links:
    st.markdown(f"- [{label}]({url})")
st.divider()

st.info(f"**Principle.** {SUMMARY['principle']}", icon="🎓")

# ---------------- Summary KPIs ----------------
k1, k2, k3, k4 = st.columns(4)
k1.metric("Duration", "10 days")
k2.metric("Total hours", f"{SUMMARY['total_hours']} h")
k3.metric("Per week", f"{SUMMARY['weekly_hours']} h")
k4.metric("Mode", "Office + Remote")

# ---------------- Weekly focus ----------------
st.subheader("🗓️ Weekly focus")
wcols = st.columns(2)
for col, (title, desc) in zip(wcols, WEEK_FOCUS):
    with col:
        st.markdown(f"**{title}**")
        st.write(desc)

st.divider()

# ---------------- Full agenda table ----------------
st.subheader("📋 Full 10-day agenda")

agenda_rows = [
    {
        "Date": d["date"],
        "Day": d["day_label"],
        "Mode": d["mode"],
        "Hours": d["hours"],
        "Check-in (h)": d["checkin"],
        "Theme": d["theme"],
    }
    for d in AGENDA
]
agenda_df = pd.DataFrame(agenda_rows)
st.dataframe(agenda_df, hide_index=True, use_container_width=True)

st.caption(
    "💡 Open the 📘 **Internship Guide** in the sidebar to see supervisor sessions, "
    "student tasks, detailed guidelines and deliverables for each day."
)

st.divider()

# ---------------- Mental model ----------------
left, right = st.columns([1.2, 1])
with left:
    st.subheader("🧭 How an energy system works (mental model)")
    st.graphviz_chart(
        """
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fillcolor="#f0f4ff", color="#3355aa"];
            Demand -> Forecast -> Decisions -> Balancing -> Grid;
            Renewables -> Balancing;
            Storage -> Balancing;
            Markets -> Decisions;
        }
        """
    )
    st.caption("Demand → Forecast → Decisions → Balancing — keep this picture in mind every day.")

with right:
    st.subheader("🎯 Learning goals")
    st.markdown(
        """
        - Understand how electricity systems must **balance in real time**
        - Read and interpret **load and generation curves** (SMARD)
        - Grasp **renewable intermittency** (solar & wind)
        - Learn the concept of **residual load** and why it matters
        - Reason about **forecast uncertainty**
        - Use AI as a **thinking partner**, not a black box
        - Build a short, clear **school presentation** from public data
        """
    )

st.divider()

# ---------------- Constraints ----------------
st.subheader("🛡️ Constraints & governance (read once, follow always)")
cols = st.columns(2)
with cols[0]:
    st.markdown("**Constraints**")
    for c in SUMMARY["constraints"]:
        st.markdown(f"- {c}")
with cols[1]:
    st.markdown("**Office-day product walkthroughs (supervisor's laptop, demo-only)**")
    st.markdown(
        """
        - **18 May** — Volume Forecasting (conceptual)
        - **19 May** — Algo Data Hub (conceptual)
        - **26 May** — Joint discussion on the energy data analysis
        - **28 May** — Help drafting school-presentation slides (public data only)
        """
    )

# ---------------- Daily tracker ----------------
st.subheader("✅ Daily learning tracker")
st.caption("Tick what you completed today. (Resets on app reload — copy notes into your own log.)")

cols = st.columns(5)
tracker_items = [
    "Did the daily 30-min check-in",
    "Read at least one public source (SMARD / ENTSO-E / Agora / E.ON site)",
    "Updated the Jupyter notebook",
    "Saved at least one chart with a caption",
    "Wrote 1+ observation in my notes",
    "Cross-checked numbers using the dashboard",
    "Asked AI a 'why' question and validated it",
    "Updated my glossary",
    "Logged 1 question for tomorrow",
    "Followed governance rules (public data only)",
]
for i, item in enumerate(tracker_items):
    with cols[i % 5]:
        st.checkbox(item, key=f"track_{i}")

st.divider()

# ---------------- Glossary + QOTD ----------------
g_col, q_col = st.columns(2)

with g_col:
    st.subheader("📚 Quick glossary")
    glossary = {
        "Load": "Electricity demand at a given moment.",
        "Base load": "The minimum level of demand on a grid over a period.",
        "Peak load": "The highest demand period (often morning & evening).",
        "Residual load": "Consumption − (Solar + Wind). What conventional/flexible sources must cover.",
        "Forecast": "An estimate of a future value (e.g. demand or generation).",
        "Forecast error": "Forecast − Actual. Can be positive (over-predicted) or negative.",
        "Balancing": "Continuously matching generation to demand in real time.",
        "15-min granularity": "Energy markets settle in 15-minute intervals — sub-hour patterns matter.",
    }
    for term, definition in glossary.items():
        st.markdown(f"**{term}** — {definition}")

with q_col:
    st.subheader("❓ Question of the Day")
    st.info(
        "Why must electricity supply and demand match **at every second**, "
        "and what would happen if they drifted apart?"
    )
    st.text_area(
        "Your answer / notes",
        key="qotd_answer",
        height=180,
        placeholder="Write your thinking here. There is no single right answer — explain your reasoning.",
    )


st.markdown(
    """
    <hr style='border:1px solid #e2001a; margin-top:2em; margin-bottom:0.5em;'>
    <div style='text-align:center; color:#e2001a; font-weight:bold; font-size:1.1em;'>
        © 2026 E.ON Energy Markets GmbH &nbsp;|&nbsp; <a href='https://www.eon.com/' style='color:#e2001a;'>eon.com</a>
    </div>
    """,
    unsafe_allow_html=True
)
