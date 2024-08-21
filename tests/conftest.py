import pytest

from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver
