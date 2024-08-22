from utilities.base_class import BaseClass
from page_objects.home_page import HomePage


class TestHomePage(BaseClass):

    def test_form_submission(self):

        homepage = HomePage(self.driver)  # type: ignore

        homepage.enter_name().send_keys("Vinicius Justen")
        homepage.enter_email().send_keys("hello@gmail.com")
        homepage.enter_password().send_keys("123456")
        homepage.mark_check_box().click()
        homepage.mark_inline_radio1().click()
        self.select_option_by_text(homepage.select_dropdown(), 'Male')

        homepage.submit_button().click()

        message = homepage.get_success_message().text
        print(message)
        assert "Success" in message
