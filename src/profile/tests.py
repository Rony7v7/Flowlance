from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import FreelancerProfile, Skill, WorkExperience, Portfolio, PortfolioProject, Course, CurriculumVitae
from .forms import AddWorkExperienceForm, AddSkillsForm, AddCourseForm, AddProjectForm, UploadCVForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse



class ProfileModuleTests(TestCase):
    
    def setUp(self):
        # Create a test user and a corresponding freelancer profile
        self.user, _ = User.objects.get_or_create(username='testuser')
        self.profile, _ = FreelancerProfile.objects.get_or_create(user=self.user)
        self.client.force_login(self.user)  # Log in the test client

    def test_profile_creation(self):
        # Test if profile is created correctly
        self.assertEqual(FreelancerProfile.objects.count(), 1)
        self.assertEqual(self.profile.user.username, 'testuser')

    def test_add_skill(self):
        # Test adding a predefined skill
        skill = Skill.objects.create(name='Python', is_custom=False)
        self.profile.skills.add(skill)
        self.assertIn(skill, self.profile.skills.all())

    def test_add_custom_skill(self):
        # Test adding a custom skill through the form
        form = AddSkillsForm(data={'custom_skills': 'Django'}, user=self.user)
        self.assertTrue(form.is_valid())
        form.save(user=self.user)
        self.assertTrue(Skill.objects.filter(name='Django', is_custom=True).exists())

    def test_add_course(self):
        # Test adding a course through the form
        portfolio = Portfolio.objects.create(freelancer_profile=self.profile)
        form_data = {
            'course_name': 'Django Mastery',
            'course_description': 'Advanced Django course',
            'organization': 'Online Academy',
            'course_link': 'http://example.com',
            'expedition_date': '2023-01-01'
        }
        form = AddCourseForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(Course.objects.count(), 1)

    def test_add_project(self):
        # Test adding a project through the form
        portfolio = Portfolio.objects.create(freelancer_profile=self.profile)
        form_data = {
            'project_name': 'Web App',
            'client': 'Client A',
            'project_description': 'Developed a web app using Django',
            'start_date': '2023-01-01',
            'end_date': '2023-06-01',
            'activities_done': 'Development, Testing',
        }
        form = AddProjectForm(data=form_data)
        self.assertTrue(form.is_valid())
        project = form.save(commit=False)
        project.portfolio = portfolio
        project.save()
        self.assertEqual(PortfolioProject.objects.count(), 1)
        self.assertEqual(portfolio.projects.first().project_name, 'Web App')

    def test_add_work_experience(self):
        # Test adding work experience
        form_data = {
            'title': 'Software Developer',
            'company': 'Tech Co',
            'start_date': '2022-01-01',
            'end_date': '2023-01-01',
            'description': 'Developed various web applications.',
        }
        form = AddWorkExperienceForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save(user=self.user)  # Pass the user during save, not init
        self.assertEqual(WorkExperience.objects.count(), 1)
        self.assertEqual(self.profile.freelancer_work_experience.first().title, 'Software Developer')


    def test_upload_cv(self):
        # Test uploading a CV
        cv_file = SimpleUploadedFile("cv.pdf", b"file_content", content_type="application/pdf")

        # Check if the profile has an associated CV, if not, set the instance to None
        if hasattr(self.profile, 'freelancer_cv'):
            instance = self.profile.freelancer_cv
        else:
            instance = None

        form = UploadCVForm(data={}, files={'file': cv_file}, instance=instance)
        self.assertTrue(form.is_valid())
        cv = form.save(commit=False)
        cv.profile = self.profile
        cv.save()
        self.assertEqual(CurriculumVitae.objects.count(), 1)
        self.assertEqual(self.profile.freelancer_cv.file.name, 'resumes/cv.pdf')



    def test_view_own_profile(self):
        # Test viewing own freelancer profile
        response = self.client.get(reverse('freelancer_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_view_other_profile(self):
        # Test viewing another user's freelancer profile
        other_user = User.objects.create(username='otheruser')
        # No need to manually create FreelancerProfile; it should be created automatically by signals
        response = self.client.get(reverse('freelancer_profile_view', args=[other_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, other_user.username)
        
        

    def test_add_experience_view(self):
        # Test adding work experience through the view
        form_data = {
            'title': 'Backend Developer',
            'company': 'Tech Innovators',
            'start_date': '2022-05-01',
            'end_date': '2023-04-01',
            'description': 'Worked on backend systems using Django.',
        }

        # Perform a POST request to the add_experience view
        response = self.client.post(reverse('add_experience'), data=form_data)

        # Check that the response redirects to the freelancer profile view
        self.assertRedirects(response, reverse('freelancer_profile'))

        # Verify that the work experience was added correctly
        self.assertEqual(WorkExperience.objects.count(), 1)
        work_experience = WorkExperience.objects.first()
        self.assertEqual(work_experience.title, 'Backend Developer')
        self.assertEqual(work_experience.company, 'Tech Innovators')
        self.assertEqual(work_experience.description, 'Worked on backend systems using Django.')
        self.assertEqual(work_experience.freelancer, self.profile)

