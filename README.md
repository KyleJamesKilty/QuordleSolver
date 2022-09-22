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


Technologies:
-ChromeWebDriver https://chromedriver.chromium.org/downloads
-Selenium https://www.selenium.dev/downloads/
-Python https://www.python.org/downloads/

Launch:
After installing Python, Selenium, and ChromeWebDriver. You must edit the PATH variable location inside 
Main.py in the openLogin function near the top of the file. 

PATH = "C:\Program Files (x86)\chromedriver.exe"

Change the path variable to the location of where you installed the ChromeWebDriver.

To modify the initial guesses, change, remove, or add any words in the guessList variable found
in the main function near the bottom of the file.

Currently, the program will sequentially solve a wordle for each guess currently listed.

Run the program.
