import os

from django.test import LiveServerTestCase
from selenium import webdriver


class WelcomeTest(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        super(WelcomeTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(WelcomeTest, self).tearDown()

    def test_welcome(self):
        selenium = self.selenium
        selenium.get('http://whole-food-cookbook.herokuapp.com/')
        welcome_text = selenium.find_element_by_class_name('welcome-text')
        self.assertIn("Welcome", welcome_text.text)

        welcome_button = selenium.find_element_by_id('welcome-but-start')
        welcome_button.click()
        assert "Welcome to \"Organic Recipe\"" in selenium.page_source
