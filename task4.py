while True:
    number = input("Введите число ")
    if number.isdigit():
        number == int(number)
        break
# Предполагаем, что число может быть любой разрядности, то есть состоять из любого количества цифр

number = int(number)
i = 1

while True:
    number_discharge = number / i
    if number_discharge < 1:
        break
    i = i*10

print("Разрядность заданного числа:" , i/10)

# Выясняем разрядность числа. Как только результат деления становится меньше 1, значит предыдущее значение i
# имело столько же цифр, сколько в заданном числе

discharge = i / 10

list = []

# Задаем пустой список и переменную равную разряду заданного числа

while True:
    a = number // discharge
    list.append(a)
    number = number % discharge
    discharge = discharge / 10
    if discharge < 1:
        break

# Проводим целочисленное деление заданного числа на разряд, полученную цифру (значение старшего разряда)
# записываем в список list. Остаток от деления переприсваеваем в number.

list.sort()
print("Наибольшая цифра в числе:" , (list[-1]))

# Сортируем list и выводим на экран последнее значение

