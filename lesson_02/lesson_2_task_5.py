def month_to_season(n_month):
    if n_month == 1 or n_month == 2 or n_month == 12:
        return "Зима"
    elif n_month == 3 or n_month == 4 or n_month == 5:
        return "Весна"
    elif n_month == 6 or n_month == 7 or n_month == 8:
        return "Лето"
    elif n_month == 9 or n_month == 10 or n_month == 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


try:
    numb_month = int(input("Введите номер месяца (1-12)"))
    print(month_to_season(numb_month))
except ValueError:
    print('Пожалуйста, введите целое число от 1 до 12')
