#!/usr/bin/env python
'''
@File      :p_10.3_guest.py
@Copyright :luoming
@Date      :
@Desc      :
'''

file_name = 'text_files/guests.txt'

while True:
    guest = input("Please tell me your name: ")
    if guest == "q":
        quit()
    else:
        print("welcome "+ guest.title()+".")
        reason = input("\nWhy you like programming?")
        with open(file_name, 'a') as file_object:
            file_object.write("\n"+guest.title()+"\n"+reason)