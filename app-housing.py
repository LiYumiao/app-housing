import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Yumiao Li')

df = pd.read_csv('housing.csv')

#have a price slider
price_slider = st.slider('Median House Price', 0, 500001, 200000)

#have a sidebar
location_type_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),
     df.ocean_proximity.unique())

income_level = st.sidebar.radio('Choose income level', ('Low', 'Medium', 'High'))

#filter by price
df = df[df.median_house_value <= price_slider]

#filter by location type
df = df[df.ocean_proximity.isin(location_type_filter)]

#filter by income level
if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium':
    df = df[df.median_income > 2.5][df.median_income < 4.5]
elif income_level == 'High':
    df = df[df.median_income >= 4.5]

#show data on map
st.write('### See more filters in the sidebar:')
st.map(df)

#show histogram
st.write('### Histogram of the Median House Value')
fig, ax = plt.subplots()
df.median_house_value.hist(ax=ax, bins=30)
st.pyplot(fig)