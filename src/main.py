import pandas as pd

# Load Dataset
df = pd.read_csv("../data/sales_data.csv")

print("===== AI DATA ANALYSIS ASSISTANT =====")

while True:
    print("\nChoose an option:")
    print("1. Show Dataset")
    print("2. Average Salary")
    print("3. Highest Salary")
    print("4. Department Wise Average Salary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(df)

    elif choice == "2":
        print("Average Salary:", df["Salary"].mean())

    elif choice == "3":
        print(df[df["Salary"] == df["Salary"].max()])

    elif choice == "4":
        print(df.groupby("Department")["Salary"].mean())

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")