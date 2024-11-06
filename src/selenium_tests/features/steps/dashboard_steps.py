from behave import given, when, then
from selenium_tests.pages.dashboard_page import DashboardPage
from selenium_tests.pages.login_page import LoginPage

@given('a freelancer user is logged in')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.navigate()
    login_page.login_as_freelancer()

@given('a company user is logged in')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.navigate()
    login_page.login_as_company()

@when('the freelancer accesses the dashboard')
@when('the company accesses the dashboard')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    context.dashboard_page.navigate()

@then('the freelancer should see their dashboard')
def step_impl(context):
    assert context.dashboard_page.is_freelancer_dashboard_visible()

@then('the company should see their dashboard')
def step_impl(context):
    assert context.dashboard_page.is_company_dashboard_visible()

@then('the freelancer should see their projects')
def step_impl(context):
    assert context.dashboard_page.are_freelancer_projects_visible()

@then('the freelancer should see their pending tasks')
def step_impl(context):
    assert context.dashboard_page.are_freelancer_pending_tasks_visible()

@then('the company should see their projects')
def step_impl(context):
    assert context.dashboard_page.are_company_projects_visible()

@then('the company should see associated freelancers')
def step_impl(context):
    assert context.dashboard_page.are_associated_freelancers_visible()

@then('the company should see ratings for freelancers')
def step_impl(context):
    assert context.dashboard_page.are_freelancer_ratings_visible()