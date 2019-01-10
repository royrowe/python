#!/usr/bin/env python
'''
@File      :p_8.14_cars.py
@Copyright :luoming
@Date      :
@Desc      :
'''


def make_car(manu, model, **type_info):
    carinfo = {}
    carinfo['manufacturer'] = manu
    carinfo['model_car'] = model
    for key, value in type_info.items():
        carinfo[key] = value
    return carinfo


car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
