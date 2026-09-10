"""Series ilustrativas. No son precios de mercado en tiempo real."""

import numpy as np
import pandas as pd

ACTIVOS = {
    "ECOPETROL": {"precio": 2160.0, "vol": 0.018, "moneda": "COP", "semilla": 11},
    "BANCOLOMBIA": {"precio": 34200.0, "vol": 0.014, "moneda": "COP", "semilla": 23},
    "TES 2028": {"precio": 105.4, "vol": 0.004, "moneda": "precio", "semilla": 41},
    "USDCOP": {"precio": 4120.0, "vol": 0.007, "moneda": "COP", "semilla": 59},
}


def serie_precios(nombre, dias=120):
    cfg = ACTIVOS[nombre]
    rng = np.random.default_rng(cfg["semilla"])
    ret = rng.normal(0.0003, cfg["vol"], dias)
    precio = cfg["precio"] * np.exp(np.cumsum(ret))
    fechas = pd.date_range(end=pd.Timestamp.today().normalize(), periods=dias, freq="B")
    return pd.DataFrame({"fecha": fechas, "precio": precio})


def panel(nombres, dias=120):
    piezas = []
    for nom in nombres:
        d = serie_precios(nom, dias=dias)
        d["activo"] = nom
        piezas.append(d)
    return pd.concat(piezas, ignore_index=True)


def ultimo_y_delta(nombre):
    d = serie_precios(nombre)
    ultimo = float(d["precio"].iloc[-1])
    previo = float(d["precio"].iloc[-2])
    return ultimo, ultimo - previo
