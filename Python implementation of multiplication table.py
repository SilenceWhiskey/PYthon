"""
打印九九乘法表
算筹珠算机器靠一旁
ENIAC横空出场
前人思想精神至今燃
图灵香农冯·诺依曼
行外，列内
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d\t" % (i, j, i*j), end="")
    print()
# 这么神奇的么？
