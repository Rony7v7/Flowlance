import os
import sys
import django
from django.test.runner import DiscoverRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del entorno Django
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selenium_tests.test_settings')
django.setup()

test_runner = DiscoverRunner()
test_runner.setup_test_environment()
old_config = test_runner.setup_databases()

def before_all(context):
    # Configuración del controlador de Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Inicializa el driver usando Service
    service = Service(ChromeDriverManager().install())
    context.browser = webdriver.Chrome(service=service, options=chrome_options)  # Cambiado a browser
    context.browser.implicitly_wait(10)
    context.server_url = 'http://localhost:8000'

def after_all(context):
    if hasattr(context, "browser"):  # Cambiado a browser
        context.browser.quit()
    test_runner.teardown_databases(old_config)
    test_runner.teardown_test_environment()
