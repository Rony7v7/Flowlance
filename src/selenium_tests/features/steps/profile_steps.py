# features/steps/profile_steps.py

from behave import given, when, then
from django.contrib.auth.models import User
from django.urls import reverse
from profile.models import FreelancerProfile, CompanyProfile, Skill, WorkExperience, Rating
from notifications.models import Notification

@given('a freelancer user "{username}" exists')
def step_impl(context, username):
    user = User.objects.create_user(username=username, password='password123')
    FreelancerProfile.objects.create(user=user, identification='12345', phone='1234567890')

@given('a company user "{username}" exists')
def step_impl(context, username):
    user = User.objects.create_user(username=username, password='password123')
    CompanyProfile.objects.create(user=user, company_name='Test Company', nit='1234567890')

@given('"{username}" is logged in')
def step_impl(context, username):
    context.browser.get(context.get_url(reverse('login')))
    context.browser.find_element_by_name('username').send_keys(username)
    context.browser.find_element_by_name('password').send_keys('password123')
    context.browser.find_element_by_css_selector('button[type="submit"]').click()

@when('the user navigates to their own profile')
def step_impl(context):
    context.browser.get(context.get_url(reverse('my_profile')))

@then('they should see their profile information')
def step_impl(context):
    assert 'Profile' in context.browser.title

@when('the company user views the freelancer\'s profile')
def step_impl(context):
    freelancer = User.objects.get(username='freelancer_user')
    context.browser.get(context.get_url(reverse('freelancer_profile_view', args=[freelancer.username])))

@then('they should see the freelancer\'s profile information')
def step_impl(context):
    assert 'Freelancer Profile' in context.browser.title


@when('the user adds a skill "{skill_name}"')
def step_impl(context, skill_name):
    context.browser.get(context.get_url(reverse('customize_profile')))
    skill = Skill.objects.create(name=skill_name)
    context.browser.find_element_by_id(f'id_predefined_skills_{skill.id}').click()
    context.browser.find_element_by_css_selector('button[type="submit"]').click()

@then('the skill should be added to their profile')
def step_impl(context):
    user = User.objects.get(username='testuser')
    assert Skill.objects.filter(freelancerprofile__user=user, name='Python').exists()

@when('the user adds work experience')
def step_impl(context):
    context.browser.get(context.get_url(reverse('add_experience')))
    for row in context.table:
        context.browser.find_element_by_name('title').send_keys(row['title'])
        context.browser.find_element_by_name('company').send_keys(row['company'])
        context.browser.find_element_by_name('start_date').send_keys(row['start_date'])
        context.browser.find_element_by_name('end_date').send_keys(row['end_date'])
        context.browser.find_element_by_name('description').send_keys(row['description'])
    context.browser.find_element_by_css_selector('button[type="submit"]').click()

@then('the work experience should be added to their profile')
def step_impl(context):
    user = User.objects.get(username='testuser')
    assert WorkExperience.objects.filter(freelancer_profile__user=user, title='Developer').exists()

@when('the company user adds a rating for the freelancer')
def step_impl(context):
    freelancer = User.objects.get(username='freelancer_user')
    context.browser.get(context.get_url(reverse('add_rating', args=[freelancer.username])))
    context.browser.find_element_by_name('stars').send_keys('4')
    context.browser.find_element_by_name('comment').send_keys('Good job!')
    context.browser.find_element_by_css_selector('button[type="submit"]').click()

@then('the rating should be added to the freelancer\'s profile')
def step_impl(context):
    freelancer = User.objects.get(username='freelancer_user')
    assert Rating.objects.filter(freelancer__user=freelancer, stars=4).exists()

@when('a freelancer registers with the following data')
def step_impl(context):
    context.browser.get(context.get_url(reverse('freelancer_register')))
    for row in context.table:
        context.browser.find_element_by_name('username').send_keys(row['username'])
        context.browser.find_element_by_name('email').send_keys(row['email'])
        context.browser.find_element_by_name('password1').send_keys(row['password'])
        context.browser.find_element_by_name('password2').send_keys(row['password'])
        context.browser.find_element_by_name('identification').send_keys(row['identification'])
        context.browser.find_element_by_name('phone').send_keys(row['phone'])
    context.browser.find_element_by_css_selector('button[type="submit"]').click()

@then('the freelancer account should be created successfully')
def step_impl(context):
    assert User.objects.filter(username='new_user').exists()
    assert FreelancerProfile.objects.filter(user__username='new_user').exists()

@when('a company registers with the following data')
def step_impl(context):
    context.browser.get(context.get_url(reverse('company_register')))
    for row in context.table:
        context.browser.find_element_by_name('username').send_keys(row['username'])
        context.browser.find_element_by_name('email').send_keys(row['email'])
        context.browser.find_element_by_name('password1').send_keys(row['password'])
        context.browser.find_element_by_name('password2').send_keys(row['password'])
        context.browser.find_element_by_name('company_name').send_keys(row['company_name'])
        context.browser.find_element_by_name('nit').send_keys(row['nit'])
        context.browser.find_element_by_name('business_type').send_keys(row['business_type'])
        context.browser.find_element_by_name('country').send_keys(row['country'])
        context.browser.find_element_by_name('business_vertical').send_keys(row['business_vertical'])
        context.browser.find_element_by_name('address').send_keys(row['address'])
        context.browser.find_element_by_name('legal_representative').send_keys(row['legal_representative'])
        context.browser.find_element_by_name('phone').send_keys(row['phone'])
    context.browser.find_element_by_css_selector('button[type="submit"]').click()

@then('the company account should be created successfully')
def step_impl(context):
    assert User.objects.filter(username='new_company').exists()
    assert CompanyProfile.objects.filter(user__username='new_company').exists()