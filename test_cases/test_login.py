import os
import unittest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.dashboard import Dashboard

import time


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_correct_login(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()
        #user_login.assert_panel_title(user_login.expected_panel_title)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()

    # def test_panel_title(self):
    #     panel_title = LoginPage(self.driver)
    #     panel_title.assert_panel_title(panel_title.expected_panel_title)
    #     time.sleep(1)

    def test_password_validation(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.click_on_the_sign_in_button()
        user_login.assert_password_validation_text(user_login.password_validation_text)
        user_login.title_of_login_page()
        time.sleep(3)

    def test_sign_out(self):
        #user_login = LoginPage(self.driver)
        #user_login.correct_login()   #correct_login method can be used instead of test_correct_login
        user_login = TestLoginPage()
        user_login.test_correct_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        dashboard.click_on_the_sign_out_button()
        time.sleep(3)
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()

    def test_remind_password(self):
        remind_password = LoginPage(self.driver)
        remind_password.click_remind_password_hyperlink()
        time.sleep(3)
        #remind_password.assert_title_of_remind_password_page()
        remind_password.click_remind_password_page_send_button()
        time.sleep(7)
        remind_password.back_to_sign_in_text_is_not_present("Back to sign in")
        # need assertion here to check the validation message for non-providing email
        # let's presume "Back to sign in" message should not already be there,
        # should be changed to some other (e.g. "Please provide your email").
        # an AssertionError at assert_element_text_is_not is expected (because "Back to sign in" is there,
        # but should not be there anymore, something like "Please provide your email" should be there,
        # based on structure of this site (other validation messages appear in the same place).

    @classmethod
    def tearDown(self):
        self.driver.quit()

