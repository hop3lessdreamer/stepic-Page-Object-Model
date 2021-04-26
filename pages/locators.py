from selenium.webdriver.common.by import By


class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    pass


class LoginPageLocators():
	LOGIN_FORM = (By.ID, 'login_form')
	REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators():
	BTN_BUY = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
	PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
	PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
	BASKET_PRICE = (By.CSS_SELECTOR, '.alert.alert-info strong')
	#NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')
	NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div')
