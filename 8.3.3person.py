#!/usr/bin/env python
'''
@File      :8.3.3person.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def build_person(first_name,last_name,age=''):
    '''返回一个字典，包含一个人的信息'''
    person = {'first': first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)