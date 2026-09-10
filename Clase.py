"""Página de inicio: introducción de la Clase 7."""

from lib import style

import streamlit as st

# ========== PERSONALICE AQUÍ ==========
NOMBRE = "Su nombre"
# ======================================

style.arranque("Clase")
style.barra_lateral(NOMBRE)

style.hero(
    "Clase 7 : Oscar Orozco",
    "Git, GitHub y Streamlit. La introducción de hoy está en esta página; las demás son el tablero.",
    marca="Machine Learning en Economía y Finanzas · FCEA",
)

g1, g2, g3, g4, g5 = st.columns(5)
g1.metric("Git", "versiono")
g2.metric("GitHub", "comparto")
g3.metric("Streamlit", "construyo")
g4.metric("Cloud", "publico")
g5.metric("Modificando", "Mi app")


c1, c2, c3, c4 = st.columns(4)
c1.page_link("pages/1_Mercado.py", label="Mercado")
c2.page_link("pages/2_Portafolio.py", label="Portafolio")
c3.page_link("pages/3_Calculadora.py", label="Calculadora")
c4.page_link("pages/4_Laboratorio.py", label="Laboratorio")

tab_git, tab_cmds, tab_gh, tab_st, tab_pub = st.tabs(
    ["Git", "Comandos Git", "GitHub", "Streamlit", "Publicar"]
)

with tab_git:
    st.header("Sin historial")
    st.code(
        "proyecto_final.py\n"
        "proyecto_final_v2.py\n"
        "proyecto_final_v3.py\n"
        "proyecto_final_ahora_si.py\n"
        "proyecto_final_definitivo.py",
        language="text",
    )
    st.write("Git registra estados del proyecto: versión 1 → commit → versión 2 → commit.")
    st.subheader("Tres zonas")
    st.code(
        "Working Directory\n"
        "        ↓  git add\n"
        "   Staging Area\n"
        "        ↓  git commit\n"
        "  Repositorio Git",
        language="text",
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.write("**Repositorio** — carpeta + historial")
    c2.write("**Commit** — una foto con mensaje")
    c3.write("**Historial** — la secuencia de fotos")
    c4.write("**Branch** — una línea de trabajo (`main`)")

with tab_cmds:
    st.header("Comandos de Git")
    st.code(
        "git init\n"
        "git status\n"
        "git add .\n"
        'git commit -m "Primera versión de la aplicación"\n'
        "git log\n"
        "git branch",
        language="bash",
    )
    st.caption("init · status · add · commit · log · branch")

with tab_gh:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Git")
        st.write("Control de versiones")
        st.write("Computador local")
        st.write("Historial del proyecto")
    with col_b:
        st.subheader("GitHub")
        st.write("Plataforma en la nube")
        st.write("Repositorio remoto")
        st.write("Compartir y colaborar")
    st.header("Comandos con el remoto")
    st.code(
        "git clone URL\n"
        "git remote add origin URL\n"
        "git remote -v\n"
        "git pull\n"
        "git push\n"
        "git push -u origin main",
        language="bash",
    )
    st.write("`git pull` trae cambios. `git push` envía cambios.")
    st.code(
        "git pull\n"
        "git status\n"
        "git add .\n"
        'git commit -m "Agrega nuevo gráfico"\n'
        "git push",
        language="bash",
    )
    st.write("En el remoto también aparecen: README.md, .gitignore, commits y, en equipo, pull requests.")

with tab_st:
    st.header("Streamlit")
    st.write("Framework de Python que convierte un script en una aplicación web.")
    st.code(
        "import streamlit as st\n\n"
        'st.title("Mi primera aplicación")\n'
        'st.write("Hola mundo")',
        language="python",
    )
    st.code("streamlit run Clase.py", language="bash")

    st.subheader("Texto")
    st.code(
        'st.title("Dashboard financiero")\n'
        'st.header("Mercado")\n'
        'st.subheader("Precios")\n'
        'st.write("Hola mundo")\n'
        'st.markdown("Tasa **8%**")',
        language="python",
    )
    st.subheader("Interacción")
    st.code(
        'activo = st.selectbox("Activo", ["TES", "CDT", "Acción"])\n'
        'monto = st.number_input("Monto", 0)\n'
        'tasa = st.slider("Tasa", 0.0, 0.2, 0.08)\n'
        'nombre = st.text_input("Cliente")\n'
        'if st.button("Calcular"):\n'
        "    st.write(monto * tasa)",
        language="python",
    )
    st.subheader("Datos, gráficos y layout")
    st.code(
        'st.metric("Precio", "2,150", "+30")\n'
        "st.dataframe(df)\n"
        "st.table(df)\n"
        "st.line_chart(df)\n"
        "st.bar_chart(df)\n"
        "st.area_chart(df)\n"
        "st.plotly_chart(fig)\n"
        'st.sidebar.text_input("Nombre")\n'
        "c1, c2 = st.columns(2)\n"
        't1, t2 = st.tabs(["Serie", "Tabla"])\n'
        'with st.expander("Notas"):\n'
        '    st.write("Fuente")',
        language="python",
    )

with tab_pub:
    st.header("Carpeta del proyecto")
    st.code(
        "App/\n"
        "├── Clase.py\n"
        "├── pages/\n"
        "├── requirements.txt\n"
        "├── README.md\n"
        "└── .gitignore",
        language="text",
    )
    st.write("`requirements.txt` lista las librerías que Cloud instala (streamlit, pandas, plotly).")
    st.header("De esta carpeta a la URL")
    st.code(
        "Python → Clase.py → Streamlit → git add → git commit → git push\n"
        "→ GitHub → Streamlit Community Cloud → aplicación web",
        language="text",
    )
    st.code(
        "git status\n"
        "git add .\n"
        'git commit -m "Actualiza título del dashboard"\n'
        "git push",
        language="bash",
    )
    st.write(
        "En share.streamlit.io: repositorio → rama `main` → archivo principal `App/Clase.py` → Deploy. "
        "Un `git push` posterior actualiza la app."
    )
    with st.expander(".gitignore"):
        st.code(".env\n.venv/\n__pycache__/\n.streamlit/secrets.toml", language="text")
    st.caption("Personalice el bloque del inicio de cada archivo y las páginas Mercado, Portafolio, Calculadora y Laboratorio.")
