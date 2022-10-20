money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение


while money_capital > 0:

    money_capital -= (spend + spend * increase)**month
    month += 1
    if money_capital > 0:
        money_capital += salary
else:
    print(month)
