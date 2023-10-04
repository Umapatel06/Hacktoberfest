import os
import time
import subprocess
import pyautogui
from random_word import RandomWords

# Path to your Chrome browser executable
bro = "C:\Program Files\Google\Chrome\Application\chrome.exe"

def pc():
    number_of_searches = 40  # Change the number of searches accordingly

    for i in range(number_of_searches):
        r = RandomWords()
        random_word = r.get_random_word()  # Get a random word

        url = "https://www.google.com/search?q=" + random_word

        try:
            subprocess.run([bro, url])  # Open browser with the URL
        except FileNotFoundError:
            print("Browser is not installed or not found on your system or path is not correct")
            print("\nPC Search Done", i, "Times")

    for i in range(number_of_searches):
        time.sleep(0.1)
        pyautogui.hotkey("ctrlleft", "w")  # Close tab using Ctrl+W

def mb():
    number_of_searches = 30  # Change the number of searches accordingly
    time.sleep(1)
    pyautogui.hotkey("ctrlleft", "t")  # Open a new tab
    pyautogui.hotkey("ctrlleft", "shiftleft", "j")  # Open address bar
    time.sleep(1)
    pyautogui.hotkey("ctrlleft", "shiftleft", "m")  # Type in the address bar
    time.sleep(2)
    pyautogui.hotkey("ctrlleft", "R")  # Reload the page
    pyautogui.hotkey("ctrlleft", "r")
    time.sleep(3)

    for j in range(number_of_searches):
        time.sleep(2)
        pyautogui.hotkey("ctrlleft", "e")  # Select address bar
        pyautogui.hotkey("ctrlleft", "l")  # Delete the current URL
        random_word = RandomWords().get_random_word()  # Get a random word

        url = "https://www.google.com/search?q=" + random_word
        time.sleep(1)
        pyautogui.typewrite(url)  # Type the URL in the address bar
        pyautogui.press("enter")  # Press Enter to initiate the search

pc()  # Perform PC searches
mb()  # Perform mobile-like searches
print("Automatic Search Done")
