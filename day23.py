def calc_loan(p, n, r):
    x1 = r * (1 + r) ** n
    x2 = (1 + r) ** n - 1
    return p * x1 / x2


print(calc_loan(1000000, 360, 0.0041))