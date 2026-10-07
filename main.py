from transaction import Transaction


transaction = Transaction(
    45.99,
    "Food",
    "Grocery store",
    "expense",
)

print(transaction.amount)
print(transaction.category)
print(transaction.description)
print(transaction.transaction_type)
print(transaction.date)
