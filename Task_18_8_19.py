sumtickets = 0
tickets = int(input("Введитете количество билетов: "))
for age in range (tickets):
    age = int(input("Введите возвраст посетителя: "))
        if age < 18:
        sumtickets += 0
    elif 18 >= age <= 25:
        sumtickets += 990
    elif age > 25:
        sumtickets += 1390
if tickets > 3:
    sumtickets -= sumtickets / 100 * 10
print("Стоимость ваших билетов: ", sumtickets)