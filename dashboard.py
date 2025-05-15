import streamlit as st
from data_wrangling import prepare_data, apply_filters
from filter_panel import filter_panel

st.set_page_config(layout='wide')
st.title("By Mohammad Alyounes")


data = prepare_data()
filters = filter_panel(data)
main_df = apply_filters(data, filters)
st.write(main_df.head())
