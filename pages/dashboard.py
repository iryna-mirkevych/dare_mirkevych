from pages.base_page import BasePage

import time


class Dashboard(BasePage):
    scouts_panel_header_xpath = "//header//child::h6[1]"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//ul[1]/div[2]"
    language_button_xpath = "//div[1]//ul[2]/div[1]"
    sign_out_button_xpath = "//div[1]//ul[2]/div[2]"
    dev_team_contact_link_xpath = "//child::div[3]/a"
    add_player_link_xpath = "//div[1]//div[3]/div[2]//a"
    last_created_player_link_xpath = "//descendant::a[3]"
    last_updated_player_link_xpath = "//descendant::a[4]"
    last_created_report_link_xpath = "//following-sibling::a[3]"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    players_page_title_xpath = "//title"
    expected_players_page_title_start = "Players"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.players_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player(self):
        self.wait_for_element_to_be_clickable(self.add_player_link_xpath)
        self.click_on_the_element(self.add_player_link_xpath)

    def click_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_button_xpath)
        self.click_on_the_element(self.players_button_xpath)

    def wait_for_presence_of_players_title_located(self):
        self.wait_for_presence_of_element_located(self.players_page_title_xpath)

    def check_title_of_players_page_starts_with(self):
        actual_title = self.driver.title
        assert actual_title.startswith(self.expected_players_page_title_start)




pass
