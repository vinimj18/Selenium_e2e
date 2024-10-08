from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
from page_objects.checkout_page import CheckoutPage
from page_objects.confirm_page import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()

        home_page = HomePage(self.driver)  # type: ignore
        home_page.shop_items().click()

        checkout_page = CheckoutPage(self.driver)  # type: ignore
        log.info('Getting all the card titles')
        cards = checkout_page.get_card_titles()
        i = -1
        for card in cards:
            card_text = card.text
            log.info(card_text)
            i += 1
            if card_text == "Blackberry":
                checkout_page.get_card_footer()[i].click()
        checkout_page.get_checkout_button().click()
        checkout_page.checkout_items().click()

        confirm_page = ConfirmPage(self.driver)  # type: ignore

        log.info('Entering country name as ind')
        confirm_page.get_country_dropdown().send_keys("ind")
        self.verify_link_presence('India')
        confirm_page.get_india().click()
        confirm_page.get_agree_checkbox().click()
        confirm_page.get_purchase_button().click()

        successText = confirm_page.get_success_message().text
        log.info(f'Text received from application is {successText}')
        assert "Success! Thank you!" in successText
