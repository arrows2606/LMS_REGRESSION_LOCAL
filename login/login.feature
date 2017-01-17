Feature:  Login to LMS
  In oder to check whether I am able to login to LMS successfully

  Scenario: login with valid account
    Given I have a valid login account
    When  I enter login account and try to login
    Then  I am able to login successfully