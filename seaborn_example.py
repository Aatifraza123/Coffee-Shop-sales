import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
tips = sns.load_dataset('tips')

# Create a scatter plot
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.title('Total Bill vs Tip')
plt.show()
