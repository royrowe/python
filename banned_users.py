#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:51:45 2018

@author: luoming
"""

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title()+", you can't post a response if you wish.")

car = 'subaru'
print ("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\n Is car ==  'audi'? I predict False.")
print(car == 'audi')