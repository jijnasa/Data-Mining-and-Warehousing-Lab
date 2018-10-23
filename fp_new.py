# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:09:50 2018

@author: Student
"""

import pyfpgrowth
transactions = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3]]
patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)
rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
print(patterns)
print(rules)