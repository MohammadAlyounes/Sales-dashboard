import pandas as pd
import streamlit as st


@st.cache_data(ttl="1d")
def load_data():
    df = pd.read_csv('sales_data.csv')
    return df


data = load_data()
st.write(data)



