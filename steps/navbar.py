from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

WEBSITE_URL = 'https://zach-smith-portfolio.com'

@given('the UI is loaded')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get(WEBSITE_URL)
    context.driver = driver

@when('I click Bio')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Bio").click()

@then('we are routed to /')
def step_impl(context):
    assert context.driver.current_url == f'{WEBSITE_URL}/'
    
@when('I click Skills')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Skills").click()

@then('we are routed to /skills')
def step_impl(context):
    assert context.driver.current_url == f'{WEBSITE_URL}/skills'
    
@when('I click Projects')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Projects").click()

@then('we are routed to /projects')
def step_impl(context):
    assert context.driver.current_url == f'{WEBSITE_URL}/projects'
    
@when('I click Contact Me')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Contact Me").click()

@then('we are routed to /contact')
def step_impl(context):
    assert context.driver.current_url == f'{WEBSITE_URL}/contact'