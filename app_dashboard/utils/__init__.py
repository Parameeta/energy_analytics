# --- E.ON branding helper ---
from pathlib import Path
import streamlit as st

def eon_branding(page_logo=True):
	"""Apply E.ON logo and color theme to the page."""
	logo_path = Path(__file__).resolve().parent.parent / "logo.png"
	if page_logo and logo_path.exists():
		st.image(str(logo_path), width=180)
	st.markdown(
		"""
		<style>
			.stApp {background-color: #fff6f6;}
			.css-18e3th9 {background-color: #fff6f6;}
			.st-bb, .st-cq, .st-emotion-cache-10trblm {color: #e2001a;}
			.stButton>button {background-color: #e2001a; color: #fff; border-radius: 6px; border: none;}
			.st-bb, .st-cq, .st-emotion-cache-10trblm {font-family: 'sans-serif';}
		</style>
		""",
		unsafe_allow_html=True,
	)
