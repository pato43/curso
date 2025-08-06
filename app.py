import streamlit as st
import pandas as pd
from datetime import date

# ─────────────────────────────
# Configuración base
# ─────────────────────────────
st.set_page_config(
    page_title="Programa Integral de Análisis y Ciencia de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────
# Estilos (tema claro, moderno)
# ─────────────────────────────
st.markdown("""
<style>
:root{
  --primary:#2563EB; --bg:#FFFFFF; --bg-soft:#F6F8FC;
  --text:#0F172A; --text-soft:#334155; --line:#E6E9F2;
  --ok:#16A34A; --warn:#B45309; --info:#0EA5E9;
}
html, body, [class*="css"] { font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
section.main > div { padding-top: .4rem; }
h1,h2,h3 { letter-spacing: -0.015em; }
h1 { font-weight:800 }
h2 { margin-top: 0.25rem }
.small { font-size: 0.92rem; color: var(--text-soft); }
.badge { display:inline-block; padding:.28rem .6rem; border-radius:999px; font-weight:600; font-size:.8rem; background:#EEF2FF; color:#3730A3; margin-right:.35rem }
.block { background:var(--bg); border:1px solid var(--line); border-radius:18px; padding:1.1rem; }
.block-soft { background:var(--bg-soft); border:1px solid var(--line); border-radius:18px; padding:1.1rem; }
.kpi { background:var(--bg-soft); border:1px solid var(--line); border-radius:14px; padding:1rem; text-align:center; }
.kpi h4 { font-size:.9rem; margin:.2rem 0; color:var(--text-soft) }
.kpi p { font-size:1.25rem; margin:0; font-weight:800; color:var(--text) }
.list-tight li { margin-bottom:.25rem }
.hr { height:1px; background:var(--line); margin:.8rem 0 1.2rem 0; }
.quote { border-left:4px solid var(--primary); padding:.5rem 0 .5rem .9rem; background:#F8FAFF; border-radius:8px; }
.anchor { font-size:.9rem; color:#475569; }
.pay { display:flex; gap:.5rem; flex-wrap:wrap; }
.pay span{ border:1px solid var(--line); background:white; padding:.35rem .6rem; border-radius:999px; font-size:.85rem; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────
# Encabezado / Hero
# ─────────────────────────────
col1, col2 = st.columns([1.25, 1])
with col1:
    st.markdown("# Programa Integral de **Análisis y Ciencia de Datos**")
    st.markdown(
        "Domina el ciclo completo: **Google Sheets → SQL (SQLite) → Python (pandas/numpy) → "
        "Visualización (matplotlib/plotly) → ML (regresión, clasificación, k-means) → "
        "Series de tiempo (ETS/ARIMA) → App con Streamlit**."
    )
    st.markdown(
        '<span class="badge">Modalidad en línea (Jitsi)</span>'
        '<span class="badge">Grabaciones y materiales incluidos</span>'
        '<span class="badge">Certificación Microsoft en alianza con Tessena</span>',
        unsafe_allow_html=True
    )
with col2:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="kpi"><h4>Duración</h4><p>4 meses</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="kpi"><h4>Ritmo</h4><p>3 clases/sem</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="kpi"><h4>Horario</h4><p>Mar–Mié–Jue<br>8:00–9:00 CDMX</p></div>', unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Propuesta de valor & Modalidad
# ─────────────────────────────
cL, cR = st.columns([1, 1])
with cL:
    st.subheader("¿Por qué este programa?")
    st.markdown("""
- **Aprender haciendo**: proyectos cortos semanales y un **Proyecto Final** con **Streamlit**.
- **Ruta profesional**: de hojas de cálculo a **pipelines reproducibles** y **apps**.
- **Stack actual**: Google Sheets, **SQLite**, Python (pandas/numpy), **visualización** (matplotlib/plotly),
  **ML** con scikit-learn y **series de tiempo** con statsmodels.
- **Enfoque laboral**: análisis útil, métricas claras y **storytelling** para presentar resultados.
    """)
    st.info("**Plataforma de videoclase:** Jitsi. Todas las sesiones quedan grabadas y se comparten con materiales.")
with cR:
    st.subheader("Certificación Microsoft × Tessena")
    st.markdown("""
Al concluir y aprobar el Proyecto Final, recibirás **certificación por parte de Microsoft en alianza con Tessena**,
con **folio verificable** para **LinkedIn** y portafolio. Acredita competencias en:
- Manipulación y análisis de datos
- SQL con SQLite
- Visualización efectiva
- Modelos de ML (supervisado, no supervisado)
- Series de tiempo y despliegue con Streamlit
    """)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Público objetivo & Resultados de aprendizaje
# ─────────────────────────────
c1, c2 = st.columns([1, 1])
with c1:
    st.subheader("¿Para quién es?")
    st.markdown("""
- **Profesionales** que analizan datos (operaciones, marketing, finanzas, logística).
- **Estudiantes** o egresados que buscan **primer rol** en datos.
- **Emprendedores** que requieren tableros e **insights** accionables.
- **Equipos** que desean estandarizar prácticas y entregar valor **rápido**.
    """)
with c2:
    st.subheader("Resultados de aprendizaje")
    st.markdown("""
- Plantear problemas con **métricas de éxito** y supuestos claros.
- Construir datasets limpios con **pandas** y **SQL**; detectar sesgos.
- Comunicar hallazgos con **gráficos persuasivos** y narrativa.
- Entrenar y evaluar **modelos** (regresión, clasificación, k-means) con *best practices*.
- Diseñar **forecasting** con ETS/ARIMA y validar con **backtesting**.
- Entregar una **app Streamlit** lista para usuarios.
    """)

# ─────────────────────────────
# Estructura & Logística del programa
# ─────────────────────────────
st.subheader("Estructura y logística")
colA, colB, colC = st.columns([1.15, 1, 1])
with colA:
    st.markdown("""
**Formato**  
- **Clases en vivo** por **Jitsi** (Mar–Mié–Jue, 8:00–9:00 CDMX).  
- **Grabaciones** y materiales (PDFs, notebooks, scripts, datasets).  
- **Repositorio base** por cohorte y guía de reproducibilidad.
    """)
with colB:
    st.markdown("""
**Materiales y entregables**  
- Mini-proyectos semanales y **quizzes** cortos.  
- Un **Proyecto Final integrador** (app + informe + demo).  
- Rúbrica con criterios técnicos y de comunicación.
    """)
with colC:
    st.markdown("""
**Herramientas**  
- **Google Sheets** y **Looker Studio** (on-line).  
- **SQLite** (local) con **DBeaver** como gestor.  
- **Python** (pandas/numpy/plotly/scikit-learn/statsmodels) y **Streamlit**.
    """)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Requisitos e instalaciones locales
# ─────────────────────────────
st.subheader("Requisitos y software a instalar")
lcol, rcol = st.columns([1, 1])
with lcol:
    st.markdown("""
- **Computadora** con conexión a Internet.  
- **Python 3.11+**  
- **DBeaver** (gestor de base de datos SQLite)  
- **Jupyter** (notebooks)  
- **Streamlit** (despliegue de apps)
    """)
with rcol:
    st.markdown("""
**Todo lo demás se maneja on-line**  
- **Google Sheets** para captura/seguimiento.  
- **Looker Studio** para reportes adicionales.  
- **Streamlit Cloud** para deploy del proyecto final.
    """)
st.caption("Nota: en la Parte 3 incluiré un checklist de instalación y validación rápida.")

# ─────────────────────────────
# Precio & pagos (dinámico 3/4 meses)
# ─────────────────────────────
st.subheader("Precio y formas de pago")
st.markdown("**Costo mensual:** $1,500 MXN. Selecciona la duración para calcular el total.")
months = st.radio("Duración del programa", [3, 4], horizontal=True, index=1, help="El temario contempla 4 meses.")
total = 1500 * months
cA, cB, cC = st.columns(3)
with cA:
    st.markdown(f'<div class="kpi"><h4>Mensualidad</h4><p>$1,500 MXN</p></div>', unsafe_allow_html=True)
with cB:
    st.markdown(f'<div class="kpi"><h4>Meses</h4><p>{months}</p></div>', unsafe_allow_html=True)
with cC:
    st.markdown(f'<div class="kpi"><h4>Total</h4><p>${total:,.0f} MXN</p></div>', unsafe_allow_html=True)

st.markdown('<div class="pay"><span>Tarjeta crédito</span><span>Tarjeta débito</span><span>PayPal</span><span>Depósito bancario</span><span>Transferencia</span></div>', unsafe_allow_html=True)
st.caption("Se emiten comprobantes. Pregunta por opciones de pago fraccionado.")

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Plan de estudios — Semanas 1 a 6 (con casos reales)
# ─────────────────────────────
st.subheader("Plan de estudios (Semanas 1–6) — Fundamentos con enfoque práctico")

# Semana 1
with st.container():
    st.markdown("### Semana 1 — Inicio, fundamentos y Python para datos")
    col = st.columns([1.1, 1])[0]
    with col:
        st.markdown("""
**Temas**
- CRISP-DM, definición de problema, métricas de éxito.
- Entorno (Python, notebooks, Git) y **estructura de proyecto** profesional.
- Python básico para datos (tipos, control de flujo, funciones reutilizables).

**Caso real destacado**
- **Ventas minoristas:** planteamiento de una pregunta de negocio (↑ conversión o ↓ inventario o ↑ margen), definición de métrica y supuestos iniciales.
        """)
        st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# Semana 2
with st.container():
    st.markdown("### Semana 2 — Numpy + Pandas para preparar datos")
    st.markdown("""
**Temas**
- Numpy (arrays, *broadcasting*, rendimiento).
- Pandas I (carga de datos, índice, selección).
- Pandas II (limpieza, `merge`, `groupby`, *tidy data*).

**Caso real destacado**
- **Operaciones/logística:** consolidación de **órdenes** de múltiples hojas de cálculo (Google Sheets) + enriquecimiento con catálogo; KPIs de tiempos de entrega.
    """)

# Semana 3
with st.container():
    st.markdown("### Semana 3 — EDA y visualización con storytelling")
    st.markdown("""
**Temas**
- EDA sistemático: valores faltantes, outliers, *profiling*.
- Gráficos con **matplotlib/Seaborn** (distribuciones/comparaciones).
- Interactividad con **Plotly** y narrativa (anotaciones, orden de lectura).

**Caso real destacado**
- **Salud pública / calidad del aire:** identificar estacionalidad y anomalías; comunicar hallazgos a un público no técnico (área directiva).
    """)

# Semana 4
with st.container():
    st.markdown("### Semana 4 — SQL con SQLite (de consultas a diseño simple)")
    st.markdown("""
**Temas**
- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`; **JOINs**, agregaciones, subconsultas.
- Índices, vistas; conexión Python↔SQLite con `pandas.read_sql`.
- Diseño de esquema simple y *data access layer* ligero.

**Caso real destacado**
- **E-commerce:** top productos por margen, cohortes de clientes por mes, *lifetime value* inicial, y preparación de tabla para dashboard.
    """)

# Semana 5
with st.container():
    st.markdown("### Semana 5 — Estadística descriptiva, probabilidad y muestreo")
    st.markdown("""
**Temas**
- Tendencia central y dispersión; robustez frente a outliers.
- Probabilidad y distribuciones (Normal, Binomial) con intuición visual.
- Muestreo, sesgos comunes y tamaños de muestra.

**Caso real destacado**
- **Marketing:** resumen ejecutivo de campañas (CTR, CPC, CPA), comparación entre canales con **intervalos de confianza**.
    """)

# Semana 6
with st.container():
    st.markdown("### Semana 6 — Inferencia y pruebas: decisiones con evidencia")
    st.markdown("""
**Temas**
- Estimación, **intervalos de confianza**, *p-values*, **poder estadístico**.
- Pruebas t, χ², ANOVA; tamaños de efecto; diseño de **A/B testing**.

**Caso real destacado**
- **Producto / growth:** experimento A/B de una **landing**; análisis de resultados con reporte para stakeholders y recomendación accionable.
    """)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Próximos bloques (se cargarán en las Partes 2 y 3)
# ─────────────────────────────
st.markdown(
    """
<div class="block-soft">
<b>Próximamente (Partes 2 y 3):</b> Semanas 7–16 (ML, series de tiempo, Streamlit avanzado, integraciones con Sheets/SQLite),
Proyecto Final (hitos y rúbrica), calendario generador por cohorte, FAQ, y formulario de inscripción.
</div>
""", unsafe_allow_html=True)

st.caption("© 2025 • Programa de Análisis y Ciencia de Datos • Microsoft + Tessena")
# ─────────────────────────────
# PARTE 2 — Semanas 7–16, Calendario, Evaluación y Proyecto Final
# (Pegar a continuación del código existente)
# ─────────────────────────────

# ------- Plan de estudios — Semanas 7 a 16 (con casos reales) -------
st.subheader("Plan de estudios (Semanas 7–16) — Modelado, series de tiempo y entrega")

# Semana 7
with st.container():
    st.markdown("### Semana 7 — ML supervisado (Regresión) I")
    st.markdown("""
**Temas**
- Regresión lineal: supuestos, diagnóstico y métricas (MAE/MSE/R²).
- *Train/validation/test*, validación cruzada y *data leakage*.
- Regularización **Ridge/Lasso** y *pipelines* en scikit-learn.

**Caso real destacado**
- **Precios de vivienda:** estimar precio por m² usando variables estructurales; comparación de modelo base vs regularizado.
    """)

# Semana 8
with st.container():
    st.markdown("### Semana 8 — ML supervisado (Clasificación) I")
    st.markdown("""
**Temas**
- Regresión logística vs **Árboles de decisión**.
- Métricas: accuracy, precisión, recall, F1, ROC-AUC; **calibración**.
- Desbalanceo: `class_weight` y **SMOTE**; *thresholding*.

**Caso real destacado**
- **Churn de clientes:** clasificación de salida; matriz de confusión y **curva de ganancias** para priorizar retención.
    """)

# Semana 9
with st.container():
    st.markdown("### Semana 9 — ML no supervisado")
    st.markdown("""
**Temas**
- **k-means**: elección de *k* (codo, silhouette) y *feature scaling*.
- **PCA**: reducción de dimensionalidad y visualización 2D/3D.
- Perfilado de segmentos y *data storytelling*.

**Caso real destacado**
- **Segmentación comercial**: agrupar clientes por comportamiento de compra e inferir estrategias por cluster.
    """)

# Semana 10
with st.container():
    st.markdown("### Semana 10 — Series de tiempo I (Fundamentos y ETS)")
    st.markdown("""
**Temas**
- Tendencia, estacionalidad, ruido; **partición temporal**.
- Benchmarks: naive, promedio móvil; **ETS/Holt-Winters**.
- *Featureization* temporal (lags, rolling stats) para modelos ML.

**Caso real destacado**
- **Demanda semanal retail:** pronóstico con Holt-Winters y comparación contra naive estacional.
    """)

# Semana 11
with st.container():
    st.markdown("### Semana 11 — Series de tiempo II (ARIMA/SARIMA)")
    st.markdown("""
**Temas**
- Identificación y diagnóstico ARIMA/SARIMA (ACF/PACF).
- Selección de órdenes y **backtesting**.
- Combinación de modelos y *error analysis*.

**Caso real destacado**
- **Tráfico web**: SARIMA con estacionalidad semanal; reporte de error por período (picos vs valle).
    """)

# Semana 12
with st.container():
    st.markdown("### Semana 12 — Streamlit I (de notebooks a app)")
    st.markdown("""
**Temas**
- Estructura de app: formularios, *session state*, `st.cache_*`.
- Gráficos interactivos, filtros, layouts, descarga de archivos.
- **UX**: orden de lectura, microcopys y manejo de errores.

**Caso real destacado**
- **Dashboard ejecutivo**: KPIs de ventas, filtros por región y exportación a CSV.
    """)

# Semana 13
with st.container():
    st.markdown("### Semana 13 — Integraciones (Google Sheets/SQLite)")
    st.markdown("""
**Temas**
- Google Sheets: `QUERY`, `FILTER`, `VLOOKUP`, `ARRAYFORMULA`.
- Conexión Py↔Sheets (`gspread`/API) y Py↔SQLite (`read_sql`).
- Mini-MVP: flujo **ingesta → consulta → visualización**.

**Caso real destacado**
- **Control de inventario**: captura en Sheets, consulta en SQLite y tablero en Streamlit.
    """)

# Semana 14
with st.container():
    st.markdown("### Semana 14 — Calidad, reproducibilidad y ética")
    st.markdown("""
**Temas**
- Validaciones de datos (checks con *asserts*/pandera), logging y configuración.
- Git y entornos (`requirements.txt`/lockfiles); versiones de datos.
- Ética, privacidad, sesgos y explicabilidad básica (importancias/SHAP breve).

**Caso real destacado**
- **Crédito**: revisión de sesgos por grupo y propuesta de mitigación (revisión de variables proxy).
    """)

# Semana 15
with st.container():
    st.markdown("### Semana 15 — Comunicación y entrega")
    st.markdown("""
**Temas**
- **Storytelling** con datos, *insight > gráfico*; orden de lectura y anotaciones.
- Empaquetado del proyecto: estructura, scripts, *Makefile* mínimo.
- Ensayo de demos y *user testing*.

**Caso real destacado**
- **Dirección general**: narrativa de 8–10 min con foco en decisión y ROI.
    """)

# Semana 16
with st.container():
    st.markdown("### Semana 16 — Integrador y Demo Day")
    st.markdown("""
**Temas**
- Práctico integrador breve (limpieza + SQL + visualización).
- **Demo Day**: presentación y retro.
- Plan de mejora y *roadmap* personal.

**Caso real destacado**
- **Entrega final** del proyecto con checklist y lecciones aprendidas.
    """)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ------- Calendario de cohorte (generador + .ics) -------
st.subheader("Calendario de cohorte (16 semanas) — Generador y descarga .ics")

from datetime import timedelta

start_date = st.date_input("Fecha de inicio de la cohorte", value=date.today())
st.caption("El calendario se genera para Martes–Miércoles–Jueves, 8:00–9:00 (América/México_City), durante 16 semanas.")

# Ajustar al próximo martes (weekday: lunes=0 → martes=1)
d0 = start_date
while d0.weekday() != 1:
    d0 += timedelta(days=1)

rows = []
events = []
for wk in range(1, 17):
    base = d0 + timedelta(weeks=wk - 1)  # martes de la semana 'wk'
    for offset, day_name in zip([0, 1, 2], ["Martes", "Miércoles", "Jueves"]):
        session_date = base + timedelta(days=offset)
        rows.append({
            "Semana": wk,
            "Día": day_name,
            "Fecha": session_date.strftime("%Y-%m-%d"),
            "Hora": "08:00–09:00",
        })
        # Crear evento ICS (hora local sin conversión de zona; TZID explícito)
        ymd = session_date.strftime("%Y%m%d")
        uid = f"{wk}{offset}@tessena"
        events.append(f"""BEGIN:VEVENT
UID:{uid}
SUMMARY:Clase {wk:02d} - Programa de Análisis y Ciencia de Datos
DTSTART;TZID=America/Mexico_City:{ymd}T080000
DTEND;TZID=America/Mexico_City:{ymd}T090000
DESCRIPTION:Sesión de la cohorte (Mar–Mié–Jue 8:00–9:00) por Jitsi.
END:VEVENT""")

cal_df = pd.DataFrame(rows)
st.dataframe(cal_df, use_container_width=True, hide_index=True)

ics_text = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Tessena//Programa Datos//ES\n" + "\n".join(events) + "\nEND:VCALENDAR"
st.download_button("Descargar calendario (.ics)", data=ics_text, file_name="cohorte_streamlit.ics", mime="text/calendar")

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ------- Evaluación y rúbrica -------
st.subheader("Evaluación y rúbrica")

eval_df = pd.DataFrame([
    ["Proyecto final integrador (app + informe + demo)", "40%"],
    ["Mini-proyectos / tareas semanales", "30%"],
    ["Quizzes cortos (estadística/ML/SQL)", "15%"],
    ["Presentación / storytelling (Demo Day)", "10%"],
    ["Participación", "5%"],
], columns=["Componente", "Ponderación"])
st.dataframe(eval_df, use_container_width=True, hide_index=True)

st.markdown("""
**Criterios para aprobar y certificar (Microsoft × Tessena)**
- Calificación final **≥ 80/100**.
- **Proyecto Final** funcional, reproducible y presentado en Demo Day.
- Entrega de repositorio con **estructura profesional** y README claro.
- Materiales completos (notebooks, scripts, datasets locales) y **app en Streamlit**.
""")

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ------- Proyecto Final Integrador (detallado) -------
st.subheader("Proyecto Final Integrador — Alcance, hitos y rúbrica técnica")

st.markdown("""
**Formato**  
- **App en Streamlit** conectada a **SQLite** y/o entrada por **Google Sheets**.  
- **Informe** (máx. 8 páginas) y **presentación** (8–10 min).  
- Repositorio (Git) con `README`, `requirements.txt` y datos de ejemplo.

**Ideas de proyecto (elige 1)**
- **Forecast de demanda/ventas** con estacionalidad y promociones.
- **Segmentación k-means** con perfilado y recomendaciones.
- **Clasificación de churn/riesgo** (logística/árboles) con umbrales operativos.
- **Monitoreo operativo** (SQL + visualización + alertas simples por Sheets).
""")

milestones = pd.DataFrame([
    ["Semana 6",  "Propuesta: problema, objetivos, métricas, fuentes, riesgos."],
    ["Semana 10", "Avance analítico: EDA, primer modelo/forecast, SQL principal."],
    ["Semana 13", "Alpha funcional: ingesta → consulta → visualización en app."],
    ["Semana 15", "Cierre técnico + storytelling; revisión de reproducibilidad."],
    ["Semana 16", "Demo Day: entrega final y retro."],
], columns=["Hito", "Descripción"])
st.markdown("**Hitos sugeridos**")
st.dataframe(milestones, use_container_width=True, hide_index=True)

rubrica = pd.DataFrame([
    ["Definición del problema y métrica de éxito", 15],
    ["Calidad de datos y EDA (limpieza, supuestos)", 15],
    ["Solidez estadística/ML (validación, métricas)", 25],
    ["App Streamlit (funcionalidad y UX)", 25],
    ["Comunicación (informe y presentación)", 20],
], columns=["Criterio", "Pts"])
st.markdown("**Rúbrica técnica (100 pts)**")
st.dataframe(rubrica, use_container_width=True, hide_index=True)

st.markdown("""
**Checklist de entrega**
- [ ] Dataset y diccionario de variables.
- [ ] Notebooks de EDA y modelado con semillas fijas.
- [ ] Script(s) de inferencia/serving y configuración.
- [ ] App Streamlit con instrucciones de despliegue (Cloud).
- [ ] Informe PDF (≤ 8 págs) y slides de presentación.
""")

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ------- FAQ ampliado -------
st.subheader("Preguntas frecuentes (FAQ)")
with st.expander("¿Las clases quedan grabadas?"):
    st.write("Sí. Todas las sesiones quedan grabadas y se comparten junto a PDFs, notebooks y scripts.")
with st.expander("¿Qué necesito instalar?"):
    st.write("DBeaver, Jupyter y Streamlit. El resto se trabaja en línea (Google Sheets, Looker Studio, Streamlit Cloud).")
with st.expander("¿Qué nivel se requiere?"):
    st.write("No hay requisitos estrictos. Partimos de fundamentos, pero avanzamos hasta ML, series de tiempo y app.")
with st.expander("¿Cómo es la certificación Microsoft × Tessena?"):
    st.write("Al aprobar (≥80/100) y completar el Proyecto Final, se emite una constancia con folio verificable para LinkedIn.")
with st.expander("¿Formas de pago y facturación?"):
    st.write("Crédito/débito, PayPal, depósito o transferencia. Se emiten comprobantes. Opciones fraccionadas disponibles.")
with st.expander("¿Plataforma de videoclase?"):
    st.write("Jitsi. Recomendado micrófono y audífonos; conexión estable a Internet.")
# ─────────────────────────────
# PARTE 3 — Inscripción (Sheets/SQLite), Checklist de instalación y Políticas
# (Pegar a continuación del código existente)
# ─────────────────────────────

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.subheader("Inscripción")

st.markdown("""
Completa el formulario para reservar tu lugar. Puedes elegir la duración (3 o 4 meses).  
Guardaremos tu registro de forma segura en **Google Sheets** (si está configurado) o en **SQLite** como respaldo.
""")

# -------- Helpers de almacenamiento --------
def storage_backend():
    """
    Determina el backend disponible:
    - Google Sheets vía gspread con service account en st.secrets
    - Fallback a SQLite (archivo local ./data/enrollments.db)
    """
    use_gsheets = False
    gsheets_state = "No configurado"
    try:
        if "gcp_service_account" in st.secrets and "gsheet" in st.secrets:
            # Validación mínima de llaves requeridas
            sa = st.secrets["gcp_service_account"]
            gs = st.secrets["gsheet"]
            required_sa = {"type","project_id","private_key_id","private_key","client_email","client_id","token_uri"}
            required_gs = {"spreadsheet_id","worksheet"}
            if required_sa.issubset(set(sa.keys())) and required_gs.issubset(set(gs.keys())):
                use_gsheets = True
                gsheets_state = "Configurado"
    except Exception:
        use_gsheets = False
        gsheets_state = "No configurado"

    return use_gsheets, gsheets_state

def save_to_gsheets(row_dict):
    import gspread
    from google.oauth2.service_account import Credentials

    sa_info = dict(st.secrets["gcp_service_account"])
    creds = Credentials.from_service_account_info(sa_info, scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
    gc = gspread.authorize(creds)
    spreadsheet_id = st.secrets["gsheet"]["spreadsheet_id"]
    worksheet_name = st.secrets["gsheet"]["worksheet"]
    sh = gc.open_by_key(spreadsheet_id)
    ws = sh.worksheet(worksheet_name)

    # Asegurar encabezados si la hoja está vacía
    headers = ["timestamp","nombre","email","telefono","cohorte_inicio","duracion_meses","metodo_pago","comentarios","monto_total_mxn","origen"]
    try:
        current = ws.get_all_values()
        if not current or (len(current) == 1 and current[0] == ['']):
            ws.append_row(headers)
    except Exception:
        ws.append_row(headers)

    values = [row_dict.get(h, "") for h in headers]
    ws.append_row(values, value_input_option="USER_ENTERED")
    return True

def ensure_sqlite():
    import os, sqlite3
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/enrollments.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS inscripciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        nombre TEXT,
        email TEXT,
        telefono TEXT,
        cohorte_inicio TEXT,
        duracion_meses INTEGER,
        metodo_pago TEXT,
        comentarios TEXT,
        monto_total_mxn REAL,
        origen TEXT
    );
    """)
    conn.commit()
    return conn

def save_to_sqlite(row_dict):
    conn = ensure_sqlite()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO inscripciones (timestamp,nombre,email,telefono,cohorte_inicio,duracion_meses,metodo_pago,comentarios,monto_total_mxn,origen)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (
        row_dict["timestamp"],
        row_dict["nombre"],
        row_dict["email"],
        row_dict["telefono"],
        row_dict["cohorte_inicio"],
        row_dict["duracion_meses"],
        row_dict["metodo_pago"],
        row_dict["comentarios"],
        row_dict["monto_total_mxn"],
        row_dict["origen"],
    ))
    conn.commit()
    return cur.lastrowid

# -------- UI de inscripción --------
with st.form("form_inscripcion"):
    ci1, ci2 = st.columns(2)
    with ci1:
        nombre = st.text_input("Nombre completo *")
        email = st.text_input("Correo *")
        telefono = st.text_input("Teléfono/WhatsApp *")
        cohorte = st.date_input("Cohorte (fecha de inicio preferida)", value=date.today())
    with ci2:
        # Usa meses de la Parte 1 si existe; si no, por defecto 4
        meses_default = 0 if "months" in globals() and globals()["months"] == 3 else 1
        duracion = st.selectbox("Duración", [3, 4], index=meses_default, help="El temario está optimizado para 4 meses.")
        metodo_pago = st.selectbox("Método de pago preferido", ["Tarjeta crédito", "Tarjeta débito", "PayPal", "Depósito bancario", "Transferencia"])
        comentarios = st.text_area("Comentarios o requerimientos", placeholder="Cuéntanos si requieres factura, si vienes con tu equipo, etc.")
    submitted = st.form_submit_button("Enviar inscripción")

if submitted:
    # Validaciones básicas
    if not nombre or not email or not telefono:
        st.error("Por favor completa los campos obligatorios marcados con *.")
    else:
        total = 1500 * int(duracion)
        now_iso = pd.Timestamp.now(tz="America/Mexico_City").isoformat()
        row = {
            "timestamp": now_iso,
            "nombre": nombre.strip(),
            "email": email.strip(),
            "telefono": telefono.strip(),
            "cohorte_inicio": str(cohorte),
            "duracion_meses": int(duracion),
            "metodo_pago": metodo_pago,
            "comentarios": comentarios.strip(),
            "monto_total_mxn": float(total),
            "origen": "streamlit_app"
        }

        use_gs, gs_state = storage_backend()
        try:
            if use_gs:
                save_to_gsheets(row)
                st.success(f"¡Gracias, {nombre}! Tu registro fue guardado en **Google Sheets**. Total estimado: **${total:,.0f} MXN**.")
                st.caption("Recibirás un correo con los pasos de pago y confirmación de cupo.")
            else:
                new_id = save_to_sqlite(row)
                st.success(f"¡Gracias, {nombre}! Tu registro fue guardado en **SQLite** (folio #{new_id}). Total estimado: **${total:,.0f} MXN**.")
                st.caption("Recibirás un correo con los pasos de pago y confirmación de cupo.")
        except Exception as e:
            st.error("Ocurrió un problema al guardar tu registro. Intenta nuevamente o contáctanos.")
            st.exception(e)

# Estado del backend (transparencia)
use_gs, gs_state = storage_backend()
st.caption(f"Estado de almacenamiento — Google Sheets: **{gs_state}**; Fallback SQLite: **activo**.")

# -------- Zona administrativa (opcional) --------
with st.expander("Administración (ver inscripciones)"):
    admin_key_cfg = st.secrets.get("admin_key", None)
    admin_key_input = st.text_input("Clave de administrador", type="password")
    if admin_key_cfg and admin_key_input == admin_key_cfg:
        # Mostrar tabla desde el backend disponible
        use_gs, _ = storage_backend()
        try:
            if use_gs:
                import gspread
                from google.oauth2.service_account import Credentials
                sa_info = dict(st.secrets["gcp_service_account"])
                creds = Credentials.from_service_account_info(sa_info, scopes=[
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive"
                ])
                gc = gspread.authorize(creds)
                sh = gc.open_by_key(st.secrets["gsheet"]["spreadsheet_id"])
                ws = sh.worksheet(st.secrets["gsheet"]["worksheet"])
                rows = ws.get_all_records()
                admin_df = pd.DataFrame(rows)
            else:
                conn = ensure_sqlite()
                admin_df = pd.read_sql_query("SELECT * FROM inscripciones ORDER BY id DESC", conn)
            st.dataframe(admin_df, use_container_width=True)
            st.download_button("Descargar CSV", data=admin_df.to_csv(index=False).encode("utf-8"), file_name="inscripciones.csv", mime="text/csv")
        except Exception as e:
            st.error("No se pudo cargar el listado de inscripciones.")
            st.exception(e)
    else:
        if admin_key_cfg:
            st.info("Ingresa la clave de administrador para ver inscripciones.")
        else:
            st.warning("No hay `admin_key` configurada en `st.secrets`. Agrega una para habilitar esta sección.")

# ─────────────────────────────
# Checklist de instalación y validación rápida
# ─────────────────────────────
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.subheader("Checklist de instalación y validación rápida")

st.markdown("""
Antes de iniciar, instala en tu equipo:
- **Python 3.11+**
- **DBeaver** (gestor de base de datos)
- **Jupyter**
- **Streamlit**
""")

col_ck1, col_ck2 = st.columns(2)
with col_ck1:
    st.markdown("**Validaciones (opcionales)**")
    run_checks = st.button("Validar mi entorno (local)")
    if run_checks:
        results = []
        def ok(msg): return f"✅ {msg}"
        def warn(msg): return f"⚠️ {msg}"
        def err(msg): return f"❌ {msg}"

        # Python y librerías clave
        try:
            import sys
            pyver = sys.version.split()[0]
            results.append(ok(f"Python {pyver}"))
        except Exception as e:
            results.append(err(f"Python no detectado: {e}"))

        for lib in ["pandas", "numpy", "matplotlib", "plotly", "scikit_learn", "statsmodels", "streamlit", "sqlite3"]:
            try:
                __import__(lib if lib != "scikit_learn" else "sklearn")
                results.append(ok(f"Librería disponible: {lib}"))
            except Exception as e:
                results.append(warn(f"Librería faltante: {lib} ({e})"))

        # Prueba SQLite básica
        try:
            import sqlite3
            conn = sqlite3.connect(":memory:")
            cur = conn.cursor()
            cur.execute("CREATE TABLE t (id INTEGER, nombre TEXT);")
            cur.execute("INSERT INTO t VALUES (1,'prueba');")
            cur.execute("SELECT COUNT(*) FROM t;")
            c = cur.fetchone()[0]
            results.append(ok(f"SQLite OK (registros: {c})"))
        except Exception as e:
            results.append(err(f"SQLite falló: {e}"))

        # Estado de Google Sheets
        use_gs, gs_state = storage_backend()
        results.append(ok("Google Sheets configurado") if use_gs else warn("Google Sheets no configurado (se usará SQLite)."))

        st.markdown("\n".join(results))
with col_ck2:
    st.markdown("**Tips**")
    st.markdown("""
- Crea un entorno: `python -m venv .venv && source .venv/bin/activate`  
- Instala: `pip install streamlit pandas numpy matplotlib plotly scikit-learn statsmodels gspread google-auth`  
- Ejecuta: `streamlit run app.py`
- DBeaver: crea una conexión a **SQLite** y abre un archivo `.db` local.
- Para **Streamlit Cloud**, añade tus `secrets`:
  ```toml
  # .streamlit/secrets.toml
  [gcp_service_account]
  type = "service_account"
  project_id = "..."
  private_key_id = "..."
  private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
  client_email = "..."
  client_id = "..."
  token_uri = "https://oauth2.googleapis.com/token"

  [gsheet]
  spreadsheet_id = "1AbCDEFghiJKLmnOPQ..."  # ID del Spreadsheet
  worksheet = "inscripciones"

  admin_key = "mi_clave_segura"
""")
