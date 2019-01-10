#!/usr/bin/env python
'''
@File      :p_8.12_sandwich.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def sandwich(*toppings):
    print("Your sandwich is made of: ")
    for topping in toppings:
        print(topping)
sandwich('egg','chees','beef')