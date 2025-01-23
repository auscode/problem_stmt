import datetime
import csv

expenses = []

def generate_id():
    return len(expenses) + 1

def add_expense():
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date_input = input("Enter date (YYYY-MM-DD, leave blank for today): ")
    try:
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date() if date_input else datetime.date.today()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expense = {
        "id": generate_id(),
        "category": category,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_summary():
    if not expenses:
        print("No expenses recorded.\n")
        return

    summary_by_category = {}
    for expense in expenses:
        category = expense["category"]
        summary_by_category[category] = summary_by_category.get(category, 0) + expense["amount"]

    print("--- Expense Summary ---")
    for category, total in summary_by_category.items():
        print(f"Category: {category}, Total: ${total:.2f}")

    overall_total = sum(expense["amount"] for expense in expenses)
    print(f"Overall Total: ${overall_total:.2f}\n")

def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return

    print("--- Current Expenses ---")
    for expense in expenses:
        print(f"ID: {expense['id']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Date: {expense['date']}")

    try:
        expense_id = int(input("Enter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    global expenses
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    print("Expense deleted successfully!\n")

def export_to_file():
    if not expenses:
        print("No expenses to export.\n")
        return

    filename = "expenses.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Category", "Amount", "Date"])
        for expense in expenses:
            writer.writerow([expense["id"], expense["category"], expense["amount"], expense["date"]])

    print(f"Expenses exported to {filename} successfully!\n")

def main_menu():
    while True:
        print("===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Delete Expense")
        print("4. Export to File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            export_to_file()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
