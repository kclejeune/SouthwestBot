import pause
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime

# query for flight info
confirmation_code = input("Confirmation Code: ")
first_name = input("First Name: ")
last_name = input("Last Name: ")
check_in_date = datetime.datetime.strptime(input("Check in date/time\n(dd/mm/yyyy hr:min): "), "%m/%d/%Y %H:%M")


# initial browser setup
chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver)
url = "https://www.southwest.com/air/check-in/"


# wait until 1 minute before 
pause.until(check_in_date - datetime.timedelta(minutes=1))

# navigate to the check in page
driver.get(url)

# fill in user info
driver.find_element_by_id("confirmationNumber").send_keys(confirmation_code)
driver.find_element_by_id("passengerFirstName").send_keys(first_name)
driver.find_element_by_id("passengerLastName").send_keys(last_name)

# locate submit button
submit = driver.find_element_by_id("form-mixin--submit-button")

# wait until the check in time to click the button
pause.until(check_in_date)
submit.click()
print("Successful Check In!")