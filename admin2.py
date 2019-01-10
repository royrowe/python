#!/usr/bin/env python
'''
@File      :admin2.py
@Copyright :luoming
@Date      :
@Desc      :
'''

class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("User's name is "+self.first_name.title()+" "+
              self.last_name.title()+
              " and age is " + str(self.age) + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() +" "+
              self.last_name.title() + ".")

    def increment_login_attempts(self,):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print(str(self.login_attempts))