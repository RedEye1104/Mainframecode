import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Opening Edge")
    else:
        driver = webdriver.Chrome()
        print("Opening Chrome")

    # Yield the driver for use in tests
    yield driver

    # Cleanup after tests
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser to use")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


################# HTML REPORT GEN ###################

def pytest_configure(config):
    config._metadata['Project Name'] ='Easemytrip'
    config._metadata['Module Name'] = 'home page'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Define the reports directory and create it if it does not exist
    reports_dir = os.path.join(os.path.abspath(os.curdir), 'reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Set the path for the HTML report with timestamp
    report_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".html"
    config.option.htmlpath = os.path.join(reports_dir, report_filename)

    #("%d-%m-%Y_%H-%M-%S")