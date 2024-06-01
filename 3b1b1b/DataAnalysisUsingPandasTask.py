import pandas as pd

# Load the dataset
file_path = 'supermarket_sales.csv'
sales_data = pd.read_csv(file_path)

print("### Dataset Structure ###")
print(sales_data.info(), "\n")

print("### First Few Rows of the Dataset ###")
print(sales_data.head(10), "\n")
