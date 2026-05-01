# Step 1 & 2: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

print("--- PANDAS AND MATPLOTLIB DEMONSTRATION ---")

# Step 3: Create dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 90, 78, 92]
}

# Step 4: Create DataFrame
df = pd.DataFrame(data)

# Step 5: Display DataFrame
print("\nStudent Data:\n", df)

# Step 6: Bar Chart
plt.figure(figsize=(6,4))
plt.bar(df['Name'], df['Marks'], color='skyblue')
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Step 7: Line Graph
plt.figure(figsize=(6,4))
plt.plot(df['Name'], df['Marks'], marker='o', color='green')
plt.title("Student Marks - Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# Step 10: End
