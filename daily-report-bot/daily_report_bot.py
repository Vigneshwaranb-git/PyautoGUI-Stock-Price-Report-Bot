import pyautogui
import pyperclip
import time
import re
from datetime import datetime


# ============================================================
# SETTINGS
# ============================================================

STOCK_NAME = "Reliance Industries"

STOCK_URL = (
    "https://www.google.com/finance/quote/"
    "RELIANCE:NSE?hl=en"
)


# ============================================================
# PYAUTOGUI SETTINGS
# ============================================================

# Move mouse to top-left corner to stop automation
pyautogui.FAILSAFE = True

# Small pause after every PyAutoGUI operation
pyautogui.PAUSE = 0.5


# ============================================================
# DATE AND TIME
# ============================================================

now = datetime.now()

date_time = now.strftime(
    "%Y-%m-%d %H:%M:%S"
)

today = now.strftime(
    "%Y-%m-%d"
)

filename = (
    f"daily_report_{today}.xlsx"
)


print("========================================")
print("DAILY STOCK STATUS REPORT")
print("========================================")

print(
    f"Date & Time : {date_time}"
)

print(
    f"Stock       : {STOCK_NAME}"
)

print(
    f"File        : {filename}"
)


# ============================================================
# STEP 1 - OPEN CHROME
# ============================================================

print()
print("Opening Chrome...")

pyautogui.hotkey(
    "win",
    "s"
)

time.sleep(1)

pyautogui.write(
    "chrome",
    interval=0.1
)

time.sleep(1)

pyautogui.press(
    "enter"
)

time.sleep(4)


# ============================================================
# STEP 2 - OPEN GOOGLE FINANCE
# ============================================================

print(
    "Opening Google Finance..."
)

pyautogui.hotkey(
    "ctrl",
    "l"
)

pyautogui.write(
    STOCK_URL,
    interval=0.03
)

pyautogui.press(
    "enter"
)

# Wait for Google Finance
time.sleep(7)


# ============================================================
# STEP 3 - COPY PAGE INFORMATION
# ============================================================

print(
    "Reading stock information..."
)

# Click somewhere on the page
pyautogui.click(
    800,
    400
)

time.sleep(1)

# Select all visible page text
pyautogui.hotkey(
    "ctrl",
    "a"
)

time.sleep(0.5)

# Copy
pyautogui.hotkey(
    "ctrl",
    "c"
)

time.sleep(1)


# ============================================================
# STEP 4 - READ CLIPBOARD
# ============================================================

page_text = pyperclip.paste().strip()

print()
print("Copied stock page information:")
print("----------------------------------------")
print(page_text[:2000])
print("----------------------------------------")


# ============================================================
# STEP 5 - EXTRACT STOCK PRICE
# ============================================================

# Look for Indian Rupee price.
#
# Examples:
#
# ₹1,425.50
# ₹2,938.40
# ₹1,234
#
price_pattern = r"₹\s*[\d,]+(?:\.\d+)?"

prices = re.findall(
    price_pattern,
    page_text
)


if prices:

    # The first matching rupee value is treated
    # as the current displayed stock price.
    stock_price = prices[0]

else:

    stock_price = "Price not found"


print()
print(
    f"Stock Price: {stock_price}"
)


# ============================================================
# STEP 6 - CREATE COMMENT
# ============================================================

# Look for percentage movement.
#
# Examples:
# +1.25%
# -0.84%
# 0.52%

percentage_pattern = (
    r"([+-]?\d+(?:\.\d+)?)\s*%"
)

percentage_matches = re.findall(
    percentage_pattern,
    page_text
)


if percentage_matches:

    try:

        change_percentage = float(
            percentage_matches[0]
        )

    except ValueError:

        change_percentage = 0

else:

    change_percentage = 0


# ============================================================
# CREATE COMMENT
# ============================================================

if change_percentage > 1:

    comment = (
        "Stock is showing a positive movement"
    )

elif change_percentage > 0:

    comment = (
        "Stock is slightly positive"
    )

elif change_percentage < -1:

    comment = (
        "Stock is showing a negative movement"
    )

elif change_percentage < 0:

    comment = (
        "Stock is slightly negative"
    )

else:

    comment = (
        "Stock movement is relatively stable"
    )


print(
    f"Comment: {comment}"
)


# ============================================================
# STEP 7 - OPEN MICROSOFT EXCEL
# ============================================================

print()
print(
    "Opening Microsoft Excel..."
)

pyautogui.hotkey(
    "win",
    "s"
)

time.sleep(1)

pyautogui.write(
    "Excel",
    interval=0.1
)

time.sleep(1)

pyautogui.press(
    "enter"
)

# Wait for Excel
time.sleep(6)


# ============================================================
# STEP 8 - CREATE NEW EXCEL WORKBOOK
# ============================================================

print("Creating new Excel workbook...")

pyautogui.hotkey( "ctrl", "n")
time.sleep(3)
pyautogui.click(250, 250) 
time.sleep(3)

print("Blank workbook should now be open...")



# ============================================================
# STEP 9 - ENTER HEADERS
# ============================================================

print(
    "Entering report..."
)

# Select A1
pyautogui.click(
    150,
    150
)


# Header 1
pyautogui.write(
    "Date & Time"
)

pyautogui.press(
    "tab"
)


# Header 2
pyautogui.write(
    "Stock Price"
)

pyautogui.press(
    "tab"
)


# Header 3
pyautogui.write(
    "Comment"
)

pyautogui.press(
    "enter"
)


# ============================================================
# STEP 10 - ENTER DATA
# ============================================================

# Date & Time
pyautogui.write(
    date_time
)

pyautogui.press(
    "tab"
)


# Stock Price
pyautogui.write(
    stock_price
)

pyautogui.press(
    "tab"
)


# Comment
pyautogui.write(
    comment
)

pyautogui.press(
    "tab"
)

# ============================================================
# STEP 11 - SAVE EXCEL FILE
# ============================================================

print()
print(
    f"Saving report as {filename}..."
)

pyautogui.hotkey(
    "ctrl",
    "s"
)

time.sleep(4)


# ============================================================
# STEP 12 - ENTER FILE NAME
# ============================================================

print("Entering filename in Save As dialog...")

pyautogui.hotkey(
    "ctrl",
    "a"
)

time.sleep(1)

pyautogui.write(
    filename,
    interval=0.05
)

time.sleep(1)

pyautogui.press(
    "enter"
)

time.sleep(5)


# ============================================================
# STEP 13 - HANDLE POSSIBLE CONFIRMATION
# ============================================================

print("Checking Excel confirmation...")

pyautogui.press(
    "enter"
)

time.sleep(3)


# ============================================================
# COMPLETED
# ============================================================

print()
print("========================================")
print("DAILY REPORT COMPLETED")
print("========================================")

print(
    f"Date & Time : {date_time}"
)

print(
    f"Stock       : {STOCK_NAME}"
)

print(
    f"Price       : {stock_price}"
)

print(
    f"Comment     : {comment}"
)

print(
    f"File        : {filename}"
)

print()
print(
    "Report saved successfully."
)
