"""
end是print函数中的默认参数
end的默认值是\n 表示换行
end是变量，可以被赋值
print自带换行功能
\t表示制表符，默认8个字符
"""
print('aaa', end='')
print('bbb')

# 打印stars
i = 1
while i <= 4:
    print('*', end='')
    i = i+1
print()
"""
break 和 continue
跳出循环 继续执行
"""
"""
字符串常用方法
find()方法：
从左往右查找字符串对应的索引.
replace()替换:
返回替换后的新字符串，原字符串不变.
strip():
默认去除字符串的首尾空格
也可以去除首尾的某字符
isdigit():
判断字符是否完全由数字组成
upper() 和 lower():
分别改变大小写
format():
格式化输出/传参stream

"""
s1 = 'hello world!'
s2 = s1[6]
print(s2)
index = s1.find('o')
print(index)

s2 = s1.replace('o', '0')
print(s2)

s1 = '               hello world!      '
s2 = s1.strip()
print(s1)
print(s2)
s1 = '@@@ hello world!@@@'
s2 = s1.strip('@')
print(s1)
print(s2)
s1 = '10'
s2 = s1.isdigit()
print(s2)
s1 = 'hello world!'
s2 = s1.upper()
print(s2)
s2 = s1.lower()
print(s2)

message = 'name == {}'.format('李肖健')
print(message)



"""
for 循环:
（字符串是一个可迭代的数据类型）
（int 类型不可迭代，因此不可以使用for 循环）
for 格式:
for 临时变量 in 可迭代内容:
    代码
流程:
    首先判断内容是否可以迭代
    取出每一个元素赋值给临时变量(从左向右)
    执行循环体，直到取完为止
枚举:
enumerate():
（元组数据类型）
返回一个元组类型并且包含索引和元组
索引默认是从零开始的
修改索引的值:
    在需要迭代的变量之后加, start = X即可改变第一个索引的值为X
"""
for s in 'hello':
    print(s, end='')
print()
print('mission success')

"""
列表:
格式:变量名 = [元素1,元素2,元素3,……]
操作:增 删 改 查
增:  
    append()在列表末尾增加元素.
    insert()在指定位置增加元素，索引从0开始.
删:
    remove()根据内容删除
    pop()根据索引删除
改:
    根据索引修改内容 变量名[index] = new+value    
查:
    根据索引查找
    根据内容返回索引index()
"""
name_list = ['NAME1', 'NAME2', 'NAME3', 'NAME4']
print(type(name_list))
# 增
name_list.append('NAME5')
print(name_list)
name_list.insert(0, 'NAME0')
print(name_list)
name_list.remove('NAME2')
print(name_list)
name_list.pop(0)
print(name_list)
name_list[0]='NAME_NULL'
print(name_list)
name = name_list[3]
print(name)
# 使用len()可以查看列表的长度
length = len(name_list)
print(length)
name_list.index('NAME3')
"""
字典
格式:
    变量名 = {name:'李肖健',age:19}
操作:
    增 删 改 查
"""
user_info = {'name': '李肖健', 'age': 20}
print(type(user_info))
# 增
user_info['weight'] = 150
print(user_info)
# 删
user_info.pop('name')
print(user_info)
# 改
user_info['age'] = 21
print(user_info)
# 查
user_info['name'] = '李肖健'
name = user_info['name']
print(name)  # 根据键查找值
age = user_info.get('age')
print(age)
