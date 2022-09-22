# QuordleSolver

### Introduction
Solver of the popular New York Times Wordle Variant, Quordle. Created using Python and Selenium library. 

Play the game on (https://www.quordle.com).  

This project aims to solve quordle in a few guesses as possible after an initial guess of the user's choice. 

##### Adieu initial guess
![QuordleGif1](https://github.com/KyleJamesKilty/QuordleSolver/blob/Images/QuordleGifs/2022-09-22%2016-59-27(1).gif)
##### Beers initial guess
![QuordleGif2](https://github.com/KyleJamesKilty/QuordleSolver/blob/Images/QuordleGifs/2022-09-22%2017-00-50(1).gif)
##### Funny initial guess
![QuordleGif2](https://github.com/KyleJamesKilty/QuordleSolver/blob/Images/QuordleGifs/2022-09-22%2017-02-19.gif)

## How to get this program running
1.Download Anaconda (https://www.anaconda.com/products/distribution).  
1.Download ChomeWebDriver (https://www.anaconda.com/products/distribution).  
2.Open the Spyder development environment that comes installed with Anaconda.  
3.Install Selenium. Using "pip install selenium" in console.  
4.Open the file or paste it into Spyder. Make sure it is saved with the .py extension.  
5.Change PATH variable in the Main.py near top of file. Set it to the file path of your ChromeWebDriver.  
5.Press Run.   

### Additonal Details about the guess weighting system
The guess json that has been included in the folder under the file name "weighted-guess.json" includes every 5 letter word in the English Dictionary. The guesses are sorted in order of frequency use across all Wikipedia articles. For example "where" and "apple" come fairly early in the list where an uncommon word like "soare" (meaning a young hawk) are low on the list. This was done because really really uncommon words are never usually used for the answers of Quordle. We don't want to waste a guess on something like that.

Secondly, the list also keeps track of the highest duplicate letter count for each word. This is done so the program can prefer guesses of words that don't use duplicate letters until it is forced to from lack of options. Guessing words with multiple of one letter is not a good strategy for narrowing down words that can't be used.

Here is the format for each entry in "weighted-guess.json":   
String:Word = [int:WorldeGame1, int:WordleGame2, int:WordleGame3, int:WordleGame4, int:highestDuplicateLetter]  

No duplicate = 0, One duplicate = 1, Two duplicates = 2 etc.  

### Example  
For example at the start of the game:  
"boony" = [0,0,0,0,1] // Boony is a potential guess for all 4 games, and is has one duplicate.  


Later on in the game once some of the words have been guessed:  
"boony" = [1,0,1,0,1] // Boony is no longer a potential guess for game 1 or game 3. 

