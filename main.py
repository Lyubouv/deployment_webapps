import streamlit as st
import pandas as pd
import numpy as np

st.title ('Aplikasi Perhitungan Molaritas')

bobot=st.number_input('Masukkan nilai bobot')
volume=st.number_input('Masukkan nilai volume')
mr=st.number_input('Masukkan nilai Mr')

tombol=st.button('Hitung Nilai Molaritas')

if tombol:
    nilai_molaritas = bobot/(mr*volume)
    st.success(f'Nilai Molaritas adalah {nilai_molaritas}')