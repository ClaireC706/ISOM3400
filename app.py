import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os

import pandas as pd
import streamlit as st

data = {
    'Product': ['A', 'B', 'C'],
    'Sales': [1200, 850, 950],
    'Customers': [300, 400, 350]
}
df = pd.DataFrame(data)

st.dataframe(df)

# Show data with Streamlit elements
st.dataframe(df)                # Interactive table
st.data_editor(df)              # Editable table
st.table(df)                    # Static table

# Customize columns directly in the dataframe display
st.dataframe(df.style.format({'Sales': '$$${:,.0f}', 'Customers': 'Number = {:,.0f}'}))
