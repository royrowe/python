#!/usr/bin/env python
'''
@File      :p_9.6_icecream.py
@Copyright :luoming
@Date      :
@Desc      :
'''

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 5

    def describe_restaurant(self):
        '''打印酒店的两项信息'''
        print("The name of restaurant is " + self.restaurant_name.title() + ".")
        print("\nThe cuisine type of the restaurant is " + self.cuisine_type+ ".")

    def open_restaurant(self):
        print("\nThe restaurant is open.")
        print("The number served is " + str(self.number_served)+ ".")

    def set_number_served(self,number):
        '''设置就餐人数'''
        self.number_served = number

    def increment_number_served(self,inc_numb):
        '''设置增加的人数'''
        self.number_served += inc_numb

class IceCreamStand(Restaurant):
    '''定义一个冰淇淋小店'''

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['banana', 'apple', 'orange']

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)

ice_cream = IceCreamStand('aicicili', 'ice cream')
ice_cream.print_flavors()
ice_cream.describe_restaurant()
