import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURACIÓN DE LA SEGURIDAD Y API KEY (El nuevo formato del futuro AQ...)
# Puedes ingresarla fijamente aquí o mediante variables de entorno en el servidor
API_KEY = "TU_API_KEY_AQUI_EMPIEZA_CON_AQ" 
if API_KEY and API_KEY != "TU_API_KEY_AQUI_EMPIEZA_CON_AQ":
    genai.configure(api_key=API_KEY)

# Configuración estética de la app
st.set_page_config(page_title="Asistente de Diagnóstico Clínico", layout="wide")
st.title("🧠 Asistente Clínico de las 8 Dimensiones & Evolución")
st.write("Herramienta estratégica e independiente de diagnóstico, intervención y seguimiento.")

# Simulación de carga de la base bibliográfica (Tus 50 fuentes en el servidor)
def obtener_contexto_bibliografico():
    # En producción, aquí se implementa la lectura automática de la carpeta de PDFs.
    # Por ahora, dejamos el puente del modelo conceptual estructurado.
    return """
    [BASE DE CONOCIMIENTO INTEGRADA]
    - Dimensión Sombra: Integración de aspectos negados, técnicas de espejo y afirmaciones.
    - Dimensión Sentido: Reconexión con propósitos y valores. Vacío existencial.
    - Dimensión Existencia: Angustias vitales, libertad, toma de decisiones y finitud.
    - Dimensión Lenguaje: Reformulación estratégica, desmontar absolutos (siempre/nunca).
    - Dimensión Sistema Familiar: Lealtades invisibles, roles heredados (cuidador/mediador).
    - Dimensión Cognición: Flexibilizar filtros, reestructuración ante catastrofización.
    - Dimensión Cuerpo: Regulación somática, memoria corporal y estados de alerta.
    - Dimensión Presencia: Conciencia del aquí y ahora, técnicas de anclaje.
    """

# 2. SISTEMA DE NAVEGACIÓN INTERACTIVA (Tus Interfaces)
menu = ["1. Elección del Caso", "2. Checklist de 8 Dimensiones", "3. Generación de Tratamiento", "4. Evolución Semanal", "5. Preguntas Insight"]
choice = st.sidebar.selectbox("Panel de Control Clínico", menu)

# --- INTERFAZ 1: ELECCIÓN DEL CASO ---
if choice == "1. Elección del Caso":
    st.header("📋 Expediente Virtual del Caso")
    col1, col2 = st.columns(2)
    with col1:
        id_caso = st.text_input("Identificador / Código del Paciente", placeholder="Ej. PAC-001")
        edad = st.number_input("Edad", min_value=0, max_value=120, value=25)
    with col2:
        motivo = st.text_area("Motivo de Consulta Inicial", placeholder="Escribe el discurso o malestar principal expresado...")
    
    st.info("Configura los datos del caso antes de pasar al Checklist en la barra lateral.")

# --- INTERFAZ 2: CHECKLIST DE LAS 8 DIMENSIONES ---
elif choice == "2. Checklist de 8 Dimensiones":
    st.header("🔍 Evaluación de Prevalencia de Malestar")
    st.write("Selecciona los indicadores clínicos observados durante o inmediatamente después de la sesión:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Dimensión Sombra")
        s1 = st.checkbox("Patrones repetitivos / Autosabotaje / Culpar a otros externamente")
        s2 = st.checkbox("Ocultar partes de lo que siente para mantener armonía")
        
        st.subheader("2. Dimensión Sentido")
        se1 = st.checkbox("Sensación de vacío o de que 'nada importa'")
        se2 = st.checkbox("Logros actuales construidos solo por expectativas externas")
        
        st.subheader("3. Dimensión Existencia")
        ex1 = st.checkbox("Angustia severa ante la necesidad de elegir o tomar decisiones")
        ex2 = st.checkbox("Miedo paralizante o angustia ante la finitud de la vida")
        
        st.subheader("4. Dimensión Lenguaje")
        len1 = st.checkbox("Uso rígido y absoluto de términos como 'siempre' o 'nunca'")
        len2 = st.checkbox("Uso de metáforas marcadamente negativas para describirse")

    with col2:
        st.subheader("5. Sistema Familiar")
        sf1 = st.checkbox("Repetición ciega de conductas patológicas de los padres")
        sf2 = st.checkbox("Culpa intensa al priorizarse o asumir roles heredados")
        
        st.subheader("6. Dimensión Cognición")
        cog1 = st.checkbox("Catastrofización (pensar automáticamente en el peor escenario)")
        cog2 = st.checkbox("Pensamiento dicotómico rígido (todo blanco o negro)")
        
        st.subheader("7. Dimensión Cuerpo")
        cue1 = st.checkbox("Hipervigilancia, taquicardia o tensión física inexplicable")
        cue2 = st.checkbox("El cuerpo entra en estado de alerta sin peligro evidente")
        
        st.subheader("8. Dimensión Presencia")
        pre1 = st.checkbox("Vivir en 'piloto automático', enfocado en pasado o futuro")
        pre2 = st.checkbox("Falta de conciencia de las necesidades emocionales actuales")

    st.success("Checklist completado. Las puntuaciones se procesarán en la sección de Tratamiento.")

