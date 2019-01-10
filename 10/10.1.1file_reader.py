#!/usr/bin/env python
'''
@File      :10.1.1file_reader.py
@Copyright :luoming
@Date      :
@Desc      :
'''

file_path = '/home/luoming/python/python/10/text_files/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)