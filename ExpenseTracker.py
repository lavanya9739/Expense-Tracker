import json
from datetime import datetime
import matplotlib.pyplot as plt

class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

    def to_dict(self):
        return {"date": self.date, "description": self.description, "amount": self.amount}


class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()  # Load existing expenses from file

    # File Handling to load expenses from JSON
    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)
                return [Expense(**exp) for exp in data]
        except FileNotFoundError:
            return []

    # File Handling to save expenses to JSON
    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump([exp.to_dict() for exp in self.expenses], file, indent=4)

    # Adding the expense
    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()  # Save after adding
        print("Expense added successfully!")

    # Removing the expense by index
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()  # Save after removing
            print("Expense removed successfully!")
        else:
            print("Invalid expense index")

    # Viewing all expenses
    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")

    # Calculating total expenses
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

    # Summarizing expenses by category (description)
    def summary_by_category(self):
        if not self.expenses:
            print("No expenses to summarize.")
            return

        summary = {}
        for expense in self.expenses:
            if expense.description not in summary:
                summary[expense.description] = 0
            summary[expense.description] += expense.amount

        print("\nExpenses by Category:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")

        self.plot_bar_chart(summary, title="Expenses by Category", xlabel="Category", ylabel="Amount")

    # Summarizing spending by month
    def summary_by_month(self):
        if not self.expenses:
            print("No expenses to summarize.")
            return

        monthly_summary = {}
        for expense in self.expenses:
            month = datetime.strptime(expense.date, "%Y-%m-%d").strftime("%Y-%m")
            if month not in monthly_summary:
                monthly_summary[month] = 0
            monthly_summary[month] += expense.amount

        print("\nExpenses by Month:")
        for month, total in monthly_summary.items():
            print(f"{month}: ${total:.2f}")

        self.plot_bar_chart(monthly_summary, title="Expenses by Month", xlabel="Month", ylabel="Amount")

    # Function to plot a bar chart using matplotlib
    def plot_bar_chart(self, data, title, xlabel, ylabel):
        categories = list(data.keys())
        amounts = list(data.values())

        plt.bar(categories, amounts, color='skyblue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()  # Adjusts the plot to fit labels
        plt.show()


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Summary by Category")
        print("6. Summary by Month")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: $"))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)

        elif choice == "2":
            index = int(input("Enter expense index to remove: ")) - 1
            tracker.remove_expense(index)

        elif choice == "3":
            tracker.view_expenses()

        elif choice == "4":
            tracker.total_expenses()

        elif choice == "5":
            tracker.summary_by_category()

        elif choice == "6":
            tracker.summary_by_month()

        elif choice == "7":
            print("Exiting the program")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
