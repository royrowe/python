#!/usr/bin/env python
'''
@File      :test1.py
@Copyright :luoming
@Date      :
@Desc      :
'''


def make_car(manufacturer, model, **type_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in type_info.items():
        profile[key] = value
    return profile


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
