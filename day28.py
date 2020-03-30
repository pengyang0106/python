def guess_num(num):
  if num > 100:
    print('请输入1-100的数字')
  elif num <1 :
    print('请输入1-100的数字')
  elif num == 7:
    print('哼，这是我最不喜欢的数字！')
  elif num == 88:
    print('哇，你我果然心有灵犀！')
  elif num < 88:
    print('猜小了')
  elif num > 88:
    print('猜大了')

guessed_num = int(input('请你猜一个1-100内我最喜欢的数字：'))
guess_num(guessed_num)

import random

num = random.randint(1, 100)
guess_chances = 7
print('您只有7次猜数字的机会哦！')

for i in range(1, guess_chances + 1):
    print('这是第' + str(i) + '次猜数字')
    guess = input('请输入数字：')
    if guess.isdigit():
        guess = int(guess)
        if guess < num:
            print('您输入的数字太小了，您还有' + str(guess_chances - i) + '次机会，请重新输入：')
        elif guess > num:
            print('您输入的数字太大了，您还有' + str(guess_chances - i) + '次机会，请重新输入：')
        elif guess == num:
            print('恭喜您猜对了')
            break
    elif guess == 'q':
        print('退出游戏！')
        break
    else:
        print('输入的内容必须为整数，请重新输入：')
while (guess_chances - i) == 0:
    print('您输入已经超过7次，游戏结束！')
    break
————————————————
版权声明：本文为CSDN博主「难能可贵是梦想」的原创文章，遵循
CC
4.0
BY - SA
版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / dhr201499 / java / article / details / 81143398