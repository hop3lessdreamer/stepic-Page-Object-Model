from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def buy_item(self):
		"""Получает цену товара и перемещает товар в корзину"""
		self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		btn_buy = self.browser.find_element(*ProductPageLocators.BTN_BUY)
		btn_buy.click()

	def get_bucket_price(self):
		"""Получает цену корзины после добавления товара в нее"""
		return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

	def check_success_mess_product_added(self, product_name):
		"""Проверяет успешно ли добавлен товар в корзину"""
		success_mess = self.browser.find_element(*ProductPageLocators.NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET).text
		if success_mess == product_name + ' has been added to your basket.':
			return True
		else: return False
