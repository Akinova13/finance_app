from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    @abstractmethod
    def calculate_effect(self):
        pass

    def get_info(self):
        return f"{self.date} | {self.category} | {self.amount}"