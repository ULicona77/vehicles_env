import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis de Datos de Vehículos')

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Gráfico de dispersión: odómetro vs precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
