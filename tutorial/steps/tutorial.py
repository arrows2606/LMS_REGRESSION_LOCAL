from behave import *

@Given('we have behave installed')
def given(self):
        print('given')

@when('we implement a test')
def when(self):
        print("we implement a test")

@then('behave will test it for us!')
def then(self):
        print("behave will test it for us!")
