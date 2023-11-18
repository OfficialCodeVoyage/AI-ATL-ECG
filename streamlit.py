import streamlit as st
from io import StringIO
import automatic_ecg_diagnosis_master.predict as predict


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
#makes the prediction
if st.button('Submit'):
    data = predict.make_prediction(path_to_hdf5="./automatic_ecg_diagnosis_master/data/ecg_tracings.hdf5", path_to_model = "./automatic_ecg_diagnosis_master/model/model.hdf5")
    # right now just returns data
    st.text(data)

