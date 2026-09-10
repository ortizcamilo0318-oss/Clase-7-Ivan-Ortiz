"""Estilo compartido: paleta del curso y CSS mínimo."""

import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

NAVY = "#1B365D"
SLATE = "#4A6FA5"
GOLD = "#C9A227"

COLORES = [NAVY, SLATE, GOLD, "#2E7D32", "#8D6E63", "#0277BD"]


def configurar_pagina(titulo, icono="📊"):
    st.set_page_config(
        page_title=titulo,
        page_icon=icono,
        layout="wide",
        initial_sidebar_state="expanded",
    )


def inyectar_css():
    st.markdown(
        """
        <style>
        @import url("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,560;9..144,650&family=Source+Sans+3:wght@400;500;600&display=swap");

        html, body, [class*="css"] { font-family: "Source Sans 3", sans-serif; }
        .stApp { background: #F6F3EE; }
        h1, h2, h3 { font-family: "Fraunces", serif !important; color: #1B365D !important; letter-spacing: -0.02em; }
        [data-testid="stSidebar"] { background: #1B365D; }
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #F6F3EE !important; }
        [data-testid="stSidebar"] input { color: #1B365D !important; background: #fff !important; }
        .hero {
            background: linear-gradient(135deg, #1B365D 0%, #4A6FA5 78%);
            border-radius: 22px;
            color: #fff;
            margin-bottom: 1.1rem;
            padding: 1.65rem 1.85rem 1.45rem;
        }
        .hero h1 { color: #fff !important; font-size: 2.05rem; margin: 0 0 0.35rem 0; }
        .hero p { color: rgba(255,255,255,0.88); font-size: 1.05rem; margin: 0; }
        .marca { color: #E8C547; font-size: 0.78rem; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; }
        div[data-testid="stMetric"] {
            background: #fff;
            border: 1px solid #E6E1D8;
            border-radius: 16px;
            padding: 0.7rem 0.9rem;
        }
        .hint {
            background: #fff;
            border-left: 4px solid #C9A227;
            border-radius: 10px;
            color: #1B365D;
            font-size: 0.92rem;
            margin: 0.4rem 0 1rem;
            padding: 0.65rem 0.9rem;
        }
        footer { visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(titulo, subtitulo, marca="Mesa de mercado · FCEA"):
    st.markdown(
        f'<div class="hero"><div class="marca">{marca}</div>'
        f"<h1>{titulo}</h1><p>{subtitulo}</p></div>",
        unsafe_allow_html=True,
    )


def pista(texto):
    st.markdown(f'<div class="hint">{texto}</div>', unsafe_allow_html=True)


def aplicar_plotly():
    pio.templates["fcea"] = go.layout.Template(
        layout=go.Layout(
            font=dict(family="Source Sans 3", color=NAVY),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            colorway=COLORES,
            xaxis=dict(gridcolor="#E6E1D8", zeroline=False),
            yaxis=dict(gridcolor="#E6E1D8", zeroline=False),
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
            margin=dict(l=40, r=20, t=30, b=40),
        )
    )
    pio.templates.default = "fcea"


def barra_lateral(nombre_default="Su nombre"):
    if "alias" not in st.session_state:
        st.session_state.alias = nombre_default
    with st.sidebar:
        st.markdown("**Clase 7 · FCEA**")
        st.caption("Git · GitHub · Streamlit")
        st.text_input("Nombre en el tablero", key="alias")
    return st.session_state.alias


def arranque(titulo_pestana):
    configurar_pagina(titulo_pestana)
    inyectar_css()
    aplicar_plotly()
