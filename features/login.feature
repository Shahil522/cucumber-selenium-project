# Login test created on QA branch
Feature: Login functionality

  Scenario Outline: Login with different credentials
    Given I am on the login page
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then I should see "<result>"

    Examples:
      | username      | password     | result            |
      | standard_user | secret_sauce | dashboard         |
      | standard_user | wrong_pass   | error             |