import os
import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from pages.edit_player_page import EditPlayerPage
from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.dashboard import Dashboard

import time


class TestPlayersPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_open_player(self):
        # login
        user_login = LoginPage(self.driver)
        user_login.correct_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        players_button = Dashboard(self.driver)
        players_button.click_players_button()
        players_button.wait_for_presence_of_players_title_located()
        players_button.check_title_of_players_page_starts_with()
        players_data = PlayersPage(self.driver)
        players_data.click_player_table_data()
        time.sleep(3)
        player = EditPlayerPage(self.driver)
        player.check_title_starts_with()

    def test_sort(self):
        user_login = LoginPage(self.driver)
        user_login.correct_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        players_button = Dashboard(self.driver)
        players_button.click_players_button()
        players_button.wait_for_presence_of_players_title_located()
        players_button.check_title_of_players_page_starts_with()
        players_page = PlayersPage(self.driver)
        players_page.click_sort_button()
        players_page.click_reports_input()
        players_page.check_reports_column_not_present()


    @classmethod
    def tearDown(self):
        self.driver.quit()

        pass