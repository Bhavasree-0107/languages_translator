import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Translation Dashboard", page_icon="📊", layout="wide")

# Title
st.title("📊 Language Translator Dashboard")
st.markdown("### Translation Analytics & Model Performance Overview")

# Simulated data (you can later log real data into a CSV)
languages = ["English", "French", "Spanish", "German", "Hindi", "Tamil", "Chinese"]
usage_count = [random.randint(10, 100) for _ in languages]
accuracy_values = [round(random.uniform(85, 99), 2) for _ in languages]

# Total translations
total_translations = sum(usage_count)
st.metric("Total Translations", f"{total_translations}")

# Section 1: Translation Usage
st.subheader("🌍 Translation Usage by Language")
col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    ax1.bar(languages, usage_count, color="#007bff")
    ax1.set_title("Number of Translations per Language")
    ax1.set_ylabel("Count")
    ax1.set_xlabel("Languages")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    ax2.pie(usage_count, labels=languages, autopct="%1.1f%%", startangle=140)
    ax2.set_title("Language Distribution (%)")
    st.pyplot(fig2)

# Section 2: Model Accuracy
st.subheader("📈 Model Accuracy Comparison")

fig3, ax3 = plt.subplots()
ax3.plot(languages, accuracy_values, marker='o', color='green')
ax3.set_title("Accuracy per Language")
ax3.set_xlabel("Languages")
ax3.set_ylabel("Accuracy (%)")
st.pyplot(fig3)

# Section 3: Summary Table
st.subheader("📋 Summary Table")
data = pd.DataFrame({
    "Language": languages,
    "Translations": usage_count,
    "Accuracy (%)": accuracy_values
})
st.dataframe(data, use_container_width=True)

# Footer
st.markdown("---")
st.caption(f"Dashboard generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
