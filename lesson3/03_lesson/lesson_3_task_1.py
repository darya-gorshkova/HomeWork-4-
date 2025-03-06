from user import User

# создаем экземпляр класса user
first_name, last_name = "Дарья", "Горшкова"
some_User = User(first_name, last_name)

# Вызываем методы и выводим результаты
print(some_User.get_first_name())
print(some_User.get_last_name())
print(some_User.get_user_info())

