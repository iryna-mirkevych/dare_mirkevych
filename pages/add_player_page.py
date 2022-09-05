from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_add_player_title = "Add player"
    submit_button_xpath = "//*[@type='submit']"
    empty_name_validation_xpath = "*// form//div[2]//p"
    empty_name_validation_text = "Required"
    name_field_xpath = "//*[@name = 'name']"
    surname_field_xpath = "//*[@name = 'surname']"
    age_field_xpath = "//*[@name = 'age']"
    main_position_field_xpath = "//*[@name = 'mainPosition']"
    expected_edit_player_title_starts_with = "Edit player"
    clear_button_xpath = "//form//button[2]"

    def assert_title_of_add_player_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_add_player_title

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def assert_empty_name_validation(self, empty_name_validation_text):
        self.assert_element_text(self.driver, self.empty_name_validation_xpath, empty_name_validation_text)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)




pass
