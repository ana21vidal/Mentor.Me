import streamlit as st
from openai import OpenAI
import os

# Crea el cliente con tu clave API
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Título de la app
st.title("Conócete como estudiante")
st.write("¿Qué quieres explorar hoy?")

# Entrada del usuario
user_input = st.text_input("Escribe aquí tu pregunta o interés:")

if user_input:
    with st.spinner("Pensando..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un mentor que ayuda a los estudiantes a conocerse y aprender mejor."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success("Respuesta generada:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")

