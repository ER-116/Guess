import random      #引入随机数作为答案
key = random.randint(1,10)     #随机数范围1~10
print('LWY made')
total = 0               #总次数
board = 1               #是否重试
right = 0               #正确次数
wrong = 0               #错误次数
retry = 'yes'
while (retry != 'no'):
        times = 3      #三次机会
        answer = input('猜猜我想的数字是什么：')   #抛出问题，用回答给answer赋值
        guess = int(answer)      #将answer转化为数字
        times = times - 1
        total = total + 1
        print('您的剩余次数',int(times))
        if guess > key:
                print('猜大了！')
        else:
                if guess < key:
                        print('猜小啦！')
                else:
                        print('哇塞！')
                        print
        while (guess != key) and (times>0):    #当猜错且机会大于零时循环
                answer = input('猜错了，请重新输入：')
                guess=int(answer)
                times = times - 1
                total = total + 1
                if guess == key:
                    print('这么强？！')
                else:
                    print('您的剩余次数')
                    print(int(times))     #显示剩余次数
                    if guess > key:
                            print('猜大了！')
                    else:
                            print('猜小啦！')
                        
        if guess == key:     #三种不同的结局：一次猜对，三次内猜对以及没猜对
                if int(times) == 2:
                        print('一次答对？？？这运气没谁了')
                        right = right + 1
                else:
                        print('猜对了!')
                        print('游戏结束!')
                        right = right + 1
        else:
            print('次数用尽，游戏结束')
            wrong = wrong + 1
        board = input('输入"E"查看计分板:')
        if board == 'E':               #输入E显示计分板
                print('总次数：',int(total))
                print('猜对次数：',int(right))
                print('猜错次数：',int(wrong))
        else:
                print('好吧，既然这样那么')
        retry = input('是否重玩？yes/no:')
print('游戏结束')
