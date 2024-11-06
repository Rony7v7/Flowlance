Feature: Login

  Scenario: Usuario accede con credenciales válidas
    Given el usuario está en la página de login
    When ingresa su nombre de usuario "testuser" y contraseña "12345"
    And hace clic en el botón de login
    Then debe ser redirigido a la página de autenticación de dos factores

  Scenario: Usuario accede con credenciales inválidas
    Given el usuario está en la página de login
    When ingresa su nombre de usuario "testuser" y contraseña "wrongpassword"
    And hace clic en el botón de login
    Then debe ver un mensaje de error que diga "Por favor revise su usuario y contraseña"
