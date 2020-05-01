year_dict = {"Январь": "Зима", "Февраль": "Зима", "Март": "Весна", "Апрель": "Весна", "Май": "Весна",
             "Июнь": "Лето", "Июль": "Лето", "Август": "Лето", "Сентябрь": "Осень", "Октябрь": "Осень",
             "Ноябрь": "Осень", "Декабрь": "Зима"}

while True:
    month = int(input("Введите номер месяца от 1 до 12 "))
    if month <= 12 and month >= 1:
        break

if month == 1:
    print(year_dict.get("Январь"))
elif month == 2:
    print(year_dict.get("Февраль"))
elif month == 3:
    print(year_dict.get("Март"))
elif month == 4:
    print(year_dict.get("Апрель"))
elif month == 5:
    print(year_dict.get("Май"))
elif month == 6:
    print(year_dict.get("Июнь"))
elif month == 7:
    print(year_dict.get("Июль"))
elif month == 8:
    print(year_dict.get("Август"))
elif month == 9:
    print(year_dict.get("Сентябрь"))
elif month == 10:
    print(year_dict.get("Октябрь"))
elif month == 11:
    print(year_dict.get("Ноябрь"))
else:
    print(year_dict.get("Декабрь"))


