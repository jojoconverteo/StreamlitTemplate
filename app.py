import pandas as pd
import streamlit as st
import plotly.express as px
import config

st.title("Contribution : Analyse Streamlit")

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])

if data is not None:
    df = pd.read_csv(data, encoding=config.encoding, sep=config.sep)
    df_melt = pd.melt(df, id_vars="date")

    if st.checkbox("Contribution Temporel :"):
        fig = px.line(df_melt, x="date", y="value", color="variable")
        st.plotly_chart(fig)
            
    if st.checkbox("Contribution Moyenne :"):
        df_bar = df_melt.groupby("variable").mean().reset_index()
        fig = px.bar(df_bar.sort_values(by="value"), x="value", y="variable", orientation='h')
        st.plotly_chart(fig)
            


       