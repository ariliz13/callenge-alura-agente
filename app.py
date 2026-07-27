import streamlit as st
import PyPDF2
from openai import OpenAI

# 1. Configuración de la interfaz
st.title("Agente IA - Lector de PDF 🤖")
st.write("Sube un documento y hazle preguntas basadas en su contenido.")

# 2. Credenciales y carga de archivo
api_key = st.text_input("Ingresa tu API Key de OpenAI:", type="password")
uploaded_file = st.file_uploader("Sube tu archivo PDF aquí", type="pdf")
pregunta = st.text_input("¿Qué deseas saber sobre el documento?")

# 3. Lógica de ejecución
if st.button("Consultar"):
    if not api_key or not uploaded_file or not pregunta:
        st.warning("Por favor, completa todos los campos (API Key, Archivo y Pregunta).")
    else:
        try:
            # Inicializar cliente de OpenAI
            client = OpenAI(api_key=api_key)
            
            # Extraer texto del PDF
            lector = PyPDF2.PdfReader(uploaded_file)
            texto_pdf = ""
            for pagina in lector.pages:
                texto_pdf += pagina.extract_text()
                
            # Limitar a los primeros 3000 caracteres para evitar errores de límite de tokens en modo express
            texto_pdf = texto_pdf[:3000] 
            
            # Consultar al modelo
            with st.spinner("El agente está pensando..."):
                respuesta = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un asistente estricto. Responde las preguntas basándote ÚNICAMENTE en el texto proporcionado. Si la respuesta no está, di 'No puedo confirmar esto'."},
                        {"role": "user", "content": f"Texto base:\n{texto_pdf}\n\nPregunta: {pregunta}"}
                    ]
                )
                
            # Mostrar resultado
            st.success("Respuesta:")
            st.write(respuesta.choices[0].message.content)
            
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
