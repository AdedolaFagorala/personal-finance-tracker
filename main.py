import argparse

from storage import load_transactions, save_transactions
from transaction import Transaction


def add_transaction(args):
    transactions = load_transactions()

    transaction = Transaction(
        args.amount,
        args.category,
        args.description,
        args.type,
    )

    transactions.append(transaction)
    save_transactions(transactions)

    print("Transaction added:")
    print(f"  Amount: ${transaction.amount:.2f}")
    print(f"  Type: {transaction.transaction_type}")
    print(f"  Category: {transaction.category}")
    print(f"  Description: {transaction.description}")
    print(f"  Date: {transaction.date}")


def main():
    parser = argparse.ArgumentParser(
        description="Personal Finance Tracker"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser(
        "add",
        help="Add a financial transaction",
    )

    add_parser.add_argument(
        "type",
        choices=["income", "expense"],
        help="Transaction type",
    )

    add_parser.add_argument(
        "amount",
        type=float,
        help="Transaction amount",
    )

    add_parser.add_argument(
        "category",
        help="Transaction category",
    )

    add_parser.add_argument(
        "description",
        help="Transaction description",
    )

    add_parser.set_defaults(func=add_transaction)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()