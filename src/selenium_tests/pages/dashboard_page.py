# selenium_tests/pages/dashboard_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        # Updated selectors based on the actual page structure
        self.freelancer_project = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div[2]/div[1]/div[2]/div/div/a")
        self.freelancer_pending_task = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div")
        
        # Additional selectors for verification
        self.projects_title = (By.XPATH, "//h2[contains(text(), 'Proyectos disponibles')]")
        self.pending_tasks_title = (By.XPATH, "//h2[contains(text(), 'Tareas Pendientes')]")
        # New selectors for company dashboard
        self.associated_freelancer = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div[1]/div[2]/div/div/div")

        self.freelancer_rating = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div[1]/div[2]/div/div/div")
        
        # Additional selectors for verification
        self.company_dashboard_title = (By.XPATH, "//h1[contains(text(), 'Dashboard de Empresa')]")

    def navigate(self):
        self.driver.get("http://localhost:8000/dashboard/")

    def is_company_dashboard_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.company_dashboard_title)
            )
            return True
        except:
            return False

    def is_associated_freelancer_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.associated_freelancer)
            )
            return True
        except:
            return False

    def is_freelancer_rating_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.freelancer_rating)
            )
            return True
        except:
            return False

    def get_associated_freelancer_info(self):
        freelancer_element = self.driver.find_element(*self.associated_freelancer)
        return freelancer_element.text

    def get_freelancer_rating(self):
        rating_element = self.driver.find_element(*self.freelancer_rating)
        # Instead of getting the 'd' attribute, we'll get the aria-label which might contain the rating value
        return rating_element.get_attribute("aria-label")  

    # Existing methods (kept for completeness)
    def is_freelancer_project_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.freelancer_project)
            )
            return True
        except:
            return False

    def is_freelancer_pending_task_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.freelancer_pending_task)
            )
            return True
        except:
            return False

    def get_project_title(self):
        project_element = self.driver.find_element(*self.freelancer_project)
        return project_element.text

    def get_pending_task_title(self):
        task_element = self.driver.find_element(*self.freelancer_pending_task)
        return task_element.text


   