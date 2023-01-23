# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 05:29:45 2022

@author: fedig
"""
import pandas as pd
import numpy as np

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


allmembers = pd.read_excel('longVerif.xlsx')






partIname=[]
partIIname=[]
SBList=[]



for ind in allmembers.index:
    #print(allmembers['Variable1'][ind], allmembers['Variable2'][ind])
    
    if (allmembers['Variable1'][ind].title().strip().count(" ")>=2):
        partIname.append(allmembers['Variable1'][ind].title().strip()[:find_nth(allmembers['Variable1'][ind].title().strip()," ",2)+1])
        partIIname.append(allmembers['Variable1'][ind].title().strip()[find_nth(allmembers['Variable1'][ind].title().strip()," ",2)+1:])
        SBList.append(allmembers['Variable2'][ind])
    else:
        partIname.append(allmembers['Variable1'][ind].title().strip()[:find_nth(allmembers['Variable1'][ind].title().strip()," ",1)+1])
        partIIname.append(allmembers['Variable1'][ind].title().strip()[find_nth(allmembers['Variable1'][ind].title().strip()," ",1)+1:])
        SBList.append(allmembers['Variable2'][ind])


Dataframe = pd.DataFrame(
    {'Variable1': partIname,
     'Variable2': partIIname,
     'Variable3': SBList
     
    })


#print(Dataframe)



split = np.array_split(Dataframe, 3)



for i in range(len(split)):
    split[i].to_csv("D:/"+str(i)+'newLongName.csv')
    



#Dataframe.to_excel('newLongName.xlsx', index = False)










