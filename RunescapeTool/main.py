import time
import pyautogui
import all_functions

pyautogui.FAILSAFE = True

disclaimer = """This is how I am learning python3, Macroes and automation in Runescape is cheating.
I am not reponsible for any damages to property, accounts and missuse of this software.
this program will simulate HID (Human Interface Device) input and mov eyour move and input text to
acomplish tasks in game for you.
this is in early stages"""

print(disclaimer)
time.sleep (1)
print("Initializting...")
time.sleep (5)
all_functions.main_menu()