#!/usr/bin/env python
'''
@File      :toppings1.py.py
@Copyright :luoming
@Date      :
@Desc      :
'''

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pin\
eapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping + ".")
    else:
        print("Sorry we don't have" + requested_topping + ".")
print("\nFinished makeing your pizza!")


