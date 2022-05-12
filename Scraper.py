# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:41:19 2022

@author: Kyle
"""
from selenium import webdriver

def openLogin():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/10001-20000")
    return driver


driver = openLogin()

Table = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/table[1]")
ListofWords = driver.find_elements_by_tag_name('tr')
def write():
    f = open('WeightedWords.txt', 'a')
    for idx,element in enumerate(ListofWords):
        if idx != 0:
            wordSplit = element.text.split(" ")
            if len(wordSplit[1]) == 5:
                print(idx)
                f.write(wordSplit[1])
                f.write('\n')
        
    f.close()

write()
        
    

