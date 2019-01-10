#!/usr/bin/env python
'''
@File      :p_7.10_dreampalace.py
@Copyright :luoming
@Date      :
@Desc      :
'''

dream_places = {}
active = True
while active:
    user = input("\nWhat's your name please? ")
    place = input("\nIf you could visti one place in the world, where would you go? ")
    dream_places[user]=place
    repeat = input("\nIs there any other users? (yes/ no)")
    if repeat == 'no':
        active = False
print("\n---Users dream pleace---")
for name, place in dream_places.items():
    print(name.title()+
          "'s dream palace is "+
          place.title()+".")