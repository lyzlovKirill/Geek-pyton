#Реализовать два небольших скрипта:
#а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
#Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count

n = int(input("Задайте начало цикла "))
x = int(input("Задайте конец цикла "))

while True:
    for el in count(n):
        if el > x:
            break
        else:
            print(el)
