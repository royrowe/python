#!/usr/bin/env python
'''
@File      :8.3.1_formatted_name.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)