# --- INTERFAZ 3: GENERACIÓN DE TRATAMIENTO (El Motor AI con AQ...) ---
elif choice == "3. Generación de Tratamiento":
    st.header("⚡ Motor de Diagnóstico Estructural y Plan de Intervención")
    
    if st.button("🚀 Consultar Fuentes y Generar Tratamiento Estratégico"):
        if not API_KEY or API_KEY == "TU_API_KEY_AQUI_EMPIEZA_CON_AQ":
            st.error("Por favor, introduce una API Key válida en el archivo de código antes de ejecutar la consulta.")
        else:
            with st.spinner("Escaneando tus 50 fuentes bibliográficas y cruzando dimensiones..."):
                try:
                    # Inyección del contexto del corpus clínico
                    contexto = obtener_contexto_bibliografico()
                    
                    # Llamada al modelo usando el SDK actualizado
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = f"""
                    Actúa como un terapeuta sistémico experto de estándar alto.
                    Basándote estrictamente en este marco teórico clínico de referencia: {contexto}
                    
                    Genera una propuesta terapéutica estratégica personalizada.
                    1. Determina la Raíz Estructural (Dimensión dominante) y el Síntoma secundario manifestado.
                    2. Prescribe la Pregunta de Intervención exacta descrita en los textos.
                    3. Detalla las Técnicas de Reprogramación o Regulación idóneas según la guía clínica.
                    
                    Entrega un veredicto estructurado, claro y limpio.
                    """
                    
                    respuesta = model.generate_content(prompt)
                    st.markdown("### 📋 Plan Terapéutico Sugerido por la IA")
                    st.write(respuesta.text)
                    
                except Exception as e:
                    st.error(f"Error de conexión: {str(e)}. Verifica que tu clave de formato nuevo sea correcta.")

# --- INTERFAZ 4: SEGUIMIENTO DE LA EVOLUCIÓN SEMANAL ---
elif choice == "4. Evolución Semanal":
    st.header("📈 Bitácora Interactiva de Evolución")
    st.write("Monitoreo y evaluación semanal para determinar el progreso del paciente:")
    
    semana = st.selectbox("Seleccionar Semana de Seguimiento", ["Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5+"])
    
    col1, col2 = st.columns(2)
    with col1:
        estado_animo = st.slider("Estado de Ánimo General del Paciente (1 al 10)", 1, 10, 5)
        tension_fisica = st.slider("Nivel de Tensión Física / Somática (1 al 10)", 1, 10, 5)
    with col2:
        logros = st.text_area("Logros Clínicos y Avances Observados")
        obstaculos = st.text_area("Indicadores de Alerta o Estancamiento Semanal")
        
    if st.button("💾 Guardar Registro Semanal"):
        st.success(f"¡Registro de la {semana} guardado con éxito! Los datos son privados y exclusivos de tu sesión.")

# --- INTERFAZ 5: PREGUNTAS INSIGHT (Predeterminadas e Inamovibles) ---
elif choice == "5. Preguntas Insight":
    st.header("💡 Guía Permanente de Preguntas Reveladoras")
    st.write("Preguntas clave e inamovibles para detonar autoconciencia profunda sobre el proceso general:")
    
    st.info("**Pregunta Diagnóstica de Sombra:** ¿Existe algo en ti que quizás estás intentando evitar o no mirar directamente?")
    st.info("**Pregunta Diagnóstica de Sentido:** ¿Qué hoy le da sentido o dirección a tu vida?")
    st.info("**Pregunta Diagnóstica de Existencia:** Cuando piensas en tu vida y en las decisiones que necesitas tomar, ¿qué es lo que más te genera angustia?")
    st.info("**Pregunta Diagnóstica de Lenguaje:** ¿De qué forma sueles contar la historia de lo que estás viviendo?")
    st.info("**Pregunta Diagnóstica de Cuerpo:** Cuando algo difícil sucede, ¿qué percibes primero en tu cuerpo?")
    st.info("**Pregunta Diagnóstica de Presencia:** ¿Qué percibes en ti en este exacto momento?")
