from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.freelancer_dashboard = (By.ID, "freelancer-dashboard")
        self.company_dashboard = (By.ID, "company-dashboard")
        self.freelancer_projects = (By.ID, "freelancer-projects")
        self.freelancer_pending_tasks = (By.ID, "freelancer-pending-tasks")
        self.company_projects = (By.ID, "company-projects")
        self.associated_freelancers = (By.ID, "associated-freelancers")
        self.freelancer_ratings = (By.ID, "freelancer-ratings")

    def navigate(self):
        self.driver.get("http://localhost:8000/dashboard/")

    def is_freelancer_dashboard_visible(self):
        return self._is_element_visible(self.freelancer_dashboard)

    def is_company_dashboard_visible(self):
        return self._is_element_visible(self.company_dashboard)

    def are_freelancer_projects_visible(self):
        return self._is_element_visible(self.freelancer_projects)

    def are_freelancer_pending_tasks_visible(self):
        return self._is_element_visible(self.freelancer_pending_tasks)

    def are_company_projects_visible(self):
        return self._is_element_visible(self.company_projects)

    def are_associated_freelancers_visible(self):
        return self._is_element_visible(self.associated_freelancers)

    def are_freelancer_ratings_visible(self):
        return self._is_element_visible(self.freelancer_ratings)

    def _is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False