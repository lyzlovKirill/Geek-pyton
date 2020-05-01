# Ввод количества секунд в цикле, чтобы не вводили отрицательные значения

while True:
    timesec = int(input("Введите время в секундах "))
    if timesec <= 0:
        print("Введите положительное число")
    else:
        break

# Расчет с помощью целочисленного деления и использования остатков от него

timehour = timesec // 3600
afterhour = timesec % 3600
timemin = afterhour // 60
timesec = afterhour % 60

print('{}:{}:{}'.format(timehour, timemin, timesec))

