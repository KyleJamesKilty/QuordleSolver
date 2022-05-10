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
import time

def OpenLogin():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.quordle.com/#/")
    return driver

#Open
#InitialGuess
#Read1 -> Update Constraints 4 -> Check 4 -> Pick Word that could potentially be in most
#Read2 
#Read3
#Read4
#Read5
#Read6
#Read7
#Read8
#Read9

#Read Function
#Update Constraints
#Check

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
    
#reads guess in each row and puts it in dictionary if guess is not correct or wasnt correct
def retrieval(rowCounter: int, correctGuesses: list ): #{1:{0:{"Present":[],"Contains":[],"Absent":[]}}}
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
    return RowRetrieval
        
    
driver = OpenLogin()
time.sleep(5)
RowRetrieval = retrieval(0,[0,0,0,0])




#"flex flex-col flex-auto p-1 first:pl-2 last:pr-2"
#/html/body/div/div/div[2]/div[1]/div[1]/div[1]

#I want to pass in [4 sets of [sets containing 5 letters]] update [4 sets] guess highest potential words. 
