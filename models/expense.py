from models.transaction import Transaction

class Expense(Transaction):
    def calculate_effect(self):
        return -self.amount