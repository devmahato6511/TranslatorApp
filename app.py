import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 AI Translator App")

text = st.text_area("Enter text to translate:")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt"
}

target_language = st.selectbox("Select target language:", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        translated = GoogleTranslator(source='auto', target=languages[target_language]).translate(text)
        st.markdown(f"**Original Text:**\n\n{text}")
        st.markdown(f"**Translated Text ({target_language}):**\n\n{translated}")
        st.code(translated, language=None)
        st.write("Click the code box above to copy the translation.")

st.markdown("---")
st.caption("Built by Bhanu Kumar Dev | Powered by Streamlit & Deep Translator")
