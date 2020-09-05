from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_edit(self):
        self.browser.get('http://localhost:8000')
        #user clicks on cv link
        link = self.browser.find_element_by_link_text('CV')
        link.click()
        #
        time.sleep(15)
        #user clicks on edit button
        edit_button = self.browser.find_elements_by_xpath("//a[@class='btn btn-default pull-right' and @href = '/cv/edit/']")[0]
        edit_button.click()
        time.sleep(2)
        #user selects text area labeld 'other'
        textarea = self.browser.find_element_by_xpath("//p//textarea[@name='other']")
        textarea.click()
        #store original text so can it can be restored after test
        tmp = textarea.get_attribute('value')
        print(tmp)
        textarea.clear()
        #user inputs their text and saves it
        textarea.send_keys("test")

        save_button = self.browser.find_element_by_xpath("//form//button[@type='submit']")
        save_button.click()

        #on the view cv page the 'other' field should now appear as 'Other: test'
        #in the list of elements in the cv 'other' field is index 9
        elements = self.browser.find_elements(By.TAG_NAME, 'p')
        for i in elements:
        	print(i.text)
        self.assertEquals(elements[9].text, 'Other: test')
        
        #reutrn other field to original value
        edit_button = self.browser.find_elements_by_xpath("//a[@class='btn btn-default pull-right' and @href = '/cv/edit/']")[0]
        edit_button.click()
        time.sleep(2)
        textarea = self.browser.find_element_by_xpath("//p//textarea[@name='other']")
        textarea.click()
        textarea.clear()
        textarea.send_keys(tmp)

        save_button = self.browser.find_element_by_xpath("//form//button[@type='submit']")
        save_button.click()
        

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