money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
i = money_capital+salary

while i > 0:
    i -= spend*(1+0.5)**month
    month += 1
    if i>0:
        i+= salary

print(month)
