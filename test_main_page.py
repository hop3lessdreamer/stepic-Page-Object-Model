from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = 'http://selenium1py.pythonanywhere.com/'
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket()
	assert page.check_empty_basket()
	assert page.check_mess_about_empty_basket() == 'Your basket is empty. Continue shopping'
