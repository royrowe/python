#!/usr/bin/env python
'''
@File      :p_7.3_10.py
@Copyright :luoming
@Date      :
@Desc      :
'''

number = input("Please enter a number: ")
number = int(number)
if number%10 == 0:
    print("这个数字是10的整数倍")
else:
    print("这不是10的整数倍")