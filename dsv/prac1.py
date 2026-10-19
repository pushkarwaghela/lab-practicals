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