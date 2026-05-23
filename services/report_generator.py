from collections import Counter, defaultdict
import matplotlib.pyplot as plt


class ReportGenerator:

    @staticmethod
    def top_expenses(transactions):
        expenses = [t for t in transactions if t.calculate_effect() < 0]

        if not expenses:
            print("\nНет расходов для анализа")
            return

        counter = Counter(t.category for t in expenses)

        print("\nТоп расходов:")
        for cat, count in counter.most_common():
            print(f"{cat}: {count} операций")

    @staticmethod
    def expenses_chart(transactions):
        data = defaultdict(float)

        for t in transactions:
            if t.calculate_effect() < 0:
                data[t.category] += abs(t.amount)

        if not data:
            print("Нет данных для графика")
            return

        categories = list(data.keys())
        values = list(data.values())

        plt.figure()
        plt.bar(categories, values)
        plt.title("Расходы по категориям")
        plt.xlabel("Категории")
        plt.ylabel("Сумма")
        plt.show()