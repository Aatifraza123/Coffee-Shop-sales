import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\razaa\OneDrive\Desktop\juypter\covid19_large_dataset.csv'
df = pd.read_csv(file_path)

# Check first few rows and column names
print(df.head())
print(df.columns)

# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# --- 1. Max Deaths ---
max_deaths = df['Deaths'].max()
country_max_deaths = df[df['Deaths'] == max_deaths]['Country'].values[0]
print(f"Max Deaths: {max_deaths} in {country_max_deaths}")

# --- 2. Max Vaccinations ---
max_vaccinations = df['Vaccinations'].max()
country_max_vaccinations = df[df['Vaccinations'] == max_vaccinations]['Country'].values[0]
print(f"Max Vaccinations: {max_vaccinations} in {country_max_vaccinations}")

# --- 3. Average Deaths ---
avg_deaths = df['Deaths'].mean()
print(f"Average Deaths: {avg_deaths:.2f}")

# --- 4. New Cases Each Month ---
# Extract year and month
df['year_month'] = df['Date'].dt.to_period('M')

# Group by year_month and sum new cases
monthly_cases = df.groupby('year_month')['new_cases'].sum()

# --- 5. Visualization ---

# Plot New Cases Each Month
plt.figure(figsize=(12,6))
monthly_cases.plot(kind='bar', color='skyblue')
plt.title('New COVID-19 Cases Each Month')
plt.xlabel('Month')
plt.ylabel('New Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Total Deaths by Country (Top 10)
top10_deaths = df.groupby('country')['deaths'].max().sort_values(ascending=False).head(10)
top10_deaths.plot(kind='bar', color='salmon', figsize=(10,6))
plt.title('Top 10 Countries by Max COVID-19 Deaths')
plt.xlabel('Country')
plt.ylabel('Max Deaths')
plt.tight_layout()
plt.show()

# Plot Total Vaccinations by Country (Top 10)
top10_vaccinations = df.groupby('country')['total_vaccinations'].max().sort_values(ascending=False).head(10)
top10_vaccinations.plot(kind='bar', color='green', figsize=(10,6))
plt.title('Top 10 Countries by Total Vaccinations')
plt.xlabel('Country')
plt.ylabel('Total Vaccinations')
plt.tight_layout()
plt.show()
