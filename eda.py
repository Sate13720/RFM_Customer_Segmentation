from re import A
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown(''' 
# Exploratory Data Analysis Web Application
''')


#How to upload file from PC
with st.sidebar.header("Upload your dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('iris')

#Profiling report for pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header("**Input DF**")
    st.write(df)
    st.write("---")
    st.header("**Profiling reports with pandas**")
    st_profile_report(pr)
else:
    st.info("Awiting for CSV file.")
    if st.button('Press to use Example data.'):
        #exapmle dataset
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5),
                columns=['age','banana','Sate','Duethland','Year'])
            return a
        df = load_data()
    pr = ProfileReport(df, explorative=True)
    st.header("**Input DF**")
    st.write(df)
    st.write("---")
    st.header("**Profiling reports with pandas**")
    st_profile_report(pr)
