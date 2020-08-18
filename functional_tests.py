from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        
        self.browser.get('http://localhost:8000')
        elements = self.browser.find_elements()
        print('elements')
        print(elements)

        
        self.assertIn('blog', self.browser.title)  
        #click on cv link
        link = self.browser.find_element_by_link_text('CV')
        link.click()
        #user taken to cv page

        elements = self.browser.find_elements(By.TAG_NAME, 'p')

        for e in elements:
            print(e.text)
        #return home
        link = self.browser.find_element_by_link_text('Django Girls Blog')
        link.click()
        
 

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  