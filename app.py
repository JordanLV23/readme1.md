import pandas as pd
import streamlit as st
import plotly.express as px



car_data = pd.read_csv(r'data/vehicles_us.csv')
hist_button = st.button('Construir Histograma')

if hist_button:
    st.write('Creación del Histograma para el conjunto de datos de anuncios de venta de coches')
    fig=px.histogram(car_data, x='odometer')
    st.plotly_chart(fig,use_container_width=True)


disp_button = st.button('Construir Gráfico de Dispersión')

if disp_button:
    st.write('Creación del gráfico de disperción para el conjunto de datos de anuncios de venta de coches')
    fig=px.scatter(car_data, x='odometer',y='price')
    #st.plotly_chart(fig,use_container_width=True)
    fig.show() 
