import streamlit as st

st.set_page_config(page_title="About Project", page_icon="ℹ️")

st.title("ℹ️ About the Language Translator Project")

st.markdown("""
### 🧠 Project Overview
This cloud-based Language Translator application allows users to translate text between multiple languages instantly.

### ☁️ Cloud Provider
- **Google Cloud Platform (GCP)**
- **Service Type:** PaaS (Platform as a Service)
- **Deployment:** Hosted via Streamlit Cloud (runs on GCP backend)

### 🧩 Tech Stack
- **Frontend/UI:** Streamlit
- **Backend Translation:** Deep Translator API
- **Visualization:** Matplotlib + Pandas
- **Storage:** CSV (local or GCP bucket for logs)

### ⚙️ Features
- Real-time text translation between 10+ languages  
- Dashboard analytics and accuracy graphs  
- Translation history tracking  
- Easy cloud deployment and scalability

### 🧾 Future Enhancements
- Integration with Google Translate API v2  
- Speech-to-Text and Text-to-Speech  
- User authentication (Google Sign-In)  
- Saving user preferences
""")
