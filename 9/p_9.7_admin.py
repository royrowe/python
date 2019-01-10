#!/usr/bin/env python
'''
@File      :p_9.7_admin.py
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

class Privileges:
    '''定义一个privis的类'''
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    '''定义一个admin的类'''

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()




admin = Admin('ming', 'yao', 32)
admin.show_privileges()
