#!/usr/bin/env python
'''
@File      :7.1.3even_or_odd.py
@Copyright :luoming
@Date      :
@Desc      :
'''

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\n The number "+
          str(number)+
          " is even.")
else:
    print("\nThe number "+
          str(number)+
          " is odd.")