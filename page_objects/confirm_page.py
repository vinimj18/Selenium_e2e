from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    country_dropdown = (By.ID, "country")

    def get_country_dropdown(self):
        return self.driver.find_element(*ConfirmPage.country_dropdown)

    dropdown_value = (By.LINK_TEXT, "India")

    def get_india(self):
        return self.driver.find_element(*ConfirmPage.dropdown_value)

    agree_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def get_agree_checkbox(self):
        return self.driver.find_element(*ConfirmPage.agree_checkbox)

    purchase_button = (By.CSS_SELECTOR, "[type='submit']")

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    success_message = (By.CLASS_NAME, "alert-success")

    def get_success_message(self):
        return self.driver.find_element(*ConfirmPage.success_message)
