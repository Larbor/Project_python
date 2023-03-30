# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:32:57 2023

@author: labor
"""

import csv
rows = []
with open("C:/Python scripts/GitHub/Programming/Project_python/Project_python/Data/archive (1)/df_full_premierleague.csv", 'r') as premier:
    csvreader = csv.reader(premier)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)


