from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from unittest import skip

import time


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e tenta enviar uma lista em branco
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys(Keys.ENTER)  # Envia uma entrada vazia
        # Satisfeitos, ambos voltam a dormir

        self.fail('Finish the test')

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')

