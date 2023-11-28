from unittest import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# URL = "https://the-internet.herokuapp.com/"

# driver = webdriver.Firefox()
# driver.get(URL)
# assert "The Internet" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

class TestSimpleUsage(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = "https://the-internet.herokuapp.com/"
        try:
            cls.driver = webdriver.Firefox()
        except:
            super().tearDownClass()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
            
    def test_open_page(self):
        self.driver.get(self.url)
        assert "The Internet" in self.driver.title


    def test_find_all_a1_tag(self):
        headings = self.driver.find_elements(By.CLASS_NAME, "heading")
        for h in headings:
            print(h)
            
