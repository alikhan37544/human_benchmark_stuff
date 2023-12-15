'''
This version of the code consistently works and gives output
between 1 second and 2 seconds, at least on my setup. 
The next version aims to improve the performance of the code :)
'''


import pyautogui
import time

# Define color ranges for each stage
COLOR_START_GAME = [(20, 100, 180), (60, 160, 230)]  # Bluish hue range
COLOR_WAIT_INPUT = [(200, 0, 0), (220, 60, 80)]      # Red range
COLOR_WAIT_CLICK = [(50, 190, 90), (100, 255, 130)]  # Green range

def is_color_in_range(color, color_range):
    return all(color[i] >= color_range[0][i] and color[i] <= color_range[1][i] for i in range(3))

def wait_for_color(color_range, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        current_color = pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1])
        if is_color_in_range(current_color, color_range):
            return True
    return False

def click_on_color_change():
    cycles = 0
    while cycles < 5:
        start_time = time.time()
        while True:
            if wait_for_color(COLOR_START_GAME):
                print("Detected Bluish hue color. Starting the game...")
                pyautogui.click()  # Click to start the game
                print("Click initiated.")
                if wait_for_color(COLOR_WAIT_INPUT):
                    print("Detected Red color. Waiting for the Green color to click...")
                    while True:
                        if wait_for_color(COLOR_WAIT_CLICK, timeout=1):
                            print("Detected Green color. Clicking...")
                            pyautogui.click()  # Click when color changes to COLOR_WAIT_CLICK
                            print("Click initiated for Green color.")
                            break
                        else:
                            print("Checking for Green color...")
                    time.sleep(2)  # 2-second delay between each game cycle
                    break  # Break the inner loop to restart the game cycle
            else:
                print("Timeout waiting for Bluish hue color", COLOR_START_GAME)
                break  # Break the inner loop to restart the game cycle
        
        cycles += 1
        print(f"Completed {cycles} game cycles.")
        elapsed_time = time.time() - start_time
        if elapsed_time < 2:
            time.sleep(2 - elapsed_time)  # Adjusting for the remaining time to meet the 2-second delay between cycles

if __name__ == '__main__':
    print("Starting auto-clicker...")
    click_on_color_change()
