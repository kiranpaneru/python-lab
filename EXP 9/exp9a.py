import numpy as np
import pandas as pd

print("--- NUMPY AND PANDAS DEMONSTRATION ---")

arr = np.array([10, 20, 30, 40, 50])

print("\nNumPy Array:", arr)
print("Sum of array:", np.sum(arr))
print("Mean of array:", np.mean(arr))

reshaped = arr.reshape(5, 1)
print("Reshaped Array:\n", reshaped)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22],
    'Marks': [85, 90, 88]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:\n", df)

print("\nNames Column:\n", df['Name'])

print("Average Marks:", df['Marks'].mean())

filtered = df[df['Marks'] > 85]
print("\nStudents with Marks > 85:\n", filtered)
