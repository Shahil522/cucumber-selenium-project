from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I am on the login page")
def step_open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.driver.find_element(By.ID, "password").send_keys(password)


@when("I click the login button")
def step_click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('I should see "{result}"')
def step_verify_result(context, result):

    if result == "dashboard":
        assert "inventory" in context.driver.current_url

    elif result == "error":
        error_message = context.driver.find_element(
            By.CSS_SELECTOR,
            "[data-test='error']"
        )
        assert error_message.is_displayed()