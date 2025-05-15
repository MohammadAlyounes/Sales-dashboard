import streamlit as st
from data_load import load_data
from filter_panel import filter_panel

data = load_data()
filter_panel(data)
st.write(data)
