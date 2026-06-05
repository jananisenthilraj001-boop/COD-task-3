import csv

filename = "expenses.csv"

# Add expenses
expenses = [
    ["Food", 250],
    ["Transport", 100],
    ["Shopping", 500]
]

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Amount"])
    writer.writerows(expenses)

print("Expenses saved successfully!")

# Read expenses and calculate total
total = 0

with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    print("\nExpense List:")
    for row in reader:
        print(f"{row[0]} - ₹{row[1]}")
        total += int(row[1])

print("\nTotal Expense: ₹", total)
