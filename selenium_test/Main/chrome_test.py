"""
Test Steps:
1. Open Chrome Browser
2. Navigate to www.google.com
3. Maximize the browser windoww
4. Enter LinkedIn login in Google Text Field
5. Hit Enter key
6. Click on LinkedIn login URL
7. Enter Username and Password
8. Click on Login Button
9. Verify the Title of the page
10. Verify the current URL of the page
11. Close the browser

Expected Result:
1. Chrome browser should be launched successfully
2. Google Webpage should be opened
3. Browser window should be entered
4. Correct text should be entered
5. Search page should show proper result
6. LinkedIn login pageg should appear
7. Username and Password should be accepted
8. LinkedIn homepage should be displayed
9. LinkedIn should be displayed in the console
10. https://www.linkedin.com/feed/ should be displayed in the console
11. Browser window should be closed
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-loggingg"])

print("test is starting")
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
driver.maximize_window()
sleep(5)

driver.find_element(By.NAME, "q").send_keys("LinkedIn Login")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
driver.find_element(By.PARTIAL_LINK_TEXT, "LinkedIn Login").click()