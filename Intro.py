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
.tarjeta a.boton {
    display: inline-block;
    background-color: #FFD6E8;
    color: #8A1C55;
    font-weight: bold;
    text-decoration: none;
    padding: 8px 18px;
    border-radius: 10px;
    border: 1px solid #F5A9CB;
}
.tarjeta a.boton:hover {
    background-color: #FFC2DC;
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


def tarjeta(titulo, imagen, ancho, etiqueta, url):
    html = (
        '<div class="tarjeta">'
        f"<h3>{titulo}</h3>"
        f'<img src="{imagen_base64(imagen)}" width="{ancho}">'
        f"<p>{etiqueta}</p>"
        f'<a class="boton" href="{url}" target="_blank">Ir a la app</a>'
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    tarjeta(
        "Análisis de Imagen",
        "gatolente.jpg",
        190,
        "Vision",
        "https://visionapp-ljxmcpt7mvoasvtogiba9y.streamlit.app/",
    )
    tarjeta(
        "Reconocimiento de Objetos",
        "txt_to_audio.png",
        200,
        "YOLO",
        "https://yolov5cmc.streamlit.app/",
    )
    tarjeta(
        "Entrenando Modelos",
        "OIG5.jpg",
        200,
        "YOLO",
        "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
    )

with col2:
    tarjeta(
        "Conversión de voz a texto",
        "traductor.jpg",
        200,
        "Voz a texto",
        "https://traductor-8dwapkhih9hxki5d8qzfx6.streamlit.app/",
    )
    tarjeta(
        "Análisis de Datos",
        "data_analisis.png",
        190,
        "Datos",
        "https://dataagente.streamlit.app/",
    )
    tarjeta(
        "Transcriptor Audio y Video",
        "OIG3.jpg",
        200,
        "Transcriptor",
        "https://transcript-whisper.streamlit.app/",
    )

with col3:
    tarjeta(
        "Generación en Contexto",
        "Chat_pdf.png",
        190,
        "RAG",
        "https://chatpdf-cc.streamlit.app/",
    )
    tarjeta(
        "Análisis de Imagen",
        "OIG4.jpg",
        200,
        "Vision",
        "https://vision2-gpt4o.streamlit.app/",
    )
    tarjeta(
        "Sistema Ciberfísico",
        "OIG6.jpg",
        200,
        "Vision",
        "https://vision2-gpt4o.streamlit.app/",
    )
