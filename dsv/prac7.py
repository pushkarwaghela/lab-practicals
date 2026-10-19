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
