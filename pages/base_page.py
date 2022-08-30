import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


def assert_element_text(driver, xpath, expected_text):
    element = driver.find_element(by=By.XPATH, value=xpath)
    element_text = element.text
    assert expected_text == element_text


class BasePage():
    sign_out_button_xpath = "//*//div[1]//ul[2]/div[2]"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, locator, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, locator).send_keys(value)

    def click_on_the_element(self, locator, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, locator).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(3)

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def wait_for_presence_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        time.sleep(6)




