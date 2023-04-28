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
    run_count = 0
    print("""is your camera facing north,
Ore box in the first spot,
and the ore you wish to mine directly south of you?""")
    user_input = input("Y/N ")
    if user_input == "N" or user_input == "n":
        print("Reposition yourself first")
        main_menu()
        pass
    
    if user_input == "Y" or user_input == "y":   
        run_count = 0
        count_down()
        while True:
            print("Run Count = ", run_count)
            #Mining With Box
            for i in range(80):
                time_between_box = random.randint(10,20)
                
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) # type: ignore #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) # type: ignore #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) # type: ignore #box
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
            run_count += 1
        else:
            print("try again")
        pass
    pass
pass

def orichalcite_mining():
    run_count = 0 
    print("""are you at the NE ore,
is your camera facing north,
Ore box in the first spot,
and the ore you wish to mine directly south of you?""")
    user_input = input("Y/N ")
    if user_input == "N" or user_input == "n":
        print("reposition youreself first")
        main_menu()
        pass

    if user_input == "Y" or user_input == "y":
        count_down()
        while True:
            print("Run Count = ", run_count)
            #Mining With Box
            for i in range(80):
                time_between_box = random.randint(10,20)
                
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) # type: ignore #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) # type: ignore #Rock
                pyautogui.click()
                time.sleep (time_between_box)
                pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) # type: ignore #box
                pyautogui.click()
                
            pass
            #To deposit
            pyautogui.moveTo(1300, 60, .5)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo(1640, 340, .5)#GAte
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
            time.sleep (5)
            run_count += 1
    else:
        print("enter something not stupid")
        main_menu()
    pass
pass

def mouse_jiggler():
    input("Press enter when ready")
    count_down()
    while True:
        jiggler_rand_time = random.randint(5, 20)
        print("delay ", jiggler_rand_time)
        pyautogui.move (20, 20, 1)
        pyautogui.move (-20, -20, 1)
        time.sleep (jiggler_rand_time)
pass

def mining_with_box():
    print("""is your camera facing north,
Ore box in the first spot,
and the ore you wish to mine directly south of you?""")
    user_input = input("Y/N ")
    if user_input == "N" or user_input == "n":
        print("position yourself then select again")
        time.sleep(1)
        main_menu()
    if user_input == "Y" or user_input == "y":
        count_down()
        while True:
            time_between_box = random.randint(10,20)
            pyautogui.moveTo(1540, 1080, .5, pyautogui.easeInElastic) # type: ignore #Rock
            pyautogui.click()
            time.sleep (time_between_box)
            pyautogui.moveTo(2722, 1203, .5, pyautogui.easeInElastic) # type: ignore #box
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

def smelting():
    run_count = 0
    print("Stand on the south side of any furnace")
    count_down()
    while True:
        print("run count ", run_count)
        pyautogui.moveTo (1540, 780, 2)
        pyautogui.click()
        pyautogui.moveTo (894, 1390, 2)
        pyautogui.click()
        time.sleep (.5)
        pyautogui.press(' ')
        pyautogui.move (300, 0, 2)
        time.sleep (50)
        run_count += 1
pass

def fletching():
        print("Stand south of a tree and it will chop and fletch sticks")
        input("Press enter when ready")
        while True:
            for i in range(20):
                pyautogui.leftClick(1523, 733)
                time.sleep(10)
                pass
            pyautogui.rightClick(2728, 1205)
            time.sleep(.5)
            pyautogui.leftClick(2707, 1254)
            time.sleep(1)
            pyautogui.press (' ')
            time.sleep(40)
            pass


            

scripts = [drakolith_mining, orichalcite_mining, mouse_jiggler, mining_with_box, smithing, smelting, fletching]

def main_menu():
    print("Pick a script to run")
    print("1. drakolith_mining  2. orichalcite_mining  3. mouse_jiggler  4. mining_with_box  5. smithing  6. smelting 7. Fletching")
    selection = int(input("Enter selection (1-7): "))
    if selection >= 1 and selection <= len(scripts):
        scripts[selection-1]()
    else:
        print("Invalid selection")
        time.sleep (1)
        main_menu()
pass

