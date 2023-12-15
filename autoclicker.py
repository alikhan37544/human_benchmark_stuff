"""
Basically we have to worry about 3 colors : 
    1. The color of the screen when the game is not running and asking for a click to start : #2b87d1
    2. The color of the screen when the game is running and waiting for input : #4BDB6A
    3. The color of the screen when the game is running and we have to wait for the click : #CE2636


    Notes :
    1. When the game is not running, we have to click to start the game. It doesn't matter how long it takes, but we have to click on the screen to start the game
    2. When the game is running, when we get color 3, which is #CE2636, we have to wait actively for the color to change. Here, timing is important, we have to actively scan and prepare
    for the click. We have to click as soon as the color changes.
    3. When the color changes to the color 2, which is #4BDB6A, we have to click on the screen. We have to click as soon as we get this color. 

    4. After clicking the color 1, we get color 3 where the game starts. We have to wait for the color to change to color 2, and then click on the screen.
    After that, the color changes to color 1 again, where we reinitiate the game

    Prefered to have a 5 second delay between each game. But for the other colors, minimum delay is prefered.
"""




import pyautogui
import time

COLOR_START_GAME = "#2b87d1"
COLOR_WAIT_INPUT = "#4BDB6A"
COLOR_WAIT_CLICK = "#CE2636"

def wait_for_color(color, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        current_color = pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1])
        if current_color == color:
            return True
    return False

def click_on_color_change():
    while True:
        if wait_for_color(COLOR_START_GAME):
            pyautogui.click()  # Click to start the game
            if wait_for_color(COLOR_WAIT_CLICK):
                pyautogui.click()  # Click when color changes to COLOR_WAIT_INPUT
                if wait_for_color(COLOR_WAIT_INPUT):
                    pyautogui.click()  # Click when color changes to COLOR_START_GAME to restart the game
                    time.sleep(5)  # 5-second delay between each game
                else:
                    print("Timeout waiting for color change to", COLOR_WAIT_INPUT)
        else:
            print("Timeout waiting for color change to", COLOR_START_GAME)

if __name__ == '__main__':
    time.sleep(2)
    print("Starting auto-clicker...")
    click_on_color_change()
