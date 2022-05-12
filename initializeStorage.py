# -*- coding: utf-8 -*-
"""
Created on Sat May  7 20:20:01 2022

@author: Kyle
"""
import json

def loadStorage():
    with open("FinalWordsList.json","r") as fiveletterwords:
        data = json.load(fiveletterwords)
    
    return data
            


    