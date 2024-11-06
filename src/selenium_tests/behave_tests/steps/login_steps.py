from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium_tests.pages.login_page import LoginPage

@given('el usuario está en la página de login')
def step_open_login_page(context):
    context.page = LoginPage(context.browser)
    context.browser.get(f"{context.base_url}/login/")
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "login-form"))
    )

@when('ingresa su nombre de usuario "{username}" y contraseña "{password}"')
def step_enter_credentials(context, username, password):
    context.page.enter_username(username)
    context.page.enter_password(password)

@when('hace clic en el botón de login')
def step_click_login_button(context):
    context.page.click_login()

@then('debe ser redirigido a la página de autenticación de dos factores')
def step_redirect_to_2fa(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_contains("two_factor_auth")
    )
    assert "two_factor_auth" in context.browser.current_url, "El usuario no fue redirigido a la autenticación de dos factores"

@then('debe ver un mensaje de error que diga "{message}"')
def step_check_error_message(context, message):
    error_message = context.page.get_error_message()
    assert message in error_message, f"El mensaje de error '{message}' no se mostró como se esperaba"