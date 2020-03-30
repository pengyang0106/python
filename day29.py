times = 0

def invite():
  # 按要求补全代码
  global times
  times = times + 1
  if times > 3:
    print('诸葛亮帮刘备平定天下去了')
  elif times == 3:
    print('三顾茅庐诸葛亮出山')
  elif times < 3:
    print('第'+ str(times) + "次请诸葛亮")

invite()
invite()
invite()
invite()