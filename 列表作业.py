#-*- coding =utf-8 -*-

'''
1.现有商品列表如下：
products = [["RTX3080",5499],["MacPro",14800],["Iphone 12",None],["瑞幸咖啡",0],["Nike",699]]
需打印出以下格式：

------ 商品列表 ------

0 RTX3080 5499
1 MacPro 14800
2 Iphone 12 缺货
3 瑞幸咖啡 免费
4 Nike 699


2.根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表
（注意缺货产品应在用户选购后提示缺货,写不出来也没关系）

3.tips：可以使用while循环来判断用户是否输入 q

'''

products = [["RTX3080",5499],["MacPro",14800],["Iphone 12",None],["瑞幸咖啡",0],["Nike",699]]

def shopping_sys_base():
    # 打印商品列表
    print("------ 商品列表 ------")
    for i,v in enumerate(products):
        print(f"{i} {v[0]} {v[1]}")
    # for i in range(0,len(products)):
    #     print(f"{i} {products[i][0]} {products[i][1]}")

    #初始化 购买列表 和 购买总额
    list = []
    price_total = 0

    # 使用while循环来持续获取输入
    while True:
        k = input("请输入购买商品号")
        if k == "2":
            print("该商品缺货中\n")
            continue
        elif k == "q":
            break
        # 将序列号追加到列表中
        list.append(k)
        print(f"{products[int(k)][0]} 已被添加倒清单\n")

    # 输出购物清单
    print("\n-----购物清单-----")
    for i in list:
        if i != None and i != "q":
            index = int(i)
            print(f"产品名称：{products[index][0]} 价格：{products[index][1]}")
            price_total += int(products[index][1]) #获取总额

    print(f"\n购买的商品总价为 {price_total}")

import test111
test111.ccc()

