expenses = []

def add_expense(amount, category):
    expenses.append({'amount': amount, 'category': category})
    print(f"Expense of {amount} in {category} added.")

def view_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print("\nYour Expenses:")
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}")
    print(f"Total Expenses: {total}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            add_expense(amount, category)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid option.")
