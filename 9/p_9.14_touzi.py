#!/usr/bin/env python
'''
@File      :p_9.14_touzi.py
@Copyright :luoming
@Date      :
@Desc      :
'''

from random import randint

class Die():
    def __init__(self, sides, times):
        self.sides = 6
        self.times = times

    def roll_die(self):
        x = 0
        while x < self.times:
                self.roll_die = randint(1, self.sides)
                print(self.roll_die)
                x += 1

die = Die(6, 10)
die.roll_die()