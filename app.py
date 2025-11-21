import streamlit as st
st.title("Business Dashboard with Streamlit Layouts")

msg = ("Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard.")
st.write(msg)

col1, col2= st.columns(2)

with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")

tab1, tab2, tab3 = st.tabs(["Sales Data", 
                            "Customer Insights",
                            "Market Trends"])

with tab1:
    st.write("Content for Sales Data")
    sales_data = { ... }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")
with tab2:
    st.write("Content for Customer Insights")
    customer_feedback = [ ... ]
    for feedback in customer_feedback:
        st.write(f"- {feedback}")
with tab3:
    st.write("Content for Market Trends")
    market_trends = { ... }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")
