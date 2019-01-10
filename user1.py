#!/usr/bin/env python
'''
@File      :user1.py
@Copyright :luoming
@Date
@Desc      :
'''

from admin2 import User

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
