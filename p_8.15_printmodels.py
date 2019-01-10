#!/usr/bin/env python
'''
@File      :p_8.15_printmodels.py
@Copyright :luoming
@Date      :
@Desc      :
'''

from printing_functions import print_models, show_completed_models
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)