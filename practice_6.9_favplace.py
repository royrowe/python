#!/usr/bin/env python
'''
@File      :practice_6.9_favplace.py
@Copyright :luoming
@Date      :
@Desc      :
'''

favorite_places = {
    'hu':['beijing', 'shanghai', 'nanjing'],
    'zhang':['haerbin', 'paris', 'tokyo'],
    'liu':['london', 'kyoto', 'sydney'],
}
for key, values in favorite_places.items():
   print(key.title()+
          "'s favorite places are ")
   for value in values:
       print(value.title())