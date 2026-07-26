import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf

titulo = "Proyecto Aplicado en Streamlit – Fundamentos de Programación"
alumno = "Miguel Flores Ccama"
modulo = "Módulo 1 – Python Fundamentals"
anio = 2026
informacion = "Soy Ing. de Sistemas que busca profundizar sus conocimientos en Python y en la ciencia de datos."
descripcion = st.text_area("El proyecto 1 pythn fundamentals busca fortalecer los conocimientos basicos en Python.")
herramientas = ["Python", "Streamli", "Numpy"]
url_imagen = "https://raw.githubusercontent.com/miguel0810/Trabajo_Practico_Modulo_1_Miguel_Flores/506e02d1926c6ed86f4438f4cf821b6531b89f51/DMC.png"


st.session_state
st.sidebar.title("Contenedor")
st.title(f"Titulo: {titulo}")
st.image(url_imagen)
st.subheader(f"Alumno: {alumno}")
st.subheader(f"Modulo: {modulo}")
st.write(f"Información general del estudiante: {informacion}")
st.write(f"Año: {anio}")
st.markdown(f"Año: {anio}")
st.markdown(descripcion)
st.markdown(f"**Las herramientas utilizadas para este proyecto fueron:** {herramientas_str}")
st.markdown(f"Las herramientas utilizadas para este proyecto fueron: : {herramientas}")



st.image("Python_logo.png")

st.sidebar.image("DMC.png")

 

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
