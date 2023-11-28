import os
import sys

sys.path.append("D:\Github\selenium_practice")

try:
    import helpers.find as find
except Exception as e:
    print(e)
    exit(1)

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "http://the-internet.herokuapp.com/"

driver = webdriver.Firefox()
driver.get(URL)
assert "The Internet" in driver.title


def find_all_by_class(driver, class_name):
    tags = driver.find_elements(By.CLASS_NAME, class_name)
    # print(tags)
    for t in tags:
        print(t.text)
        
try:
    find_all_by_class(driver, 'heading')
except Exception as e:
    print(e)

driver.close()
exit(0)