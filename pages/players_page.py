from pages.base_page import BasePage, assert_element_text


class PlayersPage(BasePage):
    player_data_link_xpath = "//td[1]"

    def click_player_table_data(self):
        self.wait_for_element_to_be_clickable(self.player_data_link_xpath)
        self.click_on_the_element(self.player_data_link_xpath)



