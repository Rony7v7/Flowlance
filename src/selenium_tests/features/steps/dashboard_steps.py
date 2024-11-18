from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.pages.login_page import LoginPage
from selenium_tests.pages.dashboard_page import DashboardPage

@given('a freelancer user exists')
def step_impl(context):
    # This step would typically involve creating a user in the database
    # For Selenium tests, we'll assume the user already exists
    context.username = "freelancer_user"
    context.password = "password123noesfacil"

@given('a company user exists')
def step_impl(context):
    # This step would typically involve creating a user in the database
    # For Selenium tests, we'll assume the user already exists
    context.username = "company_user"
    context.password = "password123noesfacil"

@given('the freelancer is logged in')
@given('the company user is logged in')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.navigate()
    login_page.login(context.username, context.password)

@given('the freelancer is on the dashboard page')
@given('the company user is on the dashboard page')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    context.dashboard_page.navigate()

@then('the freelancer should see the freelancer dashboard')
def step_impl(context):
    assert context.dashboard_page.is_freelancer_dashboard_visible()

@then('the company should see the company dashboard')
def step_impl(context):
    assert context.dashboard_page.is_company_dashboard_visible()

@given('the freelancer has an assigned project')
def step_impl(context):
    # This step would typically involve creating a project in the database
    # For Selenium tests, we'll assume the project already exists
    pass

@then('the freelancer should see the assigned project on the dashboard')
def step_impl(context):
    assert context.dashboard_page.is_freelancer_project_visible()

@given('the freelancer has a pending task')
def step_impl(context):
    # This step would typically involve creating a task in the database
    # For Selenium tests, we'll assume the task already exists
    pass

@then('the freelancer should see the pending task on the dashboard')
def step_impl(context):
    assert context.dashboard_page.is_freelancer_pending_task_visible()

@given('the company has created a project')
def step_impl(context):
    # This step would typically involve creating a project in the database
    # For Selenium tests, we'll assume the project already exists
    pass

@then('the company should see the created project on the dashboard')
def step_impl(context):
    assert context.dashboard_page.is_company_project_visible()

@given('the company has a project with an associated freelancer')
def step_impl(context):
    # This step would typically involve creating a project and associating a freelancer in the database
    # For Selenium tests, we'll assume this association already exists
    pass

@then('the company should see the associated freelancer on the dashboard')
def step_impl(context):
    assert context.dashboard_page.is_associated_freelancer_visible()

@given('the company has rated a freelancer')
def step_impl(context):
    # This step would typically involve creating a rating in the database
    # For Selenium tests, we'll assume the rating already exists
    pass

@then('the company should see the freelancer rating on the dashboard')
def step_impl(context):
    assert context.dashboard_page.is_freelancer_rating_visible()