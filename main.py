# app1_sales_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("E-commerce Sales Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload your sales CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Show dataframe
    st.write(df.head())

    # KPIs
    total_sales = df['sales_amount'].sum()
    num_orders = df['sales_id'].nunique()
    avg_order = df['sales_amount'].mean()

    st.metric("Total Sales", f"${total_sales:,.2f}")
    st.metric("Number of Orders", num_orders)
    st.metric("Average Order Value", f"${avg_order:,.2f}")

    # Sales over time
    df['date'] = pd.to_datetime(df['date'])
    sales_time = df.groupby(df['date'].dt.date)['sales_amount'].sum().reset_index()
    fig1 = px.line(sales_time, x='date', y='sales_amount', title='Sales Over Time')
    st.plotly_chart(fig1)

    # Top 10 products
    top_products = df.groupby('product_key')['sales_amount'].sum().sort_values(ascending=False).head(10).reset_index()
    fig2 = px.bar(top_products, x='product_key', y='sales_amount', title='Top 10 Products')
    st.plotly_chart(fig2)
