"""Portafolio: pesos, tabla y descarga."""

from lib import data, style

import pandas as pd
import plotly.express as px
import streamlit as st

# ========== PERSONALICE AQUÍ ==========
ACTIVOS_INICIALES = ["ECOPETROL", "TES 2028"]
# ======================================

style.arranque("Portafolio")
style.barra_lateral()
style.hero("Portafolio", "Composición por pesos y archivo CSV.")

todos = list(data.ACTIVOS.keys())
elegidos = st.multiselect(
    "Activos",
    todos,
    default=ACTIVOS_INICIALES
)

if not elegidos:
    elegidos = todos

pesos = {}

cols = st.columns(len(elegidos))

for col, nom in zip(cols, elegidos):
    pesos[nom] = col.slider(
        nom,
        min_value=0,
        max_value=100,
        value=max(1, int(100 / len(elegidos))),
        key=f"w_{nom}"
    )

total = sum(pesos.values())

if total == 0:
    total = 1

mostrar_crudo = st.checkbox(
    "Mostrar st.table",
    value=True
)

filas = []

for nom in elegidos:
    ultimo, _ = data.ultimo_y_delta(nom)

    w = pesos[nom] / total

    filas.append({
        "activo": nom,
        "peso": w,
        "precio": ultimo,
        "ponderado": w * ultimo
    })

tabla = pd.DataFrame(filas)

a, b = st.columns([1.2, 1])

with a:
    st.subheader("Composición")

    st.dataframe(
        tabla,
        use_container_width=True
    )

    if mostrar_crudo:
        st.table(tabla)

    csv = tabla.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Descargar CSV",
        csv,
        "portafolio.csv",
        "text/csv"
    )

with b:
    fig = px.bar(
        tabla,
        x="activo",
        y="peso",
        title="Pesos"
    )

    fig.update_layout(
        yaxis_tickformat=".0%"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

c1, c2, c3 = st.columns(3)

c1.metric(
    "Activos",
    str(len(elegidos))
)

c2.metric(
    "Suma de sliders",
    f"{sum(pesos.values()):.0f}"
)

c3.metric(
    "Suma de pesos",
    f"{tabla['peso'].sum():.0%}"
)
