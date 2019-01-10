#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 17:59:18 2018

@author: luoming
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+ too_expensive + " is too expensive for me.")
motorcycles.append('damotuo')
print(motorcycles)
for moto in motorcycles:
    print(moto)