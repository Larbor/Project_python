# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy

my_name = "Lars"
print(my_name)

#can not start varable with numbers or other special caracters
#1st_name = "lars"

#convention in python is to not use camelCase. Snake_case is better.
#firstName = "lars"
first_name = "lars"

#usaually good to have descriptive variable names 
#n1 = "lars"
first_name = "lars"

#type is good for examining variables
first_name = "lars"
print(type(first_name))

#dir is a function returns all properties and methods of the specified object, without the values.
print(dir(first_name))   

print(first_name.upper())

print(first_name.count("lars"))

#with boolean variables you ned to start True and False with capital letters

#Lists 
names = ["Per", "Tor", "Kjell", 5, True]
print(names)
print(names[1])
names.append("Petter")
print(names)
print(len(names))

print(names.index("Tor"))
print(names.count("Tor"))
names.remove("Tor")
print(names)
del(names[0:1])
print(names)
names.reverse()
print(names)
names.insert(3, "Tor")
print(names)
    
ages = [43, 52, 43, 12, 43]

ages_months = []

for item in ages:
    item = item * 12
    ages_months.append(item)
    print(item)

for c, value in enumerate(ages_months, 1):
    print(c, value)

ages_index = list(enumerate(ages, 1))
print(ages_index)

wheights_kg = [76, 55, 89, 115, 67]
wheights_pounds = []

for i in wheights_kg:
    pounds = round(i * 2.2, 4)
    wheights_pounds.append(pounds)
print(wheights_pounds)

import trompy

name = "paul"
if name in ["john", "paul", "george", "ringo"]:
    print(name)
    
name in ["john", "paul", "george", "ringo"]

name == "paul"

name != "paul"

if name == "paul":
    print("that is a boring name")
    
# %%
boring_names = ["lars", "jens", "guro"]

name = "lars"
name_2 = "gry"
if name in boring_names:
    print(True)
    
if name_2 in boring_names:
    print(True)
elif name in boring_names:
    print(True)
else: 
    print(False)

if name == "gry":
    print(name, "is a boring name")
elif name == "lars":
    print(name, "is a boring name")
else:
    print("Skaff deg et navn!")
# %%    
for i in boring_names:
    if i == name_2:
        print(name_2, "is a boring name")
    elif i == name:
        print(name, "is a beautiful name")
    else:
        print(i, "is an ugly name")

 
import numpy

filename = "C:/Users/labor/Downloads/Pearson-1.txt"

data = numpy.loadtxt(filename, skiprows=1)

father = data[:, 0]

son = data[:, 1]

father_cm = []

son_cm = []

for i in father:
    icm = i*2.54
    father_cm.append(icm)
   
#print(father_cm)

for i in son:
    soncm = i*2.54
    son_cm.append(soncm)
#print(son_cm)


#sumdata= son[0:2].sum() 
#print(sumdata)

#meandata= son[0:2].mean() 
#print(meandata)

# mindata= son[0:2].min() 
# print(mindata)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#ax.hist(son)

#sorted_father = numpy.sort(father)

fig, [ax1, ax2] = plt.subplots(ncols=2)
ax1_hist = ax1.hist(father, color="green")
ax2_hist = ax2.hist(son, color="blue")
#ax1_scatter = ax1.scatter(father, color="green")
#ax2_scatter = ax2.scatter(son, color="blue")

# ax.scatter(father, son, c="blue", s=20, alpha=0.2)
# ax.set_xlabel("heights of fathers (inches)")
# ax.set_ylabel("heights of sons (inches)")
# ax.set_title("Height data")

ax.scatter(father_cm, son_cm, c="blue", s=20, alpha=0.2)
ax.set_xlabel("heights of fathers (cm)")
ax.set_ylabel("heights of sons (cm)")
ax.set_title("Height data")
#ax.hist(data)

#ax.scatter(ax1, ax2)


#Functions

def say_hello(name):
    print("Hello", name)

say_hello("Karl")

def say_hello1(name_chris):
    greeting = "Hello" +" "+ name_chris
    return greeting

