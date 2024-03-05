from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
webDriver = webdriver.Chrome()

# Navigate to the login page
webDriver.get("http://20.86.139.239:8057/#/auth/login?returnUrl=%2F")

# Find the username input field by name
username_input = webDriver.find_element(By.NAME, "username")
# Find the password input field by name
password_input = webDriver.find_element(By.NAME, "password")

# Enter username and password
username_input.send_keys("ikem")
password_input.send_keys("ikemefuna2001")

# Find the login button by class name and click it
login_button = webDriver.find_element(By.CLASS_NAME, "login100-form-btn")
login_button.click()

# webDriver.get("http://20.86.139.239:8057/#/sales/salescustomerstatement-report")

# Wait for a specific element to appear indicating successful login
try:
    WebDriverWait(webDriver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))
    print("Login successful!")
except:
    print("Login failed!")

# Close the browser
webDriver.quit()