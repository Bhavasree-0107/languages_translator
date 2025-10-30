from deep_translator import GoogleTranslator
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")

# App Title
st.title("🌍 Cloud-Based Language Translator")
st.write("Translate text instantly between languages using a free translation API.")

# Get supported languages (create a temporary instance)
translator = GoogleTranslator(source="auto", target="en")
languages = translator.get_supported_languages(as_dict=True)
language_names = list(languages.keys())

# Input Section
text = st.text_area("Enter text to translate:", placeholder="Type something here...")
target_lang_name = st.selectbox("Select target language:", sorted(language_names), index=language_names.index("english"))

# Translation Process
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        try:
            target_code = languages[target_lang_name]
            translated_text = GoogleTranslator(source="auto", target=target_code).translate(text)
            st.success(f"**Translated ({target_lang_name.capitalize()}):** {translated_text}")
        except Exception as e:
            st.error(f"⚠️ Translation failed: {e}")

# Footer
st.markdown("---")
st.markdown("**Developed by:BHAVA SREE S N  | **Cloud Provider:** GCP (PaaS via Streamlit Cloud)")
