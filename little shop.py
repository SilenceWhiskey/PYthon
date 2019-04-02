"""
展示账户
展示商品 序号，名称，价格
输入账户
判断输入是否合法
输入序号
判断输入的合法性
判断输入的范围
输入数量
判断输入的合法性
判断输入的范围

输出购物车
输出余额

列表套字典
字典存信息
列表存商品
"""
product_list = \
    [
        {'name':'香蕉', 'price': 3},
        {'name':'榴莲', 'price': 10},
        {'name':'苹果', 'price': 5},
        {'name':'菠萝', 'price': 5}
    ]
# 创建一个字典购物车保存已购商品
# {'香蕉':2,'苹果':4}
shopping_car = {}
# 展示资本
money = input('请输入您的目标消费金额:')
if money.isdigit():
    print('请确认您目标消费金额:', money, '元')
    money = int(money)
    for index, product in enumerate(product_list, 1):
        print('序号:{},商品名称:{},单价:{}'.format(index, product.get('name'), product.get('price')), '元/千克')
    while True:
        index_str = input('请输入需要购买的商品序号:')
        if index_str.isdigit():
            index = int(index_str)
            if 0 < index <= len(product_list):
                weight_str = input('请输入要购买商品的重量:')
                if weight_str.isdigit():
                    weight = int(weight_str)
                    account = weight * product_list[index-1].get('price')
                    print('方才确定要购买的商品价格为:', account)
                    if account <= money:
                        value = shopping_car.get(product_list[index-1].get('name'))
                        if value:
                            value += weight
                            shopping_car[product_list[index-1].get('name')] = value
                        else:
                            shopping_car[product_list[index-1].get('name')] = weight
                        money = money - account
                        print('您购物车中的商品有{},您的余额为:{}'.format(shopping_car, money))
                        if money < 3:
                            break
                    else:
                        print('抱歉，支付出现问题,请检查您的购物车和余额:{},{}'.format(shopping_car, money))
                else:
                    print('购买方式出错！')
            else:
                print('艾玛，您这是买的啥啊？')
        else:
            print('艾玛，您这是买的啥啊？')
else:
    print('艾玛，您这是冥币啊？')
