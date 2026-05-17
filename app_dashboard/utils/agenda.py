"""Real internship agenda (18 May – 29 May 2026, 10-day school internship, ~40 h total).

Kept in one place so Home and Internship Guide stay in sync.

Entries with ``skip_details=True`` (off day, public holiday) appear in the
agenda table but do not get their own detailed task page.
"""
from __future__ import annotations

AGENDA = [
    {
        "date": "Mon, 18 May",
        "day_label": "Day 1",
        "mode": "Office (Essen)",
        "hours": 5.0,
        "checkin": 0.5,
        "theme": "Kick-off · Volume Forecasting walkthrough",
        "supervisor": (
            "Product walkthrough: **Volume Forecasting** "
            "(conceptual, on supervisor's laptop). Sharing public sources "
            "SMARD & ENTSO-E with a drafted Jupyter notebook so the student "
            "can fetch data quickly."
        ),
        "student_tasks": [
            "Read about E.ON Energy Markets (public website only)",
            "Set up Jupyter notebook environment on the school-provided machine",
            "Open SMARD and ENTSO-E and browse what is available",
            "Run the drafted notebook end-to-end to fetch a first dataset",
        ],
        "guidelines": [
            "Goal of the day is **orientation**, not deep analysis.",
            "Note 3 things you didn't know about energy markets before today.",
            "If the notebook fails to fetch data, **don't fix code blindly** — "
            "ask which URL/parameter changed and learn why.",
            "Write down 2 questions for tomorrow's check-in.",
        ],
        "deliverables": [
            "Working Jupyter notebook that fetches one SMARD series",
            "Short note (3–5 lines) on what E.ON Energy Markets does",
        ],
        "dashboard_pages": ["🌍 Public Energy Info"],
    },
    {
        "date": "Tue, 19 May",
        "day_label": "Day 2",
        "mode": "Office (Essen)",
        "hours": 5.0,
        "checkin": 0.5,
        "theme": "Algo Data Hub · Demand vs Generation",
        "supervisor": (
            "Product walkthrough: **Algo Data Hub** (conceptual, on supervisor's "
            "laptop) — what it is, why it exists, how data supports decisions."
        ),
        "student_tasks": [
            "Use SMARD to compare electricity consumption vs total generation",
            "Identify the daily load shape and the evening peak",
            "Write **3 initial observations** (1–2 sentences each)",
        ],
        "guidelines": [
            "Look at *several* days, not just one — patterns are clearer that way.",
            "Distinguish **base load** vs **peak load** in your own words.",
            "An observation is more than a number — say *what* you see and *why* it might matter.",
            "Use the dashboard's Energy Consumption page to cross-check your notebook plots.",
        ],
        "deliverables": [
            "Notebook chart of one weekday load curve",
            "Bullet list of 3 observations",
        ],
        "dashboard_pages": ["⚡ Energy Consumption"],
    },
    {
        "date": "Wed, 20 May",
        "day_label": "Day 3",
        "mode": "Off day",
        "hours": 2.0,
        "checkin": 0.0,
        "theme": "Off day",
        "supervisor": "",
        "student_tasks": [],
        "guidelines": [],
        "deliverables": [],
        "dashboard_pages": [],
        "skip_details": True,
    },
    {
        "date": "Thu, 21 May",
        "day_label": "Day 4",
        "mode": "Remote",
        "hours": 4.5,
        "checkin": 0.5,
        "theme": "Leadership mentoring · Reflection",
        "supervisor": (
            "**Leadership mentoring session (30 min)** — guided review & coaching. "
            "Topics: decision-making under uncertainty, prioritisation, career "
            "directions (STEM / data / business)."
        ),
        "student_tasks": [
            "**Before** the session: prepare 3–5 leadership questions",
            "**After** the session: write a short reflection (1 page max)",
        ],
        "guidelines": [
            "Good questions are **specific** ('How do you decide what *not* to work on?') "
            "rather than generic ('What is leadership?').",
            "Reflection prompts: what surprised you? what would you do differently? "
            "which career direction feels more interesting and why?",
            "It is fine — even good — to disagree with something you heard. "
            "Write *why* you disagree.",
        ],
        "deliverables": [
            "List of leadership questions (saved before the session)",
            "1-page written reflection (after the session)",
        ],
        "dashboard_pages": ["🤖 AI Assistant (for brainstorming questions)"],
    },
    {
        "date": "Fri, 22 May",
        "day_label": "Day 5",
        "mode": "Remote",
        "hours": 4.5,
        "checkin": 0.5,
        "theme": "Core plots · Residual load",
        "supervisor": "Guided review & coaching (30 min).",
        "student_tasks": [
            "Build the 3 **core plots**: Consumption, Solar + Wind, Residual Load",
            "Understand and compute: **Residual load = Consumption − (PV + Wind)**",
        ],
        "guidelines": [
            "Use a consistent time window for all 3 plots so they are comparable.",
            "Annotate the residual load plot: where is it highest? where is it lowest? where (if anywhere) is it negative?",
            "Use the dashboard's Residual Load page to **sanity-check** your numbers — they should be in the same ballpark for similar conditions.",
            "If your residual load is negative for many hours, double-check units (MW vs GW vs MWh).",
        ],
        "deliverables": [
            "3 core plots saved (PNG)",
            "1-paragraph definition of residual load in your own words",
        ],
        "dashboard_pages": ["⚡ Energy Consumption", "🌞 Renewables", "🔋 Residual Load"],
    },
    {
        "date": "Mon, 25 May",
        "day_label": "—",
        "mode": "Public holiday",
        "hours": 0.0,
        "checkin": 0.0,
        "theme": "Public holiday",
        "supervisor": "",
        "student_tasks": [],
        "guidelines": [],
        "deliverables": [],
        "dashboard_pages": [],
        "skip_details": True,
    },
    {
        "date": "Tue, 26 May",
        "day_label": "Day 6",
        "mode": "Office (Essen)",
        "hours": 5.0,
        "checkin": 0.5,
        "theme": "Technology & systems mentoring · Glossary",
        "supervisor": (
            "**Technology & systems mentoring** — how data flows through energy "
            "systems and why **15-minute granularity** matters. Joint discussion "
            "on the analysis done so far."
        ),
        "student_tasks": [
            "Connect data observations to **system thinking**: why does uncertainty exist?",
            "Articulate why forecasts can never be perfect",
            "Maintain a **glossary of 5 key terms** in your own words",
        ],
        "guidelines": [
            "Suggested glossary terms: load, residual load, base load, forecast error, balancing.",
            "For each term: 1 sentence definition + 1 sentence why it matters.",
            "When you say 'uncertainty', try to name *what* is uncertain "
            "(weather, behaviour, equipment, market price...).",
        ],
        "deliverables": [
            "Glossary of 5 terms (1–2 sentences each)",
            "Short note: 3 reasons forecasts can be wrong",
        ],
        "dashboard_pages": ["🎯 Forecast vs Actual"],
    },
    {
        "date": "Wed, 27 May",
        "day_label": "Day 7",
        "mode": "Remote",
        "hours": 4.5,
        "checkin": 0.5,
        "theme": "Comparative analysis: sunny day vs windy day",
        "supervisor": "Daily mentoring sync (30 min).",
        "student_tasks": [
            "Pick **one sunny day** and **one windy day** from SMARD",
            "Compare their **residual load shapes** and discuss system stress",
            "Write **5–6 insights** comparing the two",
        ],
        "guidelines": [
            "Choose days from comparable seasons so the comparison is fair.",
            "Insights should mix **what** you see and **so what** for the system.",
            "Use the dashboard's Renewables page → 'Compare two days' tool to explore quickly.",
            "If both days look similar, that is also an insight — note why.",
        ],
        "deliverables": [
            "1 comparison chart (sunny vs windy)",
            "5–6 written insights",
        ],
        "dashboard_pages": ["🌞 Renewables", "🔋 Residual Load"],
    },
    {
        "date": "Thu, 28 May",
        "day_label": "Day 8",
        "mode": "Office (Essen) · Scenario workshop",
        "hours": 5.0,
        "checkin": 0.5,
        "theme": "Scenario workshop · Decisions under uncertainty",
        "supervisor": (
            "**Scenario workshop** — using the student's own plots. Walk-through "
            "of EV evening charging, sudden solar drop, and wind variability. "
            "Discuss *which decisions become harder and why*. Help the intern "
            "begin drafting school-presentation slides (public data only)."
        ),
        "student_tasks": [
            "Run 3 scenarios in the dashboard's VPP Simulator: "
            "high EV evening demand, sudden solar drop, low-wind period",
            "For each scenario: note system stress and which decisions become harder",
            "Begin drafting **school presentation slides** (public data only)",
        ],
        "guidelines": [
            "A scenario is a **'what if'** — change one thing at a time.",
            "For each scenario, answer: *Who has to act? When? With what tool (storage, market, demand response)?*",
            "Slides: 5–7 slides max. Each slide = 1 idea + 1 chart + 1 sentence.",
            "Strict rule: **public data only**, no internal screenshots.",
        ],
        "deliverables": [
            "Table of 3 scenarios → stress level + 1-line consequence",
            "First draft of presentation slides (5–7 slides)",
        ],
        "dashboard_pages": ["🏭 VPP Simulator", "🔋 Residual Load"],
    },
    {
        "date": "Fri, 29 May",
        "day_label": "Day 9",
        "mode": "Remote",
        "hours": 4.5,
        "checkin": 0.5,
        "theme": "Consolidation · Final reflection · Presentation",
        "supervisor": "Final coaching & review (30 min).",
        "student_tasks": [
            "Finalise plots and clean up the notebook",
            "Write a **1-page reflection**",
            "Finalise the **school presentation outline** (public data only)",
        ],
        "guidelines": [
            "Reflection structure suggestion: What I learned · What surprised me · What I would explore next.",
            "Every chart in the deck must have a 1-sentence caption explaining *why it matters*.",
            "Re-read the governance rules before submitting (no internal info).",
            "Use the Final Project page checklist to make sure nothing is missing.",
        ],
        "deliverables": [
            "Final notebook (clean)",
            "1-page reflection (PDF or DOCX)",
            "Presentation outline (5–7 slides)",
        ],
        "dashboard_pages": ["🎓 Final Project"],
    },
]


SUMMARY = {
    "duration": "18 May – 29 May 2026 (10-day school internship)",
    "total_hours": 40,
    "weekly_hours": 20,
    "mode": "Mix of Essen office days and remote days",
    "constraints": [
        "No KID / no company laptop provisioned",
        "No internal data or platform access — public sources only (SMARD, ENTSO-E, Agora)",
        "All product exposure happens **on the supervisor's laptop**, demo-only",
        "All AI-tool outputs must be validated against logic and data",
    ],
    "principle": (
        "The internship is designed as an **observational and educational** "
        "exposure program rather than a production-oriented technical internship."
    ),
}


WEEK_FOCUS = [
    ("Week 1 (18–22 May)", "Understanding energy systems, forecasting concepts, and data interpretation."),
    ("Week 2 (26–29 May)", "Applying system thinking, residual load analysis, and scenario reasoning."),
]
