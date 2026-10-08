import argparse

from storage import load_transactions, save_transactions
from transaction import Transaction


def add_transaction(args):
    if args.amount <= 0:
        print("Error: Amount must be greater than 0.")
        return

    if not args.category.strip():
        print("Error: Category cannot be empty.")
        return

    if not args.description.strip():
        print("Error: Description cannot be empty.")
        return

    transactions = load_transactions()

    transaction = Transaction(
        args.amount,
        args.category,
        args.description,
        args.type,
    )

    transactions.append(transaction)
    save_transactions(transactions)

    print("Transaction added successfully.")


def list_transactions(args):
    transactions = load_transactions()

    if not transactions:
        print("No transactions found.")
        return

    print(
        f"{'#':<5}{'DATE':<12}{'TYPE':<10}"
        f"{'CATEGORY':<18}{'AMOUNT':>12}  DESCRIPTION"
    )
    print("-" * 85)

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index:<5}{transaction.date:<12}"
            f"{transaction.transaction_type:<10}"
            f"{transaction.category:<18}"
            f"${transaction.amount:>10.2f}  "
            f"{transaction.description}"
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

    transaction = transactions.pop(index)
    save_transactions(transactions)

    print(
        f"Deleted {transaction.category}: "
        f"${transaction.amount:.2f}"
    )


def edit_transaction(args):
    transactions = load_transactions()

    if not transactions:
        print("No transactions found.")
        return

    index = args.number - 1

    if index < 0 or index >= len(transactions):
        print("Invalid transaction number.")
        return

    transaction = transactions[index]

    if args.amount is not None:
        if args.amount <= 0:
            print("Error: Amount must be greater than 0.")
            return
        transaction.amount = args.amount

    if args.category is not None:
        if not args.category.strip():
            print("Error: Category cannot be empty.")
            return
        transaction.category = args.category

    if args.description is not None:
        if not args.description.strip():
            print("Error: Description cannot be empty.")
            return
        transaction.description = args.description

    if args.type is not None:
        transaction.transaction_type = args.type

    save_transactions(transactions)
    print("Transaction updated successfully.")


def show_summary(args):
    transactions = load_transactions()

    total_income = sum(
        t.amount for t in transactions
        if t.transaction_type == "income"
    )

    total_expenses = sum(
        t.amount for t in transactions
        if t.transaction_type == "expense"
    )

    spending_by_category = {}

    for transaction in transactions:
        if transaction.transaction_type == "expense":
            category = transaction.category
            spending_by_category[category] = (
                spending_by_category.get(category, 0)
                + transaction.amount
            )

    print("Financial Summary")
    print("-" * 30)
    print(f"Total income:   ${total_income:,.2f}")
    print(f"Total expenses: ${total_expenses:,.2f}")
    print(f"Balance:        ${total_income - total_expenses:,.2f}")

    print("\nSpending by category")
    print("-" * 30)

    if spending_by_category:
        for category, amount in sorted(spending_by_category.items()):
            print(f"{category:<20} ${amount:,.2f}")
    else:
        print("No expenses found.")


def main():
    parser = argparse.ArgumentParser(
        description="Personal Finance Tracker"
    )
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser(
        "list", help="List all transactions"
    )
    list_parser.set_defaults(func=list_transactions)

    add_parser = subparsers.add_parser(
        "add", help="Add a transaction"
    )
    add_parser.add_argument(
        "type", choices=["income", "expense"]
    )
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("category")
    add_parser.add_argument("description")
    add_parser.set_defaults(func=add_transaction)

    delete_parser = subparsers.add_parser(
        "delete", help="Delete a transaction"
    )
    delete_parser.add_argument("number", type=int)
    delete_parser.set_defaults(func=delete_transaction)

    edit_parser = subparsers.add_parser(
        "edit", help="Edit an existing transaction"
    )
    edit_parser.add_argument("number", type=int)
    edit_parser.add_argument("--amount", type=float)
    edit_parser.add_argument("--category")
    edit_parser.add_argument("--description")
    edit_parser.add_argument(
        "--type", choices=["income", "expense"]
    )
    edit_parser.set_defaults(func=edit_transaction)

    summary_parser = subparsers.add_parser(
        "summary", help="Show financial summary"
    )
    summary_parser.set_defaults(func=show_summary)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()