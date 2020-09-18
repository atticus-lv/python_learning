#-*- coding =utf-8 -*-

# import random

# 列表

# a = []
# for i in range(0,10):
#     a.append(random.randint(0,10))

# b = [random.randint(0,10) for i in range(0,10)]


#
# list1 = [1, 10, 10, 8, 2, 5, 4, 4, 0, 5]
#
# list2 = ["字符串",1,list1]

# print(list2)

# 增加
a = 5
b= "ss"
em = ["这是列表"]
em.append(a)
em.append(b)
# print(em)


# 删除
# em.pop()
# print(em)

# z = "这是列表"
#
# if z in em:
#     em.remove(z)
# print(em)
# if z in em:
#     em.remove(z)
# else:
#     print(f"列表中没有 {z}")
# print(em)


# 查询（索引，长度）


list1 = [1, 10, 10, 8, 2, 5, 4, 4, 0, 5]
list2 = ["字符串",1,list1]

# print(list1[0])
# print(list2[2][1])


# 更改

list2 = ["字符串",1,list1]

list2[0] = "新的字符串"
# print(list2)


# 遍历

list1 = [1, 10, 10, 8, 2, 5, 4, 4, 0, 5]

# for i in list1:
#     print(i,end=" ")


new_list = []
for i in list1:
    item = str(i*2) * 3
    new_list.append(item)

# print(new_list)

#字符串修改
str = "新的字符串"

s = str[:-3]
# print(s)

list1 = [1, 10, 10, 8, 2, 5, 4, 4, 0, 5]
s = list1[:-3]
# print(s)

# for i in list1:
#     if i != 5:
#         list1.pop(0)
#         print(list1)
#     else:
#         break


# 字典，集合，元组简单介绍

#集合
list1 = [1, 10, 10, 8, 2, 5, 4, 4, 0, 5]


newlist = list(set(list1))
# print(newlist)


dict1 = {"名字":"夫拉弗","年龄":24,"职业":"学生"}

name = dict1["名字"]
# print(name)

# for key in dict1.keys():
#     print(key)

# for value in dict1.values():
#     print(value)

for key,values in dict1.items():
    print(key,values)

keys = ["名字","性别","年龄"]
values = ["小明",1,24]

dictionary = dict(zip(keys,values))

print(dictionary)