hello_for_chris = say_hello1("Chris")

print(hello_for_chris)

def say_hello_language(name, language="English"):
    """
    Makes a greeting for a person thet you name as paramater 
    
    Parameters
    Name (str): name of the person.
    Language (opt argument, default as english): checks if it should andwer in english 
    
    Returns
    
    greeting : A greeting with a name 

    """
    if language == "English":
        greeting = "Hello " + name
    else:
        greeting = "God morgen " + name
    return greeting

karl_english = say_hello_language("Karl", "English")
karl_nor = say_hello_language("Karl", "Norsk")

print(karl_english)

print(karl_nor)



state_school_data = "C:/Users/labor/Downloads/nces330_20.csv"

import pandas as pd

with open(state_school_data, "r") as f:
    df = pd.read_csv(f, delimiter = ",")

import numpy as np
import matplotlib.pyplot as plt

data_years = list(df["Year"])
data_state = list(df["State"])
data_type = list(df["Type"])
data_length = list(df["Length"])
data_expence = list(df["Expense"])
data_value = list(df["Value"])

f, ax = plt.subplots()

ax.bar(data_years, data_value)

f, ax = plt.subplots()
df_alabama = df[df["State"] == "Alabama"]
df_alaska = df[df["State"] == "Alaska"]
ax.boxplot((df_alabama["Value"], df_alaska["Value"]))


f, ax = plt.subplots()
ax.bar(data_length, data_value)



f, ax = plt.subplots()
ax.pie(data_type)
#ax.scatter(data_value, data_length)

# %%


import csv
rows = []
with open("C:/Users/labor/Downloads/topSubscribed.csv", 'r') as youtube_file:
    csvreader = csv.reader(youtube_file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

    

#%%

# A readme editor https://readme.so/editor. Remember to use licence, acnowledgements, usage/examples, title and description. You can add a logo.
# after using the readme editor, you can just copy paste it into your readme file. 
import os
# import json
import pandas as pd


import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

os.chdir("C:\Python scripts\GitHub\Programming\Project_python\Project_python")



# playlist_uris = ["1x6F69hJQYRTiWjD5F567h",
  #               "078tWWpvyl9a3O0QIZo5B7",
   #              "3rcn9wzz5UbtQU9aJyLUUc"
    #            ]

# dirty_loops = sp.artist("5Apl0wL4OwNUDYkx69rMDQ")

# print(dirty_loops["popularity"])

# sp.artist_albums('0hEurMDQu99nJRq8pTxO14',country='No')


# for x in playlist_uris:
 #   print(sp.playlist(x)["name"])
    

sp_scopes    = "user-read-playback-state, user-read-currently-playing, user-read-playback-position, user-top-read, user-read-recently-played, playlist-read-private, playlist-read-collaborative"
sp_redirect  = "http://localhost:8888/callback" 

 

sp_user_auth = spotipy.SpotifyOAuth(
    client_id     = "0bc4658220f0466791e8436c824efd4a",       # client ID
    client_secret = "a57bd7d70878490bb2eae3fe0e8a3e30",    # Secret
    redirect_uri  = sp_redirect,   # redirect to....
    scope         = sp_scopes)        # access scope

sp_user_auth.get_authorization_code() # Should open the browser which asks your to authorize access

sp = spotipy.Spotify(auth_manager = sp_user_auth)  # Set variable to do calls

user_recently_played = sp.current_user_recently_played() # get users last played songs
#%%
# print(user_recently_played)

user_recently_played

user_recently_played["items"][0].keys() # keys to access

user_recently_played["items"][0]["track"] # info under track


user_recently_played["items"][0]["track"].keys()

user_recently_played["items"][0]["track"]["name"] # track name

top_tracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')

print(top_tracks)    

#%%

import csv
rows = []
with open("C:/Python scripts/GitHub/Programming/Project_python/Project_python/Data/archive (1)/df_full_premierleague.csv", 'r') as premier:
    csvreader = csv.reader(premier)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)




 