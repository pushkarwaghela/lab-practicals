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