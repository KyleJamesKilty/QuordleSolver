# QuordleSolver

## Introduction
Solver of the popular New York Times Wordle Variant, Quordle. Created using Python and Selenium library. 

Play the game on (https://www.quordle.com).  

This project aims to solve quordle in a few guesses as possible after an initial guess of the user's choice. 

##### Adieu:
![QuordleGif1](https://github.com/KyleJamesKilty/QuordleSolver/blob/Images/QuordleGifs/2022-09-22%2016-59-27(1).gif)
##### Beers:
![QuordleGif2](https://github.com/KyleJamesKilty/QuordleSolver/blob/Images/QuordleGifs/2022-09-22%2017-00-50(1).gif)
##### Funny:
![QuordleGif2](https://github.com/KyleJamesKilty/QuordleSolver/blob/Images/QuordleGifs/2022-09-22%2017-02-19.gif)

## How to get this program running
1.Download Anaconda (https://www.anaconda.com/products/distribution).  
1.Download ChomeWebDriver (https://www.anaconda.com/products/distribution).  
2.Open the Spyder development environment that comes installed with Anaconda.  
3.Install Selenium. Using "pip install selenium" in console.  
4.Open the file or paste it into Spyder. Make sure it is saved with the .py extension.  
5.Change PATH variable in the Main.py near top of file. Set it to the file path of your ChromeWebDriver.  
5.Press Run.   

#### Additonal Details
#### Interacting with Quordle.com
The program simply uses Selenium to handle all the interaction logic with the website. After running the program, Selenium will open up the web browser and go to Quordle, enter guesses into the Quordle game, and retrieve information about each guess.

#### Logic
After each guess is retrieved, each entry in the guess json will be checked to make sure it has no absent letters, there are no letters in an incorrect position, and the word contains no less than the minimum amount of each letter, and no more than the maximum amount of each letter. Narrowed down from all earlier guesses.

The logic will ensure each of 5 things for each entry in the guess json.  
1. Any words with absent letters are ineligible.  
2. Any words that don't have a correctly positioned letter are ineligble.  
3. Any words that have a present letter in the incorrect spot are ineligible.  

Using the responses from the previous guesses, logic will narrow down present letter counts.  

4. Any words below the minimum count of a present letter will be eliminated.  
5. Any words above the maximum count of a present letter will be eliminated.  

#### Guess-List
The guess json that has been included in the folder under the file name "weighted-guess.json" includes every 5 letter word in the English Dictionary. The guesses are sorted in order of frequency of use across all Wikipedia articles. For example "where" and "apple" come fairly early in the list, when an uncommon word like "soare" (meaning a young hawk) are low on the list. This was done because extremely uncommon words are never usually used for the answers of Quordle. We don't want to waste a guess on something like that.

Secondly, the list also keeps track of the highest duplicate letter count for each word. This is done so the program can prefer guesses of words that don't use duplicate letters, until it is forced to from lack of options. Guessing words with multiple of one letter is not a good strategy for narrowing down words that can't be used.

Here is the format for each entry in "weighted-guess.json":   
String:Word = [int:WorldeGame1, int:WordleGame2, int:WordleGame3, int:WordleGame4, int:highestDuplicateLetter]  

No duplicate = 0, One duplicate = 1, Two duplicates = 2 etc.  

##### Example  
At the start of the game:  
"boony" = [0,0,0,0,1] // Boony is a potential guess for all 4 games, and has one duplicate.  


Later on in the game- once some of the words have been guessed:  
"boony" = [1,0,1,0,1] // Boony is no longer a potential guess for game 1 or game 3. Is still a viable guess for game 2 or 4. One duplicate is constant.

