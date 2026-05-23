class Category:
    categories = [
        "Еда",
        "Транспорт",
        "Развлечения",
        "Зарплата",
        "Фриланс"
    ]

    @classmethod
    def choose_category(cls):
        print("\nВыберите категорию:")
        for i, cat in enumerate(cls.categories, 1):
            print(f"{i}. {cat}")

        while True:
            try:
                choice = int(input("Введите номер: "))
                if 1 <= choice <= len(cls.categories):
                    return cls.categories[choice - 1]
            except:
                pass
            print("Ошибка ввода, попробуйте снова.")