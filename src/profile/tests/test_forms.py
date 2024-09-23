from django.test import TestCase
from ..forms import (
    AddCourseForm,
    AddProjectForm,
    UploadCVForm,
    AddSkillsForm,
    AddWorkExperienceForm,
    RatingForm,
    RatingResponseForm,
)
from ..models import Course, PortfolioProject, FreelancerProfile, Skill
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date


class AddCourseFormTest(TestCase):
    def test_add_course_form_valid(self):
        form_data = {
            'course_name': 'Django for Beginners',
            'course_description': 'Learn Django basics',
            'organization': 'Udemy',
            'course_link': 'https://udemy.com/django-course',
            'expedition_date': date.today(),
        }
        form = AddCourseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_add_course_form_invalid(self):
        form_data = {
            'course_name': '',
            'course_description': 'Learn Django basics',
        }
        form = AddCourseForm(data=form_data)
        self.assertFalse(form.is_valid())


class AddProjectFormTest(TestCase):
   
    def test_add_project_form_invalid(self):
        form_data = {
            'project_name': '',
            'start_date': date(2023, 1, 1),
        }
        form = AddProjectForm(data=form_data)
        self.assertFalse(form.is_valid())


class UploadCVFormTest(TestCase):
    def test_upload_cv_form_valid(self):
        uploaded_file = SimpleUploadedFile('test_cv.pdf', b'file_content', content_type='application/pdf')
        form_data = {'file': uploaded_file}
        form = UploadCVForm(data=form_data, files={'file': uploaded_file})
        self.assertTrue(form.is_valid())



class AddSkillsFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile, _ = FreelancerProfile.objects.get_or_create(user=self.user)

    def test_add_skills_form_valid(self):
        skill = Skill.objects.create(name='Python', is_custom=False)
        form_data = {
            'predefined_skills': [skill.id],
            'custom_skills': 'React, Vue.js',
        }
        form = AddSkillsForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_add_skills_form_no_skills(self):
        form_data = {}
        form = AddSkillsForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())  # No skills is also a valid scenario


class AddWorkExperienceFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile, _ = FreelancerProfile.objects.get_or_create(user=self.user)

    def test_add_work_experience_form_valid(self):
        form_data = {
            'title': 'Software Developer',
            'company': 'XYZ Ltd',
            'start_date': date(2021, 1, 1),
            'end_date': date(2022, 1, 1),
            'description': 'Developed various applications',
        }
        form = AddWorkExperienceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_add_work_experience_form_invalid(self):
        form_data = {
            'title': '',
            'start_date': date(2021, 1, 1),
        }
        form = AddWorkExperienceForm(data=form_data)
        self.assertFalse(form.is_valid())


class RatingFormTest(TestCase):
    def test_rating_form_valid(self):
        form_data = {'stars': 5, 'comment': 'Excellent job!'}
        form = RatingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_rating_form_invalid(self):
        form_data = {'stars': 6}  # Stars should be between 1 and 5
        form = RatingForm(data=form_data)
        self.assertFalse(form.is_valid())


class RatingResponseFormTest(TestCase):
    def test_rating_response_form_valid(self):
        form_data = {'response_text': 'Thank you for your feedback!'}
        form = RatingResponseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_rating_response_form_invalid(self):
        form_data = {'response_text': ''}
        form = RatingResponseForm(data=form_data)
        self.assertFalse(form.is_valid())
