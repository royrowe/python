#!/usr/bin/env python
'''
@File      :p_10.2_replace.py
@Copyright :luoming
@Date      :
@Desc      :
'''

filename = 'text_files/pythoncan.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())