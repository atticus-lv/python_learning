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

#补充 通过len函数可以把列表的长度输出为整数
products = [["RTX3080",5499],["MacPro",14800],["Iphone 12",None],["瑞幸咖啡",0],["Nike",699]]
print(f"产品列表里面有 {len(products)} 个产品")
