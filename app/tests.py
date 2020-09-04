from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(executable_path="A:\\chromedriver_win32\\chromedriver.exe")
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_showIndex(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('https://seleniumtesting1.herokuapp.com/index/')
        #find the form element
        first_name = selenium.find_element_by_id('id_fname')
        last_name = selenium.find_element_by_id('id_lname')
        phone_number = selenium.find_element_by_id('id_pnumber')

        submit = selenium.find_element_by_name('welcome')

        #Fill the form with data
        first_name.send_keys('mounika')
        last_name.send_keys('k')
        phone_number.send_keys('1234567890')

        #submitting the form
        submit.send_keys(Keys.RETURN)

