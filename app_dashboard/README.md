# E.ON Energy Markets Learning Dashboard – Internship Blueprint

A lightweight educational Streamlit app for a 10-day school internship covering
energy systems, forecasting, renewables, residual load, and AI-assisted reasoning.

> Educational use only. Uses **publicly available concepts and synthetic demo data**.
> No internal E.ON systems, credentials, or sensitive operational details are referenced.

## Quick start

```bash
cd app_dashboard
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually http://localhost:8501).

## Structure

```
app_dashboard/
├── app.py                  # Home page (entry point)
├── requirements.txt
├── utils/
│   └── data.py             # Synthetic demo data generator
└── pages/
    ├── 1_📘_Internship_Guide.py
    ├── 2_🌍_Public_Energy_Info.py
    ├── 3_⚡_Energy_Consumption.py
    ├── 4_🌞_Renewables.py
    ├── 5_🔋_Residual_Load.py
    ├── 6_🎯_Forecast_vs_Actual.py
    ├── 7_🏭_VPP_Simulator.py
    ├── 8_🤖_AI_Assistant.py
    └── 9_🎓_Final_Project.py
```

## Public data sources to explore

- [SMARD](https://www.smard.de/) – German electricity market data
- [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/)
- [Agora Energiewende](https://www.agora-energiewende.org/)
- [E.ON Corporate](https://www.eon.com/) / E.ON Energy Markets public pages

The app ships with a synthetic dataset so the student can interact immediately,
and is structured so real SMARD CSV exports can be dropped into `utils/data.py`.
