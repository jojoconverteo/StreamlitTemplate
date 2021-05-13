import pandas as pd
import streamlit as st
import plotly.express as px
import config

st.title("Contribution : Analyse Streamlit")

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])

if data is not None:
    df = pd.read_csv(data, encoding=config.encoding, sep=config.sep)
    List_columns = [w for w in df.columns if 'levier' not in w]

    if st.checkbox("Show Coefficient :"):
        st_columns_without_labels = st.selectbox("Coefficient", List_columns)

        if st_columns_without_labels is not None:
            df_sorted = df.sort_values(by=st_columns_without_labels)
            fig = px.bar(df_sorted, y="leviers", x=st_columns_without_labels, orientation='h', height=1000)
            st.write(df_sorted.set_index("leviers"))
            st.plotly_chart(fig)
            


       