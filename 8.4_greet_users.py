#!/usr/bin/env python
'''
@File      :8.4_greet_users.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def greet_users(names):
    '''向列表中的每位用户都发出简单的问候'''
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)
usernames = ['hannah', 'try', 'margot']
greet_users(usernames)