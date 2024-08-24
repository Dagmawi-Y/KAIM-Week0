import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
benin_data = pd.read_csv('data/benin-malanville.csv')
sierra_leone_data = pd.read_csv('data/sierraleone-bumbuna.csv')
togo_data = pd.read_csv('data/togo-dapaong_qc.csv')

# Combine the datasets for comprehensive analysis
combined_data = pd.concat([benin_data, sierra_leone_data, togo_data], ignore_index=True)

# Summary Statistics
summary_stats = combined_data.describe()

# Data Quality Check
missing_values = combined_data.isnull().sum()
outliers = combined_data[(combined_data['GHI'] < 0) | (combined_data['DNI'] < 0) | (combined_data['DHI'] < 0)]

# Time Series Analysis
combined_data['Timestamp'] = pd.to_datetime(combined_data['Timestamp'])
time_series = combined_data.set_index('Timestamp')
ghi_plot = time_series['GHI'].plot(title='GHI over Time')

# Correlation Analysis
correlation_matrix = combined_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Wind Analysis
polar_plot = sns.scatterplot(data=combined_data, x='WD', y='WS')

# Temperature Analysis
temperature_analysis = sns.scatterplot(data=combined_data, x='Tamb', y='GHI')

# Data Cleaning
cleaned_data = combined_data.dropna()  # Drop rows with missing values

# Save the cleaned data
cleaned_data.to_csv('data/cleaned_combined_data.csv', index=False)

