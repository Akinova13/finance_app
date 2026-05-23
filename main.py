from models.income import Income
from models.expense import Expense
from models.category import Category
from services.finance_manager import FinanceManager
from services.data_manager import DataManager
from services.report_generator import ReportGenerator
from utils.input_validator import get_float, get_date
from utils.menu import show_menu

manager = FinanceManager()

while True:
    show_menu()
    choice = input("Выбор: ")

    if choice == "1":
        amount = get_float("Сумма: ")
        category = Category.choose_category()
        date = get_date("Дата (YYYY-MM-DD): ")
        manager.add_transaction(Income(amount, category, date))

    elif choice == "2":
        amount = get_float("Сумма: ")
        category = Category.choose_category()
        date = get_date("Дата (YYYY-MM-DD): ")
        manager.add_transaction(Expense(amount, category, date))

    elif choice == "3":
        for t in manager.get_all():
            print(t.get_info())

    elif choice == "4":
        print("Баланс:", manager.get_balance())

    elif choice == "5":
        cat = Category.choose_category()
        for t in manager.filter_by_category(cat):
            print(t.get_info())


    elif choice == "6":

        transactions = manager.get_all()

        print("DEBUG:", transactions)

        ReportGenerator.top_expenses(transactions)

        ReportGenerator.expenses_chart(transactions)

    elif choice == "7":
        DataManager.save(manager.get_all())

    elif choice == "8":
        manager.transactions = DataManager.load()

    elif choice == "0":
        break

    else:
        print("Ошибка выбора!")