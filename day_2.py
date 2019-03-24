# project_2
import random
"""
算术运算符：
+  -  *  /  //  %
"""
num1 = 9
num2 = 4
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
# 判断12是不是偶数
num3 = 12
num3 = num3 % 2
print(num3)
"""
比较运算符
==  !=  >=  <=  <  >  
返回值是bool类型。
"""
print(12 == 3)
"""
逻辑运算符
not（取反）
and（与）
or（或）
操作数都是bool值
"""
b1 = True
b2 = False
print(not b1)
print(b1 and b2)
print(b1 or b2)
"""
流程控制语句
顺序结构
分支结构
    单分支 if
    双分支 if else
    多分支 if elif elif elif else
循环结构
"""
# 分支结构
# 单分支结构
# 格式： if 条件表达式：
#       语句1
#       语句2
# 注意事项：1必须要有冒号（：）
#          if体中的代码一定要缩进（优雅）
# 程序自顶向下顺序执行当遇到单分支结构，判断条件表达式是否成立。
# 若成立，则执行if体，否则不执行。
print('程序开始')
num = 10
if num < 32:
    print('hello')
    print('hi')
print('程序结束')
# 双分支结构
# 格式：if 条件表达式：
#       语句1
#       语句2
#      else：
#       语句3
#       语句4
# 程序自顶向下顺序执行。
# 若条件表达式成立，则执行if体。
# 否则执行else中的内容。
# 执行完双分支后，程序继续往下执行。
print('程序开始')
ticket = True
if ticket:
    print('欢迎乘坐！')
else:
    print('请先去买票，然后进站乘车')
print('程序结束')
# 多分支结构
# 格式：if 条件表达式1：
#       if体1
#      elif 条件表达式2：
#       if体2
#      elif 条件表达式3：
#       if体3
#      else：
#       else体
# 执行流程：
# 程序自顶向下执行。
# 先判断if中的条件表达式1是否成立。
# 若成立，则if体1，完成后跳出，继续往下执行。
# 否则，判断条件表达式2是否成立。
# 若成立，则if体2，完成后跳出，继续往下执行。
# 以此类推。
# 否则执行else体。
# 程序继续往下执行。
print('程序开始')
date = input('请输入节日名称:')
if date == '情人节':
    print('给女朋友买鲜花，看电影')
elif date == '圣诞节':
    print('逛街')
elif date == '生日':
    print('买蛋糕,过生日')
else:
    print('买早餐')
print('程序结束')
"""
random模块的使用
先 import导入模块
后 使用random模块中的函数
import random
random.randint
"""
num4 = random.randint(1, 3)
print('random的生成值为:', num4)
"""
循环格式：
while循环和for循环
while循环的格式：
    初始条件的设置:-->计数器(i)
    while 条件表达式:
        循环体
    修改计数器的值。
程序自顶向下执行，判断条件表达式是否成立。
若成立，执行循环体。继续判断条件表达式是否成立，直到不成立，程序往下执行。
否则，程序忽略循环体。
"""
print('唱首歌吧')
i = 0  # 计数器
while i < 10:
    print("凉凉凉凉凉凉凉凉凉凉")
    i = i+1
print('我唱完了')
# 死循环：没有正确调整计数器的值
print('我来给你算加法1加到100')
num5 = 0
i = 1
while i <= 100:
    print(num5)
    num5 = i + num5
    i = i+1
print('最后的值为')
print(num5)
print('下一题')
num6 = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        print(num6)
        num6 = i + num6
        i = i + 2
print('最后的值为')
print(num6)
print('下一题')
a = int(input('请输入一个整数作为a的值'))
b = int(input('请输入一个整数作为b的值'))
c = int(input('请输入一个整数作为c的值'))
d = int(input('请输入一个整数作为d的值'))
e = int(input('请输入一个整数作为e的值'))
sum123 = a + b + c + d + e
S = sum123 / 5
print('以上五个数字的平均数为', S)
print('结束')
# 你的循环体呢？？？？？？？？？？？？？
print('下一题')
i = 1
while i <= 5:
    num7 = int(input('请输入数字：'))
    if i == 1:
        max_n = num7
    else:
        if max_n < num7:
            max_n = num7
    i = i + 1
print(max_n)
"""
嵌套while循环
格式：
初始化条件1
while 条件表达式1：
    循环体1
    初始化条件2
    while 条件表达式2：
        循环体2
        初始化条件3
        while 条件表达式3：
            循环体3
            修改计数器3的值
        修改计数器2的值
    修改计数器1的值
循环结束，程序继续执行。
"""
