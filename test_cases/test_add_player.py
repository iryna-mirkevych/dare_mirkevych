import os
import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from pages.add_player_page import AddPlayerPage
from pages.edit_player_page import EditPlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.edit_player_page import EditPlayerPage

import time


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        # login
        user_login = LoginPage(self.driver)
        user_login.correct_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        add_player_link = Dashboard(self.driver)
        add_player_link.click_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.assert_title_of_add_player_page()
        add_player_page.type_in_name("Ivan")
        add_player_page.type_in_surname("Ivanenko")
        add_player_page.type_in_age("12.12.2022")
        add_player_page.type_in_main_position("goalkeeper")
        add_player_page.click_on_the_submit_button()
        # checking that the edit player page opens successfully
        # we wait for the page to load
        edit_player_page = EditPlayerPage(self.driver)
        edit_player_page.wait_for_presence_of_edit_page_title_located() #time.sleep(7)
        edit_player_page.check_title_starts_with()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()

        pass