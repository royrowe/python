#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:39:06 2018

@author: luoming
"""

def make_car(manu, type, **info):
    carinfo = {}
    carinfo['manufacturer'] = manu
    carinfo['type_car'] = type
    for key, value in info.items():
        info[key] = value
    return carinfo
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)