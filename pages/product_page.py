from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def buy_item(self):
		"""Получает цену товара и перемещает товар в корзину"""
		self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		btn_buy = self.browser.find_element(*ProductPageLocators.BTN_BUY)
		btn_buy.click()

	def check_bucket_price(self):
		"""Получает цену корзины после добавления товара в нее"""
		busket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		assert self.product_price == busket_price, 'Цена корзины не соответствует цене товара'

	def check_success_mess_product_added(self, product_name):
		"""Проверяет успешно ли добавлен товар в корзину"""
		success_mess = self.browser.find_element(*ProductPageLocators.NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET).text
		assert success_mess == product_name + ' has been added to your basket.', 'Нет сообщения о том, что товар добавлен'
