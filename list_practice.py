#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:30:28 2018

@author: luoming
"""

#ptractice
dinner_names=['xiaoming', 'yao', 'zhang', 'li']
print(len(dinner_names))
dinner_names.insert(0,'zheng')
dinner_names.insert(2,'sun')
dinner_names.append('song')
print(dinner_names)
print(len(dinner_names))
print("I can invite two guests only")
name_1 = dinner_names.pop()
print(name_1.title()+" sorry to inform you")
name_1 = dinner_names.pop()
print(name_1.title()+" sorry to inform you")
name_1 = dinner_names.pop()
print(name_1.title()+" sorry to inform you")
name_1 = dinner_names.pop()
print(name_1.title()+" sorry to inform you")
name_1 = dinner_names.pop()
print(name_1.title()+" sorry to inform you")
print(dinner_names)
del dinner_names[1]
print(dinner_names)
del dinner_names[0]
print(dinner_names)