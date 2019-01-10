#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:05:18 2018

@author: luoming
"""

age = 12
if age < 4:
   price=0
elif age<18:
    price=5
else:
    price=10
print("Your admission cost is $"+str(price)+".")