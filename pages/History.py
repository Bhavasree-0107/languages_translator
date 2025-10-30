import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Translation History", page_icon="🕒")

st.title("🕒 Translation History")
st.markdown("View all translations performed in this session.")

# File to store logs
LOG_FILE = "translation_logs.csv"

# If log file exists, show data
if os.path.exists(LOG_FILE):
    data = pd.read_csv(LOG_FILE)
    st.dataframe(data, use_container_width=True)
else:
    st.info("No translations logged yet. Perform translations in the Home page!")

# Option to clear logs
if st.button("🧹 Clear History"):
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        st.success("Translation history cleared.")
