import os
from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest(LiveServerTestCase):

    def setUp(self):
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER = os.path.join(PROJECT_ROOT, "chromedriver")
        self.selenium = webdriver.Chrome(executable_path=DRIVER)
        super(LoginTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTest, self).tearDown()

    def test(self):
        selenium = self.selenium
        selenium.get('http://whole-food-cookbook.herokuapp.com/')
        welcome_text = selenium.find_element_by_class_name('welcome-text')
        self.assertIn("Welcome", welcome_text.text)
        welcome_button = selenium.find_element_by_id('welcome-but-start')
        welcome_button.click()
        assert "Welcome to \"Organic Recipe\"" in selenium.page_source
        assert "OR" in selenium.page_source
        continue_button = selenium.find_element_by_id('continue-login-button')
        continue_button.click()
        search_input = selenium.find_element_by_id('myInput')
        submit = selenium.find_element_by_class_name('menu-but-search')
        search_input.send_keys("let find something")
        submit.send_keys(Keys.RETURN)
        assert "Searching for \"let find something\"" in selenium.page_source
        assert "There are no Recipe match to your search here" in selenium.page_source
        assert "search/let" in selenium.current_url
        search_input = selenium.find_element_by_id('myInput')
        submit = selenium.find_element_by_class_name('menu-but-search')
        search_input.send_keys("fi")
        submit.send_keys(Keys.RETURN)
        sleep(5)
        assert 'SUGGESTION' in selenium.page_source
        assert "Searching for \"fi\"" in selenium.page_source
        assert "Recipe name matched" in selenium.page_source
        assert '<a href="/recipe/Breakfast%20Egg%20Muffins" class="list-group-item list-group-item-action ' \
               'bigA">Breakfast Egg Muffins</a>' in selenium.page_source
        assert '<a href="/recipe/Almond%20Flour%20Banana%20Muffins" class="list-group-item list-group-item-action ' \
               'bigA">Almond Flour Banana Muffins</a>' in selenium.page_source
        assert "search/fi" in selenium.current_url
        big_a = selenium.find_elements_by_class_name('bigA')
        big_a[0].send_keys(Keys.RETURN)
        assert 'Breakfast Egg Muffins' in selenium.page_source
        assert 'SUGGESTION' in selenium.page_source
        sleep(5)
        carousel__box = selenium.find_element_by_class_name('suggestion')
        a_suggestion = carousel__box.find_elements_by_tag_name('a')
        a_suggestion[0].send_keys(Keys.RETURN)
        assert "Organic Recipe" in selenium.page_source
        sleep(5)
        navbar = selenium.find_element_by_class_name('navbar')
        a_main = navbar.find_elements_by_tag_name('a')
        a_main[0].send_keys(Keys.RETURN)
        assert "index" in selenium.current_url
