import streamlit as st
from agent import query_to_sql
from db import run_sql_query
from visualizer import generate_chart

st.title("AI-Powered SQL Dashboard with Claude")

user_query = st.text_input("Ask a question about your data:")

if user_query:
    sql = query_to_sql(user_query)
    st.write(f"Generated SQL: {sql}")
    df = run_sql_query(sql)
    st.dataframe(df)
    fig = generate_chart(df)
    st.plotly_chart(fig)