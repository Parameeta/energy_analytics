"""Synthetic energy data generator for the learning dashboard.

The numbers here are illustrative only — they roughly resemble German grid
patterns (load ~50–80 GW, solar peaking around midday, variable wind) so the
student can develop intuition. They are NOT real measurements.

If you later want to plug in real data (e.g. SMARD CSV exports), implement
``load_real_data()`` and switch ``get_data()`` to use it.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def get_data(days: int = 30, seed: int = 42, freq_minutes: int = 60) -> pd.DataFrame:
    """Return a synthetic hourly dataset for ``days`` days.

    Columns: timestamp, consumption, solar, wind, renewables, residual_load,
    consumption_forecast, price.
    Units are illustrative GW (power) and EUR/MWh (price).
    """
    rng = np.random.default_rng(seed)
    end = pd.Timestamp.now().normalize()
    start = end - pd.Timedelta(days=days)
    idx = pd.date_range(start, end, freq=f"{freq_minutes}min", inclusive="left")

    hours = idx.hour + idx.minute / 60.0
    dow = idx.dayofweek  # 0=Mon
    day_of_year = idx.dayofyear

    # --- Consumption: morning + evening peaks, lower on weekends ---
    base = 55.0
    morning_peak = 10 * np.exp(-((hours - 8) ** 2) / 6)
    evening_peak = 14 * np.exp(-((hours - 19) ** 2) / 6)
    midday_dip = -3 * np.exp(-((hours - 14) ** 2) / 8)
    weekend = np.where(dow >= 5, -6.0, 0.0)
    noise = rng.normal(0, 1.2, len(idx))
    consumption = base + morning_peak + evening_peak + midday_dip + weekend + noise

    # --- Solar: bell curve during daylight, scaled by season ---
    season = 0.55 + 0.45 * np.sin(2 * np.pi * (day_of_year - 80) / 365)  # peak summer
    daylight = np.clip(np.sin(np.pi * (hours - 6) / 12), 0, None)
    cloud = np.clip(rng.normal(1.0, 0.18, len(idx)), 0.2, 1.2)
    solar = 35 * season * daylight ** 1.4 * cloud

    # --- Wind: smooth random walk, higher in winter ---
    wind_season = 1.3 - 0.4 * np.sin(2 * np.pi * (day_of_year - 80) / 365)
    walk = np.cumsum(rng.normal(0, 0.6, len(idx)))
    wind_raw = 18 + 8 * np.sin(walk / 12) + rng.normal(0, 2.5, len(idx))
    wind = np.clip(wind_raw * wind_season, 0.5, None)

    renewables = solar + wind
    residual = consumption - renewables

    # --- Forecast: actual + biased noise that grows with horizon-of-day ---
    forecast_noise = rng.normal(0, 1.6, len(idx)) + 0.8 * np.sin(2 * np.pi * hours / 24)
    consumption_forecast = consumption + forecast_noise

    # --- Day-ahead price: rough proxy linked to residual load ---
    price = 60 + 1.8 * (residual - residual.mean()) + rng.normal(0, 6, len(idx))
    price = np.clip(price, -50, 400)

    df = pd.DataFrame(
        {
            "timestamp": idx,
            "consumption": consumption.round(2),
            "solar": solar.round(2),
            "wind": wind.round(2),
            "renewables": renewables.round(2),
            "residual_load": residual.round(2),
            "consumption_forecast": consumption_forecast.round(2),
            "price": price.round(2),
        }
    )
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    df["weekday"] = df["timestamp"].dt.day_name()
    return df


def daily_profile(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Average ``column`` by hour-of-day."""
    return (
        df.groupby("hour", as_index=False)[column]
        .mean()
        .rename(columns={column: f"avg_{column}"})
    )
