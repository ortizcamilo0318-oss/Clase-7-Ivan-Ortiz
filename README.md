# Mesa de mercado — app Streamlit (Clase 7)

La **introducción de la clase** (Git, GitHub, Streamlit y publicación) está en **`Clase.py`**, la página de inicio. Mercado, Portafolio, Calculadora y Laboratorio son el tablero para personalizar.

Entregable: la app en Streamlit Community Cloud.

```text
App/
├── Clase.py               ← inicio (punto de entrada)
├── pages/
│   ├── 1_Mercado.py
│   ├── 2_Portafolio.py
│   ├── 3_Calculadora.py
│   └── 4_Laboratorio.py
├── lib/
├── .streamlit/config.toml
├── requirements.txt
└── .gitignore
```

## Cómo correrla

```bash
cd Clase_7/App
pip install -r requirements.txt
streamlit run Clase.py
```

## Qué personalizar

Bloque `# ========== PERSONALICE AQUÍ ==========`:

| Archivo | Qué cambiar |
|---------|-------------|
| `Clase.py` | `NOMBRE` |
| `pages/1_Mercado.py` | `ACTIVO_INICIAL`, `DIAS_INICIAL` |
| `pages/2_Portafolio.py` | `ACTIVOS_INICIALES` |
| `pages/3_Calculadora.py` | `CAPITAL`, `TASA`, `ANIOS`, `MONTO_FUTURO` |
| `pages/4_Laboratorio.py` | `TEXTO` |

## Entrega

```bash
git status
git add .
git commit -m "Personaliza la mesa de mercado"
git push
```

En [share.streamlit.io](https://share.streamlit.io): archivo principal **`App/Clase.py`**.
