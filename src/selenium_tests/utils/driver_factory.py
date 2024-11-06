from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    def __init__(self):
        self.drivers = []

    def get_driver(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.drivers.append(driver)
        return driver

    def close_all(self):
        for driver in self.drivers:
            if driver:
                driver.quit()
        self.drivers = []