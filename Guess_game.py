"""
需求：
人机大战！！！
来一场真正男人的对决吧！！！
石头剪刀布的玄学古老智慧博弈，将在此展开！！！
你渴望力量吗？少年
"""
import random
print('嘿，少年。你渴望力量吗？')
print('那就与我一战吧！')
print('在下面这一行里面，给出你的答案。')
computer = random.randint(1, 3)
player = int(input('出招吧！石头请按1，剪刀请按2，布请按3。'))
if computer == player:
    print('直面暗影，找寻真理。')
elif (computer == 1and player == 2)or(computer == 2and player == 3)or(computer == 3and player == 1):
    print('Pwn!')
else:
    print('智者无忧')
