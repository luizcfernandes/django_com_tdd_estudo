from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import time

# --- Define the correct path to the Chrome executable ---
# !!! REPLACE THIS STRING WITH YOUR ACTUAL EXECUTABLE PATH !!!
# Example for Windows:
# CHROME_BINARY_LOCATION = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# Example for macOS:
# CHROME_BINARY_LOCATION = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Example for Linux:
# CHROME_BINARY_LOCATION = "/usr/bin/google-chrome"

# Set your actual, correct path here

MAX_WAIT = 4


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        CHROME_BINARY_LOCATION = "/usr/bin/google-chrome"

        # --- Setup Options ---
        options = Options()
        options.headless = True # Run in background
        # # Assign the *verified* path to the binary_location option
        options.binary_location = CHROME_BINARY_LOCATION
        # # --- Initialize Driver ---
        try:
            self.browser = webdriver.Chrome(options=options)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("\nPlease verify that the path in 'CHROME_BINARY_LOCATION' is exactly correct.")

    def tearDown(self):
        return self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_input_box(self):
        return self.browser.find_element(By.ID, 'id_new_item')