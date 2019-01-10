#!/usr/bin/env python
'''
@File      :p_8.13_user.profile.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def build_profile(first, last, **intro):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in intro.items():
        profile[key] = value
    return profile

user_profile = build_profile('ming', 'luo', location = 'nanjing', title = 'pm')

print(user_profile)