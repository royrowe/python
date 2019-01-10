#!/usr/bin/env python
'''
@File      :practice_usercheck.py
@Copyright :luoming
@Date      :
@Desc      :
'''

current_users = ['john','lily','TOM','Jack','roy']
new_users = ['John','jerry','tom','june','july']
for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print("The username "+ new_user.title() +"have been used.")
        else:
            print("The username is OK")

