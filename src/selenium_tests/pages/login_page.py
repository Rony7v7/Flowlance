from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, ".alert-danger")
        self.old_password_input = (By.NAME, "old_password")
        self.new_password_input = (By.NAME, "new_password1")
        self.new_password_confirmation_input = (By.NAME, "new_password2")
        self.change_password_button = (By.CSS_SELECTOR, "button[type='submit']")

    def navigate(self):
        self.driver.get("http://localhost:8000/login/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def is_error_message_displayed(self, message):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.error_message)
            )
            return message in error_element.text
        except:
            return False
    
    def get_error_message_text(self, message):
        # Espera hasta que el mensaje de error esté visible en la página
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[3]/ul/li"))
        )
        return message in error_message_element.text


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def navigate_to_restore_password(self):
        self.driver.get("http://localhost:8000/restore_password/")

    def enter_old_password(self, old_password):
        self.driver.find_element(*self.old_password_input).send_keys(old_password)

    def enter_new_password(self, new_password):
        self.driver.find_element(*self.new_password_input).send_keys(new_password)

    def enter_new_password_confirmation(self, new_password):
        self.driver.find_element(*self.new_password_confirmation_input).send_keys(new_password)

    def click_change_password_button(self):
        self.driver.find_element(*self.change_password_button).click()

    def is_password_change_error_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.error_message)
            )
            return True
        except:
            return False