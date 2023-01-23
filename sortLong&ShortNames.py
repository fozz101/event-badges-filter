# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 07:06:30 2022

@author: fedig
"""

import pandas as pd
from PIL import ImageFont
import re


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start



def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    
    return newString


#  message.count('p')



members = pd.read_excel('List of Participants (badges).xlsx')

allmembers = members[["Variable1","Variable2"]]




shortList=[]
shortSBList=[]
longList=[]
longSBList=[]

font = ImageFont.truetype(font='C:/Meteoric-Bold.ttf', size=60)

for ind in members.index:
    #print(allmembers['Variable1'][ind], allmembers['Variable2'][ind])
    
    if (font.getsize(allmembers['Variable1'][ind])[0]<=392):
        
        shortList.append(allmembers['Variable1'][ind].title().strip())
        shortSBList.append(allmembers['Variable2'][ind])
        
        
    else:
        if (allmembers['Variable1'][ind].title().strip().count(" ")>=2):
            
            longList.append(replacenth(allmembers['Variable1'][ind].title().strip()," ","\n",2))
            longSBList.append(allmembers['Variable2'][ind])
        else:
            longList.append(replacenth(allmembers['Variable1'][ind].title().strip()," ","\n",1))
            longSBList.append(allmembers['Variable2'][ind])
            
    


shortDataframe = pd.DataFrame(
    {'Variable1': shortList,
     'Variable2': shortSBList
    })


longDataframe = pd.DataFrame(
    {'Variable1': longList,
     'Variable2': longSBList
    })

shortDataframe.to_excel('shortName.xlsx', index = False)
longDataframe.to_excel('longName.xlsx', index = False)










