def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Введите корректное число!")

def get_date(prompt):
    while True:
        date = input(prompt)
        if len(date) == 10:
            return date
        print("Формат: YYYY-MM-DD")