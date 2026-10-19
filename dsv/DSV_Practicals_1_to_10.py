"""
Data Science & Visualization Lab - BE (E&C), Amrutvahini College of Engineering, Sangamner
Practicals 1 to 10, matching the lab manual (DSV_Manual.zip).

HOW TO USE
  pip install pandas numpy matplotlib seaborn scikit-learn scipy keras tensorflow
  Each "# %%" block is one practical. Run it block by block in Jupyter / VS Code / Spyder,
  or run the whole file:  python DSV_Practicals_1_to_10.py

DATASETS (put these in the SAME folder as this file, same names as the manual)
  diabetes.csv         -> Practicals 3, 4   (Pima diabetes: Pregnancies, Glucose, ... Outcome)
  train.csv            -> Practical 5, 6    (Kaggle Titanic train.csv; 'titanic.csv' also works)
  your_dataset.csv     -> Practical 7       (YearsExperience, Age, EducationLevel, Salary)
  If a file is missing, the helper below downloads diabetes/titanic automatically (needs internet)
  and builds a sample salary file for Practical 7.
"""

# %% Common imports and dataset helper
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
# %% PRACTICAL 1: Data Manipulation in Python using Pandas
# Add rows/columns, drop rows/columns, rename rows/columns
# =====================================================================================
print("\n===== PRACTICAL 1: Data Manipulation using Pandas =====")

# --- Create a DataFrame
data = {"Name": ["Ram", "Shyam", "Shiv"], "Age": [18, 16, 20]}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# --- 1. Add a new column
df["Address"] = ["New Delhi", "Mumbai", "Kolkata"]
print("\nAfter adding column 'Address':\n", df)

# --- 2. Add a new row (using .loc)
df.loc[len(df.index)] = ["Ganesh", 12, "Hyderabad"]
print("\nAfter adding a new row:\n", df)

# --- 3. Remove rows / columns using drop()
data = {
    "Name": ["Ram", "Shyam", "Shiv", "Radha", "Gauri", "Girija"],
    "Age": [25, 20, 30, 18, 26, 25],
    "City": ["Delhi", "Mumbai", "Kailash", "Ujjain", "Chennai", "Shimla"],
    "Height": [170, 165, 180, 155, 160, 158],
    "Marital Status": ["Single", "Married", "Single", "Single", "Married", "Single"],
}
df2 = pd.DataFrame(data)
print("\nBefore dropping:\n", df2)

df2.drop(4, axis=0, inplace=True)              # delete one row by index label
df2.drop(index=5, inplace=True)                # delete one row using index=
df2.drop([1, 3], axis=0, inplace=True)         # delete multiple rows
print("\nAfter deleting rows 4, 5, 1, 3:\n", df2)

df2.drop("Age", axis=1, inplace=True)          # delete one column
df2.drop(columns="Marital Status", inplace=True)
print("\nAfter deleting columns 'Age' and 'Marital Status':\n", df2)

# --- 4. Rename columns using rename()
df2.rename(columns={"Name": "First_Name"}, inplace=True)
df2.rename(mapper={"City": "Address", "Height": "Height_cm"}, axis=1, inplace=True)
print("\nAfter renaming columns:\n", df2)

# --- Rename row labels (index)
df2.rename(index={0: "row_a", 2: "row_b"}, inplace=True)
print("\nAfter renaming rows (index):\n", df2)


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


# =====================================================================================
# %% PRACTICAL 5: Exploratory Data Analysis (EDA) on the Titanic dataset using Seaborn
# =====================================================================================
print("\n===== PRACTICAL 5: Titanic EDA using Seaborn =====")

df = pd.read_csv(get_csv("train.csv", "titanic.csv"))

print(df.head())
print("\nShape:", df.shape)
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())

# --- Univariate analysis
sns.countplot(x="Survived", data=df)
plt.title("Survival Distribution")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

sns.countplot(x="Pclass", data=df)
plt.title("Passenger Class Distribution")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.show()

