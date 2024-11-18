from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectListPage:
    def __init__(self, driver):
        self.driver = driver
        # URLs
        self.url = "http://localhost:8000/project/"
        
        # Locators
        self.available_projects_tab = (By.LINK_TEXT, "Disponibles")
        self.my_projects_tab = (By.LINK_TEXT, "Mis Proyectos")
        self.create_project_button = (By.LINK_TEXT, "Crear Proyecto")
        self.project_cards = (By.CSS_SELECTOR, ".grid .bg-white")
        self.project_titles = (By.CSS_SELECTOR, ".grid .bg-white h2")
        self.project_detail_links = (By.CSS_SELECTOR, ".grid a[href*='/project/']")
        self.project_budgets = (By.CSS_SELECTOR, ".grid .bg-white .text-gray-500")

    # Navegar a la página de proyectos
    def navigate(self):
        self.driver.get(self.url)

    # Hacer clic en "Crear Proyecto"
    def click_create_project(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_project_button)
        ).click()

    # Cambiar entre pestañas de "Disponibles" y "Mis Proyectos"
    def switch_to_tab(self, tab_name):
        if tab_name.lower() == "disponibles":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.available_projects_tab)
            ).click()
        elif tab_name.lower() == "mis proyectos":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.my_projects_tab)
            ).click()

    # Obtener títulos de los proyectos listados
    def get_project_titles(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.project_titles)
        )
        titles = self.driver.find_elements(*self.project_titles)
        return [title.text for title in titles]

    # Obtener presupuestos de los proyectos listados
    def get_project_budgets(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.project_budgets)
        )
        budgets = self.driver.find_elements(*self.project_budgets)
        return [budget.text for budget in budgets]

    # Hacer clic en el primer proyecto disponible
    def click_first_project(self):
        project_links = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.project_detail_links)
        )
        if project_links:
            project_links[0].click()
