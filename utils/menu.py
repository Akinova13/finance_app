from utils.colors import Colors

def show_menu():
    print(Colors.HEADER + "\n===== Финансовый менеджер =====")
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Показать все")
    print("4. Баланс")
    print("5. Фильтр по категории")
    print("6. Статистика")
    print("7. Сохранить")
    print("8. Загрузить")
    print("0. Выход")