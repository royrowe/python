#!/usr/bin/env python
'''
@File      :9.1.1.py
@Copyright :luoming
@Date      :
@Desc      :
'''

class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self, name, age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + "rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy',3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog's age is " + str(your_dog.age) + " years old.")