#!/usr/bin/env python
'''
@File      :practice_6.7.py
@Copyright :luoming
@Date      :
@Desc      :
'''

people = {
    'hbaowen':{
    'first_name': 'baowen',
    'last_name': 'hu',
    'age': 33,
    'city': 'beijing',
    },
    'zliang':{
    'first_name': 'liang',
    'last_name': 'zhang',
    'age': 33,
    'city': 'yantai',
    },
    'lxiao':{
    'first_name': 'xiao',
    'last_name': 'li',
    'age': 36,
    'city': 'penglai',
    },
}
for friend,info in people.items():
    fullname = info['first_name']+" "+info['last_name']
    print("\nMy friend "+
          friend.title()+
          "'s full name is "+
          fullname.title()+
          " age:"+
          str(info['age'])+
          " live in "+
          info['city']+".")
