#!/usr/bin/env python
'''
@File      :8.5_pizza.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def make_pizza(*toppings):
    '''概述要制作的匹萨'''
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("-"+ topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepers', 'extra cheese')
