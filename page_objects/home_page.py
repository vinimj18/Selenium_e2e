from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    shop = (By.CSS_SELECTOR, 'a[href*="shop"]')

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check_box = (By.ID, "exampleCheck1")
    inline_radio1 = (By.CSS_SELECTOR, "#inlineRadio1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_password(self):
        return self.driver.find_element(*HomePage.password)

    def mark_check_box(self):
        return self.driver.find_element(*HomePage.check_box)

    def mark_inline_radio1(self):
        return self.driver.find_element(*HomePage.inline_radio1)

    def select_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)
