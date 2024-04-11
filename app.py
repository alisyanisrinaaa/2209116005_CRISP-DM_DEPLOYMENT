import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
from streamlit_option_menu import *
from function import *

st.title("Customer Shop Trends Data Analysis and Prediction")

URL = 'shop_trends.csv'

df = pd.read_csv(URL, index_col=[0])
df2 = pd.read_csv('Before Mapping.csv')

with st.sidebar :
    selected = option_menu('Customer Shop Trends Data',['Pengenalan','Data Distribusi','Relasi','Komposisi & Perbandingan','Prediksi'],default_index=0)

if (selected == 'Pengenalan'):
    st.header('Pengenalan Customer Shop Trends Data')
    st.write("""Jelajahi **Data Tren Belanja Pelanggan** dan analisis berbagai aspek perilaku pelanggan""")
    st.image('img/customer_shop.jpeg', caption='Customer Shop Trends Data', use_column_width=True)
    st.header("Pengenalan Customer Shop Trends")
    st.write("Pilih kategori untuk melihat lebih lanjut :")

    categories = ["Accessories", "Clothing", "Footwear", "Outerwear"]
    selected_category = st.selectbox("Category", categories)

    display_category_info(selected_category)

if (selected == 'Data Distribusi'):
    st.header('Data Distribusi')
    st.subheader('Histogram Plot Berdasarkan Usia')
    age_histogram_plot(df)
    st.subheader('Histogram Plot Usia Berdasarkan Kategori')
    histogram_plot(df)
    st.subheader('Box Plot Jumlah Pembelian Berdasarkan Gender')
    box_plot(df)

if (selected == 'Relasi'):
    st.title('Relasi')
    st.subheader('Scatter Plot')
    scatter_plot(df)
    st.subheader('Korelasi')
    heatmap(df)

if(selected == 'Komposisi & Perbandingan'):
    st.subheader('1. Komposisi')
    st.write('**Pie Chart**')
    pie_chart_category(df)
    stacked_bar_chart(df)
    st.subheader('2. Perbandingan')
    st.write('**Bar Chart**')
    bar_chart_size(df)
    bar_chart_subscription(df)

if(selected == 'Prediksi'):
    predict(df2)