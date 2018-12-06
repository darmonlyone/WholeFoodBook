import os
from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver


class LoginTest(LiveServerTestCase):

    def setUp(self):
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER = os.path.join(PROJECT_ROOT, "chromedriver")
        self.selenium = webdriver.Chrome(executable_path='/home/travis/chromedriver')
        super(LoginTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTest, self).tearDown()

    def test_login_github(self):
        selenium = self.selenium
        selenium.get('http://whole-food-cookbook.herokuapp.com/login')
        github_button = selenium.find_element_by_class_name('btn-dark')
        github_button.click()
        sleep(5)
        assert 'GitHub' in selenium.page_source
        assert 'https://github.com/' in selenium.current_url

    def test_login_google(self):
        selenium = self.selenium
        selenium.get('http://whole-food-cookbook.herokuapp.com/login')
        google_button = selenium.find_element_by_class_name('btn-danger')
        google_button.click()
        sleep(5)
        assert 'Google' in selenium.page_source
        assert 'https://accounts.google.com' in selenium.current_url
