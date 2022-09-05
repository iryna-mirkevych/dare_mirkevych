from pages.base_page import BasePage


class EditPlayerPage(BasePage):
    edit_player_page_header_xpath = "//*//form/div[1]//span"
    edit_player_page_title_xpath = "//title"
    expected_title_start = "Edit player"

    def check_title_starts_with(self):
        actual_title = self.driver.title
        assert actual_title.startswith(self.expected_title_start)

    def wait_for_presence_of_edit_page_title_located(self):
        self.wait_for_presence_of_element_located(self.edit_player_page_title_xpath)

