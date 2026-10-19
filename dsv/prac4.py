# =====================================================================================
# %% PRACTICAL 4: Importing dataset (CSV) and various plots using Matplotlib
# =====================================================================================
print("\n===== PRACTICAL 4: Matplotlib plots (diabetes.csv) =====")

full = pd.read_csv(get_csv("diabetes.csv"))

# Drop columns and rows
df = full.drop(columns=["Pregnancies", "SkinThickness", "DiabetesPedigreeFunction", "Insulin", "Outcome"])
df = df.drop(df.index[10:])                               # keep first 10 rows only
print(df)

# --- Line chart
df.plot(kind="line", color=["red", "blue", "brown", "green"])
plt.title("Features responsible for diabetes")
plt.xlabel("Observations")
plt.ylabel("Values")
plt.show()

# Customised line chart
df.plot(kind="line", color=["red", "blue", "brown", "green"],
        marker="*", markersize=10, linewidth=3, linestyle="--")
plt.title("Features responsible for diabetes")
plt.xlabel("Observations")
plt.ylabel("Values")
plt.show()

# --- Bar chart
df.plot(kind="bar", title="diabetes prediction")
plt.xlabel("Observations")
plt.ylabel("Values")
plt.show()

# Customised bar chart
df.plot(kind="bar", title="diabetes prediction", color=["red", "yellow", "purple", "pink"],
        edgecolor="Green", linewidth=2, linestyle="--")
plt.xlabel("Observations")
plt.ylabel("Values")
plt.show()

# --- Scatter plot
plt.scatter(full["Age"], full["Glucose"])
plt.title("Diabetes Prediction")
plt.xlabel("Age")
plt.ylabel("Glucose")
plt.show()

# Customised scatter plot
plt.scatter(full["Glucose"], full["Insulin"], color="red", linewidth=2, marker="*", edgecolor="red")
plt.title("Diabetes Prediction")
plt.xlabel("Glucose")
plt.ylabel("Insulin")
plt.show()

# --- Histogram
df.plot(kind="hist", title="diabetes prediction")
plt.show()

# Customised histogram
df.plot(kind="hist", edgecolor="Blue", linewidth=2, linestyle=":", fill=False, hatch="o")
plt.show()

# --- Pie chart
df.plot(kind="pie", y="Glucose", title="Diabetes Prediction", legend=False, autopct="%.2f%%")
plt.ylabel("")
plt.show()
