from behave import given, when, then
from selenium_tests.pages.project_list_page import ProjectListPage
from selenium_tests.pages.project_page import ProjectPage

@given('the user is on the projects page')
def step_impl(context):
    context.project_list_page = ProjectListPage(context.driver)
    context.project_list_page.navigate()

@when('the user clicks on the new project button')
def step_impl(context):
    context.project_list_page.click_create_project()

@when('the user fills in the project form with title "{title}" and description "{description}"')
def step_impl(context, title, description):
    context.project_list_page.enter_project_title(title)
    context.project_list_page.enter_project_description(description)

@when('the user clicks the create project button')
def step_impl(context):
    context.project_list_page.submit_project_form()

@then('the user should see the project details page')
def step_impl(context):
    context.project_page = ProjectPage(context.driver)
    assert context.project_page.is_on_project_page()

@given('the user is on the project details page for project "{project_id}"')
def step_impl(context, project_id):
    context.project_page = ProjectPage(context.driver)
    context.project_page.navigate(project_id)

@when('the user clicks on the edit project button')
def step_impl(context):
    context.project_page.click_edit_project()

@when('the user updates the project form with title "{title}" and description "{description}"')
def step_impl(context, title, description):
    context.project_page.update_project_title(title)
    context.project_page.update_project_description(description)

@when('the user clicks the update project button')
def step_impl(context):
    context.project_page.submit_project_update()

@then('the user should see the updated project details page with title "{title}"')
def step_impl(context, title):
    assert title in context.project_page.get_project_title()

@when('the user clicks on the delete project button')
def step_impl(context):
    context.project_page.click_delete_project()

@then('the user should be redirected to the projects page')
def step_impl(context):
    assert context.project_list_page.is_on_projects_page()

@when('the user clicks on the "{tab_name}" tab')
def step_impl(context, tab_name):
    context.project_page.navigate_to_tab(tab_name)

@then('the user should see the "{tab_name}" page')
def step_impl(context, tab_name):
    assert context.project_page.is_on_tab(tab_name)

@when('the user clicks on the add milestone button')
def step_impl(context):
    context.project_page.click_add_milestone()

@then('the user should see the add milestone form')
def step_impl(context):
    assert context.project_page.is_add_milestone_form_visible()

@when('the user clicks on the add task button')
def step_impl(context):
    context.project_page.click_add_task()

@then('the user should see the add task form')
def step_impl(context):
    assert context.project_page.is_add_task_form_visible()