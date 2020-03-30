# 直接运行即可，随意修改可能会报错
age = 414//23
number = input('猜一猜闻闻的年龄（1-30之间）')
times = 1

while True:
  if times > 2:
    break
  if number.isnumeric():
    if int(number) == age:
      break
    if int(number) > age:
      number = input('闻闻还没有这么大')
    else:
      number = input('猜小了')
  else:
    number = input('需要在下方输入数字')
  times += 1

if times > 2 and int(number) != age:
  print('三次机会用完了')
else:
  print('恭喜你猜中了')
print('闻闻的年龄是' + str(age))

#import random
#menu = ['鸭血粉丝', '黄焖鸡米饭', '虾饺', '秦镇米皮', '麻辣烫', '盖浇饭']
#print(random.choice(menu))

print('曾经有一段真挚的爱情摆在我眼前')
print('我没有去珍惜等到失去了才后悔莫及。')
print('尘世间最痛苦的事莫过于此，')
print('如果上天能给我一个再来一次的机会，')
print('我希望能对那个女孩说我爱你，')
print('如果非要给这份爱加一个期限的话，')
print('我希望是一万年。')
print(' ')
print('    *****    *****')
print('   *******  *******')
print('  ******************')
print('   ****************')
print('     ************')
print('       ********')
print('          **')