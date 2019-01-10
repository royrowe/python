#!/usr/bin/env python
'''
@File      :p_8.5_city.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def describe_city(city,county='Iceland'):
    print(city.title()+" is in "+county.title()+".")
describe_city('reykjavik')
describe_city('akureyri')
describe_city('risbon','portuguese')