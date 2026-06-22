import streamlit as st
from groq import Groq

# Page ka Title aur Layout
st.set_page_config(page_title="Alfaz-e-AI", layout="centered")
st.title("✨ Alfaz-e-AI")
st.subheader("Urdu Zubaan ka Digital Saathi")

# API Key ka input
api_key = st.text_input("Apni Groq API Key yahan paste karo:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        user_input = st.text_area("Apna sawal ya baat Urdu mein likhen:")
        
        if st.button("Generate"):
            if user_input:
                with st.spinner("AI soch raha hai..."):
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant that speaks in a natural, native Pakistani Urdu accent."},
                            {"role": "user", "content": user_input}
                        ],
                        model="llama-3.3-70b-versatile",
                    )
                    st.success(chat_completion.choices[0].message.content)
            else:
                st.warning("Pehle kuch likhen toh sahi!")
    except Exception as e:
        st.error(f"Error: {e}")
