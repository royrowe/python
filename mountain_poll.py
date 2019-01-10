#!/usr/bin/env python
'''
@File      :mountain_poll.py
@Copyright :luoming
@Date      :
@Desc      :
'''

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input ("\nWhich mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Wloul you like to let a nother person respond?(yes/ no)")
    if repeat == "no":
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb "+ response.title() + ".")