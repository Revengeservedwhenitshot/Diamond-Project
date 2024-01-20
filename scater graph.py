# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Reading the dataset
df = pd.read_csv(r"D:\Dimond\diamonds.csv")

# Scatter plot of carat vs price
sns.scatterplot(data=df, x='carat', y='price')
plt.show()