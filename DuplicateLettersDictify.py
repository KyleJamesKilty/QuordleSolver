# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:16:33 2022

@author: Kyle
"""



def hasDuplicates(word):
    highest = float("-inf")
    for i in range(len(word) - 1):
        count = 0
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                count += 1
        if count > highest:
            highest = count
    return highest

first = open("FilteredWords.txt", "r")
second = open("FinalWordsList.txt", "w")
secondDictionary = {}
for line in first.readlines():
    flag = True
    for i in range(5):
        if line[i] == "'" or line[i] == ".":
            flag = False
            print(line[:-1])
    if flag:
        secondDictionary[line[:-1]] = [0, 0, 0, 0, hasDuplicates(line[:-1])]
newDictionary = (str(secondDictionary)).replace("'",'"')
second.write(newDictionary)
first.close()
second.close()