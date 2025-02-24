import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
file_path = r'C:\Users\razaa\OneDrive\Desktop\juypter\Coffee Shop Sales.csv'
df = pd.read_csv(file_path)

# Check the first few rows
print(df.head())

# Count occurrences of each product category
category_counts = df['product_category'].value_counts()

# Plot product category distribution
category_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Product Category Distribution')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Check number of duplicate rows
duplicate_count = df.duplicated().sum()
print(f"Total Duplicate Rows: {duplicate_count}")

# Check for duplicates based on 'product_category'
print(df.duplicated(subset=['product_category']).sum())






