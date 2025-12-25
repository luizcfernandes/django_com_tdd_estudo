from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from unittest import skip

import time


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e tenta enviar uma lista em branco
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(
                Keys.ENTER)
        # time.sleep(10)
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, '#id_text:invalid'))
        # Ela tenta novamente com um texto para o item, e isso agora funciona
        self.get_item_input_box().send_keys('Buy milk')
        # time.sleep(10)
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, '#id_text:valid'))

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy milk')

        # De forma perversa, ela agora decide submeter um segundo item em
        # branco na lista
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Ela recebe um aviso semelhante na página da lista
        self.wait_for_row_in_list_table('1:Buy milk')
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, '#id_text:invalid'))

        # E ela pode corrigir isso preenchendo o item com um texto
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy milk')
        self.wait_for_row_in_list_table('2:Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edith acessa a página inicial e começa uma nova lista
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy wellies')

        # Ela tenta acidentalmente inserir um item duplicadoself.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Ela vê uma mensagem de erro prestativa
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You've already got this in your list"
        ))
        self.fail('Finish the test')


