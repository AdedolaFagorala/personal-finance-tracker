def calculate_totals(transactions):
    total_income = sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "income"
    )

    total_expenses = sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "expense"
    )

    balance = total_income - total_expenses

    return {
        "income": total_income,
        "expenses": total_expenses,
        "balance": balance,
    }


def spending_by_category(transactions):
    spending = {}

    for transaction in transactions:
        if transaction.transaction_type == "expense":
            category = transaction.category
            spending[category] = (
                spending.get(category, 0) + transaction.amount
            )

    return spending


def filter_by_date(transactions, start_date, end_date):
    return [
        transaction
        for transaction in transactions
        if start_date <= transaction.date <= end_date
    ]
