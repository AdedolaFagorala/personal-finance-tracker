Personal Finance Tracker

A command-line application written in Python that helps users manage personal finances by recording income and expenses, tracking balances, searching transactions, and generating reports.

Features
Add transactions: Record income and expenses with an amount, category, and description.
List transactions: View all saved transactions.
Edit transactions: Update existing transaction details.
Delete transactions: Remove transactions by their list number.
View summaries: Calculate total income, total expenses, and current balance.
Analyze spending: View expenses grouped by category.
Search transactions: Find transactions by description, type, or category.
Date-range reports: View transactions and summaries for a specified period.
Persistent storage: Save transactions locally in a JSON file.
Automated tests: Test transaction handling, data storage, and reporting functions.
Requirements
Python 3.10 or newer
No third-party Python packages required
Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL
cd personal-finance-tracker

No additional packages need to be installed.

Usage

Run all commands from the project directory.

List transactions
python3 main.py list
Add income
python3 main.py add income 2500 Salary "Monthly salary"
Add an expense
python3 main.py add expense 45.50 Food "Groceries"
View a summary
python3 main.py summary
Edit a transaction

Replace 1 with the transaction number you want to edit.

python3 main.py edit 1 --amount 60 --category Food --description "Weekly groceries"
Delete a transaction

Replace 1 with the transaction number you want to remove.

python3 main.py delete 1
Search transactions

Search descriptions and categories for a keyword:

python3 main.py search --query groceries

Filter by transaction type:

python3 main.py search --type expense

Filter by category:

python3 main.py search --category Food
Generate a date-range report
python3 main.py report --from-date 2026-10-01 --to-date 2026-10-31

Change the dates to the period you want to review.

Data Storage

Transactions are stored locally in data/transactions.json. This file is created automatically when transactions are saved.

The transaction data file is excluded from Git so personal financial information is not accidentally committed to the repository.

Important: Back up your transaction data if you want to preserve it. Cloning the repository does not include your local transaction history.

Running Tests

Run the automated test suite with:

python3 -m unittest discover -s tests -v
Project Structure
personal-finance-tracker/
├── main.py
├── transaction.py
├── storage.py
├── reports.py
├── tests/
│   ├── test_transaction.py
│   ├── test_storage.py
│   └── test_reports.py
├── .gitignore
└── README.md
Future Improvements
Monthly spending summaries
Budget limits by category
Export reports to CSV
Visual spending charts
License

This project is available for personal and educational use.
