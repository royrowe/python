#!/usr/bin/env python
'''
@File      :practice_6.10_favnum.py
@Copyright :luoming
@Date      :
@Desc      :
'''

cities = {
    'beijing':{
        'country': 'china',
        'population': '2151.6万',
        'fact': 'jam',
    },
    'tokyo':{
        'country': 'janpan',
        'population': '1350万',
        'fact': 'small',

    },
    'new york':{
        'country': 'america',
        'population': '851万',
        'fact': 'far',
    }
}
for name, value in cities.items():
    print(name.title()+
          " belongs to "+
          value['country'].title()+
          ". The population of it is "+
          value['population']+
          ". One fact of it is "+
          value['fact']+
          ".")