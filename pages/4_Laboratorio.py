"""Laboratorio: comandos de Streamlit visibles."""

from datetime import date

import pandas as pd
import streamlit as st

from lib import style

# ========== PERSONALICE AQUÍ ==========
TEXTO = "Texto de ejemplo"
# ======================================

style.arranque("Laboratorio")
style.barra_lateral()
style.hero("Laboratorio: Oscar Orozco", "Cada comando aparece en pantalla.")

st.subheader("Entradas")
c1, c2 = st.columns(2)
with c1:
    corte = st.date_input("st.date_input", value=date.today())
    escenario = st.radio("st.radio", ["Base", "Estrés", "Optimista"], horizontal=True)
    extra = st.checkbox("st.checkbox", value=True)
    color = st.color_picker("st.color_picker", "#C9A227")
    comentario = st.text_input("st.text_input", TEXTO)
with c2:
    archivo = st.file_uploader("st.file_uploader", type=["csv"])
    if archivo is not None:
        st.dataframe(pd.read_csv(archivo).head(), width="stretch")
    st.code("streamlit run Clase.py", language="bash")
    with st.status("st.status", expanded=True):
        st.write(f"corte = {corte}")
        st.write(f"escenario = {escenario}")

st.divider()
st.subheader("Salidas")
if extra:
    st.markdown(f"st.markdown — acento `{color}` · {comentario}")

g1, g2 = st.columns(2)
g1.scatter_chart(pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 1, 4, 3, 6]}), x="x", y="y")
g2.json({"alias": st.session_state.get("alias", "—"), "comentario": comentario})

st.info("st.info")
st.success("st.success")
st.warning("st.warning")
st.error("st.error")

b1, b2 = st.columns(2)
with b1:
    if st.button("st.balloons"):
        st.balloons()
with b2:
    if st.button("st.snow"):
        st.snow()
