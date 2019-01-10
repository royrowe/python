#!/usr/bin/env python
'''
@File      :10.1.4.py
@Copyright :luoming
@Date      :
@Desc      :
'''

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())