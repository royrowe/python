#!/usr/bin/env python
'''
@File      :p_8.11_copy.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magician = 'the Great ' + magician.title()
        great_magicians.append(great_magician)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['xiaoming', 'yao', 'lee', 'zhang']
great_magicians = []

make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)