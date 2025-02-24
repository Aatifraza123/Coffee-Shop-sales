import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
file_path = r'C:\Users\razaa\OneDrive\Desktop\juypter\Coffee Shop Sales.csv'
df = pd.read_csv(file_path)

# Calculate Revenue (price * quantity)
df['revenue'] = df['unit_price'] * df['transaction_qty']

# Convert USD to INR
usd_to_inr = 83  # Update if needed
df['revenue_inr'] = df['revenue'] * usd_to_inr

# Group by Product Category
category_revenue_inr = df.groupby('product_category')['revenue_inr'].sum().sort_values(ascending=False)

# Plot Revenue by Product Category in INR
plt.figure(figsize=(12, 7))
bars = plt.bar(category_revenue_inr.index, category_revenue_inr.values, color='teal')

# Add labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5000, f"₹{yval:,.0f}", ha='center', va='bottom', fontsize=9)

plt.title('Revenue by Product Category (INR)', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Revenue (₹)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




