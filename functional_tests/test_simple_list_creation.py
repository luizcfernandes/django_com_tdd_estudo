from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from unittest import skip

import time


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('To-Do', header_text.text)

        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy peacock feathers')


        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar
        # outro item. Ela insere "Use peacock feathers to make a fly"
        # (Usar penas de pavão para fazer um fly – Edith é bem metódica)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # A página é atualizada novamente 77e agora mostra os dois itens em sua lista
        self.wait_for_row_in_list_table('1:Buy peacock feathers')
        self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')

    # def test_can_start_a_list_for_one_user(self):
    #     self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')
    #     self.wait_for_row_in_list_table('1:Buy peacock feathers')

    def test_multiplie_users_can_start_lists_at_different_urls(self):
        # Edith inicia uma nova lista de tarefas
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy peacock feathers')

        # Ela percebe que sua lista tem um URL único
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        ## Usamos uma nova sessão de navegador para garantir que nenhumainformação
        ## de Edith está vindo de cookies etc
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Francis acessa a página inicial. Não há nenhum sinal da lista de Edith
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis inicia uma nova lista inserindo um item novo. Ele
        # é menos interessante que Edith...
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy milk')

        # Francis obtém seu próprio URL exclusivo
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Novamente, não há nenhum sinal da lista de Edith
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

