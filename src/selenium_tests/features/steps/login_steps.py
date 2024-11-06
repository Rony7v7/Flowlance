from behave import given, when, then
from selenium_tests.pages.login_page import LoginPage
from selenium_tests.pages.dashboard_page import DashboardPage

@given('the user is on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()

@when('the user enters valid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('the user enters invalid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('the user enters empty username and password')
def step_impl(context):
    context.login_page.enter_username("")
    context.login_page.enter_password("")

@when('clicks the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('the user should be redirected to the dashboard')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    expected_dashboard_url = "http://127.0.0.1:8000/dashboard/"
    assert not context.driver.current_url == expected_dashboard_url

@then('an error message "{message}" should be displayed')
def step_impl(context, message):
    displayed_message = context.login_page.get_error_message_text(message)
    assert displayed_message, f"Expected error message '{message}' not displayed"

@given('the user is logged in')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()
    context.login_page.login("testuser", "12345noesfacil")

@given('the user is on the restore password page')
def step_impl(context):
    context.login_page.navigate_to_restore_password()

@when('the user enters an incorrect old password "{old_password}"')
def step_impl(context, old_password):
    context.login_page.enter_old_password(old_password)

@when('the user enters the new password "{new_password}" and confirmation')
def step_impl(context, new_password):
    context.login_page.enter_new_password(new_password)
    context.login_page.enter_new_password_confirmation(new_password)

@when('clicks the change password button')
def step_impl(context):
    context.login_page.click_change_password_button()
