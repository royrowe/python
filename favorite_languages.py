#!/usr/bin/env python
'''
@File      :favorite_languages.py
@Copyright :luoming
@Date      :
@Desc      :
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
investigation = ['jen', 'john', 'edward', 'lily']
for name in favorite_languages.keys():
    if name in investigation:
        print(name.title()+
              " Thank you for poll.")
    else:
        print(name.title()+
              " welcome to attend poll.")
