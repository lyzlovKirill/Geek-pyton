my_list = [7, 5, 3, 3, 2]

m = int(input("Сколько цифр вы хотите добавить? "))
# добавляем m - количество вводимых элементов, чтобы цикл не был бесконечным

i = 0

while i < m:
    n = int(input("Введите цифру "))
    my_list.append(n)
    my_list.sort()
    my_list.reverse()
    print(my_list)
    i = i + 1

