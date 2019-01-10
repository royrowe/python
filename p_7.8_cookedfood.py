#!/usr/bin/env python
'''
@File      :p_7.8_cookedfood.py
@Copyright :luoming
@Date      :
@Desc      :
'''

sandwich_orders = ['egg sandwich', 'tuna sandwich', 'fish sandwich']
finished_sandwiches =[]
while sandwich_orders:
    cooked_sandwiche = sandwich_orders.pop()
    print("I made your " + cooked_sandwiche + ".")
    finished_sandwiches.append(cooked_sandwiche)
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)