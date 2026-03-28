Feature: Hello World

  Scenario: Display hello world message
    Given I have a web page
    When I visit the page
    Then I should see "Hello, World!"