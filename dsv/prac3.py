"""pip install pandas numpy matplotlib seaborn scikit-learn scipy"""

import os
import urllib.request

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

URLS = {
    "diabetes.csv": "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv",
    "titanic.csv": "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
}


def get_csv(*names):
    """Return the first existing file from names; otherwise download the first one that has a URL."""
    for n in names:
        if os.path.exists(n):
            return n
    for n in names:
        if n in URLS:
            print(f"[{n} not found - downloading]")
            urllib.request.urlretrieve(URLS[n], n)
            return n
    raise FileNotFoundError(f"Put one of {names} in this folder")


# =====================================================================================
# %% PRACTICAL 3: Importing / Exporting CSV with Pandas and analysing data
# (shape, display of data, missing values, correlation)
# =====================================================================================
print("\n===== PRACTICAL 3: CSV import/export and analysis (diabetes.csv) =====")

df = pd.read_csv(get_csv("diabetes.csv"))                 # import

print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nDIMENSION (rows, columns):", df.shape)
print("SIZE:", df.size)
print("INDEX:", df.index)
print("Columns:\n", df.columns)
print("\nData types:\n", df.dtypes)
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe())
print("\nMemory usage (bytes):\n", df.memory_usage())

# --- Missing values
print("\nMissing values per column:\n", df.isnull().sum())
print("\nnotnull() (first 5 rows):\n", df.notnull().head())
df_clean = df.dropna()
print("\nShape after dropna():", df_clean.shape)

# --- Correlation + heatmap
correlation = df.corr()
print("\nCorrelation:\n", correlation)
plt.figure(figsize=(9, 7))
sns.heatmap(correlation, annot=True, cmap="RdYlBu")
plt.title("Correlation Heatmap - diabetes.csv")
plt.show()

# --- Export
df.to_csv("diabetes_exported.csv", index=False)
print("\nExported to diabetes_exported.csv")