Feature: Dashboard Functionality

  Scenario: Freelancer accesses dashboard
    Given a freelancer user is logged in
    When the freelancer accesses the dashboard
    Then the freelancer should see their dashboard
    And the freelancer should see their projects
    And the freelancer should see their pending tasks

  Scenario: Company accesses dashboard
    Given a company user is logged in
    When the company accesses the dashboard
    Then the company should see their dashboard
    And the company should see their projects
    And the company should see associated freelancers
    And the company should see ratings for freelancers