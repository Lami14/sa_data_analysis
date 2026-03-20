import streamlit as st
import pandas as pd
from src.data_processing import load_crime_data, load_unemployment_data, load_loadshedding_data, merge_datasets
from src.visualizations import plot_crime_trends, plot_loadshedding_trends

st.set_page_config(page_title="SA Data Dashboard", layout="wide")
st.title("South Africa Socio-Economic Insights Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
province_filter = st.sidebar.selectbox("Select Province", ["All", "Gauteng", "KwaZulu-Natal", "Western Cape"])

# Load datasets
crime_df = load_crime_data("data/crime_stats.csv")
unemployment_df = load_unemployment_data("data/unemployment.csv")
load_df = load_loadshedding_data("data/load_shedding.csv")

# Merge datasets example
merged_df = merge_datasets(crime_df, unemployment_df, load_df)

# Filter by province
if province_filter != "All":
    merged_df = merged_df[merged_df['province'] == province_filter]

# Display charts
st.subheader("Crime Trends")
crime_fig = plot_crime_trends(merged_df)
st.plotly_chart(crime_fig, use_container_width=True)

st.subheader("Load-Shedding Trends")
load_fig = plot_loadshedding_trends(load_df)
st.plotly_chart(load_fig, use_container_width=True)

st.subheader("Unemployment Data (Heatmap)")
st.write("Check Jupyter Notebook for heatmap visualization.")
