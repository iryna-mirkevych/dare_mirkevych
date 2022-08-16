from pages.base_page import BasePage


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

pass
