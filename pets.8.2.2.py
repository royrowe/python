#!/usr/bin/env python
'''
@File      :pets.8.2.2.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print("\nI have a "+ animal_type +".")
    print("My "+animal_type +"'s name is "+pet_name +".")
describe_pet(animal_type='hamster', pet_name='harry')