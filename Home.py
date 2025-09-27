import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv")
st.title("D.J Darling's")

st.header("Our Items")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    for index, row in data[:5].iterrows():
        st.subheader(row["name"])
        st.write(row["category"])
        st.subheader(row["price"])
        st.write(row["stock"])
with col2:
    for index, row in data[5:].iterrows():
        st.subheader(row["name"])
        st.write(row["category"])
        st.subheader(row["price"])
        st.write(row["stock"])