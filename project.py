import csv


FILE = "expenses.csv"


def main():
    expenses = load_expenses()

    while True:
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            description = input("Expense name: ")

            try:
                amount = float(input("Amount: "))
                add_expense(expenses, description, amount)
                save_expenses(expenses)
                print("Expense added!")
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "2":
            print(format_expenses(expenses))

        elif choice == "3":
            print(f"Total: {calculate_total(expenses):.2f}")

        elif choice == "4":
            try:
                number = int(input("Expense number to delete: "))
                delete_expense(expenses, number)
                save_expenses(expenses)
                print("Expense deleted!")
            except ValueError:
                print("Invalid expense number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


def add_expense(expenses, description, amount):
    if amount <= 0:
        raise ValueError

    expenses.append({
        "description": description,
        "amount": amount
    })


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)


def delete_expense(expenses, number):
    if number < 1 or number > len(expenses):
        raise ValueError

    expenses.pop(number - 1)


def format_expenses(expenses):
    if not expenses:
        return "No expenses yet."

    lines = []

    for number, expense in enumerate(expenses, start=1):
        lines.append(
            f'{number}. {expense["description"]}: {expense["amount"]:.2f}'
        )

    return "\n".join(lines)


def save_expenses(expenses):
    with open(FILE, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["description", "amount"]
        )
        writer.writeheader()
        writer.writerows(expenses)


def load_expenses():
    try:
        with open(FILE) as file:
            reader = csv.DictReader(file)

            return [
                {
                    "description": row["description"],
                    "amount": float(row["amount"])
                }
                for row in reader
            ]

    except FileNotFoundError:
        return []


if __name__ == "__main__":
    main()
