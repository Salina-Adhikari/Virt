from selenium import webdriver
import pytest
@pytest.fixture
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser=="firefox":
        driver=webdriver.firefox()
        print("Launching Firefox Browser")
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):

    if hasattr(config, 'metadata'):
     config.metadata['Project Name']="Virt"
     config.metadata['Module Name']="Sigin"
     config.metadata['Tester']="Salina"



@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
