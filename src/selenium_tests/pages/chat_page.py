from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChatPage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to_chat_room(self, url):
        self.browser.get(url)

    def is_chat_room_visible(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, 'chat-room'))
            )
            return True
        except:
            return False

    def send_message(self, message):
        input_field = self.browser.find_element(By.ID, 'chat-message-input')
        input_field.send_keys(message)
        self.browser.find_element(By.ID, 'chat-message-submit').click()

    def is_message_visible(self, message):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.text_to_be_present_in_element((By.ID, 'chat-messages'), message)
            )
            return True
        except:
            return False

    def soft_delete_chat(self):
        self.browser.find_element(By.ID, 'soft-delete-chat').click()

    def upload_file(self, file_path):
        file_input = self.browser.find_element(By.ID, 'file-upload')
        file_input.send_keys(file_path)
        self.browser.find_element(By.ID, 'upload-file-button').click()

    def is_file_upload_successful(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'upload-success'))
            )
            return True
        except:
            return False

    def is_file_name_in_chat(self, filename):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.text_to_be_present_in_element((By.ID, 'chat-messages'), filename)
            )
            return True
        except:
            return False

    def get_chat_room_title(self):
        return self.browser.find_element(By.ID, 'chat-room-title').text