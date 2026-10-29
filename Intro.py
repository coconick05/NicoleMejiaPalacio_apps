import base64
import os
import streamlit as st

st.set_page_config(page_title="Portafolio Nicole Mejía", layout="wide")

# ---------------------------------------------------------------------------
# Estado de navegación
# ---------------------------------------------------------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"


def ir_a(pagina):
    st.session_state.pagina = pagina


# ---------------------------------------------------------------------------
# Título y sidebar (se muestran en todas las páginas)
# ---------------------------------------------------------------------------
st.markdown(
    "<h1 style='color: #FF00FF;'>Aplicaciones de Inteligencia Artificial.</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color: #C8A2C8; font-size: 1.1rem;'>Portofolio Nicole Mejía</p>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    if st.session_state.pagina != "home":
        st.button("🏠 Volver al inicio", on_click=ir_a, args=("home",), key="side_home")

# ---------------------------------------------------------------------------
# Estilos
# ---------------------------------------------------------------------------
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
/* Tarjetas del home (más grandes) */
.tarjeta-home {
    background-color: #E6DAFA;
    border: 1px solid #C9B3F0;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 12px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    text-align: center;
}
.tarjeta-home h2 {
    color: #4B2C82;
    margin: 0 0 14px 0;
}
.tarjeta-home img {
    border-radius: 14px;
    width: 260px;
    max-width: 100%;
    margin-bottom: 14px;
}
.tarjeta-home p {
    color: #2E2447;
    font-size: 1rem;
    margin: 0;
}
</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------------------
def imagen_base64(ruta):
    extension = ruta.split(".")[-1].lower()
    mime = "jpeg" if extension in ("jpg", "jpeg") else extension
    with open(ruta, "rb") as f:
        datos = base64.b64encode(f.read()).decode()
    return f"data:image/{mime};base64,{datos}"


def tarjeta(titulo, imagen, ancho, etiqueta, url):
    # Si la imagen no existe todavía, la tarjeta se muestra sin imagen
    if os.path.exists(imagen):
        img_html = f'<img src="{imagen_base64(imagen)}" width="{ancho}">'
    else:
        img_html = ""
    html = (
        '<div class="tarjeta">'
        f"<h3>{titulo}</h3>"
        f"{img_html}"
        f"<p>{etiqueta}</p>"
        f'<a class="boton" href="{url}" target="_blank">Ir a la app</a>'
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


def tarjeta_home(titulo, imagen, descripcion):
    html = (
        '<div class="tarjeta-home">'
        f"<h2>{titulo}</h2>"
        f'<img src="{imagen_base64(imagen)}">'
        f"<p>{descripcion}</p>"
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Datos de los portafolios: cada lista interna es una columna.
# Cada tarjeta tiene este formato:
#   (
#       "TÍTULO de la tarjeta",
#       "NOMBRE_DE_LA_IMAGEN.jpg",
#       ANCHO_DE_LA_IMAGEN,
#       "TEXTO debajo de la imagen",
#       "LINK de la app",
#   )
# ---------------------------------------------------------------------------
PORTAFOLIO_1 = [
    [
        (
            "Análisis de Imagen",
            "gatolente.jpg",
            190,
            "Vision",
            "https://visionapp-ljxmcpt7mvoasvtogiba9y.streamlit.app/",
        ),
        (
            "Reconocimiento de Objetos",
            "imagenes.jpg",
            200,
            "Objetos de nicky",
            "https://wptnprewrzw6dv4shnnlv3.streamlit.app/",
        ),
        (
            "Asistente PDF",
            "chatt.jpg",
            200,
            "La info que necesitas",
            "https://chatpdf-jnmlyvpnjjaeeicfmdl9c7.streamlit.app/",
        ),
        (
            "Mi primera app",
            "gatocool.jpg",
            200,
            "La number one",
            "https://mi-primera-app-bbi28p6j4jergbkncc7mmy.streamlit.app/",
        ),
    ],
    [
        (
            "Conversión de voz a texto",
            "traductor.jpg",
            200,
            "Voz a texto",
            "https://traductor-8dwapkhih9hxki5d8qzfx6.streamlit.app/",
        ),
        (
            "Análisis de emociones",
            "emociones.jpg",
            190,
            "Feliz? Triste?",
            "https://sentimenta-3qti2sjcqeeyerxz9wk32j.streamlit.app/",
        ),
        (
            "Detección de Objetos",
            "detecdog.jpg",
            200,
            "Sube la imagen y detecta los objetos",
            "https://yolov5-nzghwfbupwoc2vvfnszrpd.streamlit.app/",
        ),
        (
            "Conversión de Texto a Audio",
            "Leecuentos.jpg",
            200,
            "Lector de cuentos",
            "https://tgfvsxrnw848nx7zarurro.streamlit.app/",
        ),
    ],
    [
        (
            "Analizar texto",
            "analizatexto.jpg",
            190,
            "texto",
            "https://tdfesp-hem4fsyq6t57nd93acwudh.streamlit.app/",
        ),
        (
            "Lector y traductor",
            "pensar.jpg",
            200,
            "Lee y traduce",
            "https://ocr-audio-bdzzbfgrxs5s6xpvssa5ji.streamlit.app/",
        ),
        (
            "Nube de palabras",
            "nube.jpg",
            200,
            "Crea tu nube",
            "https://wordcloud-mvsd7ygclnxdaentwxmvnq.streamlit.app/",
        ),
    ],
]

# 10 espacios en total: 4 + 3 + 3
PORTAFOLIO_2 = [
    # ----------------------- COLUMNA 1 (espacios 1 al 4) -----------------------
    [
        # Espacio 1 (ya tiene app)
        (
            "Dibujemosss",
            "gatodibujon.jpg",
            190,
            "Dibuja como quieras",
            "https://kmfo5yxvnd73kfeskd4eiz.streamlit.app/",
        ),
        # Espacio 2
        (
            "Analiza tu PDF",
            "gatopdf.jpg",
            200,
            "Carga y analiza",
            "https://chatpdf-jnmlyvpnjjaeeicfmdl9c7.streamlit.app/",
        ),
        # Espacio 3
        (
            "Análisis de Imagen",
            "analizaimagen.jpg",
            200,
            "Analicemos la imagen",
            "https://visionapp-ljxmcpt7mvoasvtogiba9y.streamlit.app/",
        ),
        # Espacio 4
        (
            "Lector de Sensor MQTT",
            "gatomqtt.jpg",
            200,
            "recibe los datos",
            "https://recepmqttnm.streamlit.app/",
        ),
    ],
    # ----------------------- COLUMNA 2 (espacios 5 al 7) -----------------------
    [
        # Espacio 5 (ya tiene app)
        (
            "Detección de Dígitos Escritos a Mano",
            "gatonumerico.jpg",
            200,
            "Dibuja el número y la máquina lo detecta",
            "https://mnistpred-ienskwbtzv5nhceefcvmyn.streamlit.app/",
        ),
        # Espacio 6
        (
            "Visión por Computador",
            "vision2.jpg",
            200,
            "Reconoce y detecta",
            "https://visionunion2.streamlit.app/",
        ),
        # Espacio 7
        (
            "Tablero para pintar",
            "gatopintor.jpg",
            200,
            "Pinta, pinta, pinta",
            "https://b4ehllrs5tcy7fcofegbom.streamlit.app/",
        ),
    ],
    # ----------------------- COLUMNA 3 (espacios 8 al 10) ----------------------
    [
        # Espacio 8 (ya tiene app)
        (
            "Tablero Inteligente",
            "gatocontablero.jpg",
            200,
            "Dibuja e interpreta",
            "https://eamxbaxpgmfkh7kp2bfemg.streamlit.app/",
        ),
        # Espacio 9
        (
            "Título del espacio 9",
            "imagen9.jpg",
            200,
            "Texto debajo de la imagen 9",
            "https://link-de-la-app-9.streamlit.app/",
        ),
        # Espacio 10
        (
            "Título del espacio 10",
            "imagen10.jpg",
            200,
            "Texto debajo de la imagen 10",
            "https://link-de-la-app-10.streamlit.app/",
        ),
    ],
]


def mostrar_portafolio(columnas_datos):
    st.button("← Volver al inicio", on_click=ir_a, args=("home",), key="top_home")
    columnas = st.columns(len(columnas_datos))
    for col, apps in zip(columnas, columnas_datos):
        with col:
            for app in apps:
                tarjeta(*app)


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
pagina = st.session_state.pagina

if pagina == "home":
    _, izq, der, _ = st.columns([0.5, 2, 2, 0.5])

    with izq:
        tarjeta_home(
            "Primer portafolio",
            "gatolente.jpg",
            "Mis primeras aplicaciones de IA: visión, voz, texto y más.",
        )
        st.button(
            "Entrar",
            on_click=ir_a,
            args=("portafolio1",),
            key="entrar_1",
            use_container_width=True,
        )

    with der:
        tarjeta_home(
            "Segundo portafolio",
            "gatodibujon.jpg",
            "Nuevas aplicaciones y proyectos creativos.",
        )
        st.button(
            "Entrar",
            on_click=ir_a,
            args=("portafolio2",),
            key="entrar_2",
            use_container_width=True,
        )

elif pagina == "portafolio1":
    st.subheader("Primer portafolio")
    mostrar_portafolio(PORTAFOLIO_1)

elif pagina == "portafolio2":
    st.subheader("Segundo portafolio")
    mostrar_portafolio(PORTAFOLIO_2)
