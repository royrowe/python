#!/usr/bin/env python
'''
@File      :9.5favorite_languages.py
@Copyright :luoming
@Date      :
@Desc      :
'''

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+ language.title()+ ".")