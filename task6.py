
while True:
    first_day_run = int(input("Сколько спортмен пробежал км в первый день: "))
    if first_day_run >= 0:
        break

while True:
    last_day_run = int(input("Сколько спортмен пробежал км в последний день: "))
    if last_day_run >= 0:
        break

if first_day_run >= last_day_run:
    print("Спортсмен пробежал нужно число км в первый день")
else:

    i = 1

    while True:
        i = i+1
        first_day_run = first_day_run * 1.1
        if first_day_run > last_day_run:
            break

    print("Спортсмен пробежал нужно число км в", i,  "день")


