import pandas as pd

df = pd.read_csv("sample_data.csv")

print("Original data:")
print(df.head())

df = df.fillna(method="ffill")

print("\nData summary:")
print(df.describe())

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
