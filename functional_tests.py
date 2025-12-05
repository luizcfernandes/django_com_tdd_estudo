from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

# --- Define the correct path to the Chrome executable ---
# !!! REPLACE THIS STRING WITH YOUR ACTUAL EXECUTABLE PATH !!!
# Example for Windows:
# CHROME_BINARY_LOCATION = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# Example for macOS:
# CHROME_BINARY_LOCATION = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Example for Linux:
# CHROME_BINARY_LOCATION = "/usr/bin/google-chrome"

# Set your actual, correct path here:
CHROME_BINARY_LOCATION = "/usr/bin/google-chrome"

# --- Setup Options ---
options = Options()
options.headless = True # Run in background
# Assign the *verified* path to the binary_location option
options.binary_location = CHROME_BINARY_LOCATION

# --- Initialize Driver ---
try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print(f"An error occurred: {e}")
    print("\nPlease verify that the path in 'CHROME_BINARY_LOCATION' is exactly correct.")

driver.get("http://localhost:8000")

time.sleep(3)
assert 'install' in driver.title

if __main__ == '__main__':

