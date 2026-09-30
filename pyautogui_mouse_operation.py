import pyautogui
import time

# Mouse operations
# pyautogui.moveTo(500, 500, duration=1)  # Move the mouse to (500, 500) over 1 second
# pyautogui.click(500, 500)  # Click at (500, 500)
# pyautogui.doubleClick(500, 500)  # Double click at (500, 500)
# pyautogui.rightClick(500, 500)  # Right click at (500, 500)
# pyautogui.leftClick(500, 500)  # Left click at (500, 500)
# pyautogui.middleClick(500, 500)  # Middle click at (500, 500)
# pyautogui.scroll(10)  # Scroll up 10 units 
time.sleep(3)
pyautogui.scroll(-500)
time.sleep(1)
pyautogui.scroll(500)