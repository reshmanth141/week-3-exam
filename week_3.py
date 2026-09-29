import numpy as np
import pandas as pd

# Array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Average:", np.mean(arr))

# DataFrame
data = {
    "Name": ["ram", "Sam", "chai", "Sharsh"],
    "Salary": [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# filter
filtered_df = df[df["Salary"] > 55000]


print("\nFiltered DataFrame (Salary > 55000):")
print(filtered_df)

# statistics
print("\nStatistics:")


print("Mean Salary:", df["Salary"].mean())  




print("Median Salary:", df["Salary"].median())
print("Standard Deviation:", df["Salary"].std())p

