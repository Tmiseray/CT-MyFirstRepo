# Exercise 8: Personal Finance Tracker
"""
Objective: Develop a Python program to track and analyze personal finances, focusing on categorizing expenses and income. This exercise will cover file handling for maintaining financial records, integrating Python concepts such as functions, input handling, string manipulation, and try-except blocks, along with data structures like lists and dictionaries.

Problem Statement: Create a Python program to help manage personal finances by tracking expenses and income. The financial data will be stored in a file (finance_records.txt), with each line containing a date, type (expense/income), category, and amount, separated by commas (e.g., "2023-03-21, Expense, Food, 15.00"). The program should provide insights such as total expenses, total income, and spending by category.
filename = 'Module3/Lesson5/Exercise8/finance_records.txt'
"""

def read_finances(filename):
    try:
        with open(filename, 'r') as file:
            records = []
            for line in file:
                date, record_type, category, amount = line.strip().split(',')
                records.append({'date': date, 'type': record_type, 'category': category, 'amount': float(amount)})
            return records
    except FileNotFoundError:
        return []

def analyze_total_expenses(records):
    total_expenses = sum(record['amount'] for record in records if record['type'] == 'Expense')
    print(f"Total Expenses: ${total_expenses:.2f}")

def analyze_total_income(records):
    total_income = sum(record['amount'] for record in records if record['type'] == 'Income')
    print(f"Total Expenses: ${total_income:.2f}")

def analyze_spending_by_category(records):
    expenses_by_category = {}
    for record in records:
        if record['type'] == 'Expense':
            if record['category'] not in expenses_by_category:
                expenses_by_category[record['category']] = record['amount']
            else:
                expenses_by_category[record['category']] += record['amount']

    print("Spending by Category:")
    for category, amount in expenses_by_category.items():
        print(f"{category}: ${amount:.2f}")

def main():
    finances = read_finances('Module3/Lesson5/Exercise8/finance_records.txt')

    while True:
        print("\n1. Analyze Total Expenses")
        print("2. Analyze Total Income")
        print("3. Spending by Category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            analyze_total_expenses(finances)
        elif choice == '2':
            analyze_total_income(finances)
        elif choice == '3':
            analyze_spending_by_category(finances)
        elif choice =='4':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()