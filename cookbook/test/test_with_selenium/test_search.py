from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome('cookbook/test/test_with_selenium/chromedriver')
        super(LoginTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTest, self).tearDown()

    def test_search_cannot_find(self):
        selenium = self.selenium
        selenium.get('http://whole-food-cookbook.herokuapp.com/profile')
        assert "You haven't login yet" in selenium.page_source
        search_input = selenium.find_element_by_id('myInput')
        submit = selenium.find_element_by_class_name('menu-but-search')
        search_input.send_keys("tester")
        submit.send_keys(Keys.RETURN)
        assert "Searching for \"tester\"" in selenium.page_source
        assert "There are no Recipe match to your search here" in selenium.page_source
        assert "search/tester" in selenium.current_url

    def test_search_finded(self):
        selenium = self.selenium
        selenium.get('http://whole-food-cookbook.herokuapp.com/profile')
        assert "You haven't login yet" in selenium.page_source
        search_input = selenium.find_element_by_id('myInput')
        submit = selenium.find_element_by_class_name('menu-but-search')
        search_input.send_keys("ches")
        submit.send_keys(Keys.RETURN)
        assert "Searching for \"ches\"" in selenium.page_source
        assert "Recipe name matched" in selenium.page_source
        assert '<a href="/recipe/Balsamic%20Grilled%20Steak%20Salad%20with%20Peaches" class="list-group-item ' \
               'list-group-item-action bigA">Balsamic Grilled Steak Salad with Peaches</a>' in selenium.page_source
        assert "search/ches" in selenium.current_url
        big_a = selenium.find_element_by_class_name('bigA')
        big_a.send_keys(Keys.RETURN)
        assert 'Balsamic Grilled Steak Salad with Peaches' in selenium.page_source
