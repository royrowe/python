#!/usr/bin/env python
'''
@File      :practice_river.py
@Copyright :luoming
@Date      :
@Desc      :
'''

rivers_countries = {
    'nile': 'egypt',
    'euphrates':'iraq',
    'seine': 'france',
}
for river, country in rivers_countries.items():
    print("The "+
          river.title()+
          " runs through "+
          country.title()+
          ".")
for ri in rivers_countries.keys():
    print(ri)
for coun in rivers_countries.values():
    print(coun)