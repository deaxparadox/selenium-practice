from selenium import webdriver

def all_window(driver):
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.execute_script("window.close();")
    if len(driver.window_handles) == 1:
        driver.switch_to.window(driver.window_handles[0])
        