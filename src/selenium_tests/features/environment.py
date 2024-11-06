import os
import sys
import django
from django.conf import settings

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from selenium_tests.utils.driver_factory import DriverFactory

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selenium_tests.test_settings')
django.setup()

def before_all(context):
    context.driver_factory = DriverFactory()

def before_scenario(context, scenario):
    context.driver = context.driver_factory.get_driver()

def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()

def after_all(context):
    context.driver_factory.close_all()