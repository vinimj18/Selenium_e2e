from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    card_title = (By.CSS_SELECTOR, '.card-title a')

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    card_footer = (By.CSS_SELECTOR, '.card-footer button')

    def get_card_footer(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    checkout_button = (By.CSS_SELECTOR, 'a[class*="btn-primary"]')

    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

    checkout_button_2 = (By.XPATH, "//button[@class='btn btn-success']")

    def checkout_items(self):
        return self.driver.find_element(*CheckoutPage.checkout_button_2)
