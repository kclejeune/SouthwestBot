#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import argv
import pause
import datetime

# query for flight info
confirmation_code = input("Confirmation Code: ")
first_name = input("First Name: ")
last_name = input("Last Name: ")
flight_date = datetime.datetime.strptime(
    input("Flight Date/Time\n(dd/mm/yy 24hr:min): "), "%m/%d/%y %H:%M")
check_in_date = flight_date - datetime.timedelta(days=1)
print(check_in_date)
print("Check in will begin at", check_in_date)

# wait until 1 minute before
pause.until(check_in_date - datetime.timedelta(minutes=1))

# browser setup
if len(argv) > 1:
    # configure custom chromedriver path with command line arg
    chromedriver = argv[1]
else:
    chromedriver = "chromedriver"

driver = webdriver.Chrome(chromedriver)
url = "https://www.southwest.com/air/check-in/"

# navigate to the check in page
driver.get(url)

# fill in user info
driver.find_element_by_id("confirmationNumber").send_keys(confirmation_code)
driver.find_element_by_id("passengerFirstName").send_keys(first_name)
driver.find_element_by_id("passengerLastName").send_keys(last_name)

# find the submit button
submit = driver.find_element_by_id("form-mixin--submit-button")

# wait until the check in time to click the button, click until the button disappears
pause.until(check_in_date)
while EC.presence_of_element_located((By.ID, "confirmationNumber")):
    try:
        submit.click()
    except:
        continue

# attempt to find nonexistent elements from checkin page to verify that the new page has been loaded
try:
    driver.find_element_by_id("confirmationNumber")
    driver.find_element_by_id("passengerFirstName")
    driver.find_element_by_id("passengerLastName")
    print("Check in failed. Please try again manually.")
except ValueError:
    print("Successful Check In!")
