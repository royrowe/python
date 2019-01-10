#!/usr/bin/env python
'''
@File      :p_8.6_city.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def city_country(city, country):
    place = '"'+city+','+country+'"'
    return place.title()
get_place = city_country('santiago','chile')
print(get_place)

