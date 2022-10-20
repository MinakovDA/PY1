salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
for i in range(months):
    need_money += salary - spend * (1 + increase) ** i
need_money = -need_money
print(round(need_money))
#У вас финальный ответ не учитывает, что цены растут лишь со 2го месяца
