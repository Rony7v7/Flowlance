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
        
    def test_add_work_experience(self):
        # Test adding work experience
        form_data = {
            'title': 'Software Developer',
            'occupation': 'Software Development',
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
        

    def test_upload_cv(self):
        # Test for uploading a CV file
        cv_file = SimpleUploadedFile("cv.pdf", b"file_content", content_type="application/pdf")

        # Verify if the user has a CV already uploaded else create a new instance
        if hasattr(self.profile, 'freelancer_cv'):
            instance = self.profile.freelancer_cv
        else:
            instance = None

        form = UploadCVForm(data={}, files={'file': cv_file}, instance=instance)
        self.assertTrue(form.is_valid())
        cv = form.save(commit=False)
        cv.profile = self.profile
        cv.save()
        
        # Verify that the CV file was uploaded successfully and saved in the expected path
        self.assertEqual(CurriculumVitae.objects.count(), 1)
        self.assertIn('resumes/cv', self.profile.freelancer_cv.file.name)
        
    
    def test_add_project_with_attachments(self):
        # Test for adding a project with attached files
        portfolio = Portfolio.objects.create(freelancer_profile=self.profile)
        form_data = {
            'project_name': 'Test Project with File',
            'client': 'Test Client',
            'project_description': 'Test Description',
            'start_date': '2024-01-01',
            'end_date': '2024-06-01',
            'activities_done': 'Testing, Documentation',
            'attached_files': SimpleUploadedFile('test_file.txt', b'File content', content_type='text/plain'),
        }
        form = AddProjectForm(data=form_data, files=form_data)
        self.assertTrue(form.is_valid())
        project = form.save(commit=False)
        project.portfolio = portfolio
        project.save()
        
        # Verify that the project was added successfully and the file was uploaded
        self.assertEqual(PortfolioProject.objects.count(), 1)
        self.assertIn('portfolio/test_file', project.attached_files.name)

    def test_add_project_with_external_link(self):
        """
        The code snippet contains two test functions for a Django application - one to add a project with an
        external link and another to test portfolio visibility on a freelancer's profile.
        """
        # Test to verify that a project can have an external link
        portfolio = Portfolio.objects.create(freelancer_profile=self.profile)
        form_data = {
            'project_name': 'Test Project with Link',
            'client': 'Test Client',  # Ensure required fields are present
            'project_description': 'Project with external link',
            'start_date': '2024-01-01',
            'end_date': '2024-06-01',  # Include end_date if it is a required field
            'activities_done': 'Development, Testing',  # Include activities_done if required
            'external_link': 'https://github.com/test',
        }
        form = AddProjectForm(data=form_data)
        
        # Print form errors for debugging purposes
        if not form.is_valid():
            print(form.errors)
        
        self.assertTrue(form.is_valid())
        project = form.save(commit=False)
        project.portfolio = portfolio
        project.save()
        self.assertEqual(PortfolioProject.objects.count(), 1)
        self.assertEqual(project.external_link, 'https://github.com/test')


    def test_portfolio_visibility(self):
        # Test to verify that the portfolio is visible on the freelancer's profile
        portfolio = Portfolio.objects.create(freelancer_profile=self.profile)
        
        # Create a project associated with the portfolio to ensure there is content
        PortfolioProject.objects.create(
            portfolio=portfolio,
            project_name='Test Project',
            project_description='A test project for visibility',
            start_date='2024-01-01',
            end_date='2024-06-01',
            activities_done='Development, Testing',
            project_image=SimpleUploadedFile('test_image.jpg', b'Image content', content_type='image/jpeg')
        )

        # Get the response from the freelancer's profile page
        response = self.client.get(reverse('freelancer_profile', args=[self.user.username]))
        
        # Verify that the page loads correctly
        self.assertEqual(response.status_code, 200)
        
        # Verify that the project name or some portfolio-related information is present in the HTML
        self.assertContains(response, 'Test Project')
        
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
