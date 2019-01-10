#!/usr/bin/env python
'''
@File      :p_8.8_useralbum.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def make_album(singer,album,songs=''):
    get_album={'singer':singer,'album':album,'songs':songs}
    return get_album
while True:
    print("Type 'q' to quit at any time")
    get_singer = input("\nWhat's the singer's name? ")
    if get_singer == 'q':
        break
    get_album = input("\nWhat's the album called? ")
    if get_album == 'q':
        break
    get_songs = input("\nHow many songs in it?")
    if get_songs == 'q':
        break
    get_make_album = make_album(get_singer,get_album,get_songs)
    print(get_make_album)