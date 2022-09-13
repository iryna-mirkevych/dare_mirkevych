from pages.base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    scouts_panel_title_xpath = "//form/div/div[1]/h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    language_menu_button_xpath = "//div[contains(@class,'selectMenu')]"
    language_menu_icon_xpath = "//*[@d = 'M7 10l5 5 5-5z']"
    sign_in_button_xpath = "//*[@type='submit']"
    # Prod
    # expected_panel_title = "PANEL SKAUTINGOWY"
    # Test
    expected_panel_title = "Scouts Panel"
    expected_title = "Scouts panel - sign in"
    login_url = ("https://scouts.futbolkolektyw.pl/en")
    # Test url
    #login_url = ("https://scouts-test.futbolkolektyw.pl/login")
    validation_span_xpath = "//form//div[1]/div[3]/span"
    email_validation_text = "Please provide your username or your e-mail."
    password_validation_text = "Please provide your password."
    password_validation_fragment = "password"
    remind_password_page_url = ("https://scouts.futbolkolektyw.pl/en/remind")
    #Test url
    #remind_password_page_url = ("https://scouts-test.futbolkolektyw.pl/en/remind")
    remind_password_hyperlink_xpath = "//child::div/a"
    remind_password_page_send_button_xpath = "//div[2]/button"
    remind_password_box_header_xpath = "//div[1]/h5"
    remind_password_box_header_text = "Remind password"
    back_to_sign_in_link_xpath = "//div[1]/a"
    back_to_sign_in_link_text = "Back to sign in"
    # VALID LOGIN TEST DATA
    valid_email = "user01@getnada.com"
    valid_password = "Test-1234"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_login_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def assert_panel_title(self, expected_panel_title):
        self.assert_element_text(self.driver, self.scouts_panel_title_xpath, expected_panel_title)

    def assert_email_validation_text(self, email_validation_text):
        self.assert_element_text(self.driver, self.validation_span_xpath, email_validation_text)

    def assert_password_validation_text(self, password_validation_text):
        self.assert_element_text(self.driver, self.validation_span_xpath, self.password_validation_text)

    def correct_login(self):
        self.type_in_email(self.valid_email)
        self.type_in_password(self.valid_password)
        self.click_on_the_sign_in_button()

    def click_remind_password_hyperlink(self):
        self.click_on_the_element(self.remind_password_hyperlink_xpath)

    def assert_title_of_remind_password_page(self):
        assert self.get_page_title(self.remind_password_page_url) == self.expected_title

    def click_remind_password_page_send_button(self):
        self.click_on_the_element(self.remind_password_page_send_button_xpath)

    def back_to_sign_in_text_is_not_present(self, back_to_sign_in_link_text):
        self.assert_element_text_is_not(self.driver, self.back_to_sign_in_link_xpath, back_to_sign_in_link_text)
