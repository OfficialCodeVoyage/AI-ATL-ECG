import streamlit as st
from io import StringIO

st.title('Automatic ECG diagnosis')
st.subheader('blah blah', divider='rainbow')
uploaded_file = st.file_uploader("Upload your Dicom file")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')