from HerokuPage import HerokuHelper

def test_successful_login(browser):
    heroku_main_page = HerokuHelper(browser)
    heroku_main_page.go_to_site()
    heroku_main_page.enter_login("tomsmith")
    heroku_main_page.enter_password("SuperSecretPassword!")
    heroku_main_page.click_on_the_login_button()
    info_message = heroku_main_page.check_info_bar().text
    assert "You logged into a secure area!" in info_message, "Bad login"

def test_successful_logout(browser):
    heroku_main_page = HerokuHelper(browser)
    heroku_main_page.go_to_site()
    heroku_main_page.enter_login("tomsmith")
    heroku_main_page.enter_password("SuperSecretPassword!")
    heroku_main_page.click_on_the_login_button()
    heroku_main_page.click_on_the_logout_button()
    info_message = heroku_main_page.check_info_bar().text
    assert "You logged out of the secure area!" in info_message, "Bad login"

def test_fake_username(browser):
    heroku_main_page = HerokuHelper(browser)
    heroku_main_page.go_to_site()
    heroku_main_page.enter_login("tomjones")
    heroku_main_page.enter_password("SuperSecretPassword!")
    heroku_main_page.click_on_the_login_button()
    info_message = heroku_main_page.check_info_bar().text
    assert "Your username is invalid!" in info_message, "Bad login"

def test_fake_password(browser):
    heroku_main_page = HerokuHelper(browser)
    heroku_main_page.go_to_site()
    heroku_main_page.enter_login("tomsmith")
    heroku_main_page.enter_password("SuperFakePassword!")
    heroku_main_page.click_on_the_login_button()
    info_message = heroku_main_page.check_info_bar().text
    assert "Your password is invalid!" in info_message, "Bad login"

def test_empty_username(browser):
    heroku_main_page = HerokuHelper(browser)
    heroku_main_page.go_to_site()
    heroku_main_page.enter_login("")
    heroku_main_page.enter_password("SuperFakePassword!")
    heroku_main_page.click_on_the_login_button()
    info_message = heroku_main_page.check_info_bar().text
    assert "Your username field is empty!" in info_message, "Bad login"

def test_empty_password(browser):
    heroku_main_page = HerokuHelper(browser)
    heroku_main_page.go_to_site()
    heroku_main_page.enter_login("tomsmith")
    heroku_main_page.enter_password("")
    heroku_main_page.click_on_the_login_button()
    info_message = heroku_main_page.check_info_bar().text
    assert "Your password field is empty!" in info_message, "Bad login"

def test_empty_username_and_password(browser):
    heroku_main_page = HerokuHelper(browser)
    heroku_main_page.go_to_site()
    heroku_main_page.enter_login("")
    heroku_main_page.enter_password("")
    heroku_main_page.click_on_the_login_button()
    info_message = heroku_main_page.check_info_bar().text
    assert "Your username and password fields are empty!" in info_message, "Bad login"
