import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

# Specify the relative path to the folder within the Downloads directory
download_folder_name = "your_folder_name"
download_dir = os.path.join(os.path.expanduser("~"), "Downloads", download_folder_name)

# Create a new instance of the Chrome driver with specified options
webDriver = webdriver.Chrome()

# Navigate to the login page
webDriver.get("http://20.86.139.239:8057/#/auth/login?returnUrl=%2F")

# Find the username input field by name
username_input = webDriver.find_element(By.NAME, "username")
# Find the password input field by name
password_input = webDriver.find_element(By.NAME, "password")

# Enter username and password
username_input.send_keys("")
password_input.send_keys("")

# Find the login button by class name and click it
login_button = webDriver.find_element(By.CLASS_NAME, "login100-form-btn")
login_button.click()

# Wait for 10 seconds
time.sleep(2)

# Redirect to another URL within the same domain


# List of customers and their associated search parameters
customers = [
    {"name": "Nigerian Brewries", "date_from": "03/01/2023"}
    # {"name": "Customer2", "date_from": "2024-02-01", "date_to": "2024-02-15"},
    # Add more customers as needed
]

for customer in customers:
    webDriver.get("http://20.86.139.239:8057/#/sales/salescustomerstatement-report")

    name_input = webDriver.find_element(By.NAME, "customerCode")

    name_input.clear()
    name_input.send_keys(customer["name"])

    search_input = webDriver.find_element(By.ID, "search")
    search_input.clear()
    time.sleep(5)
    search_input.send_keys(customer["name"])

    time.sleep(5)
    first_record = webDriver.find_element(By.XPATH, "//tr[@class='ng-star-inserted']")
    first_record.click()

    time.sleep(5)
    # Find the input field by its class name
    date_input = webDriver.find_element(By.CLASS_NAME, "ui-inputtext")

    # Clear any existing value in the input field
    date_input.clear()

    # Send the date_from value to the input field
    date_input.send_keys(customer["date_from"])
    time.sleep(5)
    # Select the year
    year_dropdown = Select(webDriver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
    year_dropdown.select_by_visible_text("2023")  # Replace "2023" with the desired year

    # Select the month
    month_dropdown = Select(webDriver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
    month_dropdown.select_by_visible_text("March")  # Replace "March" with the desired month
    time.sleep(5)

    #################
    # Find the first day element of the current month and click it
    webDriver.execute_script("document.querySelector('.ui-datepicker-calendar a.ui-state-default').click();")

    #Preview statement
    preview_statement = webDriver.find_element(By.CLASS_NAME, "pull-right")
    preview_statement.click()
    time.sleep(10)

    # Wait for the PDF link to be clickable
    # Switch to the iframe using JavaScript
    iframe = webDriver.find_element(By.ID, "report")
    webDriver.switch_to.frame(iframe)
    print("Switched to iframe")
    time.sleep(5)
    open_dw = webDriver.find_element(By.ID, "SalesCustomerStatementReport_ctl05_ctl04_ctl00_Button")
    open_dw.click()
    print("button for dw clicked")
    # Find the PDF link using JavaScript
    pdf_link = webDriver.find_element(By.XPATH, "//a[@title='PDF']")
    pdf_link.click()

    time.sleep(5)

    # Specify the download directory as the Downloads folder
    download_dir = os.path.expanduser("~") + "\\Downloads"

    # Get the latest downloaded file in the download directory
    list_of_files = os.listdir(download_dir)
    latest_file = max(list_of_files, key=lambda x: os.path.getmtime(os.path.join(download_dir, x)))

    # Rename the downloaded file
    downloaded_file_path = os.path.join(download_dir, latest_file)
    new_file_path = os.path.join(download_dir, customer["name"] + "StatementSkyward.pdf")  # Adjust the desired filename
    os.rename(downloaded_file_path, new_file_path)
    print("File renamed successfully")

input("Press Enter to close the browser...")

webDriver.quit()
