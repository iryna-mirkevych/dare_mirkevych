from pages.base_page import BasePage


class PlayersPage(BasePage):
    player_data_link_xpath = "//td[1]"
    sort_button_xpath = "//main//span[2]/button"
    reports_input_xpath = "//label[8]/span[1]"
    reports_column_header_xpath = "//table//tr/th[8]"

    def click_player_table_data(self):
        self.wait_for_element_to_be_clickable(self.player_data_link_xpath)
        self.click_on_the_element(self.player_data_link_xpath)

    def click_sort_button(self):
        self.wait_for_element_to_be_clickable(self.sort_button_xpath)
        self.click_on_the_element(self.sort_button_xpath)

    def click_reports_input(self):
        self.wait_for_element_to_be_clickable(self.sort_button_xpath)
        self.click_on_the_element(self.reports_input_xpath)

#check missing column after sorting = unticking reports column
    def check_reports_column_not_present(self):
        self.assert_element_is_not_present(self.reports_column_header_xpath)





