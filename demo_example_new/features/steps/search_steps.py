from nose.tools import assert_equal, assert_true,assert_in
from selenium.webdriver.common.by import By

@step('I navigate to the PyPi Home page')
def step_impl(context):
    context.home_page.navigate("https://pypi.python.org/pypi")
    assert_equal(context.home_page.get_page_title(), "PyPI - the Python Package Index : Python Package Index")

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)

@step('I am taken to the PyPi Search Results page')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Index of Packages Matching 'behave' : Python Package Index")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))

@step('I navigate to StackOverflow homepage')
def step_impl(context):
    context.home_page.navigate("https://stackoverflow.com")

@step('StackOverflow Logo is displayed')
def step_impl(context):
    context.home_page.logo_displayed()

@step('I add any tag to the URL')
def step_impl(context):
    context.home_page.add_tag('https://stackoverflow.com')

@step('page title contains the tag')
def step_impl(context):
    assert_in("angular",context.home_page.get_page_title())

@step('Shows all questions tagged with it')
def step_impl(context):
    context.home_page.count_displayed()
    print(context.home_page.count_displayed())

@step('Takes screenshot of the page')
def step_impl(context):
    context.home_page.take_screenshot()

@step('Goes to next page')
def step_impl(context):
    context.home_page.next_page()





