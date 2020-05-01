len = int(input("Какое количество элементов надо ввести в список? "))
list = []
list2 = []

i = 0
while i < len:
    element = input("Введите элемент ")
    list.append(element)
    i = i +1

print("Исходный список", list)

i = 0
if len % 2 == 0:
    while i < len:
        list2.insert(i+1, list[i])
        list2.insert(i, list[i+1])
        i = i + 2
else:
    while i < len - 1:
        list2.insert(i+1, list[i])
        list2.insert(i, list[i+1])
        i = i + 2

if len % 2 != 0:
    list2.insert(len, list[-1])


print("Измененный список", list2)