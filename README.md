# QuordleSolver
Solver of the popular New York Times Wordle Variant, Quordle. Found on https://www.quordle.com.
Created using Python with it's Selenium library.

Introduction
This project aims to solve quordle hands-free after an initial guess of the user's choice. 
The main goal is to solve Quordle in as few guesses as possible. 

Additional goals:
-accurately filter results of each guess using as few computations as possible.
-keep code clean and maintainable.
-make use of easy to read data structures to help with debugging.

![QuordleGif1](https://github.com/KyleJamesKilty/QuordleSolver/blob/Images/QuordleGifs/2022-09-22%2016-59-27(1).gif)
![QuordleExample](https://user-images.githubusercontent.com/98062591/172257316-3872a638-bc2c-4601-b01a-ec8bdbd3a43e.png)

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
