import os
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Add the project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

def before_all(context):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowlance.settings')
    context.base_url = 'http://localhost:8000'
    
    # Initialize the browser here
    context.browser = webdriver.Chrome(ChromeDriverManager().install())

def after_all(context):
    # Quit the browser after all tests
    if hasattr(context, 'browser'):
        context.browser.quit()

def before_scenario(context, scenario):
    # No need to initialize the browser for each scenario
    pass

def after_scenario(context, scenario):
    # No need to quit the browser after each scenario
    pass