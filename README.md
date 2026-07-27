# Challenge Alura Agente Inteligente 🚀

## Descripción General
Este proyecto es un agente de Inteligencia Artificial desarrollado para el Challenge de Alura. Permite cargar un documento en formato PDF y realizar preguntas sobre su contenido. El agente responde basándose estrictamente en la información del texto proporcionado.

## Arquitectura de la Solución
El proyecto utiliza una arquitectura sencilla de frontend interactivo conectado a una API de modelos de lenguaje:
1. **Frontend/Backend unificado:** Construido con Streamlit para la carga del archivo y la captura de la pregunta.
2. **Procesamiento de datos:** PyPDF2 extrae el texto del documento.
3. **Capa de Inteligencia Artificial:** OpenAI API (modelo GPT-3.5-turbo) procesa el texto extraído y el *prompt* del usuario para generar una respuesta fundamentada.

## Tecnologías y Herramientas Utilizadas
* Python 3.10+
* Streamlit (Interfaz de usuario y servidor web local)
* PyPDF2 (Extracción de texto)
* OpenAI API (LLM)
* Oracle Cloud Infrastructure (OCI) para el despliegue en la nube.

## Instrucciones para Ejecutar el Proyecto
Para correr este proyecto en tu entorno local:

1. Clona este repositorio:
   `git clone [TU_ENLACE_DE_GITHUB]`
2. Instala las dependencias necesarias:
   `pip install -r requirements.txt`
3. Ejecuta la aplicación:
   `streamlit run app.py`
4. Abre la dirección `http://localhost:8501` en tu navegador.
5. Necesitarás ingresar una clave de API de OpenAI válida en la interfaz.

## Ejemplos de Uso
**Pregunta del usuario:** 
[Escribe aquí una pregunta que le hiciste a tu documento, ej: "¿Cuáles son las fases del proyecto descritas en el documento?"]

**Respuesta generada por el agente:** 
[Pega aquí la respuesta que te dio la IA en tus pruebas]
