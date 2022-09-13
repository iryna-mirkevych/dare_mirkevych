import os
import unittest

from selenium import webdriver

from pages.edit_player_page import EditPlayerPage
from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.dashboard import Dashboard

import time


class TestPlayersPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_open_player(self):
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

    def test_view_columns(self):
        user_login = LoginPage(self.driver)
        user_login.correct_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        players_button = Dashboard(self.driver)
        players_button.click_players_button()
        players_button.wait_for_presence_of_players_title_located()
        players_button.check_title_of_players_page_starts_with()
        players_page = PlayersPage(self.driver)
        players_page.click_view_columns_button()
        players_page.click_reports_input()
        players_page.check_reports_column_not_present()

    def test_add_match_button(self): #error expected (404 page)
        add_match = TestPlayersPage()
        add_match.test_open_player()
        add_match = EditPlayerPage(self.driver)
        add_match.click_matches_button()
        time.sleep(3)
        add_match.click_add_match_button()
        time.sleep(3)
        add_match.assert_adding_match_page_title_starts_with()

    def test_add_report_button(self): #error expected (Matches page is opened, not Adding Report page)
        add_report = TestPlayersPage()
        add_report.test_open_player()
        add_report = EditPlayerPage(self.driver)
        add_report.click_reports_button()
        time.sleep(3)
        add_report.click_add_report_button()
        time.sleep(3)
        add_report.assert_adding_report_page_title_starts_with()

    @classmethod
    def tearDown(self):
        self.driver.quit()

        pass
