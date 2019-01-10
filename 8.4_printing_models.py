#!/usr/bin/env python
'''
@File      :8.4_printing_models.py
@Copyright :luoming
@Date      :
@Desc      :
'''

unprinted_designs = ['iphone case','roboot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: "+ current_design)
    completed_models.append(current_design)

print("\nThe follwing models have been printed: ")
for completed_model in completed_models:
    print(completed_model)