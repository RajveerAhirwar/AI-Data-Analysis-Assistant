import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "sales_data.csv")

df = pd.read_csv(csv_path)

# Department wise average salary
department_salary = df.groupby("Department")["Salary"].mean()

# Create graph
fig, ax = plt.subplots(figsize=(6, 4))

department_salary.plot(kind="bar", ax=ax)

ax.set_title("Average Salary by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")

plt.tight_layout()
plt.show()
