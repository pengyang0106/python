def choose_destination(fuel):
# 补全代码
distance = fuel / 8 * 100

if distance >= 472:
    print('上海')
elif distance >= 435:
    print('杭州')
elif distance >= 175:
    print('南京')
else:
    print('先去加油站吧')

real_fuel = int(input('剩余油量： '))
choose_destination(real_fuel)