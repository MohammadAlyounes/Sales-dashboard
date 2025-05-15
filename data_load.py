import pandas as pd
import streamlit as st


def load_data():
    df = pd.read_csv('sales_data.csv')
    return df


data = load_data()



