# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:44:45 2022
@author: Kyle
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from initializeStorage import loadStorage
import time

def openLogin():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.quordle.com/#/")
    return driver
    
def preparepage(driver):
    actions = ActionChains(driver)
    actions.click()
    actions.pause(2)
    actions.move_by_offset(500, 900)
    actions.perform()
    
def sendguess(guess, pause, driver):
    actions = ActionChains(driver)
    actions.send_keys(guess)
    actions.send_keys(Keys.RETURN)
    actions.pause(pause)
    actions.perform()
   
def retrieveTables(driver):
   table1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div[1]")
   table2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div[2]")
   table3 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[1]")
   table4 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[2]")
   table = [table1, table2, table3, table4]
   return table

def retrieveTableRows(table):
    table1Rows = table[0].find_elements_by_css_selector('div.flex.w-full')
    table2Rows = table[1].find_elements_by_css_selector('div.flex.w-full')
    table3Rows = table[2].find_elements_by_css_selector('div.flex.w-full')
    table4Rows = table[3].find_elements_by_css_selector('div.flex.w-full')
    tableRows = [table1Rows, table2Rows, table3Rows, table4Rows]
    return tableRows

def retrieveLetters(rows, rowCounter):
    letters = rows[rowCounter].find_elements_by_tag_name('div')
    return letters

def letterChecker(letters):
    letterSpecs = []
    for i in range(10):
        if i % 2 == 0:
            letterSpecs.append(letters[i].get_attribute('aria-label'))
    return letterSpecs
            
def updateCorrectGuess(tableRows, rowCounter, idx):
    arialabel = tableRows[idx][rowCounter].get_attribute('aria-label')
    return stringSearchAlgo(arialabel)
    
    
def stringSearchAlgo(string):
    if "correct" in string:
        return True
    return False

def stringSorter(string):
    if "incorrect" in string:
        return "Absent"
    if "correct" in string:
        return "Present"
    if "different" in string:
        return "Another"

def findNextGuess(allGuesses, correctGuesses):  
    for duplicateCount in range(6):
        for word, value in allGuesses.items():
            if value[4] == duplicateCount:
                for validTables in range(4):
                    if correctGuesses[validTables] == False:
                        if value[validTables] == 0:
                            guess = word
                            print(guess)
                            value[1] = 1
                            value[2] = 1
                            value[3] = 1
                            value[4] = 1
                            
                            return guess, allGuesses
                            
    
    
#reads guess in each row and puts it in dictionary if guess is not correct or wasnt correct
def retrieval(driver, rowCounter: int, correctGuesses: list ): #{1:{0:{"Present":[],"Contains":[],"Absent":[]}}}
    RowRetrieval = {}
    table = retrieveTables(driver)
    tableRows = retrieveTableRows(table)
    for idx in range(4): #Check if new correct Guess and update table
        correctGuesses[idx] = updateCorrectGuess(tableRows, rowCounter, idx)
    for idx, Fails in enumerate(correctGuesses): #Add letters to dictionary if table isn't correct yet
        RowRetrieval[idx] = {}
        if Fails == 1:
            continue
        elif Fails == 0:
            letters = retrieveLetters(tableRows[idx], rowCounter)
            letterSpecs = letterChecker(letters)
            for letterIdx, string in enumerate(letterSpecs):
                RowRetrieval[idx][letterIdx] = {"Present":[],"Another":[],"Absent":[]}
                RowRetrieval[idx][letterIdx][stringSorter(string)].append(string[1])      
    return RowRetrieval, correctGuesses


def validWord(word, rowTableRetrieval, letterCounts):
    word = word.upper()
    for letterIndex, presentAnotherAbsent in rowTableRetrieval.items():
        Present = presentAnotherAbsent['Present']
        Another = presentAnotherAbsent['Another']
        Absent = presentAnotherAbsent['Absent']
        if len(Present) != 0:
            if word[letterIndex] != Present[0]:
                return False
        
        if len(Another) != 0:
            if word[letterIndex] == Another[0]:
                return False
        
        if len(Absent) != 0:
            validAbsent = True
            for letter, minMax in letterCounts.items():
                if Absent[0] == letter:
                    if minMax[0] == minMax[1]:
                        validAbsent = False
            if validAbsent:
                if Absent[0] in word: 
                    return False
        
    return True
    

def validCount(word, lettersMinMax): #Checks to make sure letter count in each guess is correct
# lettersMinMax is the specific current count for one table
    letterCount = {}
    for letter in word:
        letter = letter.upper()
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    for letter, count in letterCount.items():
        if letter in lettersMinMax:
            if count < lettersMinMax[letter][0]:
                return False
            if count > lettersMinMax[letter][1]:
                return False
    for letter in lettersMinMax.keys():
        if letter not in letterCount:
            return False
    return True
    

