from address import Address
from mailing import Mailing

from_address = Address("607650", "Нижний Новгород", "проспект Гагарина", "111", "2")
to_address = Address("630625", "Санкт-Петербург", "Васильевская", "2", "3")

mailing = Mailing(to_address, from_address, 2000, "54321d")

print(mailing)  # вызов __str__()