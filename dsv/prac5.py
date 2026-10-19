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
