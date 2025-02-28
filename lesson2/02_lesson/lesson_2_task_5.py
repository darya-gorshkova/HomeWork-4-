def month_to_season(numb_month):
    if numb_month == 1 or numb_month == 2 or numb_month == 12:
        return "Зима"
    elif numb_month == 3 or numb_month == 4 or numb_month == 5:
        return "Весна"
    elif numb_month == 6 or numb_month == 7 or numb_month == 8:
        return "Лето"
    elif numb_month == 9 or numb_month == 10 or numb_month == 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


try:
    numb_month = int(input("Введите номер месяца (1-12)"))
    print(month_to_season(numb_month))
except ValueError:
    print('Пожалуйста, введите целое число от 1 до 12')