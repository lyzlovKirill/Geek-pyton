year = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
         "Декабрь"]

while True:
    month = int(input("Введите номер месяца от 1 до 12 "))
    if month <= 12 and month >= 1:
        break

print("Вы ввели ", year[month-1])

if month <= 2:
    print("Зима")
elif month <= 5:
    print("Весна")
elif month <= 8:
    print("Лето")
elif month <= 11:
    print("Осень")
else:
    print("Зима")



