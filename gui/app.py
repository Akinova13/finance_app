import tkinter as tk
from tkinter import messagebox
from models.income import Income
from models.expense import Expense
from services.finance_manager import FinanceManager

manager = FinanceManager()

def add_income():
    try:
        amount = float(entry_amount.get())
        manager.add_transaction(Income(amount, "Зарплата", "2025-01-01"))
        messagebox.showinfo("Успех", "Доход добавлен")
    except:
        messagebox.showerror("Ошибка", "Некорректный ввод")

root = tk.Tk()
root.title("Финансовый менеджер")

tk.Label(root, text="Сумма").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Добавить доход", command=add_income).pack()

root.mainloop()