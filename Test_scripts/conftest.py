
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import json




@pytest.fixture(scope="function")
def browser_fun(request):
    print("initiating chrome driver")
    #driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    print("initiating chrome driver")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
    driver.maximize_window()
    #driver.get("https://www.docker.com")
    driver.implicitly_wait(20)
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initiating chrome driver")
    #driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    print("initiating chrome driver")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
    driver.maximize_window()
    #driver.get("https://www.docker.com")
    driver.implicitly_wait(20)
    request.cls.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser")
    parser.addoption("--headless", action="store", help="input browser to execute in headless mode")


@pytest.fixture()
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    params['headless'] = request.config.getoption('--headless')
    return params


@pytest.fixture(scope="function")
def browser_crbt(request,params):
    driver=""
    if params['browser']=='chrome':
        print("initiating chrome driver")
        # driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
        print("initiating chrome driver")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
        driver.maximize_window()
        # driver.get("https://www.docker.com")
        driver.implicitly_wait(20)
        request.instance.driver = driver
        driver.maximize_window()
    elif params['browser']=='edge':
        print("initiating chrome driver")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Edge()  # instanciating edge driver inside driver variable
        driver.maximize_window()
        # driver.get("https://www.docker.com")
        driver.implicitly_wait(20)
        request.instance.driver = driver
        driver.maximize_window()
    else:
        pass


    yield driver

    driver.close()

#This is for reading data from json file
@pytest.fixture()
def readJson():
    with open('Test_Data/global.json.py') as json_file:
        data = json.load(json_file)
        return data
