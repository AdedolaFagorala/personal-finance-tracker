import unittest
from datetime import date

from transaction import Transaction


class TestTransaction(unittest.TestCase):
    def test_transaction_stores_amount(self):
        transaction = Transaction(
            25.50, "Food", "Lunch", "expense"
        )
        self.assertEqual(transaction.amount, 25.50)

    def test_transaction_stores_category(self):
        transaction = Transaction(
            25.50, "Food", "Lunch", "expense"
        )
        self.assertEqual(transaction.category, "Food")

    def test_transaction_stores_description(self):
        transaction = Transaction(
            25.50, "Food", "Lunch", "expense"
        )
        self.assertEqual(transaction.description, "Lunch")

    def test_transaction_stores_type(self):
        transaction = Transaction(
            25.50, "Food", "Lunch", "expense"
        )
        self.assertEqual(transaction.transaction_type, "expense")

    def test_transaction_date_is_today(self):
        transaction = Transaction(
            25.50, "Food", "Lunch", "expense"
        )
        self.assertEqual(transaction.date, date.today().isoformat())


if __name__ == "__main__":
    unittest.main()
