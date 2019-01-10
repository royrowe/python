#!/usr/bin/env python
'''
@File      :p_7.4_pizza.py
@Copyright :luoming
@Date      :
@Desc      :
'''


active = True
while active:
    pizza_add = input("Please input your adds: ")

    if pizza_add == 'quit':
        active = False
    else:
        print("We will add "+ pizza_add +" in your pizza!")
