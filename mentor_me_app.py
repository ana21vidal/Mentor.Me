import streamlit as st
import openai
import os

st.title("Mentor.Me 🎓")
st.subheader("Conócete como estudiante")

openai.api_key = os.getenv("OPENAI_API_KEY")

user_input = st.text_input("¿Qué quieres explorar hoy?")

if user_input:
    with st.spinner("Pensando..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Actúa como un mentor educativo."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(response['choices'][0]['message']['content'])
