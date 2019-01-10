#!/usr/bin/env python
'''
@File      :p_9.3_user.py
@Copyright :luoming
@Date      :
@Desc      :
'''

class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("User's name is "+self.first_name.title()+" "+
              self.last_name.title()+
              "and age is " + str(self.age) + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() +" "+
              self.last_name.title() + ".")


first_user = User('li','yuan',23)
second_user = User('ming','yao',37)
third_user = User('brad','pitt',45)
first_user.describe_user()
first_user.greet_user()
second_user.describe_user()
second_user.greet_user()
third_user.describe_user()
third_user.greet_user()