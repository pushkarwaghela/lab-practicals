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


















