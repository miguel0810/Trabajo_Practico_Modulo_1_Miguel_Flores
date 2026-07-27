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
    st.title("Ejercicio 3 - Uso de funciones desde una librería externa")
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
# SECCIÓN 5: EJERCICIO 4 - CRUD CON CLASES (InventarioProducto)
# ==========================================
elif opcion == "Ejercicio 4":
    st.title("Ejercicio 4 - Gestor CRUD con la Clase `InventarioProducto`")
    st.markdown("Módulo para gestionar productos en inventario mediante la clase **`InventarioProducto`**.")

    # Inicialización específica en session_state para la lista de productos de tipo InventarioProducto
    if "inventario_productos" not in st.session_state:
        st.session_state.inventario_productos = []

    tab_create, tab_read, tab_update, tab_delete = st.tabs(["Crear Producto", "Ver Inventario", "Actualizar", "Eliminar"])

    # ------------------------------------------
    # 1. CREAR (Create)
    # ------------------------------------------
    with tab_create:
        st.subheader("Registrar Nuevo Producto en Inventario")
        with st.form("form_crear_producto", clear_on_submit=True):
            nombre_p = st.text_input("Nombre del Producto")
            col1, col2 = st.columns(2)
            
            with col1:
                costo_u = st.number_input("Costo Unitario ($)", min_value=0.01, value=50.0, step=5.0, format="%.2f")
                precio_u = st.number_input("Precio Unitario ($)", min_value=0.01, value=80.0, step=5.0, format="%.2f")
            
            with col2:
                stock_act = st.number_input("Stock Actual", min_value=0, value=15, step=1)
                stock_min = st.number_input("Stock Mínimo (Alerta de Reposición)", min_value=0, value=5, step=1)

            btn_crear_prod = st.form_submit_button("Crear Objeto Producto")

        if btn_crear_prod:
            if nombre_p.strip():
                try:
                    # Instanciación del objeto InventarioProducto
                    # Si la clase está en libreria_clases_proyecto1 usa lc.InventarioProducto
                    # Si está en libreria_funciones_proyecto1 usa lf.InventarioProducto
                    nuevo_producto = lc.InventarioProducto(
                        nombre=nombre_p,
                        costo_unitario=costo_u,
                        precio_unitario=precio_u,
                        stock_actual=int(stock_act),
                        stock_minimo=int(stock_min)
                    )
                    st.session_state.inventario_productos.append(nuevo_producto)
                    st.success(f"Producto '{nombre_p}' registrado exitosamente como objeto `InventarioProducto`.")
                except ValueError as err:
                    st.error(f"Error de validación al crear el producto: {err}")
                except Exception as e:
                    st.error(f"Ocurrió un error inesperado: {e}")
            else:
                st.warning("Por favor, ingrese un nombre válido para el producto.")

    # ------------------------------------------
    # 2. LEER (Read)
    # ------------------------------------------
    with tab_read:
        st.subheader("Estado Actual del Inventario")
        if st.session_state.inventario_productos:
            # Obtención de resúmenes invocando el método .resumen() del objeto
            lista_resumenes = [p.resumen() for p in st.session_state.inventario_productos]
            df_inventario = pd.DataFrame(lista_resumenes)
            
            # Renombrar columnas para mejor lectura en la interfaz
            df_inventario.columns = [
                "Producto", "Stock Actual", "Valor Inventario ($)", 
                "Margen Unitario ($)", "Margen (%)", "Requiere Reposición"
            ]
            
            st.dataframe(df_inventario, use_container_width=True)

            # Tarjetas / Alertas de reposición usando el método .necesita_reposicion()
            st.subheader("Alertas de Stock")
            for prod in st.session_state.inventario_productos:
                res = prod.resumen()
                if prod.necesita_reposicion():
                    st.error(
                        f"⚠️ **{prod.nombre}**: STOCK CRÍTICO (Actual: {prod.stock_actual} | Mínimo: {prod.stock_minimo}). "
                        f"¡Requiere reposición inmediata!"
                    )
                else:
                    st.success(
                        f"✅ **{prod.nombre}**: Stock suficiente (Actual: {prod.stock_actual} | Mínimo: {prod.stock_minimo}). "
                        f"Valor Total: ${prod.valor_inventario():,.2f} | Margen: {prod.margen_porcentaje():.2f}%"
                    )
        else:
            st.info("No existen productos registrados en el inventario.")

    # ------------------------------------------
    # 3. ACTUALIZAR (Update)
    # ------------------------------------------
    with tab_update:
        st.subheader("Actualizar Parámetros del Producto")
        if st.session_state.inventario_productos:
            nombres_productos = [p.nombre for p in st.session_state.inventario_productos]
            prod_seleccionado_nombre = st.selectbox("Seleccione el producto a editar:", nombres_productos)

            # Buscar la instancia seleccionada
            prod_obj = next((p for p in st.session_state.inventario_productos if p.nombre == prod_seleccionado_nombre), None)

            if prod_obj:
                with st.form("form_actualizar_producto"):
                    st.markdown(f"**Modificando:** {prod_obj.nombre}")
                    c1, c2 = st.columns(2)
                    
                    with c1:
                        nuevo_costo = st.number_input("Costo Unitario ($)", value=float(prod_obj.costo_unitario), min_value=0.01, step=1.0)
                        nuevo_precio = st.number_input("Precio Unitario ($)", value=float(prod_obj.precio_unitario), min_value=0.01, step=1.0)
                    
                    with c2:
                        nuevo_stock_act = st.number_input("Stock Actual", value=int(prod_obj.stock_actual), min_value=0, step=1)
                        nuevo_stock_min = st.number_input("Stock Mínimo", value=int(prod_obj.stock_minimo), min_value=0, step=1)

                    btn_actualizar = st.form_submit_button("Guardar Cambios")

                if btn_actualizar:
                    try:
                        # Actualización directa de los atributos del objeto
                        prod_obj.costo_unitario = nuevo_costo
                        prod_obj.precio_unitario = nuevo_precio
                        prod_obj.stock_actual = nuevo_stock_act
                        prod_obj.stock_minimo = nuevo_stock_min

                        st.success(f"Producto '{prod_obj.nombre}' actualizado correctamente.")
                        st.rerun()
                    except Exception as err:
                        st.error(f"Error al actualizar el producto: {err}")
        else:
            st.info("No hay productos disponibles para actualizar.")

    # ------------------------------------------
    # 4. ELIMINAR (Delete)
    # ------------------------------------------
    with tab_delete:
        st.subheader("Eliminar Producto del Inventario")
        if st.session_state.inventario_productos:
            nombres_del = [p.nombre for p in st.session_state.inventario_productos]
            p_del_nombre = st.selectbox("Seleccione el producto a eliminar:", nombres_del)

            if st.button("Eliminar Producto", type="primary"):
                st.session_state.inventario_productos = [
                    p for p in st.session_state.inventario_productos if p.nombre != p_del_nombre
                ]
                st.success(f"El producto '{p_del_nombre}' ha sido eliminado exitosamente del inventario.")
                st.rerun()
        else:
            st.info("No hay productos registrados para eliminar.")
