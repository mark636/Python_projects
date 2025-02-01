import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def load_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def save_expense(category, amount, date):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])


def add_expense():
    category = input("Enter expense category (e.g., Food, Rent, Transport): ")
    amount = input("Enter expense amount: ")
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    save_expense(category, amount, date)
    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nRecorded Expenses:")
    print(f"{'Category':<15} {'Amount':<10} {'Date':<12}")
    print("-" * 40)
    for category, amount, date in expenses:
        print(f"{category:<15} {amount:<10} {date:<12}")
    print("-" * 40)

def main():
    print("Welcome to Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
