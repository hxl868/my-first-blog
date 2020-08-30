from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_view_cv_page(self):  
        
        self.browser.get('http://localhost:8000')
        elements = self.browser.find_elements()

        self.assertIn('blog', self.browser.title)  
        #click on cv link
        link = self.browser.find_element_by_link_text('CV')
        link.click()
        #user taken to cv page
        header_text = self.browser.find_element_by_tag_name('h2').text 
        self.assertIn('cv', header_text)
        elements = self.browser.find_elements(By.TAG_NAME, 'b')

        #all elements of the cv should be shown on the page.
        #elements = self.browser.find_elements(By.TAG_NAME, 'p'
        onpage = []
        expected = ['Name:','Address:','Nationality:','Phonenumber:','Email:','Statement:','Employment history:','Academic achievements:','Interests:','Other:','References:']
        for e in elements:
            #print(e.text)
            onpage.append(e.text)
        #return home
        self.assertListEqual(onpage, expected)

        link = self.browser.find_element_by_link_text('Django Girls Blog')
        link.click()
        
 

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  