from models.transaction import Transaction

class Income(Transaction):
    def calculate_effect(self):
        return self.amount