from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
	page = ProductPage(browser, link)
	page.open()
	page.buy_item()
	product_price = page.product_price
	page.solve_quiz_and_get_code()
	assert page.check_success_mess_product_added, 'Нет сообщения о том, что товар добавлен'
	assert page.get_bucket_price() == page.product_price, 'Цена корзины не соответствует цене товара'
