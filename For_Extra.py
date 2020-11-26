# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:15:18 2020

@author: Administrator
"""

list2 = [({'name': 'ThayCuongdeptrai', 'age':40}, {'name': 'Vu', 'age':18}), 
         ({'name': 'Linhcute', 'age':18}, {'name': 'Ronaldo', 'age':35}), 
         ({'name': 'Tokuda', 'age':86}, {'name': 'Maria', 'age':34}), 
         ({'name': 'Co', 'age':18}, {'name': 'Loan', 'age':21})]
for index, x in enumerate(list2):
    print(x)
    for index1, y in enumerate(list2[index]):
        print(y)
        print(list2[index][index1]["name"])
        print(list2[index][index1]["age"])