# Проверяем, что введено число
while True:
    number = input("Введите число ")
    if number.isdigit():
        number == int(number)
        break

# Преобразуем строку в числа увличивая изначальную строчку в 2 и 3 раза

n = int(number)
nn = int(number*2)
nnn = int(number*3)
summ = n+nn+nnn

print(summ)

