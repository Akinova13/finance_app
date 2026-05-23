import json
import os
from models.income import Income
from models.expense import Expense

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data.json")


class DataManager:

    @staticmethod
    def save(transactions):
        data = []
        for t in transactions:
            data.append({
                "type": t.__class__.__name__,
                "amount": t.amount,
                "category": t.category,
                "date": t.date
            })

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load():
        if not os.path.exists(FILE_PATH):
            print("Файл не найден")
            return []

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        transactions = []

        for item in data:
            if item["type"] == "Income":
                transactions.append(
                    Income(item["amount"], item["category"], item["date"])
                )
            else:
                transactions.append(
                    Expense(item["amount"], item["category"], item["date"])
                )

        return transactions