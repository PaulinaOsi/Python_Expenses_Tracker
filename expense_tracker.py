from expense import Expense
import calendar
import datetime


def main():
    print("🎯 Running expense tracker")
    expense_file_path = "expenses.csv"
    budget = 2000000000

    # get( user to input expense
    expense = get_user_expense()
    print(expense)

    # write to file
    save_expense_to_file(expense, expense_file_path)

    # read file and summerize expense
    summerize_expense(expense_file_path, budget)

    pass


def get_user_expense():
    print(f"🎯 User expense")
    expense_name = input("🎯 Enter expense name: ")
    expense_amount = float(input("🎯 Enter expense amount: "))
    print(f"You entered {expense_name}, {expense_amount}")

    # categories
    expense_categories = [
        "🍔 Food",
        "🏡 Home",
        "📝 Work",
        "🥎 Fun",
        "⭐️ Misc",
    ]

    while True:
        print("select category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(
            input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print(f"invalid category, Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Save User expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summerize_expense(expense_file_path, budget):
    print("🎯 Summerize expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(
                ",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)
            print(line_expense)
    print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Categroy 📝:")
    for key, amount in amount_by_category.items():
        print(f"  {key}:${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f} this month!")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(f"budget Per Day: ${daily_budget:.2f}")


if __name__ == "__main__":
    main()
