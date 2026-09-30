from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import Workbook

import time


# ============================================================
# SETTINGS
# ============================================================

AMAZON_URL = "https://www.amazon.in/gp/bestsellers/"

EXCEL_FILE = "amazon_products.xlsx"

MAX_PRODUCTS = 100

SCROLL_PAUSE = 2

# Number of times we can scroll without finding
# a new product before stopping
MAX_NO_NEW_PRODUCTS = 2


# ============================================================
# SELENIUM - OPEN CHROME
# ============================================================

print("Opening Chrome...")

options = Options()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    options=options
)


# ============================================================
# OPEN AMAZON
# ============================================================

print("Opening Amazon Best Sellers...")

driver.get(
    AMAZON_URL
)


# ============================================================
# WAIT FOR PAGE
# ============================================================

wait = WebDriverWait(
    driver,
    15
)


try:

    wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "div.p13n-sc-truncate-desktop-type2.p13n-sc-truncated"
            )
        )
    )

except Exception as e:

    print("Product titles were not found.")

    print(e)

    driver.quit()

    exit()


print("Amazon page loaded.")


# ============================================================
# CREATE EXCEL
# ============================================================

workbook = Workbook()

sheet = workbook.active

sheet.title = "Amazon Products"

sheet["A1"] = "S.No"
sheet["B1"] = "Category"
sheet["C1"] = "Product Name"


# ============================================================
# PRODUCT STORAGE
# ============================================================

products = []

seen_products = set()


# ============================================================
# FUNCTION: GET PRODUCT TITLES
# ============================================================

def get_products():

    elements = driver.find_elements(
        By.CSS_SELECTOR,
        "div.p13n-sc-truncate-desktop-type2.p13n-sc-truncated"
    )

    new_products = []

    for element in elements:

        try:

            # Get complete product title
            product_name = element.get_attribute(
                "title"
            )

            # Fallback
            if not product_name:

                product_name = element.get_attribute(
                    "aria-label"
                )

            if product_name:

                product_name = " ".join(
                    product_name.split()
                ).strip()

            # Ignore duplicates
            if (
                product_name
                and product_name not in seen_products
            ):

                seen_products.add(
                    product_name
                )

                new_products.append(
                    product_name
                )

        except Exception:

            continue

    return new_products


# ============================================================
# COLLECT PRODUCTS
# ============================================================

print()
print("========================================")
print("Searching bestseller product titles")
print("========================================")


no_new_products_count = 0


while len(products) < MAX_PRODUCTS:

    # --------------------------------------------------------
    # Search product titles
    # --------------------------------------------------------

    new_products = get_products()


    # --------------------------------------------------------
    # NEW PRODUCTS FOUND
    # --------------------------------------------------------

    if new_products:

        no_new_products_count = 0

        print()
        print(
            f"Found {len(new_products)} new product(s)."
        )


        for product in new_products:

            if len(products) >= MAX_PRODUCTS:

                break

            products.append(
                product
            )

            print(
                f"{len(products)}. {product}"
            )


    # --------------------------------------------------------
    # NO NEW PRODUCTS FOUND
    # --------------------------------------------------------

    else:

        no_new_products_count += 1

        print()
        print(
            "No new product titles found."
        )

        print(
            f"Check {no_new_products_count}/"
            f"{MAX_NO_NEW_PRODUCTS}"
        )


        # ----------------------------------------------------
        # If no new products are found repeatedly,
        # assume bestseller product search has ended.
        # ----------------------------------------------------

        if (
            no_new_products_count
            >= MAX_NO_NEW_PRODUCTS
        ):

            print()
            print(
                "========================================"
            )

            print(
                "Bestseller product title search ended."
            )

            print(
                "Stopping scroll."
            )

            print(
                "Proceeding to next step..."
            )

            print(
                "========================================"
            )

            break


    # --------------------------------------------------------
    # Maximum products reached
    # --------------------------------------------------------

    if len(products) >= MAX_PRODUCTS:

        print()
        print(
            "Maximum product limit reached."
        )

        break


    # --------------------------------------------------------
    # Check if page is already at bottom
    # --------------------------------------------------------

    current_position = driver.execute_script(
        "return window.pageYOffset;"
    )

    page_height = driver.execute_script(
        "return document.body.scrollHeight;"
    )

    window_height = driver.execute_script(
        "return window.innerHeight;"
    )


    if (
        current_position + window_height
        >= page_height - 10
    ):

        print()
        print(
            "Reached the bottom of the page."
        )

        print(
            "No more products to search."
        )

        break


    # --------------------------------------------------------
    # Scroll down
    # --------------------------------------------------------

    print()
    print(
        "Scrolling for more bestseller products..."
    )


    driver.execute_script(
        "window.scrollBy(0, 700);"
    )


    time.sleep(
        SCROLL_PAUSE
    )


# ============================================================
# WRITE PRODUCTS TO EXCEL
# ============================================================

print()
print(
    "Writing products to Excel..."
)


for index, product in enumerate(
    products,
    start=1
):

    sheet.cell(
        row=index + 1,
        column=1
    ).value = index

    sheet.cell(
        row=index + 1,
        column=2
    ).value = "Amazon Best Sellers"

    sheet.cell(
        row=index + 1,
        column=3
    ).value = product


# ============================================================
# EXCEL FORMATTING
# ============================================================

sheet.column_dimensions[
    "A"
].width = 10

sheet.column_dimensions[
    "B"
].width = 30

sheet.column_dimensions[
    "C"
].width = 100


for row in sheet.iter_rows():

    for cell in row:

        cell.alignment = cell.alignment.copy(
            wrap_text=True
        )


# ============================================================
# SAVE EXCEL
# ============================================================

workbook.save(
    EXCEL_FILE
)


# ============================================================
# NEXT STEP
# ============================================================

print()
print("========================================")
print("PRODUCT COLLECTION COMPLETED")
print("========================================")

print(
    f"Total products collected: {len(products)}"
)

print(
    f"Excel file: {EXCEL_FILE}"
)

print()
print(
    "Proceeding to the next step..."
)


# ============================================================
# YOUR NEXT AUTOMATION STEP GOES HERE
# ============================================================

# Example:
#
# next_step()
#
# or
#
# driver.get("https://some-other-page.com")


# ============================================================
# KEEP CHROME OPEN
# ============================================================

input(
    "\nPress ENTER to close Chrome..."
)

driver.quit()