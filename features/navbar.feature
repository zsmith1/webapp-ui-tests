Feature: Navbar tabs

  Scenario Outline: Click through navbar items
    Given the UI is loaded
      When I click <tab>
      Then we are routed to <endpoint>
  
    Examples: Tabs
      | tab        | endpoint  |
      | Bio        | /         |
      | Projects   | /projects |
      | Skills     | /skills   |
      | Contact Me | /contact  |