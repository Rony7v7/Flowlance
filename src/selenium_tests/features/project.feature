Feature: Manage Projects

    Background:
        Given there is an admin user
        And the admin user is logged in

    Scenario: Create a new project
        When the admin navigates to the projects page
        And the admin clicks on the new project button
        And the admin fills in the project form with title "Test Project" and description "This is a test project"
        And the admin clicks the create project button
        Then the admin should see the project details page with title "Test Project"

    Scenario: Edit a project
        Given there is a project titled "Project to Edit"
        And the admin user is logged in
        When the admin navigates to the projects page
        And the admin clicks on the new project button
        And the admin updates the project form with title "Updated Project" and description "Updated description"
        And the admin clicks the update project button
        Then the admin should see the project details page with title "Updated Project"

    Scenario: Delete a project
        Given there is a project titled "Project to Delete"
        And the admin user is logged in
        When the admin navigates to the projects page
        And the admin clicks on the delete project button
        Then the admin should be redirected to the projects page

    Scenario: Navigate through project tabs
        Given there is a project titled "Project with Tabs"
        And the admin user is logged in
        When the admin navigates to the projects page
        And the admin clicks on the "Avance del proyecto" tab
        Then the admin should see the "Avance del proyecto" page
        When the admin clicks on the "Planeación" tab
        Then the admin should see the "Planeación" page
        When the admin clicks on the "Progreso" tab
        Then the admin should see the "Progreso" page
        When the admin clicks on the "Equipo y Comunicación" tab
        Then the admin should see the "Equipo y Comunicación" page
