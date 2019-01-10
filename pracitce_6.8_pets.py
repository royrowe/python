#!/usr/bin/env python
'''
@File      :pracitce_6.8_pets.py
@Copyright :luoming
@Date      :
@Desc      :
'''

kitty = {'kind': 'cat', 'owner':'lily'}
lucky = {'kind': 'dog', 'owner':'tom'}
wenling = {'kind': 'turtle', 'owner':'ming'}
pets = [kitty, lucky, wenling]
for pet in pets:
    for key, value in pet.items():
        print(key,value)
