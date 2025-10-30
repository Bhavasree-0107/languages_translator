import streamlit as st
from deep_translator import GoogleTranslator
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="wide")

st.title("🌐 Language Translator App")
st.markdown("Translate text instantly between multiple languages using cloud-based translation.")

# ✅ Corrected language loading
translator = GoogleTranslator(source='auto', target='en')
languages = translator.get_supported_languages(as_dict=True)
language_names = list(languages.keys())


# Select boxes for source and target
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("From Language", language_names, index=language_names.index("english"))
with col2:
    target_lang = st.selectbox("To Language", language_names, index=language_names.index("french"))

# Input area
text = st.text_area("Enter text to translate:", height=150, placeholder="Type or paste text here...")

# Translate button
if st.button("Translate 🔁"):
    if text.strip():
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        st.success(f"*Translated Text ({target_lang.capitalize()}):*")
        st.write(translated_text)

        # ---- Logging Section ----
        log_file = "translation_logs.csv"
        log_data = {
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Source Language": [source_lang.capitalize()],
            "Target Language": [target_lang.capitalize()],
            "Input Text": [text],
            "Translated Text": [translated_text]
        }
        df = pd.DataFrame(log_data)

        if os.path.exists(log_file):
            df.to_csv(log_file, mode='a', header=False, index=False)
        else:
            df.to_csv(log_file, index=False)

        st.toast("✅ Translation logged successfully!", icon="💾")
    else:
        st.warning("Please enter some text to translate.")

# Footer
st.markdown("---")
st.markdown("**Developed by:** BHAVA SREE S N | **Cloud Provider:** GCP (PaaS via Streamlit Cloud)")
