from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectPage:
    def __init__(self, driver):
        self.driver = driver
        # URLs
        self.url_template = "http://localhost:8000/project/{project_id}/"
        
        # Locators
        self.navigation_tabs = {
            "avance": (By.LINK_TEXT, "Avance del proyecto"),
            "planeación": (By.LINK_TEXT, "Planeación"),
            "progreso": (By.LINK_TEXT, "Progreso"),
            "equipo": (By.LINK_TEXT, "Equipo y Comunicación"),
        }
        self.edit_project_button = (By.LINK_TEXT, "Editar")
        self.view_requirements_button = (By.LINK_TEXT, "Ver Requerimientos")
        self.show_applications_button = (By.ID, "showApplications")
        self.applications_modal = (By.ID, "applicationsModal")
        self.close_modal_button = (By.ID, "closeModal")
        self.delete_project_button = (By.LINK_TEXT, "Eliminar Proyecto")
        self.add_milestone_button = (By.LINK_TEXT, "Añadir")
        self.milestone_section = (By.CSS_SELECTOR, "h2:contains('Hitos')")
        self.notification_message = (By.ID, "notification-message")

    # Navegar a la página del proyecto
    def navigate(self, project_id):
        self.driver.get(self.url_template.format(project_id=project_id))

    # Cambiar entre pestañas de navegación
    def switch_tab(self, tab_name):
        if tab_name.lower() in self.navigation_tabs:
            tab_locator = self.navigation_tabs[tab_name.lower()]
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(tab_locator)
            ).click()

    # Hacer clic en el botón "Editar Proyecto"
    def click_edit_project(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.edit_project_button)
        ).click()

    # Hacer clic en el botón "Ver Requerimientos"
    def click_view_requirements(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.view_requirements_button)
        ).click()

    # Mostrar el modal de postulaciones
    def show_applications(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.show_applications_button)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.applications_modal)
        )

    # Cerrar el modal de postulaciones
    def close_applications_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_modal_button)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.applications_modal)
        )

    # Hacer clic en el botón "Eliminar Proyecto"
    def delete_project(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_project_button)
        ).click()

    # Hacer clic en el botón "Añadir" para hitos, tareas, etc.
    def click_add_milestone(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_milestone_button)
        ).click()

    # Verificar que un mensaje de notificación se muestre
    def get_notification_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.notification_message)
        )
        return self.driver.find_element(*self.notification_message).text
