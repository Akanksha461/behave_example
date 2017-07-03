Feature: Search

  Scenario: Search PyPI
    Given I navigate to the PyPi Home page
    When I search for "behave"
    Then I am taken to the PyPi Search Results page
    And I see a search result "behave 1.2.5"

    Scenario: StackOverflow
      Given I navigate to StackOverflow homepage
      And StackOverflow Logo is displayed
      When I add any tag to the URL
      Then page title contains the tag
      And Shows all questions tagged with it
      And Takes screenshot of the page
      And Goes to next page

