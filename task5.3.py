#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

f = open("task5.3.txt", 'r', encoding="UTF-8")
for i in f:
    s = i.split() #разбиваем строку на слова пробелами
    name = s[0]
    wage = s[1]
    if int(wage) < 20000:
        print(s[0], "получает меньше 20000")

f.close()

f = open("task5.3.txt", 'r', encoding="UTF-8")
line = 0
summ = 0
for i in f:
    s = i.split() #разбиваем строку на слова пробелами
    line = line + 1
    summ = summ + int(s[1])

middle = summ / line

print("Средняя зарплата равна ", middle)

f.close()


