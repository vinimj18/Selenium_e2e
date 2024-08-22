import pytest

from utilities.base_class import BaseClass
from page_objects.home_page import HomePage


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):

        homepage = HomePage(self.driver)  # type: ignore

        homepage.enter_name().send_keys(get_data[0])
        homepage.enter_email().send_keys(get_data[1])
        homepage.enter_password().send_keys(get_data[2])
        homepage.mark_check_box().click()
        homepage.mark_inline_radio1().click()
        self.select_option_by_text(homepage.select_dropdown(), get_data[3])

        homepage.submit_button().click()

        message = homepage.get_success_message().text
        print(message)
        assert "Success" in message

        self.driver.refresh()  # type: ignore

    @pytest.fixture(params=[
        ('Vinicius Justen', 'vinimj.lixo18@gmail.com', '123456', 'Male'),
        ('Bruna Bárbara', 'bb10@hotmail.com', '135790', 'Female'),
        ('Ana Lúcia', 'almjhonson@gmail.com', 'a1b2c3d4', 'Female'),
    ])
    def get_data(self, request):
        return request.param
