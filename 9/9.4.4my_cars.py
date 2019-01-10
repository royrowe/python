#!/usr/bin/env python
'''
@File      :9.4.4my_cars.py
@Copyright :luoming
@Date      :
@Desc      :
'''

import car

my_beetle = car.Car('volswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())