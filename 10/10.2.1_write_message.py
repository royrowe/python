#!/usr/bin/env python
'''
@File      :10.2.1_write_message.py
@Copyright :luoming
@Date      :
@Desc      :
'''

filename = 'text_files/programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")