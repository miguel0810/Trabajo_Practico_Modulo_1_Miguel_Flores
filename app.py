import streamlit as st
import numpy as np
import pandas as pd

# Importación de las librerías del proyecto
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc

# Configuración de la página
st.set_page_config(
    page_title="Proyecto 1 - Python Fundamentals",
    page_icon="🐍",
    layout="wide"
)

# ==========================================
# INICIALIZACIÓN DE ST.SESSION_STATE
# ==========================================
# Ejercicio 1: Flujo de caja
if "flujo_caja" not in st.session_state:
    st.session_state.flujo_caja = []

# Ejercicio 2: Arreglos NumPy
if "registros_numpy" not in st.session_state:
    st.session_state.registros_numpy = {
        "producto": np.array([]),
        "categoria": np.array([]),
        "precio": np.array([], dtype=float),
        "cantidad": np.array([], dtype=int),
        "total": np.array([], dtype=float)
    }

# Ejercicio 3: Histórico de funciones de la librería
if "historico_funciones" not in st.session_state:
    st.session_state.historico_funciones = []

# Ejercicio 4: CRUD con Objetos de la Librería de Clases (Persona, Estudiante, Docente)
if "personas" not in st.session_state:
    st.session_state.personas = []


# ==========================================
# MENÚ LATERAL DE NAVEGACIÓN
# ==========================================
st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox(
    "Seleccione una sección:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

st.sidebar.markdown("---")
st.sidebar.info("Especialización Python for Analytics\nMódulo 1 - Python Fundamentals")


# ==========================================
# SECCIÓN 1: HOME
# ==========================================
if opcion == "Home":
    st.title("Proyecto Aplicado en Streamlit – Fundamentos de Programación")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Datos del Estudiante")
        st.write("**Alumno:** Miguel Flores Ccama")
        st.write("**Módulo:** Módulo 1 – Python Fundamentals")
        st.write("**Año:** 2026")
        st.write("**Información general:** Ing. de Sistemas orientado a profundizar conocimientos en Python y Ciencia de Datos.")
        
    with col2:
        st.image(
            "https://raw.githubusercontent.com/miguel0810/Trabajo_Practico_Modulo_1_Miguel_Flores/506e02d1926c6ed86f4438f4cf821b6531b89f51/DMC.png",
            caption="DMC Institute",
            use_container_width=True
        )

    st.markdown("---")
    st.subheader("Descripción del Proyecto")
    st.markdown(
        """
        Este proyecto integra los conceptos fundamentales de Python (variables, control de flujo, 
        listas, NumPy, funciones especializadas de librerías externas y Programación Orientada a Objetos) 
        en una aplicación interactiva desarrollada con **Streamlit**.
        """
    )
    
    st.subheader("Tecnologías Utilizadas")
    st.markdown("- **Python** (Estructuras de datos, Funciones y POO)\n- **Streamlit** (Interfaz gráfica e interactiva)\n- **NumPy & Pandas** (Gestión de vectores y tablas de datos)")


# ==========================================
# SECCIÓN 2: EJERCICIO 1 - FLUJO DE CAJA
# ==========================================
elif opcion == "Ejercicio 1":
    st.title("Ejercicio 1 - Flujo de Caja con Listas")
    st.markdown("Módulo interactivo para registrar movimientos financieros en una lista y determinar el saldo final.")

    with st.form("form_flujo_caja", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            concepto = st.text_input("Concepto / Descripción")
        with col2:
            tipo = st.selectbox("Tipo de Movimiento", ["Ingreso", "Gasto"])
        with col3:
            valor = st.number_input("Valor ($)", min_value=0.01, step=10.0, format="%.2f")
        
        btn_agregar = st.form_submit_button("Agregar Movimiento")

    if btn_agregar:
        if concepto.strip():
            st.session_state.flujo_caja.append({
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            })
            st.success("Movimiento guardado exitosamente.")
        else:
            st.warning("Por favor, ingrese un concepto válido.")

    if st.session_state.flujo_caja:
        df_flujo = pd.DataFrame(st.session_state.flujo_caja)
        
        tot_ingresos = df_flujo[df_flujo["Tipo"] == "Ingreso"]["Valor"].sum()
        tot_gastos = df_flujo[df_flujo["Tipo"] == "Gasto"]["Valor"].sum()
        saldo_final = tot_ingresos - tot_gastos

        st.subheader("Lista de Movimientos")
        st.dataframe(df_flujo, use_container_width=True)

        m1, m2, m3 = st.columns(3)
        m1.metric("Total Ingresos", f"${tot_ingresos:,.2f}")
        m2.metric("Total Gastos", f"${tot_gastos:,.2f}")
        m3.metric("Saldo Final", f"${saldo_final:,.2f}")

        if saldo_final >= 0:
            st.success(f"El flujo de caja está **A FAVOR** por un monto de ${saldo_final:,.2f}")
        else:
            st.error(f"El flujo de caja está **EN CONTRA** por un monto de ${abs(saldo_final):,.2f}")
    else:
        st.info("No hay movimientos registrados.")


# ==========================================
# SECCIÓN 3: EJERCICIO 2 - REGISTRO CON NUMPY
# ==========================================
elif opcion == "Ejercicio 2":
    st.title("Ejercicio 2 - Registro con NumPy, Arrays y DataFrames")
    st.markdown("Registro de inventario mediante arrays unidimensionales de NumPy expuestos en un DataFrame dinámico.")

    with st.form("form_numpy", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            prod = st.text_input("Nombre del Producto")
            cat = st.selectbox("Categoría", ["Servidores", "Licencias", "Hardware", "Periféricos", "Otros"])
        with c2:
            precio = st.number_input("Precio Unitario ($)", min_value=0.1, step=1.0)
            cant = st.number_input("Cantidad", min_value=1, step=1)
        
        btn_numpy = st.form_submit_button("Agregar Registro")

    if btn_numpy:
        if prod.strip():
            total = precio * cant
            st.session_state.registros_numpy["producto"] = np.append(st.session_state.registros_numpy["producto"], prod)
            st.session_state.registros_numpy["categoria"] = np.append(st.session_state.registros_numpy["categoria"], cat)
            st.session_state.registros_numpy["precio"] = np.append(st.session_state.registros_numpy["precio"], precio)
            st.session_state.registros_numpy["cantidad"] = np.append(st.session_state.registros_numpy["cantidad"], cant)
            st.session_state.registros_numpy["total"] = np.append(st.session_state.registros_numpy["total"], total)
            st.success(f"Producto '{prod}' añadido con éxito.")
        else:
            st.warning("Ingrese un nombre de producto válido.")

    if len(st.session_state.registros_numpy["producto"]) > 0:
        df_np = pd.DataFrame(st.session_state.registros_numpy)
        df_np.columns = ["Producto", "Categoría", "Precio Unitario ($)", "Cantidad", "Total ($)"]
        st.subheader("Tabla de Registros (NumPy)")
        st.dataframe(df_np, use_container_width=True)
    else:
        st.info("No existen registros guardados.")

# ==========================================
# SECCIÓN 4: EJERCICIO 3 - LIBRERÍA DE FUNCIONES
# ==========================================
elif opcion == "Ejercicio 3":
    st.title("Ejercicio 3 - Uso de `libreria_funciones_proyecto1`")
    st.markdown("Cálculo de **Margen Neto** e indicadores financieros mediante la función `calcular_margen_neto`.")

    with st.form("form_margen_neto"):
        st.subheader("Ingreso de Parámetros Financieros")
        col1, col2 = st.columns(2)
        
        with col1:
            ingresos = st.number_input("Ingresos Totales ($)", min_value=0.01, value=10000.0, step=500.0, format="%.2f")
            costos = st.number_input("Costos ($)", min_value=0.0, value=4000.0, step=200.0, format="%.2f")
            
        with col2:
            gastos_op = st.number_input("Gastos Operativos ($)", min_value=0.0, value=2000.0, step=100.0, format="%.2f")
            impuestos = st.number_input("Impuestos ($)", min_value=0.0, value=1000.0, step=50.0, format="%.2f")

        btn_calcular = st.form_submit_button("Calcular Margen Neto")

    if btn_calcular:
        try:
            # Invocación directa a la función real de la librería
            resultado = lf.calcular_margen_neto(
                ingresos=ingresos,
                costos=costos,
                gastos_operativos=gastos_op,
                impuestos=impuestos
            )

            st.markdown("---")
            st.subheader("Resultados Obtenidos")

            # Muestra de métricas principales
            m1, m2, m3 = st.columns(3)
            m1.metric("Utilidad Bruta", f"${resultado['utilidad_bruta']:,.2f}")
            m2.metric("Utilidad Neta", f"${resultado['utilidad_neta']:,.2f}")
            m3.metric("Margen Neto (%)", f"{resultado['margen_neto_pct']:.2f}%")

            # Guardar en sesión para llevar registro histórico completo
            st.session_state.historico_funciones.append({
                "Ingresos": f"${ingresos:,.2f}",
                "Costos": f"${costos:,.2f}",
                "Gastos Operativos": f"${gastos_op:,.2f}",
                "Impuestos": f"${impuestos:,.2f}",
                "Utilidad Bruta": f"${resultado['utilidad_bruta']:,.2f}",
                "Utilidad Neta": f"${resultado['utilidad_neta']:,.2f}",
                "Margen Neto (%)": f"{resultado['margen_neto_pct']:.2f}%"
            })

            st.success("Cálculo realizado con éxito.")

        except ValueError as err:
            st.error(f"Error en los parámetros ingresados: {err}")
        except Exception as e:
            st.error(f"Ocurrió un error inesperado al ejecutar la función: {e}")

    # Mostrar histórico de evaluaciones realizadas en la sesión
    if st.session_state.historico_funciones:
        st.markdown("---")
        st.subheader("Histórico de Evaluaciones Financieras")
        st.dataframe(pd.DataFrame(st.session_state.historico_funciones), use_container_width=True)

# ==========================================
# SECCIÓN 5: EJERCICIO 4 - CRUD CON CLASES (`Persona`, `Estudiante`, `Docente`)
# ==========================================
elif opcion == "Ejercicio 4":
    st.title("Ejercicio 4 - Gestor CRUD con `libreria_clases_proyecto1`")
    st.markdown("Módulo para administrar objetos de las clases **`Persona`**, **`Estudiante`** y **`Docente`**.")

    tab_create, tab_read, tab_update, tab_delete = st.tabs(["Crear Registro", "Ver Registros", "Actualizar", "Eliminar"])

    # 1. CREAR (Create)
    with tab_create:
        st.subheader("Crear un nuevo Objeto (Persona / Estudiante / Docente)")
        tipo_clase = st.selectbox("Tipo de Registro:", ["Persona", "Estudiante", "Docente"])

        with st.form("form_crear_persona", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                nombre = st.text_input("Nombre completo")
                edad = st.number_input("Edad", min_value=1, max_value=120, value=25)
            with col2:
                dni = st.text_input("DNI / Documento")

            # Campos específicos por tipo de clase
            carrera = ""
            curso = ""
            if tipo_clase == "Estudiante":
                carrera = st.text_input("Carrera")
            elif tipo_clase == "Docente":
                curso = st.text_input("Curso a Cargo")

            btn_crear = st.form_submit_button("Guardar en Sistema")

        if btn_crear:
            if nombre.strip() and dni.strip():
                try:
                    # Instanciación real de las clases de libreria_clases_proyecto1.py
                    if tipo_clase == "Persona":
                        obj = lc.Persona(nombre=nombre, edad=edad, dni=dni)
                    elif tipo_clase == "Estudiante":
                        obj = lc.Estudiante(nombre=nombre, edad=edad, dni=dni, carrera=carrera)
                    elif tipo_clase == "Docente":
                        obj = lc.Docente(nombre=nombre, edad=edad, dni=dni, curso=curso)
                    
                    st.session_state.personas.append(obj)
                    st.success(f"Objeto tipo `{tipo_clase}` registrado exitosamente.")
                except Exception as e:
                    st.error(f"Error al instanciar el objeto: {e}")
            else:
                st.warning("Por favor complete los campos obligatorios (Nombre y DNI).")

    # 2. LEER (Read)
    with tab_read:
        st.subheader("Registros en Sistema")
        if st.session_state.personas:
            datos_tabla = []
            for idx, p in enumerate(st.session_state.personas):
                # Evaluación de los métodos y atributos reales de los objetos
                info = {
                    "Índice": idx,
                    "Tipo Clase": type(p).__name__,
                    "Nombre": p.nombre,
                    "Edad": p.edad,
                    "DNI": p.dni,
                    "Detalle / Presentación": p.presentarse() if hasattr(p, "presentarse") else str(p)
                }
                if isinstance(p, lc.Estudiante):
                    info["Atributo Especial"] = f"Carrera: {p.carrera}"
                elif isinstance(p, lc.Docente):
                    info["Atributo Especial"] = f"Curso: {p.curso}"
                else:
                    info["Atributo Especial"] = "N/A"
                
                datos_tabla.append(info)

            st.dataframe(pd.DataFrame(datos_tabla), use_container_width=True)
        else:
            st.info("No hay personas, estudiantes o docentes registrados.")

    # 3. ACTUALIZAR (Update)
    with tab_update:
        st.subheader("Actualizar Registro Existente")
        if st.session_state.personas:
            opciones_personas = [f"{idx} - {p.nombre} ({type(p).__name__})" for idx, p in enumerate(st.session_state.personas)]
            seleccion = st.selectbox("Seleccione el registro a editar:", opciones_personas)
            
            idx_sel = int(seleccion.split(" - ")[0])
            obj_sel = st.session_state.personas[idx_sel]

            with st.form("form_actualizar_persona"):
                nuevo_nombre = st.text_input("Nombre", value=obj_sel.nombre)
                nueva_edad = st.number_input("Edad", min_value=1, max_value=120, value=obj_sel.edad)
                nuevo_dni = st.text_input("DNI", value=obj_sel.dni)

                if isinstance(obj_sel, lc.Estudiante):
                    nueva_carrera = st.text_input("Carrera", value=obj_sel.carrera)
                elif isinstance(obj_sel, lc.Docente):
                    nuevo_curso = st.text_input("Curso", value=obj_sel.curso)

                btn_actualizar = st.form_submit_button("Guardar Cambios")

            if btn_actualizar:
                obj_sel.nombre = nuevo_nombre
                obj_sel.edad = nueva_edad
                obj_sel.dni = nuevo_dni
                if isinstance(obj_sel, lc.Estudiante):
                    obj_sel.carrera = nueva_carrera
                elif isinstance(obj_sel, lc.Docente):
                    obj_sel.curso = nuevo_curso
                
                st.success("Registro actualizado correctamente.")
                st.rerun()
        else:
            st.info("No hay registros disponibles para editar.")

    # 4. ELIMINAR (Delete)
    with tab_delete:
        st.subheader("Eliminar Registro")
        if st.session_state.personas:
            opciones_personas_del = [f"{idx} - {p.nombre} ({type(p).__name__})" for idx, p in enumerate(st.session_state.personas)]
            seleccion_del = st.selectbox("Seleccione el registro a eliminar:", opciones_personas_del)
            
            idx_del = int(seleccion_del.split(" - ")[0])

            if st.button("Eliminar Registro", type="primary"):
                persona_removida = st.session_state.personas.pop(idx_del)
                st.success(f"El registro de **{persona_removida.nombre}** ha sido eliminado.")
                st.rerun()
        else:
            st.info("No hay registros disponibles para eliminar.")
