from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def enter_username(self, username):
        username_field = self.browser.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.browser.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.browser.find_element(By.ID, "login-button")
        login_button.click()

    def get_error_message(self):
        error_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "error-message"))
        )
        return error_element.text