# Author Atticus_lv
# -*- coding =utf-8 -*-
# @Time : 2020/9/13 0:07
# 类

# class Student():
#     def __init__(self,sex:str,age:int,gpa:float,name:str):
#         self.sex = sex
#         self.age = age
#         self.gpa = gpa
#         self.name = name
#
#     def introduced_self(self):
#         print(f"我的名字是{self.name},我的性别是{self.sex},我今年{self.age}岁")
#
#     def introduced_gpa(self):
#         if self.gpa >= 4:
#             print("我的gpa比较差")
#         elif self.gpa >= 3 and self.gpa < 4:
#             print("我的gpa海星")
#         elif self.gpa < 3 and self.gpa >= 2:
#             print("我们聊下一个话题")
#         elif self.gpa < 2:
#             self.action_angry()
#
#     def action_angry(self):
#         print("一个滑铲")
#
# xiaoming = Student("male",24,1,"小明")


class user_info():
    def __init__(self):
        self.lines = None

    def open_info(self):
        f = open("账户密码.txt", "r", encoding="utf-8")
        self.lines = f.readlines()
        f.close()

    def creat_info(self):
        print("没有找到账户密码文件，已经新建")
        f = open("账户密码.txt", "w", encoding="utf-8")
        f.write("用户名\n")
        f.write("密码\n")
        f.write("参数\n")
        f.close()

    def get_info(self):
        try:
            self.open_info()
        except FileNotFoundError as e:
            self.creat_info()
            self.open_info()
        return self.lines


# # 使用模板 新建实例对象
# user1 = user_info()
# # 调用实例对象的实例方法，使用info 变量接收 方法的返回值
# info = user1.get_info()
# # 把变量打印出来
# print(info)

class Animal():
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def run(self):
        print(f"{self.name} is running")

    def jump(self):
        print(f"{self.name} is jumpping")


dog = Animal(name="life", type="dog", age=4)
dog.run()
dog.jump()

# 古诗读写器
# 可以不断询问使用者来输入一行古诗
# 当使用者询问某首古诗的名字时候，可以把整首古诗打印出来