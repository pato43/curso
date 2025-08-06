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

# NOTA: para reforzar tema claro en todos los dispositivos,
# crea también .streamlit/config.toml con:
# [theme]
# base="light"
# primaryColor="#2563EB"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F5F7FB"
# textColor="#0F172A"

# ─────────────────────────────
# Estilos (tema claro forzado, moderno, espacioso)
# ─────────────────────────────
st.markdown("""
<style>
:root{
  --primary:#2563EB; --bg:#FFFFFF; --bg-soft:#F6F8FC;
  --text:#0F172A; --text-soft:#334155; --line:#E6E9F2;
}
html, body, [class*="css"] { font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
/* Forzar claro incluso si el usuario tiene dark en el SO */
@media (prefers-color-scheme: dark) {
  html, body { background: #FFFFFF !important; color: #0F172A !important; }
}
section.main > div { padding-top: .4rem; }
h1,h2,h3 { letter-spacing: -0.015em; }
h1 { font-weight:800 }
h2 { margin-top: 0.25rem }
p { line-height: 1.6; }
.small { font-size: 0.92rem; color: var(--text-soft); }
.badge { display:inline-block; padding:.32rem .7rem; border-radius:999px; font-weight:600; font-size:.8rem; background:#EEF2FF; color:#3730A3; margin-right:.35rem }
.block { background:var(--bg); border:1px solid var(--line); border-radius:18px; padding:1.25rem; }
.block-soft { background:var(--bg-soft); border:1px solid var(--line); border-radius:18px; padding:1.25rem; }
.kpi { background:var(--bg-soft); border:1px solid var(--line); border-radius:14px; padding:1rem; text-align:center; }
.kpi h4 { font-size:.9rem; margin:.2rem 0; color:var(--text-soft) }
.kpi p { font-size:1.2rem; margin:0; font-weight:800; color:var(--text) }
.hr { height:1px; background:var(--line); margin:1rem 0 1.4rem 0; }
.pay { display:flex; gap:.6rem; flex-wrap:wrap; }
.pay span{ border:1px solid var(--line); background:white; padding:.4rem .7rem; border-radius:999px; font-size:.85rem; }
.logo-row { display:flex; justify-content:flex-end; align-items:center; gap:14px; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────
# Encabezado compacto con logos integrados + Hero
# (reemplaza la barra superior con logos y el hero anteriores)
# ─────────────────────────────

# Estilos para logos alineados y sin huecos
st.markdown("""
<style>
.brand-logos{
  display:flex; align-items:center; justify-content:flex-end; gap:12px; margin-bottom:12px;
}
.brand-logos img{
  height:34px; width:auto; display:block;
}
@media (min-width: 900px){
  .brand-logos img{ height:38px; }
}
</style>
""", unsafe_allow_html=True)

# Hero con dos columnas: texto a la izquierda, logos + KPIs a la derecha
col1, col2 = st.columns([1.35, 1], gap="large")

with col1:
    st.markdown("### ")  # micro-espacio
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
    # Logos alineados a la derecha, sin espacio en blanco extra
    st.markdown(
        """
        <div class="brand-logos">
            <img src="assets/tessena_logo.png" alt="Tessena" />
            <img src="assets/microsoft_logo.png" alt="Microsoft" />
        </div>
        """,
        unsafe_allow_html=True
    )

    # KPIs en cuadrícula 2×2 (más ordenados y compactos)
    k1a, k1b = st.columns(2)
    with k1a:
        st.markdown('<div class="kpi"><h4>Duración</h4><p>4 meses</p></div>', unsafe_allow_html=True)
    with k1b:
        st.markdown('<div class="kpi"><h4>Ritmo</h4><p>3 clases/sem</p></div>', unsafe_allow_html=True)

    k2a, k2b = st.columns(2)
    with k2a:
        st.markdown('<div class="kpi"><h4>Horario</h4><p>Mar–Mié–Jue<br>10:00–11:00 CDMX</p></div>', unsafe_allow_html=True)
    with k2b:
        st.markdown('<div class="kpi"><h4>Inicio</h4><p>19 Ago 2025</p></div>', unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)


# ─────────────────────────────
# Propuesta de valor & Certificación
# ─────────────────────────────
cL, cR = st.columns([1, 1])
with cL:
    st.subheader("Propuesta de valor")
    st.markdown("""
- **Aprender haciendo**: proyectos cortos semanales y un **Proyecto Final** con **Streamlit**.
- **Ruta profesional**: de hojas de cálculo a **pipelines reproducibles** y **apps**.
- **Stack actual**: Google Sheets, **SQLite**, Python (pandas/numpy), **visualización** (matplotlib/plotly),
  **ML** con scikit-learn y **series de tiempo** con statsmodels.
- **Enfoque laboral**: análisis útil, métricas claras y **storytelling** para presentar resultados.
    """)
with cR:
    st.subheader("Certificación Microsoft × Tessena")
    st.markdown("""
Al concluir y aprobar el Proyecto Final, recibirás **certificación por parte de Microsoft en alianza con Tessena**,
con **folio verificable** para **LinkedIn** y portafolio. Acredita competencias en:
- Manipulación y análisis de datos
- SQL con SQLite
- Visualización efectiva
- Modelos de ML (supervisado y no supervisado)
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
- **Estudiantes/egresados** buscando **primer rol** en datos.
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

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Estructura, logística y requisitos
# ─────────────────────────────
st.subheader("Estructura y logística")
colA, colB, colC = st.columns([1.1, 1, 1])
with colA:
    st.markdown("""
**Formato**
- **Clases en vivo por Jitsi** (Mar–Mié–Jue, 10:00–11:00 CDMX).
- **Grabaciones** y materiales (PDFs, notebooks, scripts, datasets).
- **Repositorio base** por cohorte y guía de reproducibilidad.
    """)
with colB:
    st.markdown("""
**Entregables**
- Mini-proyectos semanales y **quizzes**.
- **Proyecto Final** (app + informe + demo).
- Rúbrica con criterios técnicos y de comunicación.
    """)
with colC:
    st.markdown("""
**Requisitos**
- **Computadora** con Internet.
- Instalar: **DBeaver**, **Jupyter**, **Streamlit** y **Python 3.11+**.
- Lo demás online: **Google Sheets**, **Looker Studio**, **Streamlit Cloud**.
    """)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Precio & Pagos (4 meses fijo) + Botones Clip
# ─────────────────────────────
st.subheader("Precio y pagos")
mensualidad = 1500
total_4m = 1500 * 4
pack_descuento = total_4m - 1000  # 6000 - 1000 = 5000

k1, k2, k3 = st.columns(3)
with k1:
    st.markdown(f'<div class="kpi"><h4>Mensualidad</h4><p>${mensualidad:,.0f} MXN</p></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="kpi"><h4>Duración</h4><p>4 meses</p></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="kpi"><h4>Total estándar</h4><p>${total_4m:,.0f} MXN</p></div>', unsafe_allow_html=True)

st.markdown("**Métodos aceptados:**")
st.markdown('<div class="pay"><span>Tarjeta crédito</span><span>Tarjeta débito</span><span>PayPal</span><span>Depósito bancario</span><span>Transferencia</span></div>', unsafe_allow_html=True)

st.info("**Promo paquete 4 meses:** paga por adelantado y obtén **$1,000 MXN de descuento** (total **$5,000 MXN**). Válido hasta **11 Ago 2025**.")

# Botones Clip (HTML proporcionado)
cbtn1, cbtn2 = st.columns([1, 1])
with cbtn1:
    st.markdown("**Pagar 1 mes (MXN $1,500)**")
    st.markdown(
        '<a href="https://pago.clip.mx/6005bd8a-84e5-408a-a366-0160d023a3cf" target="_blank">'
        '<img src="https://cdn.prod.website-files.com/62588b32d8d6105ab7aa9721/63bf568610f3fdf437235192_Preview.svg" alt="Paga con Clip" />'
        '</a>',
        unsafe_allow_html=True
    )
with cbtn2:
    st.markdown("**Pagar 4 meses (MXN $5,000) — Descuento hasta 11 Ago 2025**")
    st.markdown(
        '<a href="https://pago.clip.mx/16d060d6-9824-407b-a7dd-6ebe39deae4a" target="_blank">'
        '<img src="https://cdn.prod.website-files.com/62588b32d8d6105ab7aa9721/63bf568610f3fdf437235192_Preview.svg" alt="Paga con Clip" />'
        '</a>',
        unsafe_allow_html=True
    )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# ─────────────────────────────
# Plan de estudios — Semanas 1 a 6 (sin tablas; enfoque práctico)
# ─────────────────────────────
st.subheader("Plan de estudios (Semanas 1–6) — Fundamentos y casos reales")

with st.container():
    st.markdown("### Semana 1 — Inicio, fundamentos y Python para datos")
    st.markdown("""
**Temas**
- CRISP-DM, definición de problema y métricas de éxito.
- Entorno (Python, notebooks, Git) y **estructura de proyecto** profesional.
- Python básico para datos (tipos, control de flujo, funciones reutilizables).

**Caso real**
- **Retail**: pregunta de negocio (↑ conversión / ↓ inventario / ↑ margen), métrica y supuestos.
    """)

with st.container():
    st.markdown("### Semana 2 — Numpy + Pandas para preparación de datos")
    st.markdown("""
**Temas**
- Numpy (arrays, *broadcasting*, rendimiento).
- Pandas I (carga de datos, índice, selección).
- Pandas II (limpieza, `merge`, `groupby`, *tidy data*).

**Caso real**
- **Operaciones**: consolidación de **órdenes** desde Google Sheets + catálogo; KPIs de tiempos.
    """)

with st.container():
    st.markdown("### Semana 3 — EDA y visualización con storytelling")
    st.markdown("""
**Temas**
- EDA sistemático: valores faltantes, outliers, *profiling*.
- Gráficos con **matplotlib/Seaborn**; interactividad con **Plotly**.
- Storytelling: orden de lectura, anotaciones y enfoque ejecutivo.

**Caso real**
- **Calidad del aire / salud pública**: estacionalidad, anomalías y comunicación a no técnicos.
    """)

with st.container():
    st.markdown("### Semana 4 — SQL con SQLite (de consulta a diseño simple)")
    st.markdown("""
**Temas**
- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`; **JOINs**, agregaciones, subconsultas.
- Índices, vistas; conexión Python↔SQLite (`pandas.read_sql`).
- Esquema sencillo y *data access layer* ligero.

**Caso real**
- **E-commerce**: top productos por margen, cohortes de clientes y base para dashboard.
    """)

with st.container():
    st.markdown("### Semana 5 — Descriptiva, probabilidad y muestreo")
    st.markdown("""
**Temas**
- Tendencia central y dispersión; robustez ante outliers.
- Probabilidad y distribuciones (Normal, Binomial) con intuición visual.
- Muestreo, sesgos y tamaños de muestra.

**Caso real**
- **Marketing**: CTR/CPC/CPA con **intervalos de confianza** para comparar canales.
    """)

with st.container():
    st.markdown("### Semana 6 — Inferencia y pruebas: decisiones con evidencia")
    st.markdown("""
**Temas**
- Estimación, **intervalos de confianza**, *p-values*, **poder estadístico**.
- Pruebas t, χ², ANOVA; tamaños de efecto; diseño de **A/B testing**.

**Caso real**
- **Producto/Growth**: experimento A/B de landing; reporte y recomendación accionable.
    """)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

st.caption("© 2025 • Programa de Análisis y Ciencia de Datos • Microsoft + Tessena")
# ─────────────────────────────
# PARTE 3 — Inscripción con campos extra + PDF + WhatsApp
# (Pegar a continuación del código existente)
# ─────────────────────────────

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.subheader("Inscripción")

st.markdown("""
Completa el formulario para reservar tu lugar en la cohorte que **inicia el 19 de agosto de 2025**.  
**Horario fijo:** Martes–Miércoles–Jueves, **10:00–11:00** (CDMX).  
La información se usa exclusivamente para tu registro y comunicación del curso.
""")

# -------- Helpers de almacenamiento (Google Sheets si está configurado, fallback a SQLite) --------
def storage_backend_available():
    """
    Determina el backend disponible:
    - Google Sheets vía gspread con service account en st.secrets
    - Fallback a SQLite (archivo local ./data/enrollments.db)
    """
    use_gsheets = False
    try:
        if "gcp_service_account" in st.secrets and "gsheet" in st.secrets:
            sa = st.secrets["gcp_service_account"]
            gs = st.secrets["gsheet"]
            required_sa = {"type","project_id","private_key_id","private_key","client_email","client_id","token_uri"}
            required_gs = {"spreadsheet_id","worksheet"}
            if required_sa.issubset(set(sa.keys())) and required_gs.issubset(set(gs.keys())):
                use_gsheets = True
    except Exception:
        use_gsheets = False
    return use_gsheets

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

    headers = [
        "timestamp","nombre","email","email_institucional","telefono_whatsapp","edad","condicion",
        "medio","medio_detalle","creador_cuenta","clip_recibo",
        "cohorte_inicio","horario","duracion_meses","monto_total_mxn","origen"
    ]
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
        email_institucional TEXT,
        telefono_whatsapp TEXT,
        edad INTEGER,
        condicion TEXT,
        medio TEXT,
        medio_detalle TEXT,
        creador_cuenta TEXT,
        clip_recibo TEXT,
        cohorte_inicio TEXT,
        horario TEXT,
        duracion_meses INTEGER,
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
        INSERT INTO inscripciones (
            timestamp,nombre,email,email_institucional,telefono_whatsapp,edad,condicion,
            medio,medio_detalle,creador_cuenta,clip_recibo,
            cohorte_inicio,horario,duracion_meses,monto_total_mxn,origen
        )
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        row_dict["timestamp"],
        row_dict["nombre"],
        row_dict["email"],
        row_dict["email_institucional"],
        row_dict["telefono_whatsapp"],
        row_dict["edad"],
        row_dict["condicion"],
        row_dict["medio"],
        row_dict["medio_detalle"],
        row_dict["creador_cuenta"],
        row_dict["clip_recibo"],
        row_dict["cohorte_inicio"],
        row_dict["horario"],
        row_dict["duracion_meses"],
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
        email = st.text_input("Correo electrónico *")
        email_inst = st.text_input("Correo institucional o de trabajo (opcional)")
        telefono = st.text_input("Número telefónico (WhatsApp) *")
    with ci2:
        edad = st.number_input("Edad *", min_value=12, max_value=100, step=1)
        condicion = st.text_area("¿Tienes alguna condición que debamos conocer? (opcional)", placeholder="Alergias, accesibilidad, etc.")
        # Origen / medio
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
        creador = ""
        if medio in ["Redes sociales", "YouTube/TikTok/Instagram (Creador de contenido)"]:
            creador = st.text_input("Creador/cuenta en redes (si aplica)", placeholder="@usuario o nombre del canal")
    # Código de recibo de Clip
    clip_recibo = st.text_input("Número/código de recibo generado por Clip *", help="Lo recibes por correo y aparece en pantalla al procesar el pago.")
    submitted = st.form_submit_button("Enviar inscripción")

# Persistencia + PDF + WhatsApp
if submitted:
    # Validaciones básicas
    missing = []
    if not nombre: missing.append("Nombre completo")
    if not email: missing.append("Correo electrónico")
    if not telefono: missing.append("Número telefónico (WhatsApp)")
    if edad is None or int(edad) < 12: missing.append("Edad (12+)")
    if not clip_recibo: missing.append("Código de recibo Clip")
    if not medio: missing.append("Cómo te enteraste")
    if missing:
        st.error("Por favor completa los campos obligatorios: " + ", ".join(missing) + ".")
    else:
        total = 1500 * 4  # Programa fijo 4 meses
        now_iso = pd.Timestamp.now(tz="America/Mexico_City").isoformat()
        row = {
            "timestamp": now_iso,
            "nombre": nombre.strip(),
            "email": email.strip(),
            "email_institucional": email_inst.strip(),
            "telefono_whatsapp": telefono.strip(),
            "edad": int(edad),
            "condicion": condicion.strip(),
            "medio": medio,
            "medio_detalle": medio_detalle.strip(),
            "creador_cuenta": (creador or "").strip(),
            "clip_recibo": clip_recibo.strip(),
            "cohorte_inicio": "2025-08-19",
            "horario": "Mar–Mié–Jue 10:00–11:00 (CDMX)",
            "duracion_meses": 4,
            "monto_total_mxn": float(total),
            "origen": "streamlit_app",
        }

        # Guardar
        try:
            if storage_backend_available():
                save_to_gsheets(row)
                st.success(f"¡Gracias, {row['nombre']}! Tu registro fue guardado en **Google Sheets**. Total estimado: **${total:,.0f} MXN**.")
            else:
                new_id = save_to_sqlite(row)
                st.success(f"¡Gracias, {row['nombre']}! Tu registro fue guardado en **SQLite** (folio #{new_id}). Total estimado: **${total:,.0f} MXN**.")
            st.caption("Recibirás un correo con los pasos de pago y confirmación de cupo.")
        except Exception as e:
            st.error("Ocurrió un problema al guardar tu registro. Intenta nuevamente o contáctanos.")
            st.exception(e)

        # Generar PDF de ficha técnica (persistente con session_state)
        st.markdown("#### Ficha técnica de inscripción")

        # Inicializa contenedores en session_state
        if "ficha_pdf_bytes" not in st.session_state:
            st.session_state["ficha_pdf_bytes"] = None
        if "ficha_pdf_name" not in st.session_state:
            st.session_state["ficha_pdf_name"] = None
        if "ficha_wa_link" not in st.session_state:
            st.session_state["ficha_wa_link"] = None

        # Solo regenerar el PDF justo al enviar el formulario
        try:
            from io import BytesIO
            from reportlab.lib.pagesizes import LETTER
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import inch

            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=LETTER)
            width, height = LETTER
            x_margin = 0.85 * inch
            y = {"val": height - 0.9 * inch}  # contenedor mutable

            def line(txt, dy=16, bold=False):
                if bold:
                    c.setFont("Helvetica-Bold", 11)
                else:
                    c.setFont("Helvetica", 10.5)
                c.drawString(x_margin, y["val"], txt)
                y["val"] -= dy

            # Encabezado
            c.setFont("Helvetica-Bold", 14)
            c.drawString(x_margin, y["val"], "Ficha técnica de inscripción — Programa de Análisis y Ciencia de Datos")
            y["val"] -= 24
            c.setFont("Helvetica", 10.5)
            line(f"Fecha de registro: {now_iso}")
            line("Certificación: Microsoft en alianza con Tessena")
            line("Cohorte: inicio 19/08/2025 • Horario: Mar–Mié–Jue 10:00–11:00 (CDMX)")
            y["val"] -= 6
            c.line(x_margin, y["val"], width - x_margin, y["val"])
            y["val"] -= 16

            # Datos personales
            line("Datos del participante", bold=True)
            line(f"Nombre completo: {row['nombre']}")
            line(f"Correo: {row['email']}")
            if row['email_institucional']:
                line(f"Correo institucional/trabajo: {row['email_institucional']}")
            line(f"WhatsApp: {row['telefono_whatsapp']}")
            line(f"Edad: {row['edad']}")
            if row['condicion']:
                line(f"Condición reportada: {row['condicion']}")
            y["val"] -= 6
            c.line(x_margin, y["val"], width - x_margin, y["val"])
            y["val"] -= 16

            # Origen
            line("Origen / Cómo se enteró", bold=True)
            line(f"Medio: {row['medio']}")
            if row['medio_detalle']:
                line(f"Detalle: {row['medio_detalle']}")
            if row['creador_cuenta']:
                line(f"Creador/cuenta: {row['creador_cuenta']}")
            y["val"] -= 6
            c.line(x_margin, y["val"], width - x_margin, y["val"])
            y["val"] -= 16

            # Pago
            line("Pago", bold=True)
            line(f"Código de recibo Clip: {row['clip_recibo']}")
            line("Plan: Programa de 4 meses")
            line(f"Monto estimado total: ${int(row['monto_total_mxn']):,} MXN".replace(",", ","))
            y["val"] -= 6
            c.line(x_margin, y["val"], width - x_margin, y["val"])
            y["val"] -= 16

            # Aviso
            line("Aviso de privacidad (resumen)", bold=True)
            line("Tus datos se emplean exclusivamente para gestionar tu inscripción y comunicación del curso.")

            c.showPage()
            c.save()

            # Guardar en session_state para persistir tras el re-run
            pdf_bytes = buffer.getvalue()
            buffer.close()

            # Nombre de archivo seguro
            safe_name = "".join(ch if ch.isalnum() or ch in ("_", "-", ".") else "_" for ch in nombre.strip().replace(" ", "_"))
            file_name = f"ficha_inscripcion_{safe_name}.pdf"

            st.session_state["ficha_pdf_bytes"] = pdf_bytes
            st.session_state["ficha_pdf_name"] = file_name

            # Link de WhatsApp con mensaje prellenado (el alumno adjuntará el PDF manualmente)
            from urllib.parse import quote
            msg = (
                f"Hola, adjunto mi ficha técnica de inscripción.%0A"
                f"Nombre: {row['nombre']}%0A"
                f"Correo: {row['email']}%0A"
                f"WhatsApp: {row['telefono_whatsapp']}%0A"
                f"Código de recibo Clip: {row['clip_recibo']}%0A"
                f"Cohorte: Inicio 19/08/2025, Mar–Mié–Jue 10:00–11:00 (CDMX)."
            )
            wa_link = f"https://wa.me/527225597963?text={msg}"
            st.session_state["ficha_wa_link"] = wa_link

        except Exception as e:
            st.warning("No se pudo generar el PDF. ¿Está instalada la librería `reportlab`? (agrega `reportlab` a requirements.txt y despliega de nuevo).")
            st.exception(e)

        # Mostrar descarga y WhatsApp si ya existen en session_state
        if st.session_state["ficha_pdf_bytes"] and st.session_state["ficha_pdf_name"]:
            st.download_button(
                label="Descargar ficha técnica (PDF)",
                data=st.session_state["ficha_pdf_bytes"],
                file_name=st.session_state["ficha_pdf_name"],
                mime="application/pdf",
            )
            if st.session_state["ficha_wa_link"]:
                st.markdown(f"[Enviar ficha técnica por WhatsApp]({st.session_state['ficha_wa_link']})")
                st.caption("Abre WhatsApp y **adjunta el PDF descargado** en el chat antes de enviar.")
        else:
            st.info("Generaremos tu PDF al enviar el formulario o al corregir cualquier error de guardado.")
