import pandas as pd
import numpy as np 
import streamlit as st
import plotly.express as px

# Load and clean data
data = pd.read_csv('notebooks/vehicles_us.csv')
data = data.dropna(subset=['odometer', 'model_year'])

# Data Viewer
st.header('Data Viewer')
st.dataframe(data)

# Histogram: Most Valuable Vehicle Type
st.header('Most Valuable Vehicle Type')
price_vs_vehicle_type_hist = px.histogram(
    data, 
    x='type', 
    y='price', 
    title='Most Valuable Vehicle Type', 
    labels={'type': 'Vehicle Type', 'price': 'Vehicle Price ($)'}
)
st.plotly_chart(price_vs_vehicle_type_hist)

# Scatter Plot: Odometer and Price Correlation
st.header('Odometer and Price Correlation')
odometer_vs_price_scatter = px.scatter(
    data, 
    x='odometer', 
    y='price', 
    title='Odometer and Price Correlation', 
    labels={'odometer': 'Odometer/ Mileage', 'price': 'Vehicle Cost ($)'}
)
st.plotly_chart(odometer_vs_price_scatter)

# Compare Price Distribution Between Model Years
st.header('Compare Price Distribution Between Model Years')
# Get a list of model years
year_list = sorted(data['model_year'].unique())

# Dropdown for selecting years
year_1 = st.selectbox(
    label='Select year 1', 
    options=year_list, 
    index=year_list.index(1908.0)
)
year_2 = st.selectbox(
    label='Select year 2', 
    options=year_list, 
    index=year_list.index(1936.0)
)

# Filter the dataframe based on selected years
mask_filter = (data['model_year'] == year_1) | (data['model_year'] == year_2)
df_filtered = data[mask_filter]

# Checkbox to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# Create a histogram to compare price distribution between selected model years
fig = px.histogram(
    df_filtered,
    x='price',
    nbins=30,
    color='model_year',
    histnorm=histnorm,
    barmode='overlay',
    title='Price Distribution Comparison Between Model Years',
    labels={'price': 'Vehicle Price ($)', 'model_year': 'Model Year'}
)
st.plotly_chart(fig)