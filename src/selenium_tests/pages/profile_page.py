# features/pages/profile_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to_profile(self):
        self.browser.get(self.browser.current_url + 'profile/')

    def is_profile_visible(self):
        return 'Profile' in self.browser.title

    def add_skill(self, skill_name):
        self.browser.find_element(By.NAME, 'custom_skill').send_keys(skill_name)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def add_work_experience(self, title, company, start_date, end_date, description):
        self.browser.find_element(By.NAME, 'title').send_keys(title)
        self.browser.find_element(By.NAME, 'company').send_keys(company)
        self.browser.find_element(By.NAME, 'start_date').send_keys(start_date)
        self.browser.find_element(By.NAME, 'end_date').send_keys(end_date)
        self.browser.find_element(By.NAME, 'description').send_keys(description)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def add_rating(self, stars, comment):
        self.browser.find_element(By.NAME, 'stars').send_keys(stars)
        self.browser.find_element(By.NAME, 'comment').send_keys(comment)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def register_freelancer(self, username, email, password, identification, phone):
        self.browser.find_element(By.NAME, 'username').send_keys(username)
        self.browser.find_element(By.NAME, 'email').send_keys(email)
        self.browser.find_element(By.NAME, 'password1').send_keys(password)
        self.browser.find_element(By.NAME, 'password2').send_keys(password)
        self.browser.find_element(By.NAME, 'identification').send_keys(identification)
        self.browser.find_element(By.NAME, 'phone').send_keys(phone)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def register_company(self, username, email, password, company_name, nit, business_type, country, business_vertical, address, legal_representative, phone):
        self.browser.find_element(By.NAME, 'username').send_keys(username)
        self.browser.find_element(By.NAME, 'email').send_keys(email)
        self.browser.find_element(By.NAME, 'password1').send_keys(password)
        self.browser.find_element(By.NAME, 'password2').send_keys(password)
        self.browser.find_element(By.NAME, 'company_name').send_keys(company_name)
        self.browser.find_element(By.NAME, 'nit').send_keys(nit)
        self.browser.find_element(By.NAME, 'business_type').send_keys(business_type)
        self.browser.find_element(By.NAME, 'country').send_keys(country)
        self.browser.find_element(By.NAME, 'business_vertical').send_keys(business_vertical)
        self.browser.find_element(By.NAME, 'address').send_keys(address)
        self.browser.find_element(By.NAME, 'legal_representative').send_keys(legal_representative)
        self.browser.find_element(By.NAME, 'phone').send_keys(phone)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()