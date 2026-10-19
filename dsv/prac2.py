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
# %% PRACTICAL 2: Mean, Median, Mode, Variance, Correlation and Normal Distribution
# =====================================================================================
print("\n===== PRACTICAL 2: Statistics, Correlation, Normal Distribution =====")
import statistics
from scipy.stats import norm

data = [168, 170, 150, 160, 182, 140, 175, 191, 152, 150]
print("Data      :", data)
print("Mean      :", np.mean(data))
print("Median    :", np.median(data))                     # even count -> average of 2 middle values
print("Median (odd count, first 9 values):", np.median(data[:9]))
print("Mode      :", statistics.mode(data))
print("Variance  :", np.var(data))                        # population variance (as in the manual)
print("Std. Dev. :", np.std(data))

# --- Correlation (Pearson) between orbital period and distance from the sun
orbital_period = np.array([88, 225, 365, 687, 4333, 10759, 30687, 60190])      # days
dist_from_sun = np.array([58, 108, 150, 228, 778, 1427, 2871, 4498])           # million km
corr = np.corrcoef(orbital_period, dist_from_sun)
print("\nCorrelation matrix:\n", corr)
print("Correlation coefficient r =", round(corr[0, 1], 4))

plt.scatter(orbital_period, dist_from_sun)
plt.title("Correlation Plot")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Distance from Sun (million km)")
plt.show()

# --- Normal distribution: using scipy pdf
x_axis = np.arange(-10, 10, 0.01)
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.title("Normal Distribution (PDF)")
plt.show()

# --- Normal distribution: random data + histogram
Mean, Standard_deviation, size = 170, 10, 10000
values = np.random.normal(Mean, Standard_deviation, size)
plt.hist(values, 100)
plt.axvline(values.mean(), color="k", linestyle="dashed", linewidth=2)
plt.title("Normal Distribution (Histogram)")
plt.show()
