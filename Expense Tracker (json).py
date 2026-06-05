import json

filename = "expenses.json"

# Expense data
expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Transport", "amount": 100},
    {"category": "Shopping", "amount": 500}
]

# Save to JSON file
with open(filename, "w") as file:
    json.dump(expenses, file, indent=4)

print("Expenses saved successfully!")

# Read from JSON file
with open(filename, "r") as file:
    data = json.load(file)

total = 0

print("\nExpense List:")
for item in data:
    print(f"{item['category']} - ₹{item['amount']}")
    total += item['amount']

print("\nTotal Expense: ₹", total)
