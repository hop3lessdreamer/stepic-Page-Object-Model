from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
	pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
	"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
	page.buy_item()
	page.solve_quiz_and_get_code()
	page.check_success_mess_product_added(product_name)
	page.check_bucket_price()


@pytest.mark.parametrize('link', [pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/', marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.buy_item()
	page.check_is_not_element_present(*ProductPageLocators.NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET)


@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_guest_cant_see_success_message(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.check_is_not_element_present(*ProductPageLocators.NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET)


@pytest.mark.parametrize('link', [pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/', marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.buy_item()
	page.check_is_disappeared(*ProductPageLocators.NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET)


def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = LoginPage(browser, link)
	page.open()
	page.go_to_login_page()
	page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope='function', autouse=True)
	def setup(self, browser):
		link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/'
		page = LoginPage(browser, link)
		page.open()
		page.go_to_login_page()
		email = str(time.time()) + '@fakemail.com'
		password = 'fuh123fuw3'
		page.register_new_user(email, password)
		page.should_be_authorized_user()

	@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
	def test_user_cant_see_success_message(self, browser, link):
		page = ProductPage(browser, link)
		page.open()
		page.check_is_not_element_present(*ProductPageLocators.NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET)

	@pytest.mark.need_review
	@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
	def test_user_can_add_product_to_basket(self, browser, link):
		page = ProductPage(browser, link)
		page.open()
		product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		page.buy_item()
		product_price = page.product_price
		page.check_success_mess_product_added(product_name)
		page.check_bucket_price()
