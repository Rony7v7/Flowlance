# features/profile.feature

Feature: Freelancer and Company Profile Management

  Scenario: Freelancer views own profile
    Given a freelancer user "testuser" exists
    And "testuser" is logged in
    When the user navigates to their own profile
    Then they should see their profile information

  Scenario: Company views freelancer profile
    Given a freelancer user "freelancer_user" exists
    And a company user "company_user" exists
    And "company_user" is logged in
    When the company user views the freelancer's profile
    Then they should see the freelancer's profile information
    
  Scenario: Freelancer adds skills
    Given a freelancer user "testuser" exists
    And "testuser" is logged in
    When the user adds a skill "Python"
    Then the skill should be added to their profile

  Scenario: Freelancer adds work experience
    Given a freelancer user "testuser" exists
    And "testuser" is logged in
    When the user adds work experience
      | title     | company      | start_date | end_date   | description        |
      | Developer | Test Company | 2022-01-01 | 2022-12-31 | Developed software |
    Then the work experience should be added to their profile

  Scenario: Company adds rating for freelancer
    Given a freelancer user "freelancer_user" exists
    And a company user "company_user" exists
    And "company_user" is logged in
    When the company user adds a rating for the freelancer
    Then the rating should be added to the freelancer's profile

  Scenario: Freelancer registers with valid data
    When a freelancer registers with the following data:
      | username   | email                  | password         | identification | phone      |
      | new_user   | new_user@example.com   | securePass123!   | 1234567890     | 3001234567 |
    Then the freelancer account should be created successfully

  Scenario: Company registers with valid data
    When a company registers with the following data:
      | username   | email                  | password         | company_name | nit        | business_type | country  | business_vertical | address   | legal_representative | phone      |
      | new_company| company@example.com    | securePass123!   | Test Company | 9001234567 | Tecnología    | Colombia | Software          | Calle 123 | John Doe             | 3012345678 |
    Then the company account should be created successfully