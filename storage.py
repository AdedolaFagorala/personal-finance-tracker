import json
from pathlib import Path

from transaction import Transaction


DATA_FILE = Path("data/transactions.json")


def save_transactions(transactions):
    DATA_FILE.parent.mkdir(exist_ok=True)

    data = []

    for transaction in transactions:
        data.append(
            {
                "amount": transaction.amount,
                "category": transaction.category,
                "description": transaction.description,
                "transaction_type": transaction.transaction_type,
                "date": transaction.date,
            }
        )

    with DATA_FILE.open("w") as file:
        json.dump(data, file, indent=4)


def load_transactions():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r") as file:
        data = json.load(file)

    transactions = []

    for item in data:
        transaction = Transaction(
            item["amount"],
            item["category"],
            item["description"],
            item["transaction_type"],
        )

        transaction.date = item["date"]
        transactions.append(transaction)

    return transactions
