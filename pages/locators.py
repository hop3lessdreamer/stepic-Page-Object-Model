from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.ID, 'login_form')
	REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators():
	BTN_BUY = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
	PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
	BASKET_PRICE = (By.CSS_SELECTOR, '.alert.alert-info strong')
	NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/text()')
