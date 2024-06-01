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

# Performance Analysis
sales_data['Profit Margin'] = sales_data['Total'] - sales_data['cogs']

sales_data['YearMonth'] = sales_data['Date'].dt.to_period('M')
monthly_sales = sales_data.groupby('YearMonth')['Total'].sum()
sales_growth_rate = monthly_sales.pct_change()

top_products = sales_data.groupby('Product line')['Total'].sum().sort_values(ascending=False)
top_regions = sales_data.groupby('City')['Total'].sum().sort_values(ascending=False)

print("### First Few Rows of Profit Margins ###")
print(sales_data[['Invoice ID', 'Product line', 'Total', 'cogs', 'Profit Margin']].head(8), "\n")

print("### Monthly Sales Growth Rates ###")
print(sales_growth_rate, "\n")

print("### Top Performing Products by Total Sales ###")
print(top_products, "\n")

print("### Top Performing Regions by Total Sales ###")
print(top_regions, "\n")