import streamlit as st
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="Feedback", page_icon="💬")

st.title("💬 User Feedback")
st.markdown("We value your input! Please share your thoughts about the translator.")

name = st.text_input("Your Name")
feedback = st.text_area("Your Feedback")

if st.button("Submit Feedback"):
    if name and feedback:
        data = {"Name": [name], "Feedback": [feedback], "Timestamp": [datetime.now()]}
        df = pd.DataFrame(data)
        if os.path.exists("feedback.csv"):
            df.to_csv("feedback.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("feedback.csv", index=False)
        st.success("✅ Thank you for your feedback!")
    else:
        st.warning("Please fill in all fields before submitting.")
