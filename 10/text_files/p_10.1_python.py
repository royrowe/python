#!/usr/bin/env python
'''
@File      :p_10.1_python.py
@Copyright :luoming
@Date      :
@Desc      :
'''

filename = 'pythoncan.txt'

with open(filename) as file_object:
    content = file_object.read()
    print(content)()



    for line in file_object:
        print(line)

    lines = file_object.readlines()
    for line1 in  lines:
        print(line1)