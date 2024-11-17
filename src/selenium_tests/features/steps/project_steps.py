from behave import given, when, then
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from project.models import Project
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Paso para crear el usuario administrador
@given('there is an admin user')
def step_impl(context):
    if not User.objects.filter(username='admin').exists():
        context.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )
    else:
        context.admin_user = User.objects.get(username='admin')

# Paso para iniciar sesión
@given('the admin user is logged in')
def step_impl(context):
    context.browser.get(f"{context.server_url}/login/")
    context.browser.find_element(By.NAME, 'username').send_keys('admin')
    context.browser.find_element(By.NAME, 'password').send_keys('adminpassword')
    context.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Navegar a la página de proyectos
@when('the admin navigates to the projects page')
def step_impl(context):
    context.browser.get(f"{context.server_url}/project/list/")  # Ajusta la URL si es necesario

# Hacer clic en el botón "Crear Proyecto"
@when('the admin clicks on the new project button')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    new_project_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Crear Proyecto')))
    new_project_button.click()

# Llenar el formulario de creación de proyecto
@when('the admin fills in the project form with title "{title}" and description "{description}"')
def step_impl(context, title, description):
    context.browser.find_element(By.NAME, 'title').send_keys(title)
    context.browser.find_element(By.NAME, 'description').send_keys(description)
    context.browser.find_element(By.NAME, 'budget').send_keys('1000')  # Agrega otros campos obligatorios
    context.browser.find_element(By.NAME, 'start_date').send_keys('2024-11-17')
    context.browser.find_element(By.NAME, 'end_date').send_keys('2024-12-17')

# Hacer clic en el botón de crear proyecto
@when('the admin clicks the create project button')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Verificar que se muestra la página de detalles del proyecto
@then('the admin should see the project details page with title "{title}"')
def step_impl(context, title):
    assert title in context.browser.page_source

# Crear un proyecto existente
@given('there is a project titled "{title}"')
def step_impl(context, title):
    context.project = Project.objects.create(
        title=title,
        description='Descripción de prueba',
        budget=1000,
        start_date=date.today(),
        end_date=date.today() + timedelta(days=30),
    )

# Actualizar el formulario de proyecto
@when('the admin updates the project form with title "{title}" and description "{description}"')
def step_impl(context, title, description):
    context.browser.find_element(By.NAME, 'title').clear()
    context.browser.find_element(By.NAME, 'title').send_keys(title)
    context.browser.find_element(By.NAME, 'description').clear()
    context.browser.find_element(By.NAME, 'description').send_keys(description)

# Hacer clic en el botón de actualizar proyecto
@when('the admin clicks the update project button')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Hacer clic en el botón de eliminar proyecto
@when('the admin clicks on the delete project button')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    delete_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Eliminar Proyecto')))
    delete_button.click()

# Verificar que se redirige a la página de proyectos
@then('the admin should be redirected to the projects page')
def step_impl(context):
    assert context.browser.current_url == f"{context.server_url}/project/list/"

# Navegar entre pestañas
@when('the admin clicks on the "{tab_name}" tab')
def step_impl(context, tab_name):
    wait = WebDriverWait(context.browser, 10)
    tab_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, tab_name)))
    tab_link.click()

# Verificar que se muestra la página de la pestaña
@then('the admin should see the "{tab_name}" page')
def step_impl(context, tab_name):
    page_header = context.browser.find_element(By.TAG_NAME, 'h1').text
    assert tab_name in page_header