import time
import pyautogui
import all_functions

pyautogui.FAILSAFE = True

disclaimer = """This program is a macro/scripting tool for Runescape3.
Macros and scripting in RS3 is against the T&C and will get you banned
I cant promise FUD
User risk is implied
How it Works:
Using Pyautogui python will send HID input to the system and control the game for you
Choose a function to run and hit enter, specific insturctions may follow
Pysutogui moves the mouse by the pixel and all postions on the screen are given on an x y grid
Many of the tools will not work if your monitor resolution is not equal to 3072x1920"""

print(disclaimer)
time.sleep (1)
print("Initializting...")
time.sleep (5)
all_functions.main_menu()