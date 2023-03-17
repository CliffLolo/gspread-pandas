import gspread
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

googleclient = gspread.service_account()

sheet = googleclient.open("Product Data").worksheet("January")

# Load data into a pandas DataFrame
df = pd.DataFrame(sheet.get_all_records())

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Add a Total Sales column
df['Total Sales'] = df['Quantity Ordered'] * df['Price Each']

# Insight 1: Total Revenue
total_revenue = df['Total Sales'].sum()
print(f"Total Revenue: ${total_revenue:.2f}")

# Insight 2: Best Selling Product
best_selling_product = df.groupby('Product')['Quantity Ordered'].sum().idxmax()
print(f"Best Selling Product: {best_selling_product}")

# Visualize Best Selling Product
plt.figure(figsize=(10, 6))
sns.barplot(x="Product", y="Quantity Ordered", data=df,
            order=df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=90)
plt.title('Best Selling Product')
plt.show()

# Insight 3: Most Popular City
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1])
most_popular_city = df.groupby('City')['Order ID'].count().idxmax()
print(f"Most Popular City: {most_popular_city}")

# Visualize Most Popular City
plt.figure(figsize=(10, 6))
sns.countplot(x='City', data=df, order=df['City'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Most Popular City')
plt.show()
