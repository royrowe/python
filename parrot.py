#!/usr/bin/env python
'''
@File      :parrot.py
@Copyright :luoming
@Date      :
@Desc      :
'''

prompt = "\nTell me something, adn I will repe at it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active =False
    else:
        print(message)