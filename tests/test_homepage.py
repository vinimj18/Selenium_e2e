import pytest

from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
from test_data.homepage_data import HomepageData


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):

        log = self.get_logger()

        homepage = HomePage(self.driver)  # type: ignore

        log.info(f'Name is {get_data['name']}')
        homepage.enter_name().send_keys(get_data['name'])
        homepage.enter_email().send_keys(get_data['email'])
        homepage.enter_password().send_keys(get_data['password'])
        homepage.mark_check_box().click()
        homepage.mark_inline_radio1().click()
        self.select_option_by_text(
            homepage.select_dropdown(), get_data['gender'])

        homepage.submit_button().click()

        message = homepage.get_success_message().text
        print(message)
        assert "Success" in message

        self.driver.refresh()  # type: ignore

    @pytest.fixture(params=HomepageData.test_homepage_data)
    def get_data(self, request):
        return request.param
