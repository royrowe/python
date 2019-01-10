#!/usr/bin/env python
'''
@File      :p_8.7_makealbum.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def make_album(singer,album,quantity=''):
    get_make_album={'singer':singer,'album':album,'quantity':quantity}
    return get_make_album
album=make_album('leon','beijing station',5)
print(album)