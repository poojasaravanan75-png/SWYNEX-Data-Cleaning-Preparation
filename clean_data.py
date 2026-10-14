import pandas as pd

df = pd.read_csv("raw_data.csv")
print("Before:", df.shape)
print("Missing:\n", df.isna().sum()[df.isna().sum() > 0])
print("Duplicates:", df.duplicated().sum())

# 1. Duplicate records
df = df.drop_duplicates()

# 2. Inconsistent text (extra spaces, case, short codes)
df["Name"] = df["Name"].str.strip()
df["Sex"] = df["Sex"].str.strip().str.title()
df["Embarked"] = df["Embarked"].map({"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"})

# 3. Missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")

# 4. Data types (Survived / Pclass are categories, not numbers)
df["Survived"] = df["Survived"].map({0: "No", 1: "Yes"})
df["Pclass"] = df["Pclass"].astype("category")
df["Age"] = df["Age"].round().astype(int)

df.to_csv("cleaned_data.csv", index=False)
print("After:", df.shape)
print("Missing after:", df.isna().sum().sum())
print("Duplicates after:", df.duplicated().sum())
