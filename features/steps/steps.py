from behave import given, when, then

@given('I am on the Google homepage')
def step_given_google_homepage(context):
    context.page.goto("https://www.google.com")

@when('I search for "{query}"')
def step_when_search(context, query):
    context.page.fill('textarea[name="q"]', query)
    context.page.press('textarea[name="q"]', "Enter")
    context.page.wait_for_load_state("networkidle")

@then('I should see results related to Playwright')
def step_then_see_results(context):
    title = context.page.title()
    assert "Playwright" in title or context.page.locator('text=Playwright').is_visible()

@given('I have a web page')
def step_given_web_page(context):
    # Page is already set up in environment.py
    pass

@when('I visit the page')
def step_when_visit_page(context):
    context.page.goto("data:text/html,<h1>Hello, World!</h1>")

@then('I should see "Hello, World!"')
def step_then_see_hello_world(context):
    assert context.page.locator('text=Hello, World!').is_visible()