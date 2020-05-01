# Как реализовать для любого количества товаров не успел придумать. Пока только для 3
print("К сожалению, на данном этапе разработки вы можете ввести только 3 товара")

n = 3
# Количество позиций

i = 1
staff1 = {}
staff2 = {}
staff3 = {}
# Словари для характеристик товаров

name_list = []
price_list = []
amount_list = []
dimension_list = []

# словари для сбора характеристик по отдельным ключам

while i <= n:
    my_dict = {}
    name = input("Введите название ")
    my_dict["название"] = name
    name_list.insert(i, name)
    price = input("Введите цену ")
    my_dict["цена"] = price
    price_list.insert(i, price)
    amount = input("Введите количество ")
    my_dict["количесто"] = amount
    amount_list.insert(i, amount)
    dimension = input("Введите единицы ")
    my_dict["ед"] = dimension
    dimension_list.insert(i, dimension)
    if i == 1:
        staff1.update(my_dict)
    elif i == 2:
        staff2.update(my_dict)
    else:
        staff3.update(my_dict)
    i = i + 1

# в цикле собираем информацию и сразу формируем и словари с характеристиками и списки по отдельным ключам


staff1 = ("staff1", staff1)
staff2 = ("staff2", staff2)
staff3 = ("staff3", staff3)

print(staff1)
print(staff2)
print(staff3)
print(name_list)
print(price_list)
print(amount_list)
print(dimension_list)

# выводим все на экран