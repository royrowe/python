#!/usr/bin/env python
'''
@File      :p_8.4_LTshirt.py
@Copyright :luoming
@Date      :
@Desc      :
'''

def make_shirt(size,words='I love Python'):
    '''定义制作T恤的形参'''
    print("The size of T-shirt is "+
          size+
          ", and the words should been printed is "+
          words+
          ".")
make_shirt('L')
make_shirt('M')
make_shirt('XL','人生苦短我用python')
