from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profile.models import PortfolioProject

class Tests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_vista_creacion_proyecto(self):
        """Checks that the project creation view loads correctly"""
        response = self.client.get(reverse('crear_proyecto_portafolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/crear_proyecto_portafolio.html')

    def test_formulario_valido(self):
        """Checks that the form accepts valid data and saves the project"""
        valid_data = {
            'nombre_proyecto': 'Test Project',
            'cliente': 'Test Client',
            'descripcion_proyecto': 'This is a test project',
            'fecha_inicio': '2024-01-01',
            'fecha_fin': '2024-06-01',
            'actividades_realizadas': 'Web Development',
            'enlace_proyecto': 'https://example.com'
        }
        response = self.client.post(reverse('crear_proyecto_portafolio'), valid_data)

        # Verify that it redirects correctly and saves the project
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PortfolioProject.objects.count(), 1)

    def test_formulario_invalido(self):
        """Checks that the form handles validation errors correctly"""
        invalid_data = {
            'cliente': 'Test Client',
            'descripcion_proyecto': 'This is a test project',
            'fecha_inicio': '2024-01-01',
            'fecha_fin': '2024-06-01',
            'actividades_realizadas': 'Web Development',
            'enlace_proyecto': 'https://example.com'
        }
        response = self.client.post(reverse('crear_proyecto_portafolio'), invalid_data)

        # The response should return to the page with the error and not save the project
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'nombre_proyecto', 'This field is required.')
        self.assertEqual(PortfolioProject.objects.count(), 0)

    def test_vista_agregar_curso(self):
        """Checks that the course addition view loads correctly"""
        response = self.client.get(reverse('agregar_curso'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/agregar_curso.html')
            
            
    def test_formulario_valido(self):
        """Checks that the form accepts valid data and saves the course"""
        valid_data = {
            'nombre_curso': 'Test Course',
            'descripcion_curso': 'This is a test course',
            'organizacion': 'Test Organization',
            'enlace_curso': 'https://example.com',
        }
        response = self.client.post(reverse('agregar_curso'), valid_data)

        # Verify that it redirects correctly and saves the course
        self.assertEqual(response.status_code, 302)  # Expected redirection after success
        self.assertEqual(Curso.objects.count(), 1)  # Check that the course was saved
        
    def test_formulario_invalido(self):
        """Checks that the form handles validation errors correctly"""
        invalid_data = {
            'descripcion_curso': 'This is a test course',
            'organizacion': 'Test Organization',
            'enlace_curso': 'https://example.com',
        }
        response = self.client.post(reverse('agregar_curso'), invalid_data)

        # The response should return to the page with the error
        self.assertEqual(response.status_code, 200)  # The page reloads with the error
        self.assertFormError(response, 'form', 'nombre_curso', 'This field is required.')
        self.assertEqual(Curso.objects.count(), 0)  # Nothing should be saved to the DB
        
    def test_vista_subir_curriculum(self):
        """Checks that the resume upload view loads correctly"""
        response = self.client.get(reverse('subir_curriculum'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/subir_curriculum.html')

    def test_formulario_valido(self):
        """Checks that the form accepts a valid PDF file"""
        # Simulate a PDF file
        pdf_file = SimpleUploadedFile("resume.pdf", b"binary file content", content_type="application/pdf")

        # Form data with the file
        valid_data = {
            'curriculum': pdf_file,
        }
        response = self.client.post(reverse('subir_curriculum'), valid_data)

        # Verify redirection after success
        self.assertEqual(response.status_code, 302)  # Redirection after successful upload
        # Here, we can verify that the file was correctly saved in the database or filesystem if necessary.
        
    def test_formulario_invalido_archivo_no_pdf(self):
        """Checks that the form handles invalid (non-PDF) files"""
        # Simulate a text file instead of PDF
        non_pdf_file = SimpleUploadedFile("file.txt", b"binary file content", content_type="text/plain")

        # Submit the form with an invalid file
        invalid_data = {
            'curriculum': non_pdf_file,
        }
        response = self.client.post(reverse('subir_curriculum'), invalid_data)

        # Verify that the form reloads with the error
        self.assertEqual(response.status_code, 200)  # The form reloads with an error
        self.assertFormError(response, 'form', 'curriculum', 'The file must be a PDF.')
        
        
    def test_formulario_invalido_sin_archivo(self):
        """Checks that submitting a form without an attached file is not allowed"""
        # Submit the form without attaching a file
        invalid_data = {}  # No file included

        response = self.client.post(reverse('subir_curriculum'), invalid_data)

        # Verify that the form reloads with an error
        self.assertEqual(response.status_code, 200)  # The form reloads with an error
        self.assertFormError(response, 'form', 'curriculum', 'This field is required.')
