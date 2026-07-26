import streamlit as st

import numpy as np

import libreria_funciones as lf

st.session_state

st.title("Proyecto módulo 1 Fundamentals")

st.sidebar.title("Contenedor")

 

st.image("Python_logo.png")

st.sidebar.image("DMC.png")

 

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
