#!/usr/bin/env python
'''
@File      :10.3division.py
@Copyright :luoming
@Date      :
@Desc      :
'''

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")