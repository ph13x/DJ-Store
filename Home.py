import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

data = pd.read_csv("data.csv")

st.title("D.J Darling's")

st.header("Our Items")
st.write("---")

col1, empty_col, col2  = st.columns([1.5, .5, 1.5])

with col1:
    for index, row in data[:5].iterrows():
        st.subheader(row["name"])
        st.image(f"images/{row['images']}")
        st.write(row["category"])
        st.subheader(row["price"])
        st.write(row["stock"])

with empty_col:
    print("""No cost too great," 
    "No mind to think" 
    "No will to break" 
    "No voice to cry suffering" 
    "Born of God and Void" 
    "You shall seal the blinding light that plauges their dreams"
    "You, are the vessel""")
with col2:
    for index, row in data[5:].iterrows():
        st.subheader(row["name"])
        st.image(f"images/{row['images']}")
        st.write(row["category"])
        st.subheader(row["price"])
        st.write(row["stock"])