# coding=gbk
print("hello world!")
print("nihao!")
# 这是单行注释 ctrl+/,单行注释只对一行起作用。
# 单行注释的位置一般在程序的上方或者后方标注。
"""
这是多行注释，使用三对单引号或者双引号。
python的结构是靠缩进来表示的。
"""
# 字符串类型
# 整型
print(10)
# 浮点型
print(3.1415926)
# bool类型,首字母必须是大写。
print(True)
print(False)
# ctrl+alt+L
# 字符串类型,使用单引号、双引号、三引号，里面的内容就是字符串。
print('hello world!')
print("hello world!!")
print("""hello world!!!""")
print(type('10'))
# <class 'str'>
print(type(10))
# <class 'int'>
print(type(True))
# <class 'bool'>
# 列表，字典，集合。
lst = ['Tom', 'Timmy', 'Tony']
print(type(lst))
# <class 'list'>
print(lst[5])
# 根据索引获取内容。
"""
格式：使用一对花括号，元素以键值对(key-value)形式存在，
多个键值对之间使用逗号隔开。
键和值之间使用冒号(:)连接
变量名称最好不要和数据类型的名称相同
"""
dic = {'name': '尼古拉斯赵四', 'age': 40, 'height': 1.55}
print(dic.get('name'))
# 使用get方式 获取内容。
print(dic['age'])
# 使用key方式 获取内容。
print(type(dic))
# <class 'dict'>
# 变量
"""
假设长方形长x=10，宽y=5，求面积z的大小。
x=10,y=5
z=x*y
z=10*5
x，y，z 就是变量。

在python中定义变量的格式和数学中相同。
格式：
变量=值
name=value
读法：把value赋值给name。
"""
# 练习1:使用变量保存QQ昵称和密码，并向控制台输出。
nick_name = '猪猪侠'
password = 123456
print(nick_name)
print(password)

# 练习2:使用变量保存个人信息，并输出到控制台。
# 需求：姓名 小明，年龄18，性别 不是男生，身高 1.78.
name = '小明'
age = 18
gender = False
height = 1.78

print(name)
print(age)
print(gender)
print(height)
print(name, age, gender, height,)
print('姓名：', name, '年龄:' , age, '性别：', gender, '身高：', height)
# 查看源码 ctrl + 左键.
"""
if xx :
    xxx
"""
"""
变量的命名规则：
使用数字字母下划线，且不用以数字开头。
变量的命名规范：
使用小写字母做变量名称，多个单词之间使用下划线隔开。
见名知意
"""
# 练习1 超市买苹果,每斤苹果3元买了4斤，向控制台输出总价格。
price = 3
weight = 4
total_account = price * weight
print(total_account)

# 练习2 买苹果只要超过10元 就返回2元。
total_account = total_account - 2


# input函数。
name2 = input('亲，请输入姓名:')
print(name2)

# 使用变量来接受控制台输入的姓名和年龄和身高。并将姓名输出到控制台。
name3 = input('请输入姓名：')
height3 = input('请输入身高：')
age3 = input('请输入身高：')
print(name3, height3, age3)
print(type(name3), type(height3), type(age3))
# input函数接受的内容都是字符串str类型

# 类型转换函数 int(), float(), 剩下的自己下去查
name4 = int(name3)
print(type(name4))

# 买香蕉增强版
# 收银员像机器输入单价、数量、显示总价。

price2 = input('请输入香蕉的单价:')
weight2 = input('请输入购买的重量：')
price2 = float(price2)
weight2 = float(weight2 )
total_account2 = price2 * weight2
print(total_account2)
"""
需求： 用户和电脑 输入石头剪刀布，判断，输出谁赢。
random模块：随机数生成模块。
人类胜利，电脑胜利，平局。
"""
