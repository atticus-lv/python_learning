#-*- coding =utf-8 -*-

# 函数

# def four(start_number,end_number):
#     r1 = start_number+end_number
#     r2 = start_number-end_number
#     r3 = start_number*end_number
#     r4 = start_number/end_number
#     return [r1,r2,r3,r4]
#
# start_number = four(2,10)



def chengfabiao(start_number:int, end_number:int):
    while start_number <= end_number:
        for i in range(1, start_number + 1):
            print(f"{start_number}x{i}={start_number * i}", end=" ")
        start_number += 1
        print(end="\n")


for i in range(1,6):
    print(f"这是{i}的乘法表")
    chengfabiao(1,i)
    print("\n")


# 定义


# 接收和返回


# 局部变量，全局变量


# 程序入口