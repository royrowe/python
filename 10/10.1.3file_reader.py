#!/usr/bin/env python
'''
@File      :10.1.3file_reader.py
@Copyright :luoming
@Date      :
@Desc      :
'''

file_path = '/home/luoming/python/python/10/text_files/pi_digits.txt'

with open(file_path) as file_object:
    for line in file_object:
        print(line)