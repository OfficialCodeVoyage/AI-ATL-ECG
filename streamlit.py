import streamlit as st
from io import StringIO
import numpy as np

st.title('Automatic ECG diagnosis')
st.subheader('A tool to view and analyze ECG data, backed by a deep neural network for classification', divider='blue')
uploaded_file = st.file_uploader("Upload your DICOM file (.dcm)")

st.number_input("Patient age", min_value = 0, max_value = 120, value=60)
st.selectbox("Patient sex", ["Male", "Female"])

#ECG_image = st.image()

sample_array = {"1dAVb": 13.239485, "RBBB": 0.546861, "LBBB": 0.006619, "SB": 0.052661, "AF": 0.131343, "ST": 0.000431}

st.bar_chart(data=sample_array, color="#e9a56b")
