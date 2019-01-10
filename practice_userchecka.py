#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:53:43 2018

@author: luoming
"""


current_users = ['Amada','bill','caven','john','admin']
new_users = ['admiN','bill','jack','JOHN','frank']
 
for value in new_users:
	value = value.lower()
	if value in current_users:
		print('该用户名已被注册！')
	else:
            print('nicai')