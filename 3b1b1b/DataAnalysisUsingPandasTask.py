import pandas as pd
import numpy as np

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

# Hypothesis Testing (Optional)
np.random.seed(0)
sales_data['Promotion'] = np.random.choice([0, 1], size=len(sales_data))
sales_data['Season'] = np.random.choice(['Spring', 'Summer', 'Autumn', 'Winter'], size=len(sales_data))
print("### DataFrame with New Columns ###")
print(sales_data.head(10), "\n")

def calculate_test(sample1, sample2):
    # Calculate the means
    mean1, mean2 = np.mean(sample1), np.mean(sample2)

    # Calculate the standard deviations
    std1, std2 = np.std(sample1, ddof=1), np.std(sample2, ddof=1)

    # Calculate the sample sizes
    n1, n2 = len(sample1), len(sample2)

    # Calculate the standard error of the difference in means
    sed = np.sqrt((std1 ** 2 / n1) + (std2 ** 2 / n2))

    # Calculate the t-statistic
    t_statistic = (mean1 - mean2) / sed

    # Degrees of freedom
    degrees_of_freedom = n1 + n2 - 2

    return t_statistic, degrees_of_freedom

# Hypothesis 1: Sales are higher during promotional campaigns
promotional_sales = sales_data[sales_data['Promotion'] == 1]['Total']
non_promotional_sales = sales_data[sales_data['Promotion'] == 0]['Total']

t_stat_promotion, df_promotion = calculate_test(promotional_sales, non_promotional_sales)
print(f"T-statistic (Promotion): {t_stat_promotion}, Degrees of freedom (Promotion): {df_promotion}")

# Hypothesis 2: Sales differ by seasons
spring_sales = sales_data[sales_data['Season'] == 'Spring']['Total']
summer_sales = sales_data[sales_data['Season'] == 'Summer']['Total']

t_stat_season, df_season = calculate_test(spring_sales, summer_sales)
print(f"T-statistic (Season): {t_stat_season}, Degrees of freedom (Season): {df_season}")
