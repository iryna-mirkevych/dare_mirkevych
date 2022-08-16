from pages.base_page import BasePage


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
           def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
