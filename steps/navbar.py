from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

WEBSITE_URL = 'http://zach-smith-portfolio.com'


@given('the site is reachable')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get(WEBSITE_URL)
    context.driver = driver

@when('I click Bio')
def step_impl(context):
    context.driver.find_element(By.NAME, "bio-tab").click()

@then('Bio is set to active')
def step_impl(context):
    element = None
    try:
        element = WebDriverWait(context.driver, 10).until(
            lambda a: 'active' in context.driver.find_element(By.NAME, "bio-tab").get_attribute('class')
        )
    finally:
        assert element
    
@when('I click Skills')
def step_impl(context):
    context.driver.find_element(By.NAME, "skills-tab").click()

@then('Skills is set to active')
def step_impl(context):
    element = None
    try:
        element = WebDriverWait(context.driver, 10).until(
            lambda a: 'active' in context.driver.find_element(By.NAME, "skills-tab").get_attribute('class')
        )
    finally:
        assert element
    
@when('I click Projects')
def step_impl(context):
    context.driver.find_element(By.NAME, "projects-tab").click()

@then('Projects is set to active')
def step_impl(context):
    element = None
    try:
        element = WebDriverWait(context.driver, 10).until(
            lambda a: 'active' in context.driver.find_element(By.NAME, "projects-tab").get_attribute('class')
        )
    finally:
        assert element
    
@when('I click Contact Me')
def step_impl(context):
    context.driver.find_element(By.NAME, "contact-tab").click()

@then('Contact Me is set to active')
def step_impl(context):
    element = None
    try:
        element = WebDriverWait(context.driver, 10).until(
            lambda a: 'active' in context.driver.find_element(By.NAME, "contact-tab").get_attribute('class')
        )
    finally:
        assert element