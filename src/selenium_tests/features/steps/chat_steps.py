# features/steps/chat_steps.py

from behave import given, when, then
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from project.models import Project, ProjectMember
from chat.models import Message
from django.urls import reverse
from selenium_tests.pages.chat_page import ChatPage
import os

@given('there are two users "{user1}" and "{user2}"')
def step_impl(context, user1, user2):
    context.user1 = User.objects.create_user(username=user1, password="pass")
    context.user2 = User.objects.create_user(username=user2, password="pass")

@given('there is a project "{project_name}"')
def step_impl(context, project_name):
    context.project = Project.objects.create(title=project_name)

@given('both users are members of the project')
def step_impl(context):
    ProjectMember.objects.create(user=context.user1, project=context.project)
    ProjectMember.objects.create(user=context.user2, project=context.project)

@given('user "{username}" is logged in')
def step_impl(context, username):
    context.browser.get(context.get_url('/login/'))
    context.browser.find_element(By.NAME, 'username').send_keys(username)
    context.browser.find_element(By.NAME, 'password').send_keys('pass')
    context.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

@when('user1 navigates to the chat room with user2 for the project')
def step_impl(context):
    url = reverse('chat_room', args=[context.project.id, context.user2.id])
    context.chat_page = ChatPage(context.browser)
    context.chat_page.navigate_to_chat_room(context.get_url(url))

@then('user1 should see the chat room page')
def step_impl(context):
    assert context.chat_page.is_chat_room_visible()

@then('the page should contain "{text}"')
def step_impl(context, text):
    assert text in context.chat_page.get_chat_room_title()

@given('user1 is in the chat room with user2 for the project')
def step_impl(context):
    url = reverse('chat_room', args=[context.project.id, context.user2.id])
    context.chat_page = ChatPage(context.browser)
    context.chat_page.navigate_to_chat_room(context.get_url(url))
    assert context.chat_page.is_chat_room_visible()

@when('user1 sends a message "{message}"')
def step_impl(context, message):
    context.chat_page.send_message(message)

@then('the message "{message}" should appear in the chat')
def step_impl(context, message):
    assert context.chat_page.is_message_visible(message)

@given('there is a message "{message}" in the chat')
def step_impl(context, message):
    Message.objects.create(
        sender=context.user1,
        recipient=context.user2,
        project=context.project,
        content=message
    )

@when('user1 soft deletes the chat')
def step_impl(context):
    context.chat_page.soft_delete_chat()

@then('the message should be hidden for user1')
def step_impl(context):
    message = Message.objects.filter(sender=context.user1, recipient=context.user2).first()
    assert message.hidden_for_sender

@when('user1 uploads a file "{filename}"')
def step_impl(context, filename):
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, 'w') as f:
        f.write('Test file content')
    context.chat_page.upload_file(file_path)

@then('the file should be successfully uploaded')
def step_impl(context):
    assert context.chat_page.is_file_upload_successful()

@then('the file name should appear in the chat')
def step_impl(context):
    assert context.chat_page.is_file_name_in_chat('test_file.txt')