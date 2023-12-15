import cv2
import pyautogui
import numpy as np

# Define exact RGB values for each stage
COLOR_START_GAME = (43, 135, 209)  # Bluish hue color
COLOR_WAIT_INPUT = (206, 38, 54)   # Red color
COLOR_WAIT_CLICK = (75, 219, 106)  # Green color

def detect_color(image, color):
    pixel = image[0, 0]
    return (pixel[2], pixel[1], pixel[0]) == color  # OpenCV stores color channels as BGR

def click_on_color_change():
    cycles = 0
    while cycles < 5:
        while True:
            mouse_x, mouse_y = pyautogui.position()
            screenshot = pyautogui.screenshot(region=(mouse_x - 1, mouse_y - 1, 3, 3))  # Adjust the region as needed
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            if detect_color(screenshot, COLOR_START_GAME):
                print("Detected Bluish hue color. Starting the game...")
                pyautogui.click()  # Click to start the game
                print("Click initiated.")

                screenshot = pyautogui.screenshot(region=(mouse_x - 1, mouse_y - 1, 3, 3))
                screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                if detect_color(screenshot, COLOR_WAIT_INPUT):
                    print("Detected Red color. Waiting for the Green color to click...")
                    while True:
                        screenshot = pyautogui.screenshot(region=(mouse_x - 1, mouse_y - 1, 3, 3))
                        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                        if detect_color(screenshot, COLOR_WAIT_CLICK):
                            print("Detected Green color. Clicking...")
                            pyautogui.click()  # Click when color changes to COLOR_WAIT_CLICK
                            print("Click initiated for Green color.")
                            break

                        # Continue checking for Green color

                    break  # Break the inner loop to restart the game cycle

            # Continue checking for Bluish hue color

        cycles += 1
        print(f"Completed {cycles} game cycles.")

if __name__ == '__main__':
    print("Starting auto-clicker...")
    click_on_color_change()
