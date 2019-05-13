from selenium.webdriver.common.by import By
from base_page_object import BasePage


class GoogleHomePage(BasePage):

    def __init__(self, contex):
        BasePage.__init__(
            self,
            contex.browser,
            base_url='https://google.com')

    locator_dictionary = {
        "search_box": (By.ID, 'search-input-location'),
        "search_button:": (By.ID, "search-submit")
    }
    
    def type_search(self, word):
        print(word)
        self.search_box.send_keys(word)
