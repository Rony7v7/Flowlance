Feature: Company Dashboard Functionality

  Background:
    Given a company user exists
    And the company user is logged in
    And the company user is on the dashboard page

  Scenario: Company can view associated freelancers
    Given the company has a project with an associated freelancer
    Then the company should see the associated freelancer on the dashboard

  Scenario: Company can view ratings for freelancers
    Given the company has rated a freelancer
    Then the company should see the freelancer rating on the dashboard