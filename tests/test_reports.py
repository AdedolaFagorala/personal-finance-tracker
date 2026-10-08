import unittest

from reports import (
    calculate_totals,
    spending_by_category,
    filter_by_date,
)
from transaction import Transaction


class TestReports(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            Transaction(2500.00, "Salary", "Paycheck", "income"),
            Transaction(45.50, "Food", "Groceries", "expense"),
            Transaction(20.00, "Food", "Lunch", "expense"),
            Transaction(100.00, "Bills", "Internet", "expense"),
        ]

    def test_calculate_totals(self):
        totals = calculate_totals(self.transactions)

        self.assertEqual(totals["income"], 2500.00)
        self.assertEqual(totals["expenses"], 165.50)
        self.assertEqual(totals["balance"], 2334.50)

    def test_spending_by_category(self):
        spending = spending_by_category(self.transactions)

        self.assertEqual(spending["Food"], 65.50)
        self.assertEqual(spending["Bills"], 100.00)
        self.assertNotIn("Salary", spending)

    def test_filter_by_date(self):
        results = filter_by_date(
            self.transactions,
            self.transactions[0].date,
            self.transactions[0].date,
        )

        self.assertEqual(len(results), len(self.transactions))


if __name__ == "__main__":
    unittest.main()
