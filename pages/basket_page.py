from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def check_mess_about_empty_basket(self):
		mess_about_empty_basket = self.browser.find_element(*BasketPageLocators.MESS_BASKET_IS_EMPTY)
		return mess_about_empty_basket.text

	def check_empty_basket(self):
		return self.is_not_element_present(*BasketPageLocators.FORM_BASKET_PRODUCT)
