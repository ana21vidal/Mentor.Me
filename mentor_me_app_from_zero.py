
import streamlit as st
import openai

# ----------- Seguridad: Contraseña de acceso ----------
PASSWORD = "mentorme2025"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Acceso a Mentor.Me")
    password_input = st.text_input("Introduce la contraseña:", type="password")
    if password_input == PASSWORD:
        st.session_state.authenticated = True
        st.experimental_rerun()
    else:
        st.stop()

# ----------- Configuración del cliente OpenAI ----------
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ----------- Interfaz de usuario ----------
st.title("🌱 Mentor.Me")
st.write("Elige un pilar para comenzar tu camino de aprendizaje:")

pilar = st.selectbox("Selecciona tu pilar:", [
    "Conócete (Oráculo de Delfos)",
    "Desarrolla tu Talento",
    "Planifica tu Ruta"
])

pregunta = st.text_input("¿Qué quieres explorar hoy?")

if st.button("Explorar"):
    if pregunta.strip() == "":
        st.warning("Por favor, escribe tu pregunta o interés.")
    else:
        with st.spinner("Consultando a tu mentor..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"Eres un mentor educativo experto en el pilar '{pilar}'."},
                    {"role": "user", "content": pregunta}
                ]
            )
            st.success("Respuesta de tu mentor:")
            st.write(response.choices[0].message.content)
