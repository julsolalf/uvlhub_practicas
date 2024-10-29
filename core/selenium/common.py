from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


def initialize_driver():
    # Initializes the browser options
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    chromedriver_path = "/usr/local/bin/chromedriver/chromedriver"
    # Initialise the browser using WebDriver Manager
    # service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
    return driver


def close_driver(driver):
    driver.quit()
