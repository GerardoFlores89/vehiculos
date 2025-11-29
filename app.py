# Se importan las librerias
import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # lectura del archivo

st.markdown("<h1 style='text-align: center;'>Vehiculos</h1>",
            unsafe_allow_html=True)

histogram_button = st.button('Construir histograma')

if histogram_button:
    st.write(
        'Creación de un histograma para la visualización de los precios')
    fig = px.histogram(car_data, x='price',
                       color='condition',
                       title='Distribución de precio de los vehiculos de acuerdo a su condición')
    fig.update_layout(
        title_x=0.2,
        xaxis_title='Precio ($)',
        yaxis_title='Número de Vehículos',
        xaxis=dict(dtick=30000),
        yaxis=dict(dtick=400),
        width=800,
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Gráfico de dispersión')

if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión para analizar la relación entre odómetro y precio')
    fig = px.scatter(car_data, x='odometer', y='price',
                     color='condition',
                     title='Relación entre Odómetro y Precio de acuerdo a su condición')
    fig.update_layout(
        title_x=0.2,
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio ($)'
    )
    st.plotly_chart(fig, use_container_width=True)
