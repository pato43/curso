import streamlit as st
import pandas as pd

# ─────────────────────────────
# Configuración base
# ─────────────────────────────
st.set_page_config(
    page_title="Programa Integral de Análisis y Ciencia de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Recomendado: forzar tema claro en .streamlit/config.toml
# [theme]
# base="light"
# primaryColor="#2563EB"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F5F7FB"
# textColor="#0F172A"

# ─────────────────────────────
# Constantes
# ─────────────────────────────
START_DATE_STR_LONG = "26 Ago 2025"
START_DATE_ISO = "2025-08-26"
DISCOUNT_DEADLINE = "25 Ago 2025"
HORARIO_STR = "Mar–Mié–Jue 10:00–11:00 (CDMX)"
MENSUALIDAD = 1500
TOTAL_4M = MENSUALIDAD * 4
TOTAL_PROMO = TOTAL_4M - 1000  # 6000 - 1000 = 5000

CLIP_1M_URL = "https://pago.clip.mx/6005bd8a-84e5-408a-a366-0160d023a3cf"
CLIP_4M_URL = "https://pago.clip.mx/91475443-2068-4972-a23f-18fe61a5fb57"  # NUEVO

# Contacto (puedes sobrescribir con st.secrets)
ORG_WA = st.secrets.get("support_whatsapp", "527225597963")
SUPPORT_EMAIL = st.secrets.get("support_email", "rojasalexander10@gmail.com")

# Política (modifica libremente este texto corto)
REFUND_POLICY = (
    "Reembolsos solicitados **antes del inicio** del curso: 100% menos comisiones de pasarela. "
    "Una vez iniciada la cohorte, evaluamos **casos excepcionales** (salud, fuerza mayor)."
)

# ─────────────────────────────
# Estilos (fondo claro + imágenes nítidas)
# ─────────────────────────────
st.markdown("""
<style>
:root{
  --primary:#2563EB; --bg:#FFFFFF; --bg-soft:#F6F8FC;
  --text:#0F172A; --text-soft:#334155; --line:#E6E9F2;
}
html, body, [class*="css"] { font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
/* Forzar claro aunque el SO esté en dark */
@media (prefers-color-scheme: dark) {
  html, body { background: #FFFFFF !important; color: #0F172A !important; }
}
section.main > div { padding-top: .4rem; }
h1,h2,h3 { letter-spacing: -0.015em; }
h1 { font-weight:800 }
h2 { margin-top: 0.25rem }
p { line-height: 1.6; }
.small { font-size: 0.92rem; color: var(--text-soft); }

/* Bloques y badges */
.badge { display:inline-block; padding:.32rem .7rem; border-radius:999px; font-weight:600; font-size:.8rem; background:#EEF2FF; color:#3730A3; margin-right:.35rem }
.block { background:var(--bg); border:1px solid var(--line); border-radius:18px; padding:1.25rem; }
.block-soft { background:var(--bg-soft); border:1px solid var(--line); border-radius:18px; padding:1.25rem; }

/* KPIs */
.kpi { background:var(--bg-soft); border:1px solid var(--line); border-radius:14px; padding:1rem; text-align:center; }
.kpi h4 { font-size:.9rem; margin:.2rem 0; color:var(--text-soft) }
.kpi p { font-size:1.2rem; margin:0; font-weight:800; color:var(--text) }

/* Línea divisoria */
.hr { height:1px; background:var(--line); margin:1rem 0 1.4rem 0; }

/* Stepper */
.stepper { display:flex; gap:8px; flex-wrap:wrap; margin:.4rem 0 1rem; }
.step{ padding:.45rem .75rem; border-radius:999px; border:1px solid var(--line); font-size:.88rem; }
.step.active{ background: var(--primary); color: #fff; border-color: var(--primary); }

/* Logos + imágenes nítidas y responsivas */
.brand-logos{ display:flex; align-items:center; justify-content:flex-end; gap:12px; margin-bottom:12px; }
img, svg { max-width: 100%; height:auto; image-rendering:-webkit-optimize-contrast; image-rendering:crisp-edges; }

/* Tarjeta de soporte */
.support { display:flex; gap:16px; flex-wrap:wrap; align-items:center; }
.support .card { border:1px solid var(--line); border-radius:14px; padding:1rem 1.2rem; background:var(--bg-soft); }

/* Ocultar footer Streamlit */
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────
# Hero (2 columnas): texto + KPIs/Logos
# ─────────────────────────────
left, right = st.columns([1.35, 1], gap="large")

with left:
    st.markdown("### ")
    st.markdown("# Programa Integral de **Análisis y Ciencia de Datos**")
    st.markdown(
        "Domina el ciclo completo: **Google Sheets → SQL (SQLite) → Python (pandas/numpy) → "
        "Visualización (matplotlib/plotly) → ML (regresión, clasificación, k-means) → "
        "Series de tiempo (ETS/ARIMA) → App con Streamlit**."
    )
    st.markdown(
        '<span class="badge">Certificación Microsoft en alianza con Tessena</span>'
        '<span class="badge">Herramientas 100% libres y gratuitas</span>'
        '<span class="badge">No necesitas una PC potente</span>'
        '<span class="badge">Modalidad en línea (Jitsi)</span>'
        '<span class="badge">Grabaciones y materiales incluidos</span>',
        unsafe_allow_html=True
    )
    # Contador a la fecha de inicio (días restantes)
    try:
        today = pd.Timestamp.now(tz="America/Mexico_City").normalize()
        start_dt = pd.Timestamp(START_DATE_ISO, tz="America/Mexico_City")
        days_left = (start_dt.normalize() - today).days
        if days_left >= 0:
            st.info(f"**Iniciamos el {START_DATE_STR_LONG}.** Faltan **{days_left}** días.")
        else:
            st.info(f"**Cohorte iniciada** el {START_DATE_STR_LONG}.")
    except Exception:
        pass

with right:
    l1, l2 = st.columns(2)
    with l1:
        st.image("assets/tessena_logo.png", caption="Tessena", use_container_width=True)
    with l2:
        st.image("assets/microsoft_logo.png", caption="Microsoft", use_container_width=True)

    st.write("")
    k1a, k1b = st.columns(2)
    with k1a:
        st.markdown('<div class="kpi"><h4>Duración</h4><p>4 meses</p></div>', unsafe_allow_html=True)
    with k1b:
        st.markdown('<div class="kpi"><h4>Ritmo</h4><p>3 clases/sem</p></div>', unsafe_allow_html=True)

    k2a, k2b = st.columns(2)
    with k2a:
        st.markdown(f'<div class="kpi"><h4>Horario</h4><p>{HORARIO_STR}</p></div>', unsafe_allow_html=True)
    with k2b:
        st.markdown(f'<div class="kpi"><h4>Inicio</h4><p>{START_DATE_STR_LONG}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Tabs principales (incluye FAQ + Soporte)
# ─────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Resumen", "Plan de estudios", "Precios y pago", "Inscripción", "FAQ y Soporte"])

with tab1:
    cL, cR = st.columns([1, 1])
    with cL:
        st.subheader("Propuesta de valor")
        st.markdown("""
- **Aprender haciendo**: proyectos semanales y un **Proyecto Final** con **Streamlit**.
- **Ruta profesional**: de hojas de cálculo a **pipelines reproducibles** y **apps**.
- **Stack actual**: Google Sheets, **SQLite**, Python (pandas/numpy), **visualización** (matplotlib/plotly),
  **ML** con scikit-learn y **series de tiempo** con statsmodels.
- **Enfoque laboral**: análisis útil, métricas claras y **storytelling** para presentar resultados.
        """)
    with cR:
        st.subheader("Certificación Microsoft × Tessena")
        st.markdown(f"""
Al concluir y aprobar el Proyecto Final, recibirás **certificación por parte de Microsoft en alianza con Tessena**,
con **folio verificable** para **LinkedIn** y portafolio. Acredita competencias en:
- Manipulación y análisis de datos
- SQL con SQLite
- Visualización efectiva
- Modelos de ML (supervisado y no supervisado)
- Series de tiempo y despliegue con Streamlit

**Inicio de cohorte:** {START_DATE_STR_LONG} • **Horario:** {HORARIO_STR}
        """)

with tab2:
    st.subheader("Plan de estudios (Semanas 1–6) — Fundamentos y casos reales")

    st.markdown("### Semana 1 — Inicio, fundamentos y Python para datos")
    st.markdown("""
**Temas**
- CRISP-DM, definición de problema y métricas de éxito.
- Entorno (Python, notebooks, Git) y **estructura de proyecto** profesional.
- Python básico para datos (tipos, control de flujo, funciones reutilizables).

**Caso real**
- **Retail**: pregunta de negocio (↑ conversión / ↓ inventario / ↑ margen), métrica y supuestos.
    """)

    st.markdown("### Semana 2 — Numpy + Pandas para preparación de datos")
    st.markdown("""
**Temas**
- Numpy (arrays, *broadcasting*, rendimiento).
- Pandas I (carga de datos, índice, selección).
- Pandas II (limpieza, `merge`, `groupby`, *tidy data*).

**Caso real**
- **Operaciones**: consolidación de **órdenes** desde Google Sheets + catálogo; KPIs de tiempos.
    """)

    st.markdown("### Semana 3 — EDA y visualización con storytelling")
    st.markdown("""
**Temas**
- EDA sistemático: valores faltantes, outliers, *profiling*.
- Gráficos con **matplotlib/Seaborn**; interactividad con **Plotly**.
- Storytelling: orden de lectura, anotaciones y enfoque ejecutivo.

**Caso real**
- **Calidad del aire / salud pública**: estacionalidad, anomalías y comunicación a no técnicos.
    """)

    st.markdown("### Semana 4 — SQL con SQLite (de consulta a diseño simple)")
    st.markdown("""
**Temas**
- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`; **JOINs**, agregaciones, subconsultas.
- Índices, vistas; conexión Python↔SQLite (`pandas.read_sql`).
- Esquema sencillo y *data access layer* ligero.

**Caso real**
- **E-commerce**: top productos por margen, cohortes de clientes y base para dashboard.
    """)

    st.markdown("### Semana 5 — Descriptiva, probabilidad y muestreo")
    st.markdown("""
**Temas**
- Tendencia central y dispersión; robustez ante outliers.
- Probabilidad y distribuciones (Normal, Binomial) con intuición visual.
- Muestreo, sesgos y tamaños de muestra.

**Caso real**
- **Marketing**: CTR/CPC/CPA con **intervalos de confianza** para comparar canales.
    """)

    st.markdown("### Semana 6 — Inferencia y pruebas: decisiones con evidencia")
    st.markdown("""
**Temas**
- Estimación, **intervalos de confianza**, *p-values*, **poder estadístico**.
- Pruebas t, χ², ANOVA; tamaños de efecto; diseño de **A/B testing**.

**Caso real**
- **Producto/Growth**: experimento A/B de landing; reporte y recomendación accionable.
    """)

with tab3:
    st.subheader("Precio y pagos")
    k1, k2, k3 = st.columns(3)
    with k1:
        st.markdown(f'<div class="kpi"><h4>Mensualidad</h4><p>${MENSUALIDAD:,.0f} MXN</p></div>', unsafe_allow_html=True)
    with k2:
        st.markdown('<div class="kpi"><h4>Duración</h4><p>4 meses</p></div>', unsafe_allow_html=True)
    with k3:
        st.markdown(f'<div class="kpi"><h4>Total estándar</h4><p>${TOTAL_4M:,.0f} MXN</p></div>', unsafe_allow_html=True)

    st.info(f"**Promo paquete 4 meses:** paga por adelantado y obtén **$1,000 MXN de descuento** (total **${TOTAL_PROMO:,.0f} MXN**). Válido hasta **{DISCOUNT_DEADLINE}**.")

    cbtn1, cbtn2 = st.columns([1, 1])
    with cbtn1:
        st.markdown("**Pagar 1 mes (MXN $1,500)**")
        st.markdown(
            f'''
            <a href="{CLIP_1M_URL}" target="_blank" rel="noopener noreferrer">
                <img src="https://cdn.prod.website-files.com/62588b32d8d6105ab7aa9721/63bf568610f3fdf437235192_Preview.svg" alt="Paga con Clip" />
            </a>
            ''',
            unsafe_allow_html=True
        )
    with cbtn2:
        st.markdown(f"**Pagar 4 meses (MXN ${TOTAL_PROMO:,.0f}) — Descuento hasta {DISCOUNT_DEADLINE}**")
        st.markdown(
            f"""
            <a href="{CLIP_4M_URL}" target="_blank" rel="noopener noreferrer">
                <img src="https://assets-global.website-files.com/62588b32d8d6105ab7aa9721/63bf568610f3fdf437235192_Preview.svg" alt="Logo Paga con Clip" />
            </a>
            """,
            unsafe_allow_html=True
        )

with tab4:
    # Stepper visual
    st.subheader("Inscripción")
    st.markdown("""
<div class="stepper">
  <span class="step active">1) Realiza tu pago en Clip</span>
  <span class="step">2) Completa tus datos</span>
  <span class="step">3) Descarga tu PDF y envíalo</span>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
**Inicio de cohorte:** {START_DATE_STR_LONG}  •  **Horario:** {HORARIO_STR}

**Cómo funciona**
1) **Paga** (mensual o paquete de 4 meses) y **guarda** tu código/recibo de Clip.  
2) **Llena el formulario**.  
3) **Descarga el PDF** de tu ficha técnica y **envíalo por WhatsApp o correo** para confirmar tu lugar.
""")

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

    # Atajos de pago
    pay1, pay2 = st.columns(2)
    with pay1:
        st.markdown("**Pago mensual (MXN $1,500)**")
        st.markdown(
            f'''
            <a href="{CLIP_1M_URL}" target="_blank" rel="noopener noreferrer">
                <img src="https://cdn.prod.website-files.com/62588b32d8d6105ab7aa9721/63bf568610f3fdf437235192_Preview.svg" alt="Paga con Clip" />
            </a>
            ''',
            unsafe_allow_html=True
        )
    with pay2:
        st.markdown(f"**Paquete 4 meses (MXN ${TOTAL_PROMO:,.0f}) — hasta {DISCOUNT_DEADLINE}**")
        st.markdown(
            f"""
            <a href="{CLIP_4M_URL}" target="_blank" rel="noopener noreferrer">
                <img src="https://assets-global.website-files.com/62588b32d8d6105ab7aa9721/63bf568610f3fdf437235192_Preview.svg" alt="Logo Paga con Clip" />
            </a>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

    # Formulario sin almacenamiento (solo PDF)
    st.markdown("### Paso 2 — Completa tus datos")
    st.caption("Tus datos se usan únicamente para tu ficha y comunicación del curso. **No guardamos** información en bases de datos.")

    with st.form("form_inscripcion_pdf"):
        ci1, ci2 = st.columns(2)
        with ci1:
            nombre = st.text_input("Nombre completo *")
            email = st.text_input("Correo electrónico *")
            telefono = st.text_input("Número telefónico (WhatsApp) *")
            edad = st.number_input("Edad *", min_value=12, max_value=100, step=1)
        with ci2:
            medio = st.selectbox("¿Cómo te enteraste del curso? *", [
                "Redes sociales",
                "YouTube/TikTok/Instagram (Creador de contenido)",
                "Búsqueda en Google",
                "LinkedIn",
                "Universidad/Empresa",
                "Recomendación (amigos/colegas)",
                "Otro"
            ])
            medio_detalle = st.text_input("Especifica el medio (canal, universidad, empresa, etc.) (opcional)")
            condicion = st.text_area("¿Alguna condición que debamos conocer? (opcional)", placeholder="Alergias, accesibilidad, etc.")
            clip_recibo = st.text_input("Número/código de recibo Clip *", help="Lo recibes por correo y aparece en pantalla al procesar el pago.")
        acepta = st.checkbox("Confirmo que la información es correcta y acepto ser contactado por la organización del curso *")
        submitted = st.form_submit_button("Generar ficha técnica (PDF)")

    if submitted:
        # Validaciones
        faltantes = []
        if not nombre: faltantes.append("Nombre completo")
        if not email: faltantes.append("Correo electrónico")
        if not telefono: faltantes.append("WhatsApp")
        if edad is None or int(edad) < 12: faltantes.append("Edad (12+)")
        if not clip_recibo: faltantes.append("Código de recibo Clip")
        if not medio: faltantes.append("Cómo te enteraste")
        if not acepta: faltantes.append("Aceptación de contacto")

        if faltantes:
            st.error("Por favor completa: " + ", ".join(faltantes) + ".")
        else:
            # Intentar generar PDF
            try:
                from io import BytesIO
                from reportlab.lib.pagesizes import LETTER
                from reportlab.pdfgen import canvas
                from reportlab.lib.units import inch

                buffer = BytesIO()
                c = canvas.Canvas(buffer, pagesize=LETTER)
                width, height = LETTER
                x_margin = 0.85 * inch
                y = {"val": height - 0.9 * inch}

                def line(txt, dy=16, bold=False):
                    if bold: c.setFont("Helvetica-Bold", 11)
                    else: c.setFont("Helvetica", 10.5)
                    c.drawString(x_margin, y["val"], txt)
                    y["val"] -= dy

                now_iso = pd.Timestamp.now(tz="America/Mexico_City").isoformat()

                # Encabezado
                c.setFont("Helvetica-Bold", 14)
                c.drawString(x_margin, y["val"], "Ficha técnica de inscripción — Programa de Análisis y Ciencia de Datos")
                y["val"] -= 24
                c.setFont("Helvetica", 10.5)
                line(f"Fecha de registro: {now_iso}")
                line("Certificación: Microsoft en alianza con Tessena")
                line("Herramientas: 100% libres y gratuitas • Requisitos: no necesitas una PC potente")
                line(f"Cohorte: inicio {START_DATE_STR_LONG} • Horario: {HORARIO_STR}")
                y["val"] -= 6
                c.line(x_margin, y["val"], width - x_margin, y["val"])
                y["val"] -= 16

                # Datos personales
                line("Datos del participante", bold=True)
                line(f"Nombre completo: {nombre}")
                line(f"Correo: {email}")
                line(f"WhatsApp: {telefono}")
                line(f"Edad: {int(edad)}")
                if condicion: line(f"Condición reportada: {condicion}")
                y["val"] -= 6
                c.line(x_margin, y["val"], width - x_margin, y["val"])
                y["val"] -= 16

                # Origen
                line("Origen / Cómo se enteró", bold=True)
                line(f"Medio: {medio}")
                if medio_detalle: line(f"Detalle: {medio_detalle}")
                y["val"] -= 6
                c.line(x_margin, y["val"], width - x_margin, y["val"])
                y["val"] -= 16

                # Pago
                line("Pago", bold=True)
                line(f"Código de recibo Clip: {clip_recibo}")
                line(f"Plan: Programa de 4 meses — Total estándar: ${TOTAL_4M:,.0f} MXN — Promo anticipada: ${TOTAL_PROMO:,.0f} MXN hasta {DISCOUNT_DEADLINE}")
                y["val"] -= 6
                c.line(x_margin, y["val"], width - x_margin, y["val"])
                y["val"] -= 16

                # Aviso
                line("Aviso de privacidad (resumen)", bold=True)
                line("Tus datos se utilizan exclusivamente para gestionar tu lugar y la comunicación del curso.")

                c.showPage()
                c.save()

                pdf_bytes = buffer.getvalue()
                buffer.close()

                # Nombre de archivo
                safe_name = "".join(ch if ch.isalnum() or ch in ("_", "-", ".") else "_" for ch in nombre.strip().replace(" ", "_"))
                file_name = f"ficha_inscripcion_{safe_name}.pdf"

                st.success("¡Listo! Descarga tu ficha y envíala por WhatsApp o correo para confirmar tu lugar.")
                st.download_button("Descargar ficha técnica (PDF)", data=pdf_bytes, file_name=file_name, mime="application/pdf")

                # Link de WhatsApp con mensaje prellenado (el alumno adjuntará el PDF manualmente)
                msg = (
                    f"Hola, adjunto mi ficha técnica de inscripción.%0A"
                    f"Nombre: {nombre}%0A"
                    f"Correo: {email}%0A"
                    f"WhatsApp: {telefono}%0A"
                    f"Código de recibo Clip: {clip_recibo}%0A"
                    f"Cohorte: Inicio {START_DATE_STR_LONG}, {HORARIO_STR}."
                )
                wa_link = f"https://wa.me/{ORG_WA}?text={msg}"
                st.markdown(f"[Enviar ficha técnica por WhatsApp]({wa_link})")
                st.caption("Abre WhatsApp y **adjunta el PDF descargado** antes de enviar.")

            except Exception as e:
                st.error("No se pudo generar el PDF. Asegúrate de instalar `reportlab` (agrega `reportlab` a requirements.txt).")
                st.exception(e)

with tab5:
    st.subheader("Preguntas frecuentes (FAQ)")
    with st.expander("¿Realmente no necesito una PC potente?"):
        st.markdown("Correcto. Trabajamos con **herramientas ligeras y gratuitas**: Google Sheets, SQLite, Python 3.11+, Jupyter/Colab y Streamlit. Un equipo promedio funciona bien.")
    with st.expander("¿Las herramientas son libres y gratuitas?"):
        st.markdown("Sí. Usamos **software libre o gratuito**. No hay suscripciones obligatorias de pago.")
    with st.expander("¿Cómo recibo la certificación de Microsoft en alianza con Tessena?"):
        st.markdown("Al **aprobar el Proyecto Final**, emitimos un certificado con **folio verificable** que puedes añadir a **LinkedIn** y a tu portafolio.")
    with st.expander("¿Qué pasa si falto a una clase?"):
        st.markdown("Tendrás **grabaciones** y materiales para ponerte al día. También hay **espacios de dudas**.")
    with st.expander("¿Puedo pedir factura?"):
        st.markdown("Sí. Tras tu pago, responde al correo de confirmación con tus **datos fiscales** y el **recibo de Clip**.")
    with st.expander("¿Hay reembolsos?"):
        st.markdown(REFUND_POLICY)
    with st.expander("¿Cómo accedo a las clases (Jitsi)?"):
        st.markdown("Enviaremos el **enlace de Jitsi** y el calendario por correo **24 horas antes** del inicio.")
    with st.expander("¿El cupo es limitado?"):
        st.markdown("Sí, mantenemos grupos **pequeños** para dar atención personalizada.")
    with st.expander("¿Qué software instalo?"):
        st.markdown("- **Python 3.11+**, **Jupyter/Colab**, **Streamlit**, **DBeaver** (para SQLite). Todo gratuito.\n- Extras: Git, VS Code (opcional).")

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    st.subheader("Soporte")
    st.markdown("""
<div class="support">
  <div class="card"><b>WhatsApp:</b> <a href="https://wa.me/""" + ORG_WA + """" target="_blank" rel="noopener">+""" + ORG_WA + """</a></div>
  <div class="card"><b>Correo:</b> <a href="mailto:""" + SUPPORT_EMAIL + """?subject=Duda%20curso%20Datos">""" + SUPPORT_EMAIL + """</a></div>
  <div class="card"><b>Horario de atención:</b> Lun–Vie 10:00–18:00 (CDMX)</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.caption("© 2025 • Programa de Análisis y Ciencia de Datos • Microsoft + Tessena • Herramientas libres y gratuitas • No requieres una PC potente")
