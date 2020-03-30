def calc_profit(n):
    price = 24
    cost = 8
    profit = (price - cost) * n - 500
    return profit

def calc_perf(profit):
    if profit > 2000:
        print('合格')
    else:
        print('不合格')

n = int(input('请输入今天咖啡店的销量'))
print(calc_profit(n))
profit = calc_profit(n)
calc_perf(profit)