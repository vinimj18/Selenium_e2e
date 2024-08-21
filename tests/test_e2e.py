# type: ignore

import pytest
import time

from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
from page_objects.checkout_page import CheckoutPage
from page_objects.confirm_page import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        home_page = HomePage(self.driver)
        home_page.shop_items().click()

        checkout_page = CheckoutPage(self.driver)
        cards = checkout_page.get_card_titles()
        i = -1
        for card in cards:
            card_text = card.text
            print(card_text)
            i += 1
            if card_text == "Blackberry":
                checkout_page.get_card_footer()[i].click()
        checkout_page.get_checkout_button().click()
        checkout_page.checkout_items().click()

        confirm_page = ConfirmPage(self.driver)

        confirm_page.get_country_dropdown().send_keys("ind")
        self.verify_link_presence('India')
        confirm_page.get_india().click()
        confirm_page.get_agree_checkbox().click()
        confirm_page.get_purchase_button().click()

        successText = confirm_page.get_success_message().text
        assert "Success! Thank you!" in successText
