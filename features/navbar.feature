Feature: Tabs

  Scenario Outline: Click through tabs
    Given the site is reachable
      When I click <tab>
      Then <tab> is set to active
  
    Examples: Tabs
      | tab        |
      | Bio        |
      | Projects   |
      | Skills     |
      | Contact Me |