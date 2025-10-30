import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- Configuration and Data Setup ---
st.set_page_config(
    page_title="Sample Interactive Dashboard",
    layout="wide", # Use full browser width
    initial_sidebar_state="expanded"
)

# Function to generate dummy data for the example
@st.cache_data
def load_data():
    # Create a DataFrame with hypothetical sales data
    data = {
        'Date': pd.date_range('2024-01-01', periods=100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
        'Sales': np.random.randint(100, 5000, 100),
        'Product_Category': np.random.choice(['A', 'B', 'C', 'D'], 100)
    }
    df = pd.DataFrame(data)
    df['Date'] = df['Date'].dt.date # Keep just the date part
    return df

df = load_data()

# --- Title and Header ---
st.title("📊 Sales Performance Dashboard")

# --- Sidebar for Filtering ---
with st.sidebar:
    st.header("Filter Data")

    # 1. Region Filter (Multiselect)
    selected_regions = st.multiselect(
        "Select Region(s):",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )

    # 2. Product Category Filter (Selectbox)
    category_options = ['All'] + list(df['Product_Category'].unique())
    selected_category = st.selectbox(
        "Select Product Category:",
        options=category_options,
        index=0 # Default to 'All'
    )

# --- Apply Filters ---
df_filtered = df[df['Region'].isin(selected_regions)]

if selected_category != 'All':
    df_filtered = df_filtered[df_filtered['Product_Category'] == selected_category]

# --- Main Content Layout ---

## Key Metrics Section
st.subheader("Key Performance Indicators (KPIs)")
col1, col2, col3 = st.columns(3)

# KPI 1: Total Sales
with col1:
    total_sales = df_filtered['Sales'].sum()
    st.metric(label="💰 Total Sales", value=f"${total_sales:,.2f}")

# KPI 2: Average Sale Value
with col2:
    avg_sale = df_filtered['Sales'].mean()
    st.metric(label="📈 Avg. Sale Value", value=f"${avg_sale:,.2f}")

# KPI 3: Total Transactions
with col3:
    total_transactions = df_filtered.shape[0]
    st.metric(label="📦 Total Transactions", value=f"{total_transactions:,}")

## Visualization Section
st.subheader("Data Visualizations")
viz_col1, viz_col2 = st.columns(2)

# Visualization 1: Sales Distribution by Region (Bar Chart)
with viz_col1:
    st.markdown("**Sales by Region**")
    region_sales = df_filtered.groupby('Region')['Sales'].sum().reset_index()
    fig_bar = px.bar(
        region_sales, 
        x='Region', 
        y='Sales', 
        color='Region',
        title='Total Sales by Geographic Region'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Visualization 2: Sales Trend Over Time (Line Chart)
with viz_col2:
    st.markdown("**Sales Trend**")
    date_sales = df_filtered.groupby('Date')['Sales'].sum().reset_index()
    fig_line = px.line(
        date_sales, 
        x='Date', 
        y='Sales', 
        title='Daily Sales Trend'
    )
    st.plotly_chart(fig_line, use_container_width=True)


## Raw Data View
st.subheader("Filtered Data Table")
st.dataframe(df_filtered, height=250)

# Footer
st.markdown("---")
st.markdown("**Developed by:BHAVA SREE S N  | **Cloud Provider:** GCP (PaaS via Streamlit Cloud)")
