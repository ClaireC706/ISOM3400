import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
