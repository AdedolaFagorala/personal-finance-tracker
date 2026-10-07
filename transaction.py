from datetime import date


class Transaction:
    def __init__(self, amount, category, description, transaction_type):
        self.amount = amount
        self.category = category
        self.description = description
        self.transaction_type = transaction_type
        self.date = date.today().isoformat()





