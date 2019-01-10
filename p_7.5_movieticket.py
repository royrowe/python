#!/usr/bin/env python
'''
@File      :p_7.5_movieticket.py
@Copyright :luoming
@Date      :
@Desc      :
'''

prompt = "0~3 for free, 3~12 for 10$, 12~ for 15$"
prompt += "\n How old are you? "

while True:
    age = input(prompt)
    age = int(age)
    if age <= 3:
        print("Oh! you can watch movie for free!")
    elif age <= 12:
        print("You need pay 10$")
    else:
        print("You need pay 15$")
