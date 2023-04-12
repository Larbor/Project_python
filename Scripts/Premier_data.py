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

#%%

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 



# Write a HTML or a PDF with a link to the project. It should also decribe the project in not to many words. 

#Histogram

results = []

for row in rows:
    result = row[6]
    result = result.split('-')
    home = int(result[0])
    away = int(result[1])
    if home>away:
        results.append("h")
    elif home<away:
        results.append("a")
    else:
        results.append("d")
print(results)

plt.hist(results)
plt.show() 

#%%

#Bar chart

#%%

# Pie chart

#%%

# Iinear regression

from sklearn import linear_model

#Lists of home team shots on target, sorted by home possession in precentails of 10.
home_poss0_10 = []
home_poss10_20 = []
home_poss20_30 = []
home_poss30_40 = []
home_poss40_50 = []
home_poss50_60 = []
home_poss60_70 = []
home_poss70_80 = []
home_poss80_90 = []
home_poss90_100 = []

#appending shots on target for lists. 
for row in rows:
    home_possesion = float(row[13])
    if home_possesion < 10:
        home_poss0_10.append(row(16))
    elif home_possesion > 10 and home_possesion < 20:
        home_poss10_20.append(row[16])
    elif home_possesion > 20 and home_possesion < 30:
        home_poss20_30.append(row[16])
    elif home_possesion > 30 and home_possesion < 40:
        home_poss30_40.append(row[16])
    elif home_possesion > 40 and home_possesion < 50:
        home_poss40_50.append(row[16])
    elif home_possesion > 50 and home_possesion < 60:
        home_poss50_60.append(row[16])
    elif home_possesion > 60 and home_possesion < 70:
        home_poss60_70.append(row[16])
    elif home_possesion > 70 and home_possesion < 80:
        home_poss70_80.append(row[16])
    elif home_possesion > 80 and home_possesion < 90:
        home_poss80_90.append(row[16])
    elif home_possesion > 90 and home_possesion < 100:
        home_poss90_100.append(row[16])


average_shot_home_poss0_10 = np.average(home_poss0_10)
average_shot_home_poss10_20 = np.average(home_poss10_20)        
print(average_shot_home_poss10_20)        
        
        
#%%       
away_poss = []

for row in rows:
    away_possesion = float(row[25])
    away_poss.append(away_possesion)
#print(away_poss)    

hshot_ontarget = []

for row in rows:
    hsot = float(row[16])
    hshot_ontarget.append(hsot)
#print(hshot_ontarget)

ashot_ontarget = []

for row in rows:
    asot = float(row[28])
    ashot_ontarget.append(asot)
#print(ashot_ontarget)

#%%


lin_mod = linear_model.LinearRegression()

lin_mod.fit(X = pd.DataFrame(home_poss), 
                     y = hshot_ontarget)


print(lin_mod.intercept_)

print(lin_mod.coef_)

plt.scatter(home_poss, hshot_ontarget)






    