sns.histplot(df["Age"].dropna(), bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# --- Bivariate analysis
sns.barplot(x="Sex", y="Survived", data=df)
plt.title("Survival Rate by Gender")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.show()

sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Pclass")
plt.ylabel("Survival Rate")
plt.show()

sns.barplot(x="Embarked", y="Survived", data=df)
plt.title("Survival Rate by Embarked")
plt.xlabel("Embarked")
plt.ylabel("Survival Rate")
plt.show()

sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Fare vs. Survival")
plt.xlabel("Survived")
plt.ylabel("Fare")
plt.show()

# --- Multivariate analysis
sns.scatterplot(x="Age", y="Fare", hue="Survived", style="Pclass", data=df)
plt.title("Survival Rate by Age and Passenger Class")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

sns.pairplot(df[["Age", "Fare", "Pclass", "Survived"]].dropna(), hue="Survived")
plt.show()

# --- Correlation heatmap (numeric columns)
plt.figure(figsize=(8, 6))
sns.heatmap(df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# =====================================================================================
# %% PRACTICAL 6: Training / testing dataset to predict probability of survival on Titanic
# (based on gender, age and passenger class) - Logistic Regression
# =====================================================================================
print("\n===== PRACTICAL 6: Titanic survival prediction =====")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# a. Load the data
data = pd.read_csv(get_csv("titanic.csv", "train.csv"))

# b. Select relevant features
data = data[["Survived", "Pclass", "Sex", "Age"]].copy()

# c. Handle missing values in Age (median)
data["Age"] = data["Age"].fillna(data["Age"].median())

# d. Encode categorical variable
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# Split the data (80/20)
X = data[["Pclass", "Sex", "Age"]]
y = data["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training set:", X_train.shape, " Testing set:", X_test.shape)

# Build and train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Probability of survival
probabilities = model.predict_proba(X_test)[:, 1]
print("Predicted probabilities of survival (first 10):", np.round(probabilities[:10], 3))

# Probability for a new passenger: [Pclass, Sex, Age]
new_passenger = pd.DataFrame({"Pclass": [1], "Sex": [1], "Age": [25]})
print("\nSurvival probability (1st class, female, age 25): %.2f%%" % (model.predict_proba(new_passenger)[0][1] * 100))
new_passenger = pd.DataFrame({"Pclass": [3], "Sex": [0], "Age": [40]})
print("Survival probability (3rd class, male, age 40)  : %.2f%%" % (model.predict_proba(new_passenger)[0][1] * 100))


# =====================================================================================
# %% PRACTICAL 7: Simple and Multiple Linear Regression with scikit-learn
# =====================================================================================
print("\n===== PRACTICAL 7: Linear Regression =====")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# If your_dataset.csv is not available, build a sample salary dataset
if not os.path.exists("your_dataset.csv"):
    rng = np.random.default_rng(42)
    n = 60
    exp = np.round(rng.uniform(1, 15, n), 1)
    age = np.round(21 + exp + rng.uniform(0, 6, n)).astype(int)
    edu = rng.integers(1, 5, n)
    sal = 25000 + 6500 * exp + 3000 * edu + rng.normal(0, 4000, n)
    pd.DataFrame({"YearsExperience": exp, "Age": age, "EducationLevel": edu,
                  "Salary": np.round(sal)}).to_csv("your_dataset.csv", index=False)
    print("[your_dataset.csv not found - sample salary dataset created]")

data = pd.read_csv("your_dataset.csv")
print(data.head())

# ---------------- Simple Linear Regression ----------------
X_simple = data[["YearsExperience"]]
y_simple = data["Salary"]
X_train_simple, X_test_simple, y_train_simple, y_test_simple = train_test_split(
    X_simple, y_simple, test_size=0.2, random_state=42)

simple_model = LinearRegression()
simple_model.fit(X_train_simple, y_train_simple)
y_pred_simple = simple_model.predict(X_test_simple)

mse_simple = mean_squared_error(y_test_simple, y_pred_simple)
r2_simple = r2_score(y_test_simple, y_pred_simple)
print("\n--- Simple Linear Regression ---")
print(f"Slope (m): {simple_model.coef_[0]:.2f}   Intercept (b): {simple_model.intercept_:.2f}")
print(f"Simple Linear Regression MSE: {mse_simple:.2f}")
print(f"Simple Linear Regression R²: {r2_simple:.2f}")

order = np.argsort(X_test_simple["YearsExperience"].values)       # sort so the line is drawn cleanly
plt.scatter(X_test_simple, y_test_simple, color="blue", label="Actual")
plt.plot(X_test_simple.values[order], y_pred_simple[order], color="red", label="Predicted")
plt.title("Simple Linear Regression")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

# ---------------- Multiple Linear Regression ----------------
X_multiple = data[["YearsExperience", "Age", "EducationLevel"]]
y_multiple = data["Salary"]
X_train_multiple, X_test_multiple, y_train_multiple, y_test_multiple = train_test_split(
    X_multiple, y_multiple, test_size=0.2, random_state=42)

multiple_model = LinearRegression()
multiple_model.fit(X_train_multiple, y_train_multiple)
y_pred_multiple = multiple_model.predict(X_test_multiple)

mse_multiple = mean_squared_error(y_test_multiple, y_pred_multiple)
r2_multiple = r2_score(y_test_multiple, y_pred_multiple)
n_test, k = X_test_multiple.shape
adj_r2 = 1 - (1 - r2_multiple) * (n_test - 1) / (n_test - k - 1)
print("\n--- Multiple Linear Regression ---")
print("Coefficients:", dict(zip(X_multiple.columns, np.round(multiple_model.coef_, 2))))
print(f"Intercept: {multiple_model.intercept_:.2f}")
print(f"Multiple Linear Regression MSE: {mse_multiple:.2f}")
print(f"Multiple Linear Regression R²: {r2_multiple:.2f}")
print(f"Adjusted R²: {adj_r2:.2f}")

plt.scatter(y_test_multiple, y_pred_multiple, color="green")
plt.plot([y_test_multiple.min(), y_test_multiple.max()],
         [y_test_multiple.min(), y_test_multiple.max()], "r--")
plt.title("Multiple Linear Regression: Actual vs Predicted")
plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.show()


# =====================================================================================
# %% PRACTICAL 8: Decision Tree Classifier using Python with a suitable dataset (Iris)
# =====================================================================================
print("\n===== PRACTICAL 8: Decision Tree Classifier =====")
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data["target"] = iris.target
print(data.head())

X = data.drop("target", axis=1)
y = data["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)
y_pred = dt_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=iris.target_names)
print(f"Accuracy: {accuracy:.2f}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{class_report}")

plt.figure(figsize=(14, 8))
tree.plot_tree(dt_classifier, feature_names=iris.feature_names,
               class_names=iris.target_names, filled=True)
plt.title("Decision Tree - Iris")
plt.show()


# =====================================================================================
# %% PRACTICAL 9 and 10: AND / NAND and OR / NOR gates using Feed-Forward Neural Network
# (Keras: 2 inputs -> 2 sigmoid hidden neurons -> 1 sigmoid output)
# =====================================================================================
import os as _os
_os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import keras
from keras.models import Sequential
from keras.layers import Dense, Input

keras.utils.set_random_seed(42)

X_gate = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])


