import gspread
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
goocleclient = gspread.service_account()

sheet = goocleclient.open("Product Data").worksheet("January")

# Load data into a pandas DataFrame
df = pd.DataFrame(sheet.get_all_records())

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Add a Total Sales column
df['Total Sales'] = df['Quantity Ordered'] * df['Price Each']
#
# Insight 1: Total Revenue
total_revenue = df['Total Sales'].sum()
print(f"Total Revenue: ${total_revenue:.2f}")