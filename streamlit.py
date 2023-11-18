import streamlit as st
from io import StringIO
import numpy as np
import automatic_ecg_diagnosis_master.predict as predict

np.set_printoptions(suppress=True)
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
#makes the prediction
if st.button('Submit'):
    data = predict.make_prediction(path_to_hdf5 = "./automatic_ecg_diagnosis_master/data/ecg_tracings.hdf5", 
                                   path_to_model = "./automatic_ecg_diagnosis_master/model/model.hdf5")
    st.text(data)
    percent_data = np.round(data * 100.0, 2).astype(np.float16)
    st.text(percent_data)


