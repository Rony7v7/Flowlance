import os
import sys
import django
from django.conf import settings
from django.core.management import call_command
import os
import django
from django.conf import settings
from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from selenium_tests.utils.driver_factory import DriverFactory

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selenium_tests.test_settings')
django.setup()

test_runner = DiscoverRunner()
test_runner.setup_test_environment()
old_config = test_runner.setup_databases()

def before_all(context):
    # Set up the test database
    context.test_case = TransactionTestCase()
    context.test_case._pre_setup()

    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.implicitly_wait(10)
    context.server_url = 'http://localhost:8000'

def after_all(context):
    # Clean up the test database
    context.test_case._post_teardown()
    test_runner.teardown_databases(old_config)
    test_runner.teardown_test_environment()

    # Quit the Selenium browser
    context.browser.quit()

def before_scenario(context, scenario):
    # Reset the database before each scenario
    context.test_case._pre_setup()

def after_scenario(context, scenario):
    # Clean up the database after each scenario
    context.test_case._post_teardown()