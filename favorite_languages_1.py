#!/usr/bin/env python
'''
@File      :favorite_languages_1.py
@Copyright :luoming
@Date      :
@Desc      :
'''

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward':['ruby','go'],
    'phil': ['python','haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages)<2:
        print("/n"+
          name.title()+
          "'s favorite language is")
    else:
        print("/n"+
          name.title()+
          "'s favorite language are")
    for language in languages:
        print(language.title())