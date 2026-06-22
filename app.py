import streamlit as st
import os
from groq import Groq

# Encoding ka masla solve karne ke liye
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Page setup
st.set_page_config(page_title="Alfaz-e-AI", layout="centered")
st.title("✨ Alfaz-e-AI")
st.subheader("Urdu Zubaan ka Digital Saathi")

# API Key input
api_key = st.text_input("Apni Groq API Key yahan paste karo:", type="password")

if api_key:
    client = Groq(api_key=api_key)
    user_input = st.text_area("Apna sawal ya baat Urdu mein likhen:")
    
    if st.button("Generate"):
        if user_input:
            with st.spinner("AI soch raha hai..."):
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant. Always reply in Urdu."},
                            {"role": "user", "content": user_input}
                        ],
                        model="llama-3.3-70b-versatile",
                    )
                    # Jawab ko saaf display karna
                    st.success(chat_completion.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Pehle kuch likhen toh sahi!")
          
