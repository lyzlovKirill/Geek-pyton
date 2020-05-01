
while True:
    revenue = int(input("Укажите выручку: "))
    if revenue >= 0:
        break

while True:
    costs = int(input("Укажите издержки: "))
    if costs >= 0:
        break

if revenue > costs:
    print("Фирма работает с прибылью")
    profitability = (revenue-costs) / revenue * 100
    print("Рентабельность: ", profitability, "%")
    number_of_employees = int(input("Укажите число сотрудников: "))
    profit_employees = (revenue-costs) / number_of_employees
    print("Прибыль фирмы на одного сотрудника: ", profit_employees)
    
elif revenue < costs:
    print("Фирма работает в убыток")

elif revenue == costs:
    print("Фирма работает в ноль")