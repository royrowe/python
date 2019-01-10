#!/usr/bin/env python
'''
@File      :electric_car.py
@Copyright :luoming
@Date      :
@Desc      :
'''

from car import Car


class Battery():
    '''一次模拟电动汽车电瓶'''
    def __init__(self, battery_size = 70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print("This car has a " + str(self.battery_size) + "-kWh Battery.")

    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

        message = "This car can go approximately "+ str(range)
        message += " miles on a full charge."

        print(message)


class ElectricCar(Car):
    '''电动汽车的独特之处'''
    def __init__(self, make, model, year):
        '''初始化父类的属性'''
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        '''打印一条描述点评容量的消息'''
        print("This car has a " + str(self.batterry_size) + "-kWh battery.")