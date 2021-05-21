import pandas as pd
import streamlit as st
import plotly.express as px
import config

st.title("Remanence X KPI : Analyse Streamlit")

data = st.file_uploader("Upload a Dataset", type=config.type)

if data is not None:
    df = pd.read_csv(data, encoding=config.encoding, sep=config.sep)
    st_budget = st.selectbox("Leviers", config.columns_budget)

    if st_budget is not None:
        min_cluster = min(config.clusters)
        max_cluster = max(config.clusters)
        st_cluster = st.slider('Cluster :', min_cluster, max_cluster)

        if st_cluster is not None:
            df_cluster = df[df[config.column_cluster] == st_cluster]
            fig = px.scatter(df_cluster, x=st_budget, y=config.column_kpi, trendline="ols")
            results = px.get_trendline_results(fig)

            st.plotly_chart(fig)


                


       