#!/usr/bin/env python
'''
@File      :10.1.5pi_string.py
@Copyright :luoming
@Date      :
@Desc      :
'''

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))