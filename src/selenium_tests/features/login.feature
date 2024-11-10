Feature: User Login

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid username "testuser" and password "12345noesfacil"
    And clicks the login button
    Then the user should be redirected to the dashboard

  Scenario: Failed login with invalid credentials
    Given the user is on the login page
    When the user enters invalid username "wronguser" and password "wrongpassword"
    And clicks the login button
    Then an error message "Por favor revise su usuario y contraseña" should be displayed

  Scenario: Failed login with empty fields
    Given the user is on the login page
    When the user enters empty username and password
    And clicks the login button

  Scenario: Failed password change with incorrect old password
    Given the user is logged in
    And the user is on the restore password page
    When the user enters an incorrect old password "wrongoldpassword"
    And the user enters the new password "newpassword123" and confirmation
    And clicks the change password button
