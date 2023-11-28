from selenium.webdriver.common.by import By

def find_all_by_class(driver, class_name):
    tags = driver.find_elements(By.CLASS_NAME, class_name)
    print(tags)
    for t in tags:
        print(t)