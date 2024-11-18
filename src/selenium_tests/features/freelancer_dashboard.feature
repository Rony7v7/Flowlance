Feature: Freelancer Dashboard Functionality

  Background:
    Given a freelancer user exists
    And the freelancer is logged in
    And the freelancer is on the dashboard page

  Scenario: Freelancer can view assigned projects
    Given the freelancer has an assigned project
    Then the freelancer should see the assigned project on the dashboard

  Scenario: Freelancer can view pending tasks
    Given the freelancer has a pending task
    Then the freelancer should see the pending task on the dashboard