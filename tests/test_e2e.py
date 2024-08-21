# type: ignore

import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.base_class import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = 0
        for card in cards:
            i += 1
            card_text = card.text
            print(card_text)
            if card_text == "Blackberry":
                self.driver.find_element(
                    By.XPATH, f"//app-card[{i}]//div[1]//div[2]//button[1]").click()

        self.driver.find_element(
            By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(
            By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(
            By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(
            By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText
        self.driver.close()
