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


def list_transactions(args):
    transactions = load_transactions()

    if not transactions:
        print("No transactions found.")
        return

    print(
        f"{'#':<5}"
        f"{'DATE':<12}"
        f"{'TYPE':<10}"
        f"{'CATEGORY':<18}"
        f"{'AMOUNT':>12}"
        f"  DESCRIPTION"
    )

    print("-" * 75)

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index:<5}"
            f"{transaction.date:<12}"
            f"{transaction.transaction_type:<10}"
            f"{transaction.category:<18}"
            f"${transaction.amount:>10.2f}"
            f"  {transaction.description}"
        )


def delete_transaction(args):
    transactions = load_transactions()

    if not transactions:
        print("No transactions found.")
        return

    index = args.number - 1

    if index < 0 or index >= len(transactions):
        print("Invalid transaction number.")
        return

    transaction = transactions[index]

    print(
        f"Deleting: ${transaction.amount:.2f} "
        f"{transaction.category} - {transaction.description}"
    )

    transactions.pop(index)
    save_transactions(transactions)

    print("Transaction deleted.")


def main():
    parser = argparse.ArgumentParser(
        description="Personal Finance Tracker"
    )

    subparsers = parser.add_subparsers(dest="command")

    # LIST command
    list_parser = subparsers.add_parser(
        "list",
        help="List all transactions",
    )

    list_parser.set_defaults(func=list_transactions)

    # ADD command
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

    # DELETE command
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a transaction",
    )

    delete_parser.add_argument(
        "number",
        type=int,
        help="Transaction number to delete",
    )

    delete_parser.set_defaults(func=delete_transaction)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()