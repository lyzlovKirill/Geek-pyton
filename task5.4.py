#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1 Two — 2 Three — 3 Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.

f = open("task5.4.txt", 'r', encoding="UTF-8")
f_1 = open("task5.4-2.txt", 'w', encoding="UTF-8")
namerus = 0
for i in f:
    s = i.split()
    name = s[0]
    if name == "One":
        namerus = "Один - 1"
        f_1.write(namerus + '\n')
    elif name == "Two":
        namerus = "Два -2"
        f_1.write(namerus + '\n')
    elif name == "Three":
        namerus = "Три - 3"
        f_1.write(namerus + '\n')
    elif name == "Four":
        namerus = "Четыре - 4"
        f_1.write(namerus + '\n')

f.close()
f_1.close()