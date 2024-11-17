Feature: Manage Projects

    Scenario: Create a new project
        Given the user is on the projects page
        When the user clicks on the new project button
        And the user fills in the project form with title "Test Project" and description "This is a test project"
        And the user clicks the create project button
        Then the user should see the project details page

    Scenario: Edit a project
        Given the user is on the project details page for project "1"
        When the user clicks on the edit project button
        And the user updates the project form with title "Updated Project" and description "Updated description"
        And the user clicks the update project button
        Then the user should see the updated project details page with title "Updated Project"

    Scenario: Delete a project
        Given the user is on the project details page for project "1"
        When the user clicks on the delete project button
        Then the user should be redirected to the projects page

    Scenario: Navigate through project tabs
        Given the user is on the project details page for project "1"
        When the user clicks on the "Avance del proyecto" tab
        Then the user should see the "Avance del proyecto" page
        When the user clicks on the "Planeación" tab
        Then the user should see the "Planeación" page
        When the user clicks on the "Progreso" tab
        Then the user should see the "Progreso" page
        When the user clicks on the "Equipo y Comunicación" tab
        Then the user should see the "Equipo y Comunicación" page
