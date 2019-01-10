#!/usr/bin/env python
'''
@File      :p_7.6_3exits.py
@Copyright :luoming
@Date      :
@Desc      :
'''

prompt = "0~3 for free, 3~12 for 10$, 12~ for 15$"
prompt += "\n How old are you? "
age = " "
while age!= 'quit':
    age = input(prompt)
    if int(age) <= 3:
        print("Oh! you can watch movie for free!")
    elif int(age) <= 12:
        print("You need pay 10$")
    else:
        print("You need pay 15$")