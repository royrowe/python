#!/usr/bin/env python
'''
@File      :practice_fav_numbers.py
@Copyright :luoming
@Date      :
@Desc      :
'''

"""
6-4 词汇表 2  ：既然你知道了如何遍历字典，现在请整理你为完成练习 6-3 而编写的代码，将其中的一系列 
print 语句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后，
再在词汇表中添加 5 个 Python 术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
"""

vocabulary = {'php': '世界上最好的语言', 'python': '最简洁的语言',
              'java': '世界上用的最广的语言', 'sql': '独一无二的数据库语言'}

for language, info in vocabulary.items():
    print(language + ":\n" + info)
