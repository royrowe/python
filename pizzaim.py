#!/usr/bin/env python
'''
@File      :8.6.1_pizza.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def make_pizza(size,*toppings):
    '''概述要制作的匹萨'''
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+ topping)