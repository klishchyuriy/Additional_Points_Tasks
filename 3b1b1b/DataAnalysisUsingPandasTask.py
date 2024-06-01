import pandas as pd

# Load the dataset
file_path = 'supermarket_sales.csv'
sales_data = pd.read_csv(file_path)

print("### Dataset Structure ###")
print(sales_data.info(), "\n")

print("### First Few Rows of the Dataset ###")
print(sales_data.head(10), "\n")

# Data Cleaning
print("### Checking for Missing Values ###")
print(sales_data.isnull().sum(), "\n")

sales_data = sales_data.dropna()

sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['Time'] = pd.to_datetime(sales_data['Time'], format='%H:%M')
sales_data['Total'] = sales_data['Total'].astype(float)

print("### Data Types After Cleaning ###")
print(sales_data.dtypes, "\n")

# Data Exploration
print("### Summary Statistics for Numerical Columns ###")
print(sales_data.describe(), "\n")

print("### Count of Each Product Line ###")
print(sales_data['Product line'].value_counts(), "\n")

print("### Count of Sales by City ###")
print(sales_data['City'].value_counts(), "\n")
