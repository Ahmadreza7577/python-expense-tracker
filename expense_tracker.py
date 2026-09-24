import json
from datetime import datetime

EXPENSES_FILE = "expenses.json"


def load_expenses():
    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)




def add_expense(expenses):
    print("\n--- Add Expense ---")

    title = input("Title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    try:
        amount = float(input("Amount (€): "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    valid_categories = [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Other"
    ]

    category = input(
        "Category (Food/Transport/Shopping/Bills/Other): "
    ).strip().title()

    if category not in valid_categories:
        print("Invalid category.")
        print(
            "Please choose: Food, Transport, Shopping, Bills, or Other."
        )
        return

    date_input = input(
        "Date (YYYY-MM-DD) [Press Enter for today]: "
    ).strip()

    if not date_input:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")






def show_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"{expense['title']} | "
            f"€{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total: €{total:.2f}")



def monthly_report(expenses):
    print("\n--- Monthly Report ---")

    if not expenses:
        print("No expenses found.")
        return

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid format. Use YYYY-MM.")
        return

    monthly_expenses = [
        expense
        for expense in expenses
        if expense["date"].startswith(month)
    ]

    if not monthly_expenses:
        print("No expenses found for this month.")
        return

    total = sum(
        expense["amount"]
        for expense in monthly_expenses
    )

    print(f"\nExpenses for {month}")
    print("-" * 35)

    for expense in monthly_expenses:
        print(
            f"{expense['date']} | "
            f"{expense['title']} | "
            f"€{expense['amount']:.2f} | "
            f"{expense['category']}"
        )

    print("-" * 35)
    print(f"Monthly total: €{total:.2f}")



def show_statistics(expenses):
    print("\n--- Expense Statistics ---")

    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)
    highest = max(expenses, key=lambda expense: expense["amount"])

    print(f"Total expenses: €{total:.2f}")
    print(f"Average expense: €{average:.2f}")

    print("\nHighest expense:")
    print(f"Title: {highest['title']}")
    print(f"Amount: €{highest['amount']:.2f}")
    print(f"Category: {highest['category']}")
    print(f"Date: {highest['date']}")



def search_expenses(expenses):
    print("\n--- Search Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    keyword = input("Enter title or category to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = []

    for expense in expenses:
        if (
            keyword in expense["title"].lower()
            or keyword in expense["category"].lower()
        ):
            results.append(expense)

    if not results:
        print("No matching expenses found.")
        return

    print("\n--- Search Results ---")

    for index, expense in enumerate(results, start=1):
        print(
            f"{index}. "
            f"{expense['title']} | "
            f"€{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )

def show_category_summary(expenses):
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category, total in categories.items():
        print(f"{category:<15} €{total:.2f}")

def delete_expense(expenses):
    show_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(number - 1)
        save_expenses(expenses)

        print(f"Deleted: {deleted['title']}")

    except ValueError:
        print("Please enter a valid number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("      EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Total")
        print("4. Category Summary")
        print("5. search Expense")
        print("6. statistics")
        print("7. Monthly Report")
        print("8. Delete Expense")
        print("9. Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            show_category_summary(expenses)

        elif choice == "5":
            search_expenses(expenses)
       
        elif choice =="6":
            show_statistics(expenses)

        elif choice =="7":
            monthly_report(expenses)
        
        elif choice == "8":
           delete_expense(expenses)
      
        elif choice == "9":
           print("Goodbye!")
           break  

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
