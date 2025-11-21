import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20,3)), columns = ["a","b","c"])
st.area_chart(df)

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", 
     "Home phone", 
     "Mobile phone"),
)

st.write("You selected:", option)
