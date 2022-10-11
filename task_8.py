money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def trash(mc, sl, sp, ic):
    k = 1
    l = 0
    while mc > 0:
        k *= (1 + ic)
        mc += sl - sp * k
        l += 1
    return l // 2


# TODO Оформить решение

print(trash(money_capital, salary, spend, increase))
