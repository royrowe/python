#!/usr/bin/env python
'''
@File      :p_9.13_ordereddict.py
@Copyright :luoming
@Date      :
@Desc      :
'''

from collections import OrderedDict

charc = OrderedDict()

charc["a"] = "zifu"
charc["b"] = "zheng shu"
charc["c"] = "fu dian"
charc["d"] = "bu er"
charc["e"] = "kai fa"

for key, value in charc.items():
    print(key, value)