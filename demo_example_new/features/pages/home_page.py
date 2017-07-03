from selenium.webdriver.common.by import By
from browser import Browser
from random import randint


class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "term")
    SUBMIT_BUTTON = (By.ID, "submit")
    SO_LOGO = (By.CSS_SELECTOR,"span.-img")
    QUESTION_COUNT = (By.CSS_SELECTOR,"div.summarycount.al")
    PAGE_NEXT = (By.CSS_SELECTOR,"span.page-numbers.next")


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)

    def logo_displayed(self, *locator):
        self.driver.find_element(*HomePageLocator.SO_LOGO).is_displayed()

    def count_displayed(self):
        return print(self.driver.find_element(*HomePageLocator.QUESTION_COUNT).text)

    def add_tag(self,address):
        self.driver.get(address+"/questions/tagged/angular")

    def take_screenshot(self):
        self.driver.get_screenshot_as_file('screenshot'+str(randint(0, 9))+".png")

    def next_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(*HomePageLocator.PAGE_NEXT)



