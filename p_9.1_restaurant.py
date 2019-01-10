#!/usr/bin/env python
'''
@File      :p_9.1_restaurant.py
@Copyright :luoming
@Date      :
@Desc      :
'''

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''打印酒店的两项信息'''
        print("The name of restaurant is " + self.restaurant_name.title() + ".")
        print("\nThe cuisine type of the restaurant is " + self.cuisine_type+ ".")

    def open_restaurant(self):
        print("\nThe restaurant is open.")

info_res = Restaurant('Shangrila', 'hotel')
info_res.describe_restaurant()
info_res.open_restaurant()