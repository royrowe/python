#!/usr/bin/env python
'''
@File      :practic_numbers.py
@Copyright :luoming
@Date      :
@Desc      :
'''

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(number+"st")
    elif number == 2:
        print(number+"nd")
    elif number == 3:
        print(number+"rd")
    else:
        print(number+"th")