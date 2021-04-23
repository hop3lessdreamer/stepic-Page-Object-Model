from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
	"""
	Добавление параметра для pytest в командной строке.
	Позволяет выбирать браузер, на котором будет проводиться
	тестирование. По умолчанию chrome. Пример:
	pytest --browser_name=firefox test.py
	"""
	parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')

@pytest.fixture
def browser(request):
	"""
	Автоматически подтягивается к тестовым ф-циям, методам, если передать в кач-ве параметра (browser)
	"""
	browser_name = request.config.getoption('browser_name')
	browser = None
	if browser_name == 'chrome':
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		browser = webdriver.Chrome(options=options)
	elif browser_name == 'firefox':
		browser = webdriver.Firefox()
	else: raise pytest.UsageError("--browsername should be chrome or firefox")
	yield browser
	browser.quit()
