from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    shop = (By.CSS_SELECTOR, 'a[href*="shop"]')

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)
