from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import unittest

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


class NewVisitorTest(unittest.TestCase):

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

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')


time.sleep(3)

if __name__ == '__main__':
    unittest.main(warnings='ignore')

