from selenium.webdriver.common.by import By


class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class BasketPageLocators():
	FORM_BASKET_PRODUCT = (By.CSS_SELECTOR, 'form.basket_summary') #форма товара в корзине. для проверки есть ли товар в корзине
	MESS_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p:nth-child(1)')


class LoginPageLocators():
	LOGIN_FORM = (By.ID, 'login_form')
	REGISTRATION_FORM = (By.ID, 'register_form')
	REGISTER_EMAIL = (By.ID, 'id_registration-email')
	REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
	REGISTER_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
	REGISTER_BTN = (By.CSS_SELECTOR, 'button[name=registration_submit]')


class ProductPageLocators():
	BTN_BUY = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
	PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
	PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
	BASKET_PRICE = (By.CSS_SELECTOR, '.alert.alert-info strong')
	NOTE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div')
