

import os
import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.base_page import assert_element_text
from pages.dashboard import Dashboard

import time


class TestPasswordValidation(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_password_validation(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.click_on_the_sign_in_button()
        password_validation_text = LoginPage(self.driver)
        password_validation_text.assert_password_validation_text(password_validation_text.password_validation_text)
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()


