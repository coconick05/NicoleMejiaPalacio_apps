import base64
import streamlit as st

# Título en color fucsia
st.markdown(
    "<h1 style='color: #FF00FF;'>Aplicaciones de Inteligencia Artificial.</h1>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# Estilos de las tarjetas
st.markdown(
    """
<style>
.tarjeta {
    background-color: #E6DAFA;
    border: 1px solid #C9B3F0;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
}
.tarjeta h3 {
    color: #4B2C82;
    font-size: 1.25rem;
    margin: 0 0 12px 0;
    padding: 0;
}
.tarjeta img {
    border-radius: 12px;
    display: block;
    margin-bottom: 12px;
}
.tarjeta p {
    color: #2E2447;
    font-size: 0.95rem;
    margin: 0 0 10px 0;
}
.tarjeta a {
    color: #6B3FD4;
    font-weight: bold;
}
</style>
""",
    unsafe_allow_html=True,
)


def imagen_base64(ruta):
    extension = ruta.split(".")[-1].lower()
    mime = "jpeg" if extension in ("jpg", "jpeg") else extension
    with open(ruta, "rb") as f:
        datos = base64.b64encode(f.read()).decode()
    return f"data:image/{mime};base64,{datos}"


def tarjeta(titulo, imagen, ancho, descripcion, etiqueta, url):
    html = (
        '<div class="tarjeta">'
        f"<h3>{titulo}</h3>"
        f'<img src="{imagen_base64(imagen)}" width="{ancho}">'
        f"<p>{descripcion}</p>"
        f'<p>{etiqueta}: <a href="{url}" target="_blank">Enlace</a></p>'
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    tarjeta(
        "Conversión de texto a voz",
        "txt_to_audio2.png",
        190,
        "En el siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial",
        "Texto a voz",
        "https://visionapp-ljxmcpt7mvoasvtogiba9y.streamlit.app/",
    )
    tarjeta(
        "Reconocimiento de Objetos",
        "txt_to_audio.png",
        200,
        "En el siguiente enlace veremos cómo se detectan objetos en imágenes.",
        "YOLO",
        "https://yolov5cmc.streamlit.app/",
    )
    tarjeta(
        "Entrenando Modelos",
        "OIG5.jpg",
        200,
        "En el siguiente enlace veremos cómo puedes usar tu modelo entrenado.",
        "YOLO",
        "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
    )

with col2:
    tarjeta(
        "Conversión de voz a texto",
        "OIG8.jpg",
        200,
        "En el siguiente enlace veremos una aplicación que usa la conversión de voz a texto.",
        "Voz a texto",
        "https://traductorw.streamlit.app/",
    )
    tarjeta(
        "Análisis de Datos",
        "data_analisis.png",
        190,
        "En el siguiente enlace veremos cómo se pueden analizar datos usando agentes.",
        "Datos",
        "https://dataagente.streamlit.app/",
    )
    tarjeta(
        "Transcriptor Audio y Video",
        "OIG3.jpg",
        200,
        "En el siguiente enlace veremos cómo realizamos transcripciones de audio/video.",
        "Transcriptor",
        "https://transcript-whisper.streamlit.app/",
    )

with col3:
    tarjeta(
        "Generación en Contexto",
        "Chat_pdf.png",
        190,
        "En el siguiente enlace veremos una aplicación que usa RAG a partir de un documento (PDF).",
        "RAG",
        "https://chatpdf-cc.streamlit.app/",
    )
    tarjeta(
        "Análisis de Imagen",
        "OIG4.jpg",
        200,
        "En el siguiente enlace veremos la capacidad de análisis en imágenes.",
        "Vision",
        "https://vision2-gpt4o.streamlit.app/",
    )
    tarjeta(
        "Sistema Ciberfísico",
        "OIG6.jpg",
        200,
        "En el siguiente enlace veremos la capacidad de interacción con el mundo físico.",
        "Vision",
        "https://vision2-gpt4o.streamlit.app/",
    )
