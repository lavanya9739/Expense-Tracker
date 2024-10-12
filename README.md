# Expense-Tracker
Create a Personal Expense Tracker that allows users to log their daily expenses, view summaries, and track their spending over time. This project will help you apply data structures, file handling, and basic data analysis in Python.

**Personal Expense Tracker**
A simple Python-based Personal Expense Tracker that allows users to log, manage, and summarize their daily expenses. The program stores data persistently using JSON files and provides both text-based and graphical summaries of expenses, using the matplotlib library for visualization.

**Features**
- Add Expenses: Log new expenses by specifying the amount, category, and date.
- View Expenses: View a list of all recorded expenses.
- Remove Expenses: Delete an expense from the list by its index.
- Summarize by Category: View total spending for each category.
- Summarize by Month: View total spending for each month.
- Total Expenses: View the total of all expenses.
- Data Persistence: Expenses are saved to a JSON file, ensuring data is stored between program runs.
- Graphical Summary: Provides bar charts for category-wise and month-wise expenses using matplotlib.
  
**Requirements**
Python 3.x
matplotlib (for graphical summaries)
Install matplotlib
You can install matplotlib using pip:

Upon starting the program, you will see a menu with options.
Choose the appropriate option by typing the number corresponding to the action you want to perform.
When adding an expense, you will need to provide the date, description (category), and amount.
Menu Options:

1. Add Expense: Add a new expense.
2. Remove Expense: Remove an expense by index.
3. View Expenses: View a list of all expenses.
4. Total Expenses: View the total amount of all expenses.
5. Summary by Category: View the total amount spent in each category with a bar chart.
6. Summary by Month: View the total amount spent each month with a bar chart.
7. Exit: Exit the program.

Example Usage

**Adding an Expense**
- Enter date (YYYY-MM-DD): 2024-10-12
- Enter description: Food
- Enter amount: $45.00
- Expense added successfully!
- Viewing a Bar Chart of Expenses by Category

**Expenses by Category:**
- Food: $150.00
- Transport: $75.00
- Entertainment: $30.00
- This will display a bar chart with categories on the x-axis and total expenses on the y-axis.

**File Structure**
bash
code
├── expense_tracker.py   # Main Python file for the expense tracker
├── expenses.json        # JSON file where expenses are saved (automatically created)
└── README.md            # This README file

**Future Improvements**
Add the ability to edit existing expenses.
Add support for recurring expenses.
Implement more advanced data analysis features.
Improve the user interface (e.g., with a graphical user interface using Tkinter or PyQt).
