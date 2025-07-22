import streamlit as st
import openai

# Clave de API (en Streamlit Cloud debe ir en secrets)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Título de la app
st.title("Conócete como estudiante")
st.write("¿Qué quieres explorar hoy?")

# Entrada de texto
user_input = st.text_input("Escribe aquí tu pregunta o interés:")

# Selección del mentor
mentores = {
    "Sócrates": "Eres SócratesGPT. Haces una o dos preguntas para ayudar al estudiante a reflexionar, no das respuestas directamente.",
    "Oráculo de Delfos": "Eres el Oráculo de Delfos. Das respuestas simbólicas y profundas, invitas a pensar en el sentido de las cosas.",
    "Telos": "Eres TelosGPT. Ayudas al usuario a descubrir sus fines y metas más importantes con preguntas inspiradoras."
}
selected_mentor = st.selectbox("Elige tu mentor:", list(mentores.keys()))

# Generación de respuesta
if user_input:
    with st.spinner("Pensando..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": mentores[selected_mentor]},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success("Respuesta generada:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