def create_and_train_model(X, y, hidden=2, epochs=5000):
    model = Sequential()
    model.add(Input(shape=(2,)))
    model.add(Dense(hidden, activation="sigmoid"))          # hidden layer
    model.add(Dense(1, activation="sigmoid"))               # output layer
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(X, y, epochs=epochs, verbose=0)
    return model


def show_gate(model, X, y, name):
    pred = model.predict(X, verbose=0)
    print(f"\n{name} Gate Predictions:")
    print(" A B | target | probability | output")
    for (a, b), t, p in zip(X, y.ravel(), pred.ravel()):
        print(f" {a} {b} |   {t}    |   {p:.4f}    |   {int(p >= 0.5)}")
    print("Accuracy:", model.evaluate(X, y, verbose=0)[1])


def plot_predictions(model, X, title):
    predictions = model.predict(X, verbose=0)
    plt.scatter(X[:, 0], X[:, 1], c=predictions.flatten(), cmap="coolwarm", s=300)
    for (a, b), p in zip(X, predictions.flatten()):
        plt.text(a, b + 0.06, f"{p:.2f}", ha="center")
    plt.colorbar(label="Predicted output")
    plt.title(title)
    plt.xlabel("Input 1")
    plt.ylabel("Input 2")
    plt.xlim(-0.3, 1.3)
    plt.ylim(-0.3, 1.3)
    plt.show()


# %% PRACTICAL 9: AND / NAND gate using FFNN
print("\n===== PRACTICAL 9: AND / NAND gate =====")
y_and = np.array([[0], [0], [0], [1]])        # AND gate outputs
y_nand = np.array([[1], [1], [1], [0]])       # NAND gate outputs

and_model = create_and_train_model(X_gate, y_and)
nand_model = create_and_train_model(X_gate, y_nand)
show_gate(and_model, X_gate, y_and, "AND")
show_gate(nand_model, X_gate, y_nand, "NAND")
plot_predictions(and_model, X_gate, "AND Gate Predictions")
plot_predictions(nand_model, X_gate, "NAND Gate Predictions")

# %% PRACTICAL 10: OR / NOR gate using FFNN
print("\n===== PRACTICAL 10: OR / NOR gate =====")
y_or = np.array([[0], [1], [1], [1]])         # OR gate outputs
y_nor = np.array([[1], [0], [0], [0]])        # NOR gate outputs

or_model = create_and_train_model(X_gate, y_or)
nor_model = create_and_train_model(X_gate, y_nor)
show_gate(or_model, X_gate, y_or, "OR")
show_gate(nor_model, X_gate, y_nor, "NOR")
plot_predictions(or_model, X_gate, "OR Gate Predictions")
plot_predictions(nor_model, X_gate, "NOR Gate Predictions")
