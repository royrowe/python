#!/usr/bin/env python
'''
@File      :10.3.3_division.py
@Copyright :luoming
@Date      :
@Desc      :
'''

print("Give me two numbers, adn I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFisrt number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)