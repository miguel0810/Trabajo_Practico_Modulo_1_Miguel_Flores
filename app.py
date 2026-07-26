import streamlit as st

import numpy as np

import libreria_funciones_proyecto1 as lf

st.session_state

st.title("Proyecto Aplicado en Streamlit – Fundamentos de Programación")

st.sidebar.title("Contenedor")
autor = "Miguel Flores Ccama"
st.subheader(f"Autor: {autor}")

st.write("Prueba 1")

st.markdown("Markdown")

st.image("https://github.com/miguel0810/Trabajo_Practico_Modulo_1_Miguel_Flores/blob/506e02d1926c6ed86f4438f4cf821b6531b89f51/DMC.png")

st.image("Python_logo.png")

st.sidebar.image("DMC.png")

 

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
