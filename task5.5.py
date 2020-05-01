#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

a = ("4 15 24 56 32 78 192")

f = open("task5.5.txt", 'w', encoding="UTF-8")
f.write(a)
f = open("task5.5.txt", 'r', encoding="UTF-8")

x = f.readline()
x = list(map(int, x.split()))

summ = sum(x)
print(summ)







