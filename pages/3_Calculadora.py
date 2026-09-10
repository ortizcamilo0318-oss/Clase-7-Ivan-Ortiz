"""Calculadora de valor futuro y presente."""

from lib import style

import streamlit as st

# ========== PERSONALICE AQUÍ ==========
CAPITAL = 5_000_000
TASA = 0.08
ANIOS = 3
MONTO_FUTURO = 6_000_000
# ======================================

style.arranque("Calculadora")
style.barra_lateral()
style.hero("Calculadora: Oscar Orozco", "Valor futuro de un capital y valor presente de un monto.")

st.latex(r"VF = C\,(1+r)^{n}\qquad VP = \dfrac{M}{(1+r)^{n}}")

c1, c2, c3, c4 = st.columns(4)
capital = c1.number_input("Capital C (COP)", min_value=0, value=CAPITAL, step=100_000)
tasa = c2.slider("Tasa r", 0.0, 0.25, TASA, 0.005)
anios = c3.number_input("Años n", min_value=1, max_value=30, value=ANIOS)
monto = c4.number_input("Monto futuro M (COP)", min_value=0, value=MONTO_FUTURO, step=100_000)

vf = capital * (1 + tasa) ** anios
interes = vf - capital
vp = monto / (1 + tasa) ** anios

x, y, z = st.columns(3)
x.metric("Valor futuro", f"${vf:,.0f}")
y.metric("Interés", f"${interes:,.0f}")
z.metric("Valor presente de M", f"${vp:,.0f}")

st.divider()
st.subheader("st.form")
with st.form("nota"):
    nota = st.text_area("Nota", "Escenario base.")
    enviado = st.form_submit_button("Registrar nota")
if enviado:
    st.write(nota)

st.progress(min(1.0, tasa / 0.25), text=f"st.progress — tasa {tasa:.1%}")
