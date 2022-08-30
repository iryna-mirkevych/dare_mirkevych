from pages.base_page import BasePage, assert_element_text


class EditPlayerPage(BasePage):
    edit_player_page_header_xpath = "//*//form/div[1]//span"
    expected_title_start = "Edit player"

    def check_title_starts_with(self):
        actual_title = self.driver.title
        assert actual_title.startswith(self.expected_title_start)





