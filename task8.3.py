#Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
#скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
#Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input("Введите цифры и нажмите Ввод "))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                ask = input(f'Попробовать еще раз? Y/N ')

                if ask == 'Y' or ask == 'y':
                    print(try_except.my_input())
                elif ask == 'N' or ask == 'n':
                    return f"Программа завершена"
                else:
                    return f"Программа завершена"

try_except = Error(1)
print(try_except.my_input())