def dictionaryNewOrAdd(countDict, letter, minmax, increment = None):
    if letter in countDict:
        if minmax == "min":
            countDict[letter][0] += 1 #Increments
        elif minmax == "max":
            countDict[letter][1] = increment #Sets Max
    else:
        countDict[letter] = [1,5] #Initialization Value
    return countDict

def compareAndUpdateDicts(masterDict, comparisonDict, tableIdx, minCount):
    for letter, minMaxList in comparisonDict.items():
        if letter not in masterDict[tableIdx]:
            masterDict[tableIdx][letter] = minMaxList
        else:
            if minMaxList[0] > masterDict[tableIdx][letter][0]:
                masterDict[tableIdx][letter][0] = minMaxList[0]
            elif minMaxList[1] < masterDict[tableIdx][letter][1]:
                masterDict[tableIdx][letter][1] = minMaxList[1]
    
    return masterDict

def updateMasterDict(letterCounts): #Fixes max Letters in letterCounts if bounded by 5 and OtherLetters
    for tableIdx in range(4):
        minLetters = 0
        if len(letterCounts[tableIdx]) == 0:
            continue
        for letter, minMaxList in letterCounts[tableIdx].items():
            minLetters += minMaxList[0]
        for letter, minMaxList in letterCounts[tableIdx].items():
            if 5 + minMaxList[0] - minLetters < minMaxList[1]:
                minMaxList[1] = 5 + minMaxList[0] - minLetters
    return letterCounts
            

def updateCount(letterCounts, rowRetrieval):
    for tableIdx in range(4):
        comparison = {}
        if len(rowRetrieval[tableIdx]) == 0:
            continue
        else:
            minCount = 0
            for letterIdx in range(5): #Updates Min
                PresentLetter = rowRetrieval[tableIdx][letterIdx]['Present']   
                AnotherLetter = rowRetrieval[tableIdx][letterIdx]['Another']   
                if len(PresentLetter) != 0:
                    comparison = dictionaryNewOrAdd(comparison, PresentLetter[0], "min")
                    minCount += 1
                if len(AnotherLetter) != 0:
                    comparison = dictionaryNewOrAdd(comparison, AnotherLetter[0], "min")
                    minCount += 1
                   
            for letterIdx in range(5): #Updates Max
                for letters, minMax in comparison.items():
                    spacesLeft = 5 + minMax[0] - minCount
                    if spacesLeft < minMax[1]:
                        minMax[1] = spacesLeft
                AbsentLetter = rowRetrieval[tableIdx][letterIdx]['Absent']
                if len(AbsentLetter) != 0:
                    if AbsentLetter[0] in comparison:
                        comparison[AbsentLetter[0]][1] = comparison[AbsentLetter[0]][0] 
                letterCounts = compareAndUpdateDicts(letterCounts, comparison, tableIdx, minCount)
                letterCounts = updateMasterDict(letterCounts)
    return letterCounts
                
   # {0: {'a':[1,5],'b':[2,3],'c':[3,5]} 1....}       
   # format for return     
    # Min on left only increases if more are found in a single retrieval, Max on right decreases if other letters found or if found/absent combo
     
    return letterCounts

def filterAllGuesses(allGuesses: dict, letterCounts, rowRetrieval):
    for tableIdx in range(4):
        if len(rowRetrieval[tableIdx]) == 0:
            continue
        else:
            for word, value in allGuesses.items():
                if value[tableIdx] == 1:
                    continue
                else:
                    if not validCount(word, letterCounts[tableIdx]):
                        value[tableIdx] = 1 #Think this mutates list in dictionary but not sure
                        continue
                    if not validWord(word, rowRetrieval[tableIdx], letterCounts[tableIdx]):
                        value[tableIdx] = 1
                        continue
    return allGuesses


        
def main():
    allGuesses = loadStorage()
    driver = openLogin()
    preparepage(driver)
    sendguess("funny", 0.5 , driver) #Initial Guess
    time.sleep(1)
    rowCounter = 0
    correctGuesses = [0, 0, 0, 0]
    letterCounts = {0: {}, 1: {}, 2: {}, 3: {}}
    while rowCounter < 9:
        rowRetrieval, correctGuesses = retrieval(driver, rowCounter,correctGuesses)
        # Debug RowRetrieval
        letterCounts = updateCount(letterCounts, rowRetrieval)
        allGuesses = filterAllGuesses(allGuesses, letterCounts, rowRetrieval)
        rowCounter += 1
        guess, allGuesses = findNextGuess(allGuesses, correctGuesses)
        sendguess(guess, 0.5 , driver)
        
    
    

if __name__ == "__main__":
   main()