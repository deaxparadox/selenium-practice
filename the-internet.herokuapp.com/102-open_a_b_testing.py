from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "http://the-internet.herokuapp.com/"

driver = webdriver.Firefox()
driver.get(URL)


links = driver.find_elements(By.TAG_NAME, 'a')

for a in links:
    if a.text == "A/B Testing":
        a.click()
        break



driver.close()
exit(0)