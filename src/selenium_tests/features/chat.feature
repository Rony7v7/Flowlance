# features/chat.feature

Feature: Chat Functionality

  Background:
    Given there are two users "user11" and "user22"
    And there is a project "Test Project1"
    And both users are members of the project
    And user "user1" is logged in

  Scenario: User can access chat room
    When user1 navigates to the chat room with user2 for the project
    Then user1 should see the chat room page
    And the page should contain "Chat con user2"

  Scenario: User can send and receive messages
    Given user1 is in the chat room with user2 for the project
    When user1 sends a message "Hello, user2!"
    Then the message "Hello, user2!" should appear in the chat

  Scenario: User can soft delete a chat
    Given user1 is in the chat room with user2 for the project
    And there is a message "This will be deleted" in the chat
    When user1 soft deletes the chat
    Then the message should be hidden for user1

  Scenario: User can upload a file
    Given user1 is in the chat room with user2 for the project
    When user1 uploads a file "test_file.txt"
    Then the file should be successfully uploaded
    And the file name should appear in the chat