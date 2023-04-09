import time
import pyautogui
import random

def deposit():
    pyautogui.moveTo (1647, 656, 1) #Deposit box
    pyautogui.click()
    time.sleep (5)
    pyautogui.moveTo (1112, 564, 1) #select Ore
    pyautogui.click(button='right')
    time.sleep (2)
    pyautogui.moveTo (1134, 707, 1) #deposit all
    pyautogui.click()
    time.sleep (2)
    pyautogui.press ('esc')
    time.sleep (1)
    pyautogui.moveTo (2717, 1204, 1)
    pyautogui.click(button='right')
    time.sleep (2)
    pyautogui.moveTo (2571, 1353, 1) #use
    pyautogui.click()
    time.sleep (2)
    pyautogui.moveTo (1420, 927, 1)#deposit box
    pyautogui.click()
    time.sleep (2)
    pyautogui.moveTo (1180, 1208, 1) #exit
    pyautogui.click()
pass

def count_down():
    countdown = 5
    while countdown > 0:
        print("Starting in", countdown)
        time.sleep(1)
        countdown -= 1

    print("Start!")
    pass
pass

def drakolith_mining():
    print("""is your camera facing north,
Ore box in the first spot,
and the ore you wish to mine directly south of you?""")
    user_input = input("Y/N ")
    if user_input == "N":
        print("Reposition yourself first")
        main_menu()
        pass
    if user_input == "n":
        print("reposition yourself first")
        main_menu()
        pass
    if user_input == "y":    
        count_down()
        while True:
            #Mining With Box
            for i in range(80):
                time_between_box = random.randint(10,20)
                
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) #box
                pyautogui.click()
                
            pass
            #To deposit
            pyautogui.moveTo (1140, 49, 1) #1st door
            pyautogui.click()
            time.sleep(10)
            pyautogui.moveTo (2230, 1280, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2230, 1000, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2230, 1000, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1760, 50, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1649, 256, 1) #Gate
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (650, 236, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1247, 334, 1) #2nd door
            pyautogui.click()
            time.sleep(5)
            #Deposit
            deposit()
            time.sleep(5)
            #back to ore
            pyautogui.moveTo (2249, 1878, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2249, 1878, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1180, 1890, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1180, 1890, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (423, 1180, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (765, 551, 1)
            pyautogui.click()
            time.sleep(10)
            pyautogui.moveTo (1873, 1887, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1626, 1163, 1)
            pyautogui.click()
            time.sleep (5)
        pass
    if user_input == "Y":    
        count_down()
        while True:
            #Mining With Box
            for i in range(80):
                time_between_box = random.randint(10,20)
                
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) #box
                pyautogui.click()
                
            pass
            #To deposit
            pyautogui.moveTo (1140, 49, 1) #1st door
            pyautogui.click()
            time.sleep(10)
            pyautogui.moveTo (2230, 1280, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2230, 1000, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2230, 1000, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1760, 50, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1649, 256, 1) #Gate
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (650, 236, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1247, 334, 1) #2nd door
            pyautogui.click()
            time.sleep(5)
            #Deposit
            deposit()
            time.sleep(5)
            #back to ore
            pyautogui.moveTo (2249, 1878, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2249, 1878, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1180, 1890, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1180, 1890, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (423, 1180, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (765, 551, 1)
            pyautogui.click()
            time.sleep(10)
            pyautogui.moveTo (1873, 1887, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1626, 1163, 1)
            pyautogui.click()
            time.sleep (5)
        pass
pass

def orichalcite_mining():
    print("""are you at the NE ore,
is your camera facing north,
Ore box in the first spot,
and the ore you wish to mine directly south of you?""")
    user_input = input("Y/N ")
    if user_input == "N":
        print("reposition youreself first")
        main_menu()
        pass
    if user_input == "n"
        print("reposition youreself first")
        main_menu()
        pass
    if user_input == "Y"
        count_down()
        while True:
            #Mining With Box
            for i in range(80):
                time_between_box = random.randint(10,20)
                
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) #box
                pyautogui.click()
                
            pass
            #To deposit
            pyautogui.moveTo(1300, 60, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo(1640, 344, .5)#GAte
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (650, 236, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1247, 334, 1) #2nd door
            pyautogui.click()
            time.sleep(5)
            #Deposit
            deposit()
            time.sleep(5)
            #back to ore
            pyautogui.moveTo (2217, 1886, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2264, 1875, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1542, 1853, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1542, 1853, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1734, 1185, .5)
            pyautogui.click()
    pass
    if user_input == "y"
        count_down()
        while True:
            #Mining With Box
            for i in range(80):
                time_between_box = random.randint(10,20)
                
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) #box
                pyautogui.click()
                
            pass
            #To deposit
            pyautogui.moveTo(1300, 60, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo(1640, 344, .5)#GAte
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (650, 236, 1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1247, 334, 1) #2nd door
            pyautogui.click()
            time.sleep(5)
            #Deposit
            deposit()
            time.sleep(5)
            #back to ore
            pyautogui.moveTo (2217, 1886, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (2264, 1875, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1542, 1853, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1542, 1853, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo (1734, 1185, .5)
            pyautogui.click()
    pass
pass

def mouse_jiggler():
    count_down()
    while True:
        jiggler_rand_time = random.randint(5, 20)
        pyautogui.move (20, 20, 1)
        pyautogui.move (-20, -20, 1)
        time.sleep (jiggler_rand_time)
pass

def mining_with_box():
    print("""is your camera facing north,
Ore box in the first spot,
and the ore you wish to mine directly south of you?""")
    user_input = input("Y/N ")
    if user_input == "N":
        print("position yourself then select again")
        time.sleep(1)
        main_menu()
    if user_input == "n":
        print("position yourself then select again")
        time.sleep(1)
        main_menu()
    if user_input == "Y":
        count_down()
        while True:
            time_between_box = random.randint(10,20)
            pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
            pyautogui.click()
            time.sleep (time_between_box)
            pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) #box
            pyautogui.click()
    if user_input == "y":
        count_down()
        while True:
            time_between_box = random.randint(10,20)
            pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) #Rock
            pyautogui.click()
            time.sleep (time_between_box)
            pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) #box
            pyautogui.click()
    else:
        print("please input somthing not stupid")
        mining_with_box()
pass

def smithing():
    print("""stand north of lumbridge anvil
camera facing north""")
    input("Press enter when ready")
    while True:
        pyautogui.moveTo (1535, 767, 1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo (1533, 1172, 1)
        pyautogui.click()
        time.sleep (20)
        pass
pass

scripts = [drakolith_mining, orichalcite_mining, mouse_jiggler, mining_with_box, smithing]

def main_menu():
    print("Pick a script to run")
    print("1. drakolith_mining  2. orichalcite_mining  3. mouse_jiggler  4. mining_with_box  5. smithing")
    selection = int(input("Enter selection (1-5): "))
    if selection >= 1 and selection <= len(scripts):
        scripts[selection-1]()
    else:
        print("Invalid selection")
        time.sleep (1)
        main_menu()
pass

