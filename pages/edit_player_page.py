import time

from pages.base_page import BasePage


class EditPlayerPage(BasePage):
    edit_player_page_header_xpath = "//*//form/div[1]//span"
    edit_player_page_title_xpath = "//title"
    expected_title_start = "Edit player"
    matches_button_xpath = "//ul[2]/div[2]"
    add_match_button_xpath = "//div[1]/main/a/button"
    reports_button_xpath = "//ul[2]/div[3]"
    add_report_button_xpath = "//main/a"
    expected_adding_match_page_title_start = "Adding match"
    expected_adding_report_page_title_start = "Adding report"

    def check_title_starts_with(self):
        actual_title = self.driver.title
        assert actual_title.startswith(self.expected_title_start)

    def wait_for_presence_of_edit_page_title_located(self):
        self.wait_for_presence_of_element_located(self.edit_player_page_title_xpath)
        time.sleep(3)

    def click_matches_button(self):
        self.wait_for_element_to_be_clickable(self.matches_button_xpath)
        self.click_on_the_element(self.matches_button_xpath)

    def click_add_match_button(self):
        self.wait_for_element_to_be_clickable(self.add_match_button_xpath)
        self.click_on_the_element(self.add_match_button_xpath)

    def assert_adding_match_page_title_starts_with(self):
        actual_title = self.driver.title
        assert actual_title.startswith(self.expected_adding_match_page_title_start)

    def click_reports_button(self):
        self.wait_for_element_to_be_clickable(self.reports_button_xpath)
        self.click_on_the_element(self.reports_button_xpath)

    def click_add_report_button(self):
        self.wait_for_element_to_be_clickable(self.add_report_button_xpath)
        self.click_on_the_element(self.add_report_button_xpath)

    def assert_adding_report_page_title_starts_with(self):
        actual_title = self.driver.title
        assert actual_title.startswith(self.expected_adding_report_page_title_start)

