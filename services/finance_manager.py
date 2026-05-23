class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        return sum(t.calculate_effect() for t in self.transactions)

    def get_all(self):
        return self.transactions

    def filter_by_category(self, category):
        return [t for t in self.transactions if t.category == category]

    def total_income(self):
        return sum(t.amount for t in self.transactions if t.calculate_effect() > 0)

    def total_expense(self):
        return sum(t.amount for t in self.transactions if t.calculate_effect() < 0)