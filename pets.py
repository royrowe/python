#!/usr/bin/env python
'''
@File      :pets.py
@Copyright :luoming
@Date      :
@Desc      :
'''

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)