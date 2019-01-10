#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:01:23 2018

@author: luoming
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_pizzas=my_foods[:]
my_foods.append('other')
friend_pizzas.append('beef')
print("My favorite pizzas are:")
for my_food in my_foods:
    print(my_food)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)