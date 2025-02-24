import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
file_path = r'C:\Users\razaa\OneDrive\Desktop\juypter\Coffee Shop Sales.csv'
data = pd.read_csv(file_path)

# Create a revenue column
data['revenue'] = data['transaction_qty'] * data['unit_price']

# Display first few rows to confirm
print(data.head())



# Calculate total revenue per product
data['revenue'] = data['transaction_qty'] * data['unit_price']
total_revenue_per_product = data.groupby('product_detail')['revenue'].sum().sort_values(ascending=False)

# Product categories sold per date
categories_per_date = data.groupby(['transaction_date', 'product_category'])['transaction_qty'].sum().unstack(fill_value=0)

# Plot total revenue per product (Top 10)
plt.figure(figsize=(12, 6))
sns.barplot(
    x=total_revenue_per_product.head(10).values,
    y=total_revenue_per_product.head(10).index,
    hue=total_revenue_per_product.head(10).index,  # Add hue
    palette='viridis',
    legend=False  # Disable legend since hue is for coloring only
)

plt.title('Top 10 Products by Total Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Product')
plt.tight_layout()
plt.show()

# Plot product category sales over time
plt.figure(figsize=(14, 6))
categories_per_date.plot(kind='line', figsize=(14,6))
plt.title('Product Category Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.legend(title='Product Category')
plt.tight_layout()
plt.show()

