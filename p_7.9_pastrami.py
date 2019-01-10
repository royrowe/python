#!/usr/bin/env python
'''
@File      :p_7.9_pastrami.py
@Copyright :luoming
@Date      :
@Desc      :
'''

sandwich_orders = ['egg', 'pastrami','tuna','pastrami', 'fish','pastrami']
print("Pastrami have been sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
