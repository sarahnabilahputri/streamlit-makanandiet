import pickle
import numpy as np
import streamlit as st

# membaca model
model = pickle.load(open('OlahMakananDiet.sav', 'rb'))

# judul web
st.title('Memprediksi Makanan Diet dengan Mengukur Kalori, Protein, dan Lemak')

kalori = st.number_input('Masukkan Jumlah Kalori Pada Makanan Mu', key='kalori_input')

protein = st.number_input('Masukkan Jumlah Protein Pada Makanan Mu', key='protein_input')

fat = st.number_input('Masukkan Jumlah Lemak Pada Makanan Mu', key='fat_input')

# code untuk prediksi
makanandiet_prediksi = ''

# membuat tombol untuk prediksi
if st.button('Prediksi Makanan Mu'):
    prediksi_diet = model.predict([[kalori, protein, fat]])

    if (prediksi_diet[0] == 1):
        makanandiet_prediksi ='Makanan ini cocok untuk diet'
    else :
        makanandiet_prediksi ='Makanan ini tidak cocok untuk diet'

    st.success(makanandiet_prediksi) 