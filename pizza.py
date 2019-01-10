#!/usr/bin/env python
'''
@File      :pizza.py
@Copyright :luoming
@Date      :
@Desc      :
'''

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra chees'],
}
print("You ordered a "+
      pizza['crust'] +
      "-crust pizza"+
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" +topping)