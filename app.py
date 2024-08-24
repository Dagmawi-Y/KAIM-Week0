import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
@st.cache_data
def load_data():
    return pd.read_csv('data/cleaned_combined_data.csv')

data = load_data()

# Streamlit App
st.title("Solar Farm Data Analysis Dashboard")
st.write("""
### Overview
This dashboard presents visualizations and insights from solar farm data collected at various locations.
""")

# Sidebar for user input
st.sidebar.header("User Input")
location = st.sidebar.selectbox("Select a location", ("Benin-Malanville", "Sierra Leone-Bumbuna", "Togo-Dapaong"))
st.sidebar.write("Selected location: ", location)

# Filter data based on location (dummy implementation for this step)
# You would need to adjust this if you have separate data for each location
# filtered_data = data[data['Location'] == location]

# Time Series Plot
st.subheader("Solar Irradiance Components Over Time")
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(data['Timestamp'], data['GHI'], label='GHI')
ax.plot(data['Timestamp'], data['DNI'], label='DNI')
ax.plot(data['Timestamp'], data['DHI'], label='DHI')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Irradiance')
ax.set_title(f'Solar Irradiance Components Over Time - {location}')
ax.legend()
st.pyplot(fig)

# Correlation Heatmap
st.subheader("Correlation Matrix of Solar and Weather Data")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Matrix')
st.pyplot(fig)

# Wind Direction vs Speed Scatter Plot
st.subheader("Wind Direction vs Speed")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='WD', y='WS', data=data, ax=ax)
ax.set_xlabel('Wind Direction (Degrees)')
ax.set_ylabel('Wind Speed (m/s)')
ax.set_title('Wind Direction vs Speed')
st.pyplot(fig)

# Ambient Temperature vs GHI Scatter Plot
st.subheader("Ambient Temperature vs GHI")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='Tamb', y='GHI', data=data, ax=ax)
ax.set_xlabel('Ambient Temperature (°C)')
ax.set_ylabel('Global Horizontal Irradiance (GHI)')
ax.set_title('Ambient Temperature vs GHI')
st.pyplot(fig)

# Histogram of GHI
st.subheader("Distribution of GHI")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data['GHI'], bins=30, kde=True, ax=ax)
ax.set_xlabel('Global Horizontal Irradiance (GHI)')
ax.set_title('Distribution of GHI')
st.pyplot(fig)
