from behave import *
from features.lib.pages import *

use_step_matcher("re")


@Given("I am in the Google home")
def step_impl(context):
    page = GoogleHomePage(context)
    page.visit("http://www.google.co.uk")


@when("I search for London")
def step_impl(context):
    # Locate the search
    page = GoogleHomePage(context)
    page.type_search("London\n")
    # page.search_box.send_keys("London")
    # Type search


@when(u'I click on search button')
def step_impl(context):
    page = GoogleHomePage(context)
    counter = "1 - 25 of 10,000+"
    m, _, _ = counter.partition("of")
    _, _, m = m.partition("-")
    m = m.strip()
    print("the number is: {}".format(m))



@then(u'the number of resulting listings must be equal to number of listing')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the number of resulting listings must be equal to number of listing')
