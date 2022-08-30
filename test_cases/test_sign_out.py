import os
import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from pages.add_player_page import AddPlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.base_page import assert_element_text
from pages.dashboard import Dashboard

import time


class TestSignOut(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sign_out(self):
        user_login = LoginPage(self.driver)
        user_login.correct_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        dashboard.click_on_the_sign_out_button()
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()

