from time import sleep

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "http://the-internet.herokuapp.com/"

driver = webdriver.Firefox()
driver.get(URL)

def close_all_windows(driver):
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.execute_script("window.close();")
    if len(driver.window_handles) == 1:
        driver.switch_to.window(driver.window_handles[0])
        

links = driver.find_elements(By.TAG_NAME, 'a')

a_b_links: str|None = None
for a in links:
    if a.text == "A/B Testing":
        a_b_links = a.get_attribute("href")
        break

current_tab = driver.current_window_handle
driver.switch_to.new_window("tab")
# driver.swi
driver.get(a_b_links)

# sleep(3)
close_all_windows(driver)


driver.close()
exit(0)