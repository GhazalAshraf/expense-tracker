# Expense Tracker

#### Video Demo: https://youtu.be/pkznP4q_hYY

#### Description:

Expense Tracker Ghazal Github : Ghazal Ashraf edX: ghazal12399 Erfurt Germany 16 september 2026Expense Tracker is a command-line Python program that helps users record and manage their everyday expenses. I created this project as my CS50P Final Project. The program allows a user to add expenses, view saved expenses, calculate the total amount spent, and delete an expense.

When the program starts, it displays a simple menu with five options. The first option allows the user to add a new expense. The user enters the name of the expense and the amount spent. For example, the user can enter "Coffee" and an amount of 5. The program checks that the amount is valid before adding it.

The second option displays all saved expenses. Each expense is shown with a number, description, and amount. These numbers also make it easier for the user to choose an expense to delete.

The third option calculates the total amount of all saved expenses. The program adds the amounts together and displays the result with two decimal places.

The fourth option allows the user to delete an expense. The user enters the number of the expense they want to remove. The program checks whether the number is valid before deleting the expense.

The fifth option exits the program.

The project uses a CSV file called `expenses.csv` to store information. This means that expenses are not lost when the program is closed. When the program starts again, it reads the saved expenses from the CSV file.

The main program is stored in `project.py`. The `main` function controls the menu and user interaction. The `add_expense` function adds expenses to the list and prevents invalid amounts. The `calculate_total` function calculates the total amount spent. The `format_expenses` function formats the expense list so that it is easy to read. The `delete_expense` function removes an expense using its number. The `save_expenses` and `load_expenses` functions are responsible for saving and loading data from the CSV file.

The file `test_project.py` contains automated tests using pytest. These tests check important functions such as adding an expense, calculating the total, and formatting expenses. Testing helped make sure that the main parts of the program work correctly.

I chose an expense tracker because it is a practical application that can be useful in everyday life. While developing the project, I learned more about functions, lists, dictionaries, CSV files, exception handling, loops, user input, and automated testing in Python.
