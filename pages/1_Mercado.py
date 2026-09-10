"""Mercado: series y gráficos."""

from lib import data, style

import plotly.express as px
import streamlit as st

# ========== PERSONALICE AQUÍ ==========
ACTIVO_INICIAL = "ECOPETROL"
DIAS_INICIAL = 90
# ======================================

style.arranque("Mercado")
style.barra_lateral()
style.hero("Mercado:Oscar Orozco", "Precio y retorno del activo seleccionado.")

nombres = list(data.ACTIVOS.keys())
idx = nombres.index(ACTIVO_INICIAL) if ACTIVO_INICIAL in nombres else 0
activo = st.selectbox("Activo", nombres, index=idx)
dias = st.slider("Ventana (días hábiles)", 90, 360, DIAS_INICIAL)
vista = st.radio("Vista", ["Precio", "Retorno"], horizontal=True)

serie = data.serie_precios(activo, dias=dias)
serie["retorno"] = serie["precio"].pct_change()
grafico = serie.dropna() if vista == "Retorno" else serie
y = "retorno" if vista == "Retorno" else "precio"

ultimo = float(serie["precio"].iloc[-1])
delta = float(serie["precio"].iloc[-1] - serie["precio"].iloc[-2])

k1, k2, k3 = st.columns(3)
k1.metric("Último", f"{ultimo:,.2f}", f"{delta:+.2f}")
k2.metric("Mínimo", f"{serie['precio'].min():,.2f}")
k3.metric("Máximo", f"{serie['precio'].max():,.2f}")

tab_linea, tab_area, tab_plotly, tab_barra = st.tabs(
    ["st.line_chart", "st.area_chart", "st.plotly_chart", "st.bar_chart"]
)
with tab_linea:
    st.line_chart(grafico, x="fecha", y=y)
with tab_area:
    st.area_chart(grafico, x="fecha", y=y)
with tab_plotly:
    fig = px.line(grafico, x="fecha", y=y, title=f"{activo} · {vista}")
    fig.update_traces(line_width=2.4)
    st.plotly_chart(fig, width="stretch")
with tab_barra:
    st.bar_chart(serie.tail(12), x="fecha", y="precio")

with st.expander("Últimas observaciones"):
    st.dataframe(serie.tail(8), width="stretch")
