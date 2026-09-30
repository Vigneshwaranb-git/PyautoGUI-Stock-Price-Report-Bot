import pyautogui
import time
import pyscreeze

# pyautogui.typewrite('Hello, World!', interval=0.1)  # Type 'Hello, World!' with a 0.1 second delay between each character
# time.sleep(2)  # gives you time to focus the target application
# pyautogui.hotkey('cmd', 'c')  # Copy the selected text
# pyautogui.hotkey('cmd', 'v')  # Paste the copied text
# pyautogui.press('enter')  # Press the Enter key
# pyautogui.hotkey('ctrl', 's')  # Save the file (on Windows/Linux)
# pyautogui.hotkey('cmd', 's')  # Save the file (on macOS)
# pyautogui.keyDown('shift')  # Hold down the Shift key

# Screenshot example
screenshot = pyautogui.screenshot()  # Take a screenshot and save it as 'screenshot.png'
screenshot.save('screenshot.png')  # Save the screenshot to a file