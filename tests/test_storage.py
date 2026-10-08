import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import storage
from transaction import Transaction


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "transactions.json"

        self.file_patch = patch.object(storage, "DATA_FILE", self.data_file)
        self.file_patch.start()
        self.addCleanup(self.file_patch.stop)
        self.addCleanup(self.temp_dir.cleanup)

    def test_load_returns_empty_list_when_file_missing(self):
        self.assertEqual(storage.load_transactions(), [])

    def test_save_and_load_transaction(self):
        transaction = Transaction(
            25.50, "Food", "Lunch", "expense"
        )

        storage.save_transactions([transaction])
        loaded = storage.load_transactions()

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].amount, 25.50)
        self.assertEqual(loaded[0].category, "Food")
        self.assertEqual(loaded[0].description, "Lunch")
        self.assertEqual(loaded[0].transaction_type, "expense")
        self.assertEqual(loaded[0].date, transaction.date)

    def test_save_writes_valid_json(self):
        transaction = Transaction(
            100, "Salary", "Paycheck", "income"
        )

        storage.save_transactions([transaction])

        with self.data_file.open("r") as file:
            data = json.load(file)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["category"], "Salary")


if __name__ == "__main__":
    unittest.main()
