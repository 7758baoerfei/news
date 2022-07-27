# class Student:
#     def study_python(self):
#         print('张三喜欢学习python')
#         # print(zs.name, zs.age)
#         print(self.name, self.age)
#
# zs = Student()
# zs.name = '张三'
# zs.age = '18'
# zs.study_python()
# class student:
#     def print_info(self):
#         ls.name ='李四'
#         ls.age = '18'
#         print(self.name, self.age)
#
#
# ls = student()
# ls.print_info()
# class Sbaa:
#     def __init__(self):
#         print('---1---')
# zs =Sbaa()
# print('---2---')
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#      # def print_info(self):
#      #    print(self.name, self.age)
#
#
# ls = Student('张三', 10)
# ls.print_info()
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name, self.age)
#
#     def print_info(self):
#         print(self.name, self.age)
#
# ls = Student('李四',18)
# ls.print_info()
# ls = Student('王五', 20)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'姓名为{self.name}年龄为{self.age}'
# ls = Student('李四', 18)
# print(ls)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#         print(self.name, self.__age)
#
#     def ou_age(self):
#         return  self.__age
#
#     def au_age(self, age):
#         self.age = age
#         print(self.age)
#
#
#
# rose = Person('小红', 18)
# # print(rose.name)
# # print(rose.ou_age())
# ab = rose.au_age(45)
# print(ab)
# class Mankind:
#     def __init__(self):
#         self.f''
# class Car:
#     def __init__(self, color, speed, type):
#       self.color = color
#       self.speed = speed
#       self.type = type
#     def move(self):
#         print('汽车开始跑了')
# BMW_X9 = Car('白色', 80, 'x7')
# print(BMW_X9.color, BMW_X9.speed, BMW_X9.type)
# BMW_X9.move()
# AUDI_A9 = Car('黑色', 100, 's6')
# print(AUDI_A9.color, AUDI_A9.speed, AUDI_A9.type)
# AUDI_A9.move()

# class Mnimal:
#     def __init__(self, name, age, food):
#      self.name = name
#      self.age = age
#      self.food = food
#
#
#     def run(self):
#       print(f"{self.name}在奔跑")
#     def get_age(self):
#       print(f'{self.name}今年{self.age }了')
#     def eat(self):
#      print(f'{self.name}正在吃{self.food}')
# Horse = Mnimal('汗血马', 6,'青草')
# Horse.run()
# Cat = Mnimal('加菲猫',2,'猫粮')
# Cat.get_age()
# Dog = Mnimal('金毛', 5, '狗粮')
# Dog.eat()
#
# class Person:
#     """
#     定义一个人“类”
#     """
#
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return f'姓名{self.name}, 体重{self.weight}kg'
#         return "我的名字叫%s 体重是%.2fkg" % (self.name, self.weight)
#
# xiaoming = Person("小明", 56)
#
# xiaomei = Person("小美", 44)
# print(xiaoming)
# print(xiaomei)


