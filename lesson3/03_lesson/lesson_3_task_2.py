from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "Galaxy", "+79052323233"),
    Smartphone("Samsung", "M31", "+79052323235"),
    Smartphone("Techno", "Pro", "+79052323266"),
    Smartphone("iPhone", "14Pro", "+79052323255"),
    Smartphone("iPhone", "15Pro", "+79022222222")

]

for smartphone in catalog :
    print(f"{smartphone.mark_phone} - {smartphone.model_phone} . {smartphone.ab_number} .")

