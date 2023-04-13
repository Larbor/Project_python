# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:32:57 2023

@author: labor
"""

# A program with simple analysis of premier league(2010-2021) stats for data visualization. 
import csv
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import os

os.chdir('C:\Python scripts\GitHub\Programming\Project_python\Project_python')


#%%
# rows = []
# with open("C:/Python scripts/GitHub/Programming/Project_python/Project_python/Data/archive (1)/df_full_premierleague.csv", 'r') as premier:
#     csvreader = csv.reader(premier)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)
#%%

matches = pd.read_csv("C:/Python scripts/GitHub/Programming/Project_python/Project_python/Data/archive (1)/df_full_premierleague.csv")
matches.head()

#%%

# Making different dataframes for Man United and Liverpool games. 

united_matches_home = matches.loc[matches['home_team'] == 'Manchester United']

liverpool_matches_home = matches.loc[matches['home_team'] == 'Liverpool']

united_matches_away = matches.loc[matches['away_team'] == 'Manchester United']

liverpool_matches_away = matches.loc[matches['away_team'] == 'Liverpool']

united_matches = united_matches_home.append(united_matches_away, ignore_index=True)

liverpool_matches = liverpool_matches_home.append(liverpool_matches_away, ignore_index=True)

machester_vs_liverpool = united_matches_home.loc[matches['away_team'] == 'Liverpool']

liverpool_vs_manchester = liverpool_matches_home.loc[matches['away_team'] == 'Manchester United']

clashes = machester_vs_liverpool.append(liverpool_vs_manchester, ignore_index=True)

#%%
#print(machester_vs_liverpool['home_possession'].mean())

#print(liverpool_vs_manchester['home_possession'].mean())

#%%

# Making a barplot to see how ball possession relates to full time score (full time goal difference).
sns.set_style("whitegrid")
sns.set_context("paper")
# I prefered whitegrid and paper for this one. 

fig = sns.barplot(x='sg_match_ft', y='home_possession', data=clashes, palette='YlGnBu', 
            color = 'red', hue='home_team', saturation=0.75, errcolor=".5")
# Setting title and lable.
plt.xlabel("Goal Difference")
plt.ylabel("Ball Possession (%)")
plt.title("Ball ossession by goal difference in Man United vs Liverpool games")



#%%

# Making a lineplot showing how red card per game has developed over the premier 
# league seasons in this data set. Both for all teams and comparing all liverpool to united games.
# I think the chart was more clear with this palette and with marker for the individual seasons.

sns.set_style("darkgrid")
sns.lineplot(data=matches, x="season", y="red_cards_avg_H", palette='YlGnBu', marker= 'o', markersize=6)
# Setting title and lable.
plt.xlabel("Premier League Seasons")
plt.ylabel("Average red cards per game")
plt.title("Developement of red cards per game over seasons")
# Adding Liverpool and United stats.
sns.lineplot(data=liverpool_matches, x="season", y="red_cards_avg_H", palette='YlGnBu', marker= '^', markersize=6)
sns.lineplot(data=united_matches, x="season", y="red_cards_avg_H", palette='YlGnBu', marker= 's', markersize=6)
# Setting and placing legend.
plt.legend(["All Teams", "Manchester united", "Liverpool"], loc ="upper right")

#%%

# A swarmplot showing how shots on target relates to ful time goal difference in all united vs liverpool games (2010-2021). 

sns.set_theme(style="darkgrid", palette="muted")

plot = sns.swarmplot(data=clashes, x="sg_match_ft", y="home_shots_on_target", hue = 'home_team')
plot = sns.swarmplot(data=clashes, x="sg_match_ft", y="away_shots_on_target", hue = 'away_team')

# Setting title and lable.
plt.title("Shots on target to game goal difference")
plot.set(ylabel="Goal difference", xlabel='Shots on target')

# Changing placement of legend. 
plt.legend(["Manchester United", "Liverpool"], bbox_to_anchor=(1, 1.1))


#%%


# results = []

# for row in rows:
#     result = row[6]
#     result = result.split('-')
#     home = int(result[0])
#     away = int(result[1])
#     if home>away:
#         results.append("h")
#     elif home<away:
#         results.append("a")
#     else:
#         results.append("d")
# print(results)

# plt.hist(results, color='red')
# plt.title('Amounts of draws, home, and away wins.')
# plt.ylabel('Number of restults')
# plt.xlabel('Home wins, Draws and Away wins')
# plt.show() 


# Iinear regression

# from sklearn import linear_model

#Lists of home team shots on target, sorted by home possession in precentails of 10.
# home_poss0_10 = []
# home_poss10_20 = []
# home_poss20_30 = []
# home_poss30_40 = []
# home_poss40_50 = []
# home_poss50_60 = []
# home_poss60_70 = []
# home_poss70_80 = []
# home_poss80_90 = []
# home_poss90_100 = []

#appending shots on target for lists. 
# for row in rows:
#     home_possesion = float(row[13])
#     if home_possesion < 10:
#         home_poss0_10.append(float(row[16]))
#     elif home_possesion > 10 and home_possesion < 20:
#         home_poss10_20.append(float(row[16]))
#     elif home_possesion > 20 and home_possesion < 30:
#         home_poss20_30.append(float(row[16]))
#     elif home_possesion > 30 and home_possesion < 40:
#         home_poss30_40.append(float(row[16]))
#     elif home_possesion > 40 and home_possesion < 50:
#         home_poss40_50.append(float(row[16]))
#     elif home_possesion > 50 and home_possesion < 60:
#         home_poss50_60.append(float(row[16]))
#     elif home_possesion > 60 and home_possesion < 70:
#         home_poss60_70.append(float(row[16]))
#     elif home_possesion > 70 and home_possesion < 80:
#         home_poss70_80.append(float(row[16]))
#     elif home_possesion > 80 and home_possesion < 90:
#         home_poss80_90.append(float(row[16]))
#     elif home_possesion > 90 and home_possesion < 100:
#         home_poss90_100.append(float(row[16]))

# Getting average shots on tarhget for each interval of ball possesion.
# average_shot_home_poss0_10 = np.average(home_poss0_10)
# average_shot_home_poss10_20 = np.average(home_poss10_20)        
# average_shot_home_poss20_30 = np.average(home_poss20_30)
# average_shot_home_poss30_40 = np.average(home_poss30_40)           
# average_shot_home_poss40_50 = np.average(home_poss40_50)
# average_shot_home_poss50_60 = np.average(home_poss50_60)           
# average_shot_home_poss60_70 = np.average(home_poss60_70)
# average_shot_home_poss70_80 = np.average(home_poss70_80)     
# average_shot_home_poss80_90 = np.average(home_poss80_90)
# average_shot_home_poss90_100 = np.average(home_poss90_100)   



      
#%%       
# away_poss = []


# for row in rows:
#     away_possesion = float(row[25])
#     away_poss.append(away_possesion)
#print(away_poss)    

# hshot_ontarget = []

# for row in rows:
#     hsot = float(row[16])
#     hshot_ontarget.append(hsot)
#print(hshot_ontarget)

# ashot_ontarget = []

# for row in rows:
#     asot = float(row[28])
#     ashot_ontarget.append(asot)
#print(ashot_ontarget)

#%%


# lin_mod = linear_model.LinearRegression()

# lin_mod.fit(X = pd.DataFrame(home_poss), 
#                      y = hshot_ontarget)


# print(lin_mod.intercept_)

# print(lin_mod.coef_)

# plt.scatter(home_poss, hshot_ontarget)






    