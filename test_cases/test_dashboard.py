import os
import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.dashboard import Dashboard

import time


class TestDashboardButtons(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_players_button(self):
        user_login = LoginPage(self.driver)
        user_login.correct_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        players_button = Dashboard(self.driver)
        players_button.click_players_button()
        players_button.wait_for_presence_of_players_title_located()
        players_button.check_title_of_players_page_starts_with()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()

        pass