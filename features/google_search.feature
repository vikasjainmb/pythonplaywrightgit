Feature: Google Search
  As a user
  I want to search on Google
  So that I can find information

  Scenario: Search for Playwright
    Given I am on the Google homepage
    When I search for "Playwright"
    Then I should see results related to Playwright