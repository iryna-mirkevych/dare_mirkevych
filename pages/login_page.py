from pages.base_page import BasePage, assert_element_text
from selenium import webdriver


class LoginPage(BasePage):
    scouts_panel_title_xpath = "//form/div/div[1]/h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_hyperlink_xpath = "//child::div/a"
    language_menu_button_xpath = "//div[contains(@class,'selectMenu')]"
    language_menu_icon_xpath = "//*[@d = 'M7 10l5 5 5-5z']"
    sign_in_button_xpath = "//*[@type='submit']"
    username_e_mail_validation_span_xpath = "//*[text()='Please provide your username or your e-mail.']"
    password_validation_span_xpath = "//*[text()='Please provide your password.']"
    expected_panel_title = "Scouts Panel"
    expected_title = "Scouts panel - sign in"
    login_url = ("https://scouts-test.futbolkolektyw.pl/login")

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def assert_panel_title(self, expected_panel_title):
        assert_element_text(self.driver, self.scouts_panel_title_xpath, expected_panel_title)

