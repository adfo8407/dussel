import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cuadro Sinóptico: Dussel",
                   page_icon="🦅", layout="wide")

# Estilos personalizados para darle un toque académico y humanístico
st.markdown("""
    <style>
    .titulo-principal { font-size: 36px; font-weight: bold; color: #2C3E50; }
    .instrucciones { font-size: 18px; color: #34495E; font-style: italic; }
    .rama-titulo { font-size: 22px; font-weight: bold; color: #8E44AD; }
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown('<p class="titulo-principal">☀️ Cuadro Sinóptico Interactivo: Europa, modernidad y eurocentrismo 🦅</p>', unsafe_allow_html=True)
st.write("**Autor:** Enrique Dussel | **Área:** Ciencias Sociales y Filosofía Latinoamericana")
st.markdown('<p class="instrucciones">📜 Instrucciones: Lee las premisas del cuadro sinóptico y completa los espacios en blanco con los conceptos clave del texto. Presiona "Verificar Respuestas" al final para evaluar tu comprensión.</p>', unsafe_allow_html=True)
st.divider()

# Variables de estado para las respuestas
respuestas_correctas = {
    "q1": ["semita", "semítico"],
    "q2": ["romanticismo", "romanticismo aleman", "romanticismo alemán"],
    "q3": ["emancipación", "emancipacion", "salida"],
    "q4": ["1492"],
    "q5": ["centro"],
    "q6": ["periferia", "periferias"],
    "q7": ["conquiro"],
    "q8": ["violencia", "guerra", "dominación"],
    "q9": ["trans-modernidad", "transmodernidad", "trans modernidad"]
}

# --- CUADRO SINÓPTICO ---

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<p class="rama-titulo">🏺 1. El concepto de "Europa"</p>',
                unsafe_allow_html=True)
    with st.expander("Deslizamiento semántico", expanded=True):
        st.write("Dussel argumenta que la mitológica Europa tiene orígenes fenicios, es decir, un origen oriental y no occidental.")
        q1 = st.text_input(
            "La mitológica Europa es hija de fenicios, de un origen: ________", key="q1")

        st.write(
            "La narrativa clásica de la historia es una invención tardía y racista.")
        q2 = st.text_input(
            "La secuencia unilineal Grecia-Roma-Europa es un invento ideológico del ________ alemán del siglo XVIII.", key="q2")

with col2:
    st.markdown('<p class="rama-titulo">🌎 2. Dos Conceptos de Modernidad</p>',
                unsafe_allow_html=True)
    with st.expander("Visión Eurocéntrica vs. Mundial", expanded=True):
        st.write("**Visión Eurocéntrica (Provinciana):**")
        q3 = st.text_input(
            "Considera que la modernidad es puramente intra-europea, vista como una ________ de la inmadurez (según Kant y Habermas).", key="q3")

        st.write("**Visión Mundial (Histórica):**")
        q4 = st.text_input(
            "La modernidad inicia empíricamente con la expansión y el descubrimiento de América en el año ________.", key="q4")
        q5 = st.text_input(
            "Europa se constituye por primera vez como el ________ de la Historia Mundial...", key="q5")
        q6 = st.text_input(
            "...dejando a todas las demás culturas (América Latina, África, Asia) como su ________.", key="q6")

with col3:
    st.markdown('<p class="rama-titulo">🐆 3. El Mito y la Transmodernidad</p>',
                unsafe_allow_html=True)
    with st.expander("Crítica y Proyecto de Liberación", expanded=True):
        st.write("La racionalidad europea oculta un reverso de dominación.")
        q7 = st.text_input(
            "El 'ego cogito' (yo pienso) fue antecedido por el 'ego ________' (yo conquisto) que impuso su voluntad al indio americano.", key="q7")

        st.write(
            "El Mito de la Modernidad justifica la dominación como un proceso 'civilizatorio'.")
        q8 = st.text_input(
            "Al oponerse el 'bárbaro' al proceso civilizador, la modernidad justifica la ________ y el sacrificio de las víctimas (indígenas, esclavos).", key="q8")

        st.write("**Superación:**")
        q9 = st.text_input(
            "El proyecto mundial de liberación que busca la co-realización solidaria entre el Centro y la Alteridad negada (la Periferia) se denomina ________.", key="q9")

st.divider()

# Botón de verificación
if st.button("🦅 Verificar Respuestas 🌽"):
    aciertos = 0
    respuestas_usuario = {
        "q1": q1.strip().lower(), "q2": q2.strip().lower(), "q3": q3.strip().lower(),
        "q4": q4.strip().lower(), "q5": q5.strip().lower(), "q6": q6.strip().lower(),
        "q7": q7.strip().lower(), "q8": q8.strip().lower(), "q9": q9.strip().lower()
    }

    # Evaluar
    for key, correctas in respuestas_correctas.items():
        if respuestas_usuario[key] in correctas:
            aciertos += 1

    # Resultados
    st.subheader(f"Resultados: {aciertos} / 9 aciertos")
    if aciertos == 9:
        st.success("¡Excelente! ☀️ Has comprendido a la perfección la crítica al eurocentrismo y el proyecto de la Transmodernidad propuesto por Dussel.")
        st.balloons()
    elif aciertos >= 5:
        st.warning("¡Buen intento! 🏺 Tienes una buena noción del texto, pero te recomendamos repasar las diferencias entre el paradigma eurocéntrico y mundial.")
    else:
        st.error("Es necesario repasar la lectura. 📜 Recuerda prestar atención a cómo Dussel desmitifica la linealidad histórica y propone la centralidad de 1492 en el Sistema-mundo.")

    with st.expander("Ver respuestas correctas (Solo si ya lo intentaste)"):
        st.markdown("""
        1. **semita** (Europa venía de Oriente)
        2. **romanticismo** (Fines del siglo XVIII)
        3. **emancipación** (Salida de la inmadurez)
        4. **1492** (Inicio del sistema-mundo)
        5. **centro** (Hegemonía global)
        6. **periferia** (Zonas dominadas/colonizadas)
        7. **conquiro** (Yo conquisto, antes del yo pienso)
        8. **violencia** (Guerra justa colonial justificada por el mito)
        9. **Trans-modernidad** (Incorporación de la alteridad)
        """)
