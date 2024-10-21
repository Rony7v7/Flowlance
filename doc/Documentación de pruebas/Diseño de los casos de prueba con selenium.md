# Diseño de los casos de prueba 

### Funcionalidades que van a ser probadas con Selenium

- Login
- Register de Freelancer
- Register de Cliente
- Postulacion a un proyecto
- Creacion de un Proyecto
- Edicion de la informacion de un Proyecto
- Eliminacion de un Proyecto
- Creacion de Milestones
- Eliminacion de Milestone
- Edicion de una Milestone
- Creacion de Entregables dentro de una Milestone
- Creacion de Tareas
- Generacion de Informe de Reporte
- Creacion de Actualizaciones del Proyecto
- Busqueda de un proyecto

### Casos de Prueba que seran realizados con Selenium

### Escenario: Login de Usuario

#### Caso de Prueba 1: Login Exitoso
- **Descripción**: Verificar que un usuario registrado (freelancer o cliente) puede iniciar sesión exitosamente con credenciales correctas.
- **Precondiciones**: El usuario debe estar registrado en el sistema.
- **Pasos**:
  1. Navegar a la página de login.
  2. Ingresar correo electrónico y contraseña válidos.
  3. Hacer clic en el botón "Iniciar sesión".
- **Resultado Esperado**:
  - El usuario es redirigido al **dashboard**.
  - Aparece el mensaje o notificación de bienvenida, si es aplicable.

#### Caso de Prueba 2: Login Fallido por Credenciales Incorrectas
- **Descripción**: Verificar que el sistema no permite iniciar sesión con credenciales incorrectas.
- **Precondiciones**: El usuario no ingresa credenciales válidas.
- **Pasos**:
  1. Navegar a la página de login.
  2. Ingresar correo electrónico y/o contraseña incorrectos.
  3. Hacer clic en el botón "Iniciar sesión".
- **Resultado Esperado**:
  - El usuario permanece en la página de login.
  - Aparece un mensaje de error (por ejemplo, "Credenciales incorrectas").

#### Caso de Prueba 3: Login Fallido por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite iniciar sesión si los campos de correo electrónico o contraseña están vacíos.
- **Precondiciones**: Ninguno.
- **Pasos**:
  1. Navegar a la página de login.
  2. Dejar el campo de correo electrónico vacío y solo ingresar la contraseña (o viceversa).
  3. Hacer clic en el botón "Iniciar sesión".
- **Resultado Esperado**:
  - El usuario permanece en la página de login.
  - Aparece un mensaje de advertencia indicando que los campos obligatorios deben llenarse.

#### Caso de Prueba 4: Redirección después del Login
- **Descripción**: Verificar que después de iniciar sesión exitosamente, el usuario es redirigido a la página correcta.
- **Precondiciones**: El usuario debe estar registrado en el sistema.
- **Pasos**:
  1. Navegar a la página de login.
  2. Ingresar correo electrónico y contraseña válidos.
  3. Hacer clic en el botón "Iniciar sesión".
- **Resultado Esperado**:
  - El usuario es redirigido al **dashboard** del sistema.

#### Caso de Prueba 5: Verificación de la Persistencia de la Sesión
- **Descripción**: Verificar que el sistema mantenga la sesión iniciada al refrescar la página.
- **Precondiciones**: El usuario debe haber iniciado sesión correctamente.
- **Pasos**:
  1. Iniciar sesión exitosamente.
  2. Refrescar la página.
- **Resultado Esperado**:
  - La sesión sigue activa y el usuario permanece en el dashboard sin necesidad de volver a iniciar sesión.

#### Caso de Prueba 6: Logout Funcional
- **Descripción**: Verificar que el usuario puede cerrar sesión correctamente.
- **Precondiciones**: El usuario debe estar autenticado en el sistema.
- **Pasos**:
  1. Iniciar sesión correctamente.
  2. Hacer clic en el botón "Cerrar sesión".
- **Resultado Esperado**:
  - El usuario es redirigido a la página de inicio o login.
  - La sesión es finalizada correctamente.

### Gherkin

Feature: Login

  Scenario: Login Exitoso
    Given el usuario está registrado en el sistema
    When navego a la página de login
    And ingreso correo electrónico y contraseña válidos
    And hago clic en el botón "Iniciar sesión"
    Then el usuario es redirigido al dashboard
    And aparece un mensaje de bienvenida

  Scenario: Login Fallido por Credenciales Incorrectas
    Given el usuario no ingresa credenciales válidas
    When navego a la página de login
    And ingreso correo electrónico y/o contraseña incorrectos
    And hago clic en el botón "Iniciar sesión"
    Then el usuario permanece en la página de login
    And aparece un mensaje de error "Credenciales incorrectas"

  Scenario: Login Fallido por Campos Vacíos
    Given no hay precondiciones
    When navego a la página de login
    And dejo el campo de correo electrónico vacío y solo ingreso la contraseña
    And hago clic en el botón "Iniciar sesión"
    Then el usuario permanece en la página de login
    And aparece un mensaje de advertencia indicando que los campos obligatorios deben llenarse

  Scenario: Redirección después del Login
    Given el usuario está registrado en el sistema
    When navego a la página de login
    And ingreso correo electrónico y contraseña válidos
    And hago clic en el botón "Iniciar sesión"
    Then el usuario es redirigido al dashboard del sistema

  Scenario: Verificación de la Persistencia de la Sesión
    Given el usuario ha iniciado sesión correctamente
    When inicio sesión exitosamente
    And refresco la página
    Then la sesión sigue activa y el usuario permanece en el dashboard sin necesidad de volver a iniciar sesión

  Scenario: Logout Funcional
    Given el usuario está autenticado en el sistema
    When inicio sesión correctamente
    And hago clic en el botón "Cerrar sesión"
    Then el usuario es redirigido a la página de inicio o login
    And la sesión es finalizada correctamente


### Escenario: Registro de Freelancer

#### Caso de Prueba 1: Registro Exitoso de Freelancer
- **Descripción**: Verificar que un freelancer puede registrarse exitosamente proporcionando toda la información requerida.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Freelancer**.
  3. Llenar todos los campos requeridos (Nombre completo, ID, Teléfono, Correo electrónico, Contraseña, Confirmación de contraseña).
  4. Subir una foto de perfil opcional (opcional).
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema crea la cuenta del freelancer.
  - El usuario es redirigido al **dashboard**.
  - Aparece un mensaje de confirmación de registro exitoso.

#### Caso de Prueba 2: Registro Fallido por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite el registro si alguno de los campos obligatorios está vacío.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Freelancer**.
  3. Dejar uno o varios campos requeridos vacíos (por ejemplo, el campo de ID o correo electrónico).
  4. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de advertencia indicando que los campos obligatorios deben llenarse.

#### Caso de Prueba 3: Registro Fallido por Contraseñas No Coincidentes
- **Descripción**: Verificar que el sistema no permite el registro si la contraseña y la confirmación de la contraseña no coinciden.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Freelancer**.
  3. Llenar todos los campos obligatorios.
  4. Ingresar una contraseña y una confirmación de contraseña que no coincidan.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que las contraseñas no coinciden.

#### Caso de Prueba 4: Validación de Correo Electrónico
- **Descripción**: Verificar que el sistema no permite el registro si el formato del correo electrónico no es válido.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Freelancer**.
  3. Ingresar una dirección de correo electrónico con un formato incorrecto (por ejemplo, "usuario@correo" sin dominio).
  4. Completar los demás campos correctamente.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el formato del correo electrónico es inválido.

#### Caso de Prueba 5: Registro Fallido por Correo Electrónico Duplicado
- **Descripción**: Verificar que el sistema no permite el registro con un correo electrónico que ya está registrado.
- **Precondiciones**: Un freelancer con el mismo correo electrónico ya está registrado en el sistema.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Freelancer**.
  3. Ingresar un correo electrónico que ya esté asociado a otra cuenta.
  4. Completar los demás campos correctamente.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el correo electrónico ya está en uso.

#### Caso de Prueba 6: Registro Fallido por Formato Incorrecto en ID o Teléfono
- **Descripción**: Verificar que el sistema no permite el registro si el ID o el número de teléfono tienen un formato inválido.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Freelancer**.
  3. Ingresar un ID o número de teléfono en un formato no permitido (por ejemplo, letras en lugar de números).
  4. Completar los demás campos correctamente.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el formato de ID o teléfono es inválido.

#### Caso de Prueba 7: Subir Foto de Perfil Opcional
- **Descripción**: Verificar que el freelancer puede subir una foto de perfil opcional durante el registro.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Freelancer**.
  3. Llenar los campos obligatorios correctamente.
  4. Subir una foto de perfil.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema permite completar el registro con éxito.
  - La foto de perfil se asocia a la cuenta creada.

### Gherkin

Feature: Registro de Freelancer

  Scenario: Registro Exitoso de Freelancer
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Freelancer
    And lleno todos los campos requeridos (Nombre completo, ID, Teléfono, Correo electrónico, Contraseña, Confirmación de contraseña)
    And subo una foto de perfil opcional
    And hago clic en el botón "Registrarse"
    Then el sistema crea la cuenta del freelancer
    And el usuario es redirigido al dashboard
    And aparece un mensaje de confirmación de registro exitoso

  Scenario: Registro Fallido por Campos Vacíos
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Freelancer
    And dejo uno o varios campos requeridos vacíos
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de advertencia indicando que los campos obligatorios deben llenarse

  Scenario: Registro Fallido por Contraseñas No Coincidentes
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Freelancer
    And lleno todos los campos obligatorios
    And ingreso una contraseña y una confirmación de contraseña que no coinciden
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que las contraseñas no coinciden

  Scenario: Validación de Correo Electrónico
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Freelancer
    And ingreso una dirección de correo electrónico con un formato incorrecto
    And completo los demás campos correctamente
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que el formato del correo electrónico es inválido

  Scenario: Registro Fallido por Correo Electrónico Duplicado
    Given un freelancer con el mismo correo electrónico ya está registrado en el sistema
    When navego a la página de registro
    And selecciono la opción de registrarse como Freelancer
    And ingreso un correo electrónico que ya está asociado a otra cuenta
    And completo los demás campos correctamente
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que el correo electrónico ya está en uso

  Scenario: Registro Fallido por Formato Incorrecto en ID o Teléfono
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Freelancer
    And ingreso un ID o número de teléfono en un formato no permitido
    And completo los demás campos correctamente
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que el formato de ID o teléfono es inválido

  Scenario: Subir Foto de Perfil Opcional
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Freelancer
    And lleno los campos obligatorios correctamente
    And subo una foto de perfil
    And hago clic en el botón "Registrarse"
    Then el sistema permite completar el registro con éxito
    And la foto de perfil se asocia a la cuenta creada


### Escenario: Registro de Cliente

#### Caso de Prueba 1: Registro Exitoso de Cliente
- **Descripción**: Verificar que un cliente puede registrarse exitosamente proporcionando toda la información requerida.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Cliente**.
  3. Llenar todos los campos requeridos (Nombre de usuario, Nombre de la empresa, NIT, Tipo de negocio, País, Vertical de negocio, Dirección, Representante legal, Teléfono, Correo electrónico, Contraseña, Confirmación de contraseña).
  4. Subir una foto de perfil (opcional).
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema crea la cuenta del cliente.
  - El usuario es redirigido al **dashboard**.
  - Aparece un mensaje de confirmación de registro exitoso.

#### Caso de Prueba 2: Registro Fallido por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite el registro si alguno de los campos obligatorios está vacío.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Cliente**.
  3. Dejar uno o varios campos requeridos vacíos (por ejemplo, el campo de NIT o correo electrónico).
  4. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de advertencia indicando que los campos obligatorios deben llenarse.

#### Caso de Prueba 3: Registro Fallido por Contraseñas No Coincidentes
- **Descripción**: Verificar que el sistema no permite el registro si la contraseña y la confirmación de la contraseña no coinciden.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Cliente**.
  3. Llenar todos los campos obligatorios.
  4. Ingresar una contraseña y una confirmación de contraseña que no coincidan.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que las contraseñas no coinciden.

#### Caso de Prueba 4: Validación de Correo Electrónico
- **Descripción**: Verificar que el sistema no permite el registro si el formato del correo electrónico no es válido.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Cliente**.
  3. Ingresar una dirección de correo electrónico con un formato incorrecto (por ejemplo, "usuario@correo" sin dominio).
  4. Completar los demás campos correctamente.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el formato del correo electrónico es inválido.

#### Caso de Prueba 5: Registro Fallido por Correo Electrónico Duplicado
- **Descripción**: Verificar que el sistema no permite el registro con un correo electrónico que ya está registrado.
- **Precondiciones**: Un cliente con el mismo correo electrónico ya está registrado en el sistema.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Cliente**.
  3. Ingresar un correo electrónico que ya esté asociado a otra cuenta.
  4. Completar los demás campos correctamente.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el correo electrónico ya está en uso.

#### Caso de Prueba 6: Registro Fallido por Formato Incorrecto en NIT, Teléfono o ID del Representante Legal
- **Descripción**: Verificar que el sistema no permite el registro si el NIT, el número de teléfono o el número de identificación del representante legal tienen un formato inválido.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Cliente**.
  3. Ingresar un NIT, número de teléfono o número de identificación en un formato incorrecto (por ejemplo, letras en lugar de números).
  4. Completar los demás campos correctamente.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el formato de NIT, teléfono o ID es inválido.

#### Caso de Prueba 7: Registro Exitoso con Foto de Perfil Opcional
- **Descripción**: Verificar que el cliente puede subir una foto de perfil opcional durante el registro.
- **Precondiciones**: Ninguna.
- **Pasos**:
  1. Navegar a la página de registro.
  2. Seleccionar la opción de registrarse como **Cliente**.
  3. Llenar los campos obligatorios correctamente.
  4. Subir una foto de perfil.
  5. Hacer clic en el botón "Registrarse".
- **Resultado Esperado**:
  - El sistema permite completar el registro con éxito.
  - La foto de perfil se asocia a la cuenta creada.

### Gherkin

Feature: Registro de Cliente

  Scenario: Registro Exitoso de Cliente
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Cliente
    And lleno todos los campos requeridos (Nombre de usuario, Nombre de la empresa, NIT, Tipo de negocio, País, Vertical de negocio, Dirección, Representante legal, Teléfono, Correo electrónico, Contraseña, Confirmación de contraseña)
    And subo una foto de perfil opcional
    And hago clic en el botón "Registrarse"
    Then el sistema crea la cuenta del cliente
    And el usuario es redirigido al dashboard
    And aparece un mensaje de confirmación de registro exitoso

  Scenario: Registro Fallido por Campos Vacíos
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Cliente
    And dejo uno o varios campos requeridos vacíos
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de advertencia indicando que los campos obligatorios deben llenarse

  Scenario: Registro Fallido por Contraseñas No Coincidentes
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Cliente
    And lleno todos los campos obligatorios
    And ingreso una contraseña y una confirmación de contraseña que no coinciden
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que las contraseñas no coinciden

  Scenario: Validación de Correo Electrónico
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Cliente
    And ingreso una dirección de correo electrónico con un formato incorrecto
    And completo los demás campos correctamente
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que el formato del correo electrónico es inválido

  Scenario: Registro Fallido por Correo Electrónico Duplicado
    Given un cliente con el mismo correo electrónico ya está registrado en el sistema
    When navego a la página de registro
    And selecciono la opción de registrarse como Cliente
    And ingreso un correo electrónico que ya está asociado a otra cuenta
    And completo los demás campos correctamente
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que el correo electrónico ya está en uso

  Scenario: Registro Fallido por Formato Incorrecto en NIT, Teléfono o ID del Representante Legal
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Cliente
    And ingreso un NIT, número de teléfono o número de identificación en un formato incorrecto
    And completo los demás campos correctamente
    And hago clic en el botón "Registrarse"
    Then el sistema muestra un mensaje de error indicando que el formato de NIT, teléfono o ID es inválido

  Scenario: Registro Exitoso con Foto de Perfil Opcional
    Given no hay precondiciones
    When navego a la página de registro
    And selecciono la opción de registrarse como Cliente
    And lleno los campos obligatorios correctamente
    And subo una foto de perfil
    And hago clic en el botón "Registrarse"
    Then el sistema permite completar el registro con éxito
    And la foto de perfil se asocia a la cuenta creada


### Escenario: Postulación de Freelancer a un Proyecto

#### Caso de Prueba 1: Postulación Exitosa a un Proyecto
- **Descripción**: Verificar que un freelancer puede postularse exitosamente a un proyecto.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe al menos un proyecto disponible para postulación.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto al cual desea postularse y hace clic en "Ver más".
  3. Hace clic en el botón **Postularse**.
  4. Confirma la postulación si es necesario.
- **Resultado Esperado**:
  - El sistema procesa la postulación.
  - Aparece un mensaje de confirmación indicando que la postulación ha sido exitosa.
  - El proyecto aparece como "Postulado" en la lista de proyectos del freelancer.

#### Caso de Prueba 2: Postulación Fallida por Proyecto Cerrado
- **Descripción**: Verificar que un freelancer no puede postularse a un proyecto que ya no está disponible para postulaciones.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - El proyecto está marcado como **Cerrado** o no permite más postulaciones.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona un proyecto que está cerrado o que ya no permite postulaciones.
  3. Intenta hacer clic en el botón **Postularse**.
- **Resultado Esperado**:
  - El botón de postulación está deshabilitado o no está disponible.
  - El sistema muestra un mensaje informando que no es posible postularse a este proyecto porque está cerrado o no permite más postulaciones.

#### Caso de Prueba 3: Postulación Fallida por Freelancer Ya Postulado
- **Descripción**: Verificar que un freelancer no puede postularse a un proyecto en el que ya está postulado.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - El freelancer ya se ha postulado al proyecto.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto al cual ya se ha postulado.
  3. Intenta hacer clic nuevamente en el botón **Postularse**.
- **Resultado Esperado**:
  - El botón **Postularse** está deshabilitado o no está disponible.
  - El sistema muestra un mensaje indicando que el freelancer ya se ha postulado a este proyecto.

#### Caso de Prueba 4: Postulación Fallida por Cliente del Proyecto
- **Descripción**: Verificar que un cliente no puede postularse a su propio proyecto.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - El cliente es el dueño del proyecto.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona su propio proyecto y verifica si el botón **Postularse** está presente.
- **Resultado Esperado**:
  - El botón **Postularse** no está disponible para el cliente en sus propios proyectos.

#### Caso de Prueba 5: Notificación de Aprobación de Postulación
- **Descripción**: Verificar que el freelancer recibe una notificación cuando su postulación es aprobada por el cliente.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - El cliente aprueba la postulación del freelancer a un proyecto.
- **Pasos**:
  1. El cliente aprueba la postulación del freelancer en un proyecto.
  2. El freelancer inicia sesión y navega a su panel de control.
- **Resultado Esperado**:
  - El freelancer recibe una notificación (visual o por correo) indicando que su postulación ha sido aprobada.
  - El estado del proyecto en la lista del freelancer cambia a "Aprobado".

#### Caso de Prueba 6: Postulación Fallida por Error en el Sistema
- **Descripción**: Verificar que el sistema maneja correctamente los errores en la postulación de un freelancer debido a problemas del sistema.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - El sistema tiene un error que impide la postulación (por ejemplo, fallo en la conexión).
- **Pasos**:
  1. El freelancer intenta postularse a un proyecto siguiendo los pasos estándar.
  2. Ocurre un error en el sistema durante el proceso.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error informando sobre el fallo en la postulación.
  - El freelancer puede intentar nuevamente o contactar con el soporte si es necesario.

### Gherkin

Feature: Postulación a Proyecto

  Scenario: Postulación Exitosa a un Proyecto
    Given el freelancer está registrado y autenticado
    And existe al menos un proyecto disponible para postulación
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto al cual desea postularse y hace clic en "Ver más"
    And hace clic en el botón Postularse
    And confirma la postulación si es necesario
    Then el sistema procesa la postulación
    And aparece un mensaje de confirmación indicando que la postulación ha sido exitosa
    And el proyecto aparece como "Postulado" en la lista de proyectos del freelancer

  Scenario: Postulación Fallida por Proyecto Cerrado
    Given el freelancer está registrado y autenticado
    And el proyecto está marcado como Cerrado o no permite más postulaciones
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona un proyecto que está cerrado o que ya no permite postulaciones
    And intenta hacer clic en el botón Postularse
    Then el botón de postulación está deshabilitado o no está disponible
    And el sistema muestra un mensaje informando que no es posible postularse a este proyecto porque está cerrado o no permite más postulaciones

  Scenario: Postulación Fallida por Freelancer Ya Postulado
    Given el freelancer está registrado y autenticado
    And el freelancer ya se ha postulado al proyecto
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto al cual ya se ha postulado
    And intenta hacer clic nuevamente en el botón Postularse
    Then el botón Postularse está deshabilitado o no está disponible
    And el sistema muestra un mensaje indicando que el freelancer ya se ha postulado a este proyecto

  Scenario: Postulación Fallida por Cliente del Proyecto
    Given el cliente está registrado y autenticado
    And el cliente es el dueño del proyecto
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona su propio proyecto
    Then el botón Postularse no está disponible para el cliente en sus propios proyectos

  Scenario: Notificación de Aprobación de Postulación
    Given el freelancer está registrado y autenticado
    And el cliente aprueba la postulación del freelancer a un proyecto
    When el freelancer inicia sesión y navega a su panel de control
    Then el freelancer recibe una notificación indicando que su postulación ha sido aprobada
    And el estado del proyecto en la lista del freelancer cambia a "Aprobado"

  Scenario: Postulación Fallida por Error en el Sistema
    Given el freelancer está registrado y autenticado
    And el sistema tiene un error que impide la postulación
    When el freelancer intenta postularse a un proyecto
    And ocurre un error en el sistema durante el proceso
    Then el sistema muestra un mensaje de error informando sobre el fallo en la postulación
    And el freelancer puede intentar nuevamente o contactar con el soporte si es necesario


### Escenario: Creación de Proyecto por Cliente

#### Caso de Prueba 1: Creación Exitosa de Proyecto
- **Descripción**: Verificar que un cliente puede crear un proyecto exitosamente proporcionando toda la información requerida.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Hace clic en el botón **Crear Proyecto**.
  3. Completa todos los campos requeridos: Nombre del proyecto, Especificaciones, Requerimientos, Presupuesto, Fecha de inicio, Fecha de finalización.
  4. Hace clic en **Confirmar** para enviar el formulario.
- **Resultado Esperado**:
  - El proyecto se crea exitosamente.
  - La UI se actualiza y el nuevo proyecto aparece en la lista de proyectos.
  - Aparece una notificación de confirmación indicando que el proyecto se ha creado correctamente.

#### Caso de Prueba 2: Creación Fallida por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite crear un proyecto si uno o más campos obligatorios están vacíos.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Hace clic en el botón **Crear Proyecto**.
  3. Deja uno o varios campos obligatorios vacíos (por ejemplo, el campo de Nombre del Proyecto o el Presupuesto).
  4. Hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear el proyecto.

#### Caso de Prueba 3: Validación de Fechas Inválidas
- **Descripción**: Verificar que el sistema no permite crear un proyecto si la fecha de inicio es posterior a la fecha de finalización.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Hace clic en el botón **Crear Proyecto**.
  3. Ingresa una fecha de inicio posterior a la fecha de finalización.
  4. Completa el resto de los campos correctamente y hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que la fecha de inicio no puede ser posterior a la fecha de finalización.

#### Caso de Prueba 4: Creación Fallida por Presupuesto en Formato Incorrecto
- **Descripción**: Verificar que el sistema no permite crear un proyecto si el campo de presupuesto contiene un valor en un formato inválido (por ejemplo, letras en lugar de números).
- **Precondiciones**:
  - El cliente está registrado y autenticado.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Hace clic en el botón **Crear Proyecto**.
  3. Ingresa un presupuesto con un formato incorrecto (por ejemplo, "ABC" en lugar de un número).
  4. Completa el resto de los campos y hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el formato del presupuesto es inválido.

#### Caso de Prueba 5: Creación Exitosa de Proyecto con Campos Adicionales
- **Descripción**: Verificar que un proyecto se puede crear con éxito cuando se llenan también los campos opcionales (como la foto de perfil, si existe esta opción).
- **Precondiciones**:
  - El cliente está registrado y autenticado.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Hace clic en el botón **Crear Proyecto**.
  3. Completa todos los campos requeridos, incluyendo la fecha de inicio, finalización y otros campos adicionales (si aplican).
  4. Hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El proyecto se crea exitosamente y los campos adicionales también se reflejan en la vista del proyecto.

#### Caso de Prueba 6: Creación Fallida por Error en el Sistema
- **Descripción**: Verificar que el sistema maneja correctamente los errores internos que impiden la creación del proyecto (por ejemplo, fallos en la conexión o en la base de datos).
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un problema temporal en el servidor o en la base de datos.
- **Pasos**:
  1. El cliente intenta crear un proyecto llenando el formulario correctamente.
  2. Se produce un error en el sistema durante el proceso.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error general indicando que no se pudo crear el proyecto debido a un problema técnico.
  - El cliente puede intentar nuevamente o recibir instrucciones sobre cómo proceder.

#### Caso de Prueba 7: Restricción de Creación de Proyectos por Freelancers
- **Descripción**: Verificar que un freelancer no puede acceder a la funcionalidad de creación de proyectos.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Intenta buscar el botón **Crear Proyecto**.
- **Resultado Esperado**:
  - El botón **Crear Proyecto** no está visible para el freelancer.
  - El sistema no permite al freelancer acceder a la funcionalidad de creación de proyectos.

### Gherkin

Feature: Creación de Proyecto

  Scenario: Creación Exitosa de Proyecto
    Given el cliente está registrado y autenticado
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And hace clic en el botón Crear Proyecto
    And completa todos los campos requeridos: Nombre del proyecto, Especificaciones, Requerimientos, Presupuesto, Fecha de inicio, Fecha de finalización
    And hace clic en Confirmar para enviar el formulario
    Then el proyecto se crea exitosamente
    And la UI se actualiza y el nuevo proyecto aparece en la lista de proyectos
    And aparece una notificación de confirmación indicando que el proyecto se ha creado correctamente

  Scenario: Creación Fallida por Campos Vacíos
    Given el cliente está registrado y autenticado
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And hace clic en el botón Crear Proyecto
    And deja uno o varios campos obligatorios vacíos
    And hace clic en Confirmar
    Then el sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear el proyecto

  Scenario: Validación de Fechas Inválidas
    Given el cliente está registrado y autenticado
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And hace clic en el botón Crear Proyecto
    And ingresa una fecha de inicio posterior a la fecha de finalización
    And completa el resto de los campos correctamente y hace clic en Confirmar
    Then el sistema muestra un mensaje de error indicando que la fecha de inicio no puede ser posterior a la fecha de finalización

  Scenario: Creación Fallida por Presupuesto en Formato Incorrecto
    Given el cliente está registrado y autenticado
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And hace clic en el botón Crear Proyecto
    And ingresa un presupuesto con un formato incorrecto
    And completa el resto de los campos y hace clic en Confirmar
    Then el sistema muestra un mensaje de error indicando que el formato del presupuesto es inválido

  Scenario: Creación Exitosa de Proyecto con Campos Adicionales
    Given el cliente está registrado y autenticado
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And hace clic en el botón Crear Proyecto
    And completa todos los campos requeridos y opcionales
    And hace clic en Confirmar
    Then el proyecto se crea exitosamente
    And los campos adicionales también se reflejan en la vista del proyecto

  Scenario: Creación Fallida por Error en el Sistema
    Given el cliente está registrado y autenticado
    And existe un problema temporal en el servidor o en la base de datos
    When el cliente intenta crear un proyecto llenando el formulario correctamente
    And se produce un error en el sistema durante el proceso
    Then el sistema muestra un mensaje de error general indicando que no se pudo crear el proyecto debido a un problema técnico
    And el cliente puede intentar nuevamente o recibir instrucciones sobre cómo proceder

  Scenario: Restricción de Creación de Proyectos por Freelancers
    Given el freelancer está registrado y autenticado
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And intenta buscar el botón Crear Proyecto
    Then el botón Crear Proyecto no está visible para el freelancer
    And el sistema no permite al freelancer acceder a la funcionalidad de creación de proyectos


### Escenario: Edición de Proyecto por Cliente

#### Caso de Prueba 1: Edición Exitosa de Proyecto
- **Descripción**: Verificar que un cliente puede editar exitosamente la información de un proyecto.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto que desea editar y hace clic en el botón **Editar proyecto**.
  3. Modifica uno o más campos de la información del proyecto (por ejemplo, nombre del proyecto, presupuesto, etc.).
  4. Hace clic en **Guardar cambios** o **Confirmar**.
- **Resultado Esperado**:
  - Los cambios en el proyecto se guardan exitosamente.
  - La UI se actualiza mostrando la nueva información del proyecto.
  - Aparece una notificación de confirmación indicando que la edición fue exitosa.

#### Caso de Prueba 2: Edición Fallida por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite guardar cambios en un proyecto si uno o más campos obligatorios están vacíos.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto que desea editar y hace clic en **Editar proyecto**.
  3. Deja uno o varios campos obligatorios vacíos (por ejemplo, el nombre del proyecto o el presupuesto).
  4. Intenta guardar los cambios.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que los campos obligatorios no pueden estar vacíos.
  - El sistema no guarda los cambios hasta que se completen los campos obligatorios.

#### Caso de Prueba 3: Validación de Fechas Inválidas en la Edición
- **Descripción**: Verificar que el sistema no permite guardar cambios si la fecha de inicio del proyecto es posterior a la fecha de finalización.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona el proyecto y hace clic en **Editar proyecto**.
  2. Cambia la fecha de inicio del proyecto a una fecha posterior a la fecha de finalización.
  3. Intenta guardar los cambios.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que la fecha de inicio no puede ser posterior a la fecha de finalización.
  - El sistema no permite guardar los cambios hasta que las fechas sean válidas.

#### Caso de Prueba 4: Edición Fallida por Formato Incorrecto en el Presupuesto
- **Descripción**: Verificar que el sistema no permite guardar cambios si el presupuesto del proyecto contiene un valor en formato incorrecto (por ejemplo, letras en lugar de números).
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona el proyecto y hace clic en **Editar proyecto**.
  2. Modifica el presupuesto ingresando un valor en formato incorrecto (por ejemplo, letras en lugar de números).
  3. Intenta guardar los cambios.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que el formato del presupuesto es inválido.
  - El sistema no permite guardar los cambios hasta que el presupuesto tenga un formato válido.

#### Caso de Prueba 5: Restricción de Edición para Freelancers
- **Descripción**: Verificar que los freelancers no pueden editar la información de un proyecto.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe al menos un proyecto visible para el freelancer.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona un proyecto al que tiene acceso y verifica si puede ver el botón **Editar proyecto**.
- **Resultado Esperado**:
  - El botón **Editar proyecto** no está visible para el freelancer.
  - El sistema no permite al freelancer realizar cambios en los proyectos.

#### Caso de Prueba 6: Edición Fallida por Error del Sistema
- **Descripción**: Verificar que el sistema maneja correctamente los errores internos que impiden la edición de la información de un proyecto (por ejemplo, fallo en la conexión o en la base de datos).
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
  - El sistema tiene problemas temporales (por ejemplo, conexión o base de datos).
- **Pasos**:
  1. El cliente selecciona un proyecto y hace clic en **Editar proyecto**.
  2. Intenta guardar los cambios en el proyecto.
  3. Ocurre un error en el sistema.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error general indicando que no se pudo guardar la edición debido a un problema técnico.
  - El cliente puede intentar nuevamente o contactar con el soporte si es necesario.

#### Caso de Prueba 7: Verificación de Edición en Tiempo Real
- **Descripción**: Verificar que la información actualizada del proyecto se refleja en tiempo real en la UI después de guardar los cambios.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona un proyecto y hace clic en **Editar proyecto**.
  2. Modifica uno o más campos y hace clic en **Guardar cambios**.
  3. Verifica que los cambios se reflejan inmediatamente en la pantalla del proyecto.
- **Resultado Esperado**:
  - La UI se actualiza en tiempo real mostrando la nueva información del proyecto sin necesidad de recargar la página.
  - Aparece una notificación de confirmación indicando que la edición fue exitosa.

### Gherkin

Feature: Edición de Proyecto

  Scenario: Edición Exitosa de Proyecto
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto que desea editar y hace clic en el botón Editar proyecto
    And modifica uno o más campos de la información del proyecto
    And hace clic en Guardar cambios
    Then los cambios en el proyecto se guardan exitosamente
    And la UI se actualiza mostrando la nueva información del proyecto
    And aparece una notificación de confirmación indicando que la edición fue exitosa

  Scenario: Edición Fallida por Campos Vacíos
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto que desea editar y hace clic en Editar proyecto
    And deja uno o varios campos obligatorios vacíos
    And intenta guardar los cambios
    Then el sistema muestra un mensaje de error indicando que los campos obligatorios no pueden estar vacíos
    And el sistema no guarda los cambios hasta que se completen los campos obligatorios

  Scenario: Validación de Fechas Inválidas en la Edición
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente selecciona el proyecto y hace clic en Editar proyecto
    And cambia la fecha de inicio del proyecto a una fecha posterior a la fecha de finalización
    And intenta guardar los cambios
    Then el sistema muestra un mensaje de error indicando que la fecha de inicio no puede ser posterior a la fecha de finalización
    And el sistema no permite guardar los cambios hasta que las fechas sean válidas

  Scenario: Edición Fallida por Formato Incorrecto en el Presupuesto
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente selecciona el proyecto y hace clic en Editar proyecto
    And modifica el presupuesto ingresando un valor en formato incorrecto
    And intenta guardar los cambios
    Then el sistema muestra un mensaje de error indicando que el formato del presupuesto es inválido
    And el sistema no permite guardar los cambios hasta que el presupuesto tenga un formato válido

  Scenario: Restricción de Edición para Freelancers
    Given el freelancer está registrado y autenticado
    And existe al menos un proyecto visible para el freelancer
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona un proyecto al que tiene acceso y verifica si puede ver el botón Editar proyecto
    Then el botón Editar proyecto no está visible para el freelancer
    And el sistema no permite al freelancer realizar cambios en los proyectos

  Scenario: Edición Fallida por Error del Sistema
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    And el sistema tiene problemas temporales
    When el cliente selecciona un proyecto y hace clic en Editar proyecto
    And intenta guardar los cambios en el proyecto
    And ocurre un error en el sistema
    Then el sistema muestra un mensaje de error general indicando que no se pudo guardar la edición debido a un problema técnico
    And el cliente puede intentar nuevamente o contactar con el soporte si es necesario

  Scenario: Verificación de Edición en Tiempo Real
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente selecciona un proyecto y hace clic en Editar proyecto
    And modifica uno o más campos y hace clic en Guardar cambios
    Then la UI se actualiza en tiempo real mostrando la nueva información del proyecto sin necesidad de recargar la página
    And aparece una notificación de confirmación indicando que la edición fue exitosa


### Escenario: Eliminación de Proyecto por Cliente

#### Caso de Prueba 1: Eliminación Exitosa de un Proyecto
- **Descripción**: Verificar que un cliente puede eliminar un proyecto exitosamente.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto que desea eliminar y accede a la pantalla del proyecto.
  3. Hace clic en el botón **Eliminar proyecto**.
  4. Confirma la eliminación cuando el sistema solicita una confirmación.
- **Resultado Esperado**:
  - El proyecto se elimina exitosamente del sistema.
  - La UI se actualiza y el proyecto desaparece de la lista de proyectos.
  - Aparece una notificación de confirmación indicando que el proyecto fue eliminado correctamente.

#### Caso de Prueba 2: Eliminación Fallida por Cancelación de la Confirmación
- **Descripción**: Verificar que el cliente puede cancelar la eliminación de un proyecto si decide no proceder con la acción.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona un proyecto y hace clic en **Eliminar proyecto**.
  2. El sistema solicita una confirmación de eliminación.
  3. El cliente decide cancelar y no confirmar la eliminación.
- **Resultado Esperado**:
  - El proyecto no se elimina.
  - La UI permanece sin cambios y el proyecto sigue visible en la lista de proyectos.
  - Aparece una notificación indicando que la eliminación fue cancelada.

#### Caso de Prueba 3: Restricción de Eliminación para Freelancers
- **Descripción**: Verificar que los freelancers no pueden eliminar proyectos.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe al menos un proyecto visible para el freelancer.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona un proyecto al que tiene acceso y verifica si puede ver el botón **Eliminar proyecto**.
- **Resultado Esperado**:
  - El botón **Eliminar proyecto** no está visible para el freelancer.
  - El sistema no permite al freelancer eliminar proyectos.

#### Caso de Prueba 4: Eliminación Fallida por Error en el Sistema
- **Descripción**: Verificar que el sistema maneja correctamente los errores internos que impiden la eliminación de un proyecto (por ejemplo, problemas de conexión o base de datos).
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
  - El sistema tiene problemas temporales (por ejemplo, conexión o base de datos).
- **Pasos**:
  1. El cliente selecciona un proyecto y hace clic en **Eliminar proyecto**.
  2. El sistema solicita una confirmación de eliminación.
  3. Ocurre un error en el sistema después de que el cliente confirma la eliminación.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error general indicando que no se pudo eliminar el proyecto debido a un problema técnico.
  - El proyecto sigue visible en la lista de proyectos y no se elimina.

#### Caso de Prueba 5: Eliminación de un Proyecto que Tiene Hitos y Tareas Asociadas
- **Descripción**: Verificar que se puede eliminar un proyecto que tiene hitos, tareas y entregables asociados.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto que contiene hitos, tareas y entregables creados.
- **Pasos**:
  1. El cliente selecciona un proyecto que contiene hitos, tareas y entregables.
  2. Hace clic en **Eliminar proyecto** y confirma la eliminación.
- **Resultado Esperado**:
  - El proyecto, junto con sus hitos, tareas y entregables, se elimina exitosamente.
  - La UI se actualiza y el proyecto desaparece de la lista, junto con todos los elementos relacionados.
  - Aparece una notificación de confirmación indicando que el proyecto y sus componentes fueron eliminados correctamente.

#### Caso de Prueba 6: Verificación de Eliminación en Tiempo Real
- **Descripción**: Verificar que la eliminación de un proyecto se refleja en tiempo real en la UI después de confirmar la eliminación.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona un proyecto y hace clic en **Eliminar proyecto**.
  2. Confirma la eliminación.
  3. Verifica que el proyecto desaparece inmediatamente de la lista sin necesidad de recargar la página.
- **Resultado Esperado**:
  - La UI se actualiza en tiempo real, y el proyecto eliminado ya no aparece en la lista de proyectos.
  - Aparece una notificación de confirmación indicando que el proyecto fue eliminado exitosamente.

### Gherkin

Feature: Eliminación de Proyecto

  Scenario: Eliminación Exitosa de un Proyecto
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto que desea eliminar y accede a la pantalla del proyecto
    And hace clic en el botón Eliminar proyecto
    And confirma la eliminación cuando el sistema solicita una confirmación
    Then el proyecto se elimina exitosamente del sistema
    And la UI se actualiza y el proyecto desaparece de la lista de proyectos
    And aparece una notificación de confirmación indicando que el proyecto fue eliminado correctamente

  Scenario: Eliminación Fallida por Cancelación de la Confirmación
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente selecciona un proyecto y hace clic en Eliminar proyecto
    And el sistema solicita una confirmación de eliminación
    And el cliente decide cancelar y no confirmar la eliminación
    Then el proyecto no se elimina
    And la UI permanece sin cambios y el proyecto sigue visible en la lista de proyectos
    And aparece una notificación indicando que la eliminación fue cancelada

  Scenario: Restricción de Eliminación para Freelancers
    Given el freelancer está registrado y autenticado
    And existe al menos un proyecto visible para el freelancer
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona un proyecto al que tiene acceso y verifica si puede ver el botón Eliminar proyecto
    Then el botón Eliminar proyecto no está visible para el freelancer
    And el sistema no permite al freelancer eliminar proyectos

  Scenario: Eliminación Fallida por Error en el Sistema
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    And el sistema tiene problemas temporales
    When el cliente selecciona un proyecto y hace clic en Eliminar proyecto
    And el sistema solicita una confirmación de eliminación
    And ocurre un error en el sistema después de que el cliente confirma la eliminación
    Then el sistema muestra un mensaje de error general indicando que no se pudo eliminar el proyecto debido a un problema técnico
    And el proyecto sigue visible en la lista de proyectos y no se elimina

  Scenario: Eliminación de un Proyecto que Tiene Hitos y Tareas Asociadas
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto que contiene hitos, tareas y entregables creados
    When el cliente selecciona un proyecto que contiene hitos, tareas y entregables
    And hace clic en Eliminar proyecto y confirma la eliminación
    Then el proyecto, junto con sus hitos, tareas y entregables, se elimina exitosamente
    And la UI se actualiza y el proyecto desaparece de la lista, junto con todos los elementos relacionados
    And aparece una notificación de confirmación indicando que el proyecto y sus componentes fueron eliminados correctamente

  Scenario: Verificación de Eliminación en Tiempo Real
    Given el cliente está registrado y autenticado
    And existe al menos un proyecto creado por el cliente
    When el cliente selecciona un proyecto y hace clic en Eliminar proyecto
    And confirma la eliminación
    And verifica que el proyecto desaparece inmediatamente de la lista sin necesidad de recargar la página
    Then la UI se actualiza en tiempo real, y el proyecto eliminado ya no aparece en la lista de proyectos
    And aparece una notificación de confirmación indicando que el proyecto fue eliminado exitosamente


### Creación de Milestones

#### Caso de Prueba 1: Creación Exitosa de Milestone
- **Descripción**: Verificar que un cliente puede crear un milestone exitosamente dentro de un proyecto.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto al que desea agregar un milestone.
  3. Hace clic en el botón **Crear Milestone**.
  4. Completa todos los campos requeridos (por ejemplo, nombre del hito, fecha de entrega, etc.).
  5. Hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El milestone se crea exitosamente.
  - La UI se actualiza y el nuevo milestone aparece en la lista de hitos del proyecto.
  - Aparece una notificación de confirmación indicando que el milestone fue creado correctamente.

#### Caso de Prueba 2: Creación Fallida por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite crear un milestone si uno o más campos obligatorios están vacíos.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y selecciona un proyecto.
  2. Hace clic en **Crear Milestone**.
  3. Deja uno o varios campos obligatorios vacíos.
  4. Intenta confirmar la creación.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear el milestone.

#### Caso de Prueba 3: Validación de Fecha de Entrega
- **Descripción**: Verificar que el sistema no permite crear un milestone si la fecha de entrega es anterior a la fecha actual.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona un proyecto y hace clic en **Crear Milestone**.
  2. Ingresa una fecha de entrega que es anterior a la fecha actual.
  3. Completa el resto de los campos correctamente y hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual.

### Gherkin 

Feature: Creación de Milestones

  Scenario: Creación Exitosa de Milestone
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto al que desea agregar un milestone
    And hace clic en el botón Crear Milestone
    And completa todos los campos requeridos
    And hace clic en Confirmar
    Then el milestone se crea exitosamente
    And la UI se actualiza y el nuevo milestone aparece en la lista de hitos del proyecto
    And aparece una notificación de confirmación indicando que el milestone fue creado correctamente

  Scenario: Creación Fallida por Campos Vacíos
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente inicia sesión y selecciona un proyecto
    And hace clic en Crear Milestone
    And deja uno o varios campos obligatorios vacíos
    And intenta confirmar la creación
    Then el sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear el milestone

  Scenario: Validación de Fecha de Entrega
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente selecciona un proyecto y hace clic en Crear Milestone
    And ingresa una fecha de entrega que es anterior a la fecha actual
    And completa el resto de los campos correctamente y hace clic en Confirmar
    Then el sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual

### Eliminación de Milestone

#### Caso de Prueba 1: Eliminación Exitosa de Milestone
- **Descripción**: Verificar que un cliente puede eliminar un milestone exitosamente.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un milestone creado dentro de un proyecto del cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto y el milestone que desea eliminar.
  3. Hace clic en el botón **Eliminar Milestone**.
  4. Confirma la eliminación cuando el sistema solicita una confirmación.
- **Resultado Esperado**:
  - El milestone se elimina exitosamente.
  - La UI se actualiza y el milestone desaparece de la lista de hitos del proyecto.
  - Aparece una notificación de confirmación indicando que el milestone fue eliminado correctamente.

#### Caso de Prueba 2: Eliminación Fallida por Cancelación de la Confirmación
- **Descripción**: Verificar que el cliente puede cancelar la eliminación de un milestone si decide no proceder con la acción.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un milestone creado dentro de un proyecto del cliente.
- **Pasos**:
  1. El cliente selecciona un milestone y hace clic en **Eliminar Milestone**.
  2. El sistema solicita una confirmación de eliminación.
  3. El cliente decide cancelar y no confirma la eliminación.
- **Resultado Esperado**:
  - El milestone no se elimina.
  - La UI permanece sin cambios y el milestone sigue visible en la lista de hitos del proyecto.

#### Caso de Prueba 3: Restricción de Eliminación para Freelancers
- **Descripción**: Verificar que los freelancers no pueden eliminar milestones.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe al menos un milestone visible para el freelancer.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona un proyecto y verifica si puede ver el botón **Eliminar Milestone**.
- **Resultado Esperado**:
  - El botón **Eliminar Milestone** no está visible para el freelancer.
  - El sistema no permite al freelancer eliminar milestones.

### Gherkin

Feature: Eliminación de Milestones

  Scenario: Eliminación Exitosa de Milestone
    Given el cliente está registrado y autenticado
    And existe al menos un milestone creado dentro de un proyecto del cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto y el milestone que desea eliminar
    And hace clic en el botón Eliminar Milestone
    And confirma la eliminación cuando el sistema solicita una confirmación
    Then el milestone se elimina exitosamente
    And la UI se actualiza y el milestone desaparece de la lista de hitos del proyecto
    And aparece una notificación de confirmación indicando que el milestone fue eliminado correctamente

  Scenario: Eliminación Fallida por Cancelación de la Confirmación
    Given el cliente está registrado y autenticado
    And existe al menos un milestone creado dentro de un proyecto del cliente
    When el cliente selecciona un milestone y hace clic en Eliminar Milestone
    And el sistema solicita una confirmación de eliminación
    And el cliente decide cancelar y no confirma la eliminación
    Then el milestone no se elimina
    And la UI permanece sin cambios y el milestone sigue visible en la lista de hitos del proyecto

  Scenario: Restricción de Eliminación para Freelancers
    Given el freelancer está registrado y autenticado
    And existe al menos un milestone visible para el freelancer
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona un proyecto y verifica si puede ver el botón Eliminar Milestone
    Then el botón Eliminar Milestone no está visible para el freelancer
    And el sistema no permite al freelancer eliminar milestones

### Edición de una Milestone

#### Caso de Prueba 1: Edición Exitosa de Milestone
- **Descripción**: Verificar que un cliente puede editar exitosamente la información de un milestone.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un milestone creado dentro de un proyecto del cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto y el milestone que desea editar.
  3. Hace clic en el botón **Editar Milestone**.
  4. Modifica uno o más campos de la información del milestone (por ejemplo, fecha de entrega, nombre del hito, etc.).
  5. Hace clic en **Guardar cambios** o **Confirmar**.
- **Resultado Esperado**:
  - Los cambios en el milestone se guardan exitosamente.
  - La UI se actualiza mostrando la nueva información del milestone.
  - Aparece una notificación de confirmación indicando que la edición fue exitosa.

#### Caso de Prueba 2: Edición Fallida por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite guardar cambios en un milestone si uno o más campos obligatorios están vacíos.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un milestone creado dentro de un proyecto del cliente.
- **Pasos**:
  1. El cliente selecciona un milestone y hace clic en **Editar Milestone**.
  2. Deja uno o varios campos obligatorios vacíos.
  3. Intenta guardar los cambios.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que los campos obligatorios no pueden estar vacíos.
  - El sistema no guarda los cambios hasta que se completen los campos obligatorios.

#### Caso de Prueba 3: Validación de Fecha de Entrega en la Edición
- **Descripción**: Verificar que el sistema no permite guardar cambios si la nueva fecha de entrega es anterior a la fecha actual.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe al menos un milestone creado dentro de un proyecto del cliente.
- **Pasos**:
  1. El cliente selecciona un milestone y hace clic en **Editar Milestone**.
  2. Cambia la fecha de entrega a una fecha anterior a la fecha actual.
  3. Intenta guardar los cambios.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual.

#### Caso de Prueba 4: Restricción de Edición para Freelancers
- **Descripción**: Verificar que los freelancers no pueden editar la información de un milestone.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe al menos un milestone visible para el freelancer.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona un proyecto y un milestone.
  3. Intenta buscar el botón **Editar Milestone**.
- **Resultado Esperado**:
  - El botón **Editar Milestone** no está visible para el freelancer.
  - El sistema no permite al freelancer realizar cambios en los milestones.

### Gherkin

Feature: Edición de Milestones

  Scenario: Edición Exitosa de Milestone
    Given el cliente está registrado y autenticado
    And existe al menos un milestone creado dentro de un proyecto del cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto y el milestone que desea editar
    And hace clic en el botón Editar Milestone
    And modifica uno o más campos de la información del milestone
    And hace clic en Guardar cambios
    Then los cambios en el milestone se guardan exitosamente
    And la UI se actualiza mostrando la nueva información del milestone
    And aparece una notificación de confirmación indicando que la edición fue exitosa

  Scenario: Edición Fallida por Campos Vacíos
    Given el cliente está registrado y autenticado
    And existe al menos un milestone creado dentro de un proyecto del cliente
    When el cliente selecciona un milestone y hace clic en Editar Milestone
    And deja uno o varios campos obligatorios vacíos
    And intenta guardar los cambios
    Then el sistema muestra un mensaje de error indicando que los campos obligatorios no pueden estar vacíos
    And el sistema no guarda los cambios hasta que se completen los campos obligatorios

  Scenario: Validación de Fecha de Entrega en la Edición
    Given el cliente está registrado y autenticado
    And existe al menos un milestone creado dentro de un proyecto del cliente
    When el cliente selecciona un milestone y hace clic en Editar Milestone
    And cambia la fecha de entrega a una fecha anterior a la fecha actual
    And intenta guardar los cambios
    Then el sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual

  Scenario: Restricción de Edición para Freelancers
    Given el freelancer está registrado y autenticado
    And existe al menos un milestone visible para el freelancer
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona un proyecto y un milestone
    And intenta buscar el botón Editar Milestone
    Then el botón Editar Milestone no está visible para el freelancer
    And el sistema no permite al freelancer realizar cambios en los milestones


### Creación de Entregables dentro de una Milestone

#### Caso de Prueba 1: Creación Exitosa de Entregable
- **Descripción**: Verificar que un cliente puede crear un entregable exitosamente dentro de una milestone.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente con al menos una milestone.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto que contiene la milestone donde desea agregar un entregable.
  3. Accede a la sección de la milestone y hace clic en el botón **Crear Entregable**.
  4. Completa todos los campos requeridos (por ejemplo, nombre del entregable, descripción, fecha de entrega, etc.).
  5. Hace clic en **Confirmar** o **Guardar**.
- **Resultado Esperado**:
  - El entregable se crea exitosamente.
  - La UI se actualiza y el nuevo entregable aparece en la lista de entregables de la milestone.
  - Aparece una notificación de confirmación indicando que el entregable fue creado correctamente.

#### Caso de Prueba 2: Creación Fallida por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite crear un entregable si uno o más campos obligatorios están vacíos.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente con al menos una milestone.
- **Pasos**:
  1. El cliente inicia sesión y selecciona el proyecto y la milestone.
  2. Hace clic en **Crear Entregable**.
  3. Deja uno o varios campos obligatorios vacíos.
  4. Intenta confirmar la creación.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear el entregable.

#### Caso de Prueba 3: Validación de Fecha de Entrega
- **Descripción**: Verificar que el sistema no permite crear un entregable si la fecha de entrega es anterior a la fecha actual.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente con al menos una milestone.
- **Pasos**:
  1. El cliente selecciona el proyecto y la milestone.
  2. Hace clic en **Crear Entregable**.
  3. Ingresa una fecha de entrega que es anterior a la fecha actual.
  4. Completa el resto de los campos correctamente y hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual.

#### Caso de Prueba 4: Restricción de Creación para Freelancers
- **Descripción**: Verificar que los freelancers no pueden crear entregables dentro de una milestone.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe un proyecto creado por un cliente con al menos una milestone visible para el freelancer.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto y la milestone.
  3. Busca el botón **Crear Entregable** y verifica si está visible.
- **Resultado Esperado**:
  - El botón **Crear Entregable** no está visible para el freelancer.
  - El sistema no permite al freelancer crear entregables dentro de milestones.

#### Caso de Prueba 5: Verificación de Creación en Tiempo Real
- **Descripción**: Verificar que la creación de un entregable se refleja en tiempo real en la UI después de confirmar la creación.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente con al menos una milestone.
- **Pasos**:
  1. El cliente selecciona el proyecto y la milestone.
  2. Hace clic en **Crear Entregable** y completa los campos requeridos.
  3. Hace clic en **Confirmar**.
  4. Verifica que el entregable aparece inmediatamente en la lista de entregables sin necesidad de recargar la página.
- **Resultado Esperado**:
  - La UI se actualiza en tiempo real, y el nuevo entregable ya aparece en la lista de entregables de la milestone.
  - Aparece una notificación de confirmación indicando que el entregable fue creado exitosamente.

### Gherkin

Feature: Creación de Entregables dentro de una Milestone

  Scenario: Creación Exitosa de Entregable
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente con al menos una milestone
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto que contiene la milestone
    And accede a la sección de la milestone
    And hace clic en el botón Crear Entregable
    And completa todos los campos requeridos
    And hace clic en Confirmar
    Then el entregable se crea exitosamente
    And la UI se actualiza mostrando el nuevo entregable en la lista de entregables de la milestone
    And aparece una notificación de confirmación indicando que el entregable fue creado correctamente

  Scenario: Creación Fallida por Campos Vacíos
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente con al menos una milestone
    When el cliente inicia sesión y selecciona el proyecto y la milestone
    And hace clic en Crear Entregable
    And deja uno o varios campos obligatorios vacíos
    And intenta confirmar la creación
    Then el sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear el entregable

  Scenario: Validación de Fecha de Entrega
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente con al menos una milestone
    When el cliente selecciona el proyecto y la milestone
    And hace clic en Crear Entregable
    And ingresa una fecha de entrega que es anterior a la fecha actual
    And completa el resto de los campos correctamente
    And hace clic en Confirmar
    Then el sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual

  Scenario: Restricción de Creación para Freelancers
    Given el freelancer está registrado y autenticado
    And existe un proyecto creado por un cliente con al menos una milestone visible para el freelancer
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto y la milestone
    And busca el botón Crear Entregable
    Then el botón Crear Entregable no está visible para el freelancer
    And el sistema no permite al freelancer crear entregables dentro de milestones

  Scenario: Verificación de Creación en Tiempo Real
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente con al menos una milestone
    When el cliente selecciona el proyecto y la milestone
    And hace clic en Crear Entregable y completa los campos requeridos
    And hace clic en Confirmar
    Then la UI se actualiza en tiempo real mostrando el nuevo entregable en la lista de entregables de la milestone
    And aparece una notificación de confirmación indicando que el entregable fue creado exitosamente


### Creación de Tareas

#### Caso de Prueba 1: Creación Exitosa de Tarea
- **Descripción**: Verificar que un cliente puede crear una tarea exitosamente dentro de un proyecto.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto en el que desea agregar una tarea.
  3. Accede a la sección de **Tareas** dentro del proyecto.
  4. Hace clic en el botón **Crear Tarea**.
  5. Completa todos los campos requeridos (por ejemplo, nombre de la tarea, descripción, fecha de entrega, etc.).
  6. Hace clic en **Confirmar** o **Guardar**.
- **Resultado Esperado**:
  - La tarea se crea exitosamente.
  - La UI se actualiza y la nueva tarea aparece en la lista de tareas del proyecto.
  - Aparece una notificación de confirmación indicando que la tarea fue creada correctamente.

#### Caso de Prueba 2: Creación Fallida por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite crear una tarea si uno o más campos obligatorios están vacíos.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y selecciona el proyecto.
  2. Navega a la sección de **Tareas** y hace clic en **Crear Tarea**.
  3. Deja uno o varios campos obligatorios vacíos.
  4. Intenta confirmar la creación.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear la tarea.

#### Caso de Prueba 3: Validación de Fecha de Entrega
- **Descripción**: Verificar que el sistema no permite crear una tarea si la fecha de entrega es anterior a la fecha actual.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona el proyecto y navega a la sección de **Tareas**.
  2. Hace clic en **Crear Tarea**.
  3. Ingresa una fecha de entrega que es anterior a la fecha actual.
  4. Completa el resto de los campos correctamente y hace clic en **Confirmar**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual.

#### Caso de Prueba 4: Restricción de Creación para Freelancers
- **Descripción**: Verificar que los freelancers no pueden crear tareas dentro de un proyecto.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe un proyecto creado por un cliente con al menos una tarea visible para el freelancer.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto y verifica si puede ver el botón **Crear Tarea**.
- **Resultado Esperado**:
  - El botón **Crear Tarea** no está visible para el freelancer.
  - El sistema no permite al freelancer crear tareas dentro de un proyecto.

#### Caso de Prueba 5: Verificación de Creación en Tiempo Real
- **Descripción**: Verificar que la creación de una tarea se refleja en tiempo real en la UI después de confirmar la creación.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente selecciona el proyecto y navega a la sección de **Tareas**.
  2. Hace clic en **Crear Tarea** y completa los campos requeridos.
  3. Hace clic en **Confirmar**.
  4. Verifica que la tarea aparece inmediatamente en la lista de tareas sin necesidad de recargar la página.
- **Resultado Esperado**:
  - La UI se actualiza en tiempo real, y la nueva tarea ya aparece en la lista de tareas del proyecto.
  - Aparece una notificación de confirmación indicando que la tarea fue creada exitosamente.

### Gherkin

Feature: Creación de Tareas

  Scenario: Creación Exitosa de Tarea
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto en el que desea agregar una tarea
    And accede a la sección de Tareas dentro del proyecto
    And hace clic en el botón Crear Tarea
    And completa todos los campos requeridos
    And hace clic en Confirmar
    Then la tarea se crea exitosamente
    And la UI se actualiza mostrando la nueva tarea en la lista de tareas del proyecto
    And aparece una notificación de confirmación indicando que la tarea fue creada correctamente

  Scenario: Creación Fallida por Campos Vacíos
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente inicia sesión y selecciona el proyecto
    And navega a la sección de Tareas y hace clic en Crear Tarea
    And deja uno o varios campos obligatorios vacíos
    And intenta confirmar la creación
    Then el sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear la tarea

  Scenario: Validación de Fecha de Entrega
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente selecciona el proyecto y navega a la sección de Tareas
    And hace clic en Crear Tarea
    And ingresa una fecha de entrega que es anterior a la fecha actual
    And completa el resto de los campos correctamente
    And hace clic en Confirmar
    Then el sistema muestra un mensaje de error indicando que la fecha de entrega no puede ser anterior a la fecha actual

  Scenario: Restricción de Creación para Freelancers
    Given el freelancer está registrado y autenticado
    And existe un proyecto creado por un cliente con al menos una tarea visible para el freelancer
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto
    And verifica si puede ver el botón Crear Tarea
    Then el botón Crear Tarea no está visible para el freelancer
    And el sistema no permite al freelancer crear tareas dentro de un proyecto

  Scenario: Verificación de Creación en Tiempo Real
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente selecciona el proyecto y navega a la sección de Tareas
    And hace clic en Crear Tarea y completa los campos requeridos
    And hace clic en Confirmar
    Then la UI se actualiza en tiempo real mostrando la nueva tarea en la lista de tareas del proyecto
    And aparece una notificación de confirmación indicando que la tarea fue creada exitosamente


### Generación de Informe de Reporte

#### Caso de Prueba 1: Generación Exitosa de Informe
- **Descripción**: Verificar que un cliente puede generar un informe de progreso exitosamente dentro de un proyecto.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente que tiene hitos y tareas.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto del cual desea generar un informe.
  3. Accede a la sección **Progreso** dentro del proyecto.
  4. Hace clic en el botón **Generar Informe**.
- **Resultado Esperado**:
  - El informe se genera exitosamente y se muestra en pantalla o se descarga.
  - El informe incluye el progreso de los hitos y tareas, con información detallada según las especificaciones.

#### Caso de Prueba 2: Informe sin Progreso
- **Descripción**: Verificar que se maneja correctamente la situación en la que no hay hitos o tareas disponibles para generar un informe.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente que no tiene hitos ni tareas.
- **Pasos**:
  1. El cliente inicia sesión y selecciona el proyecto.
  2. Accede a la sección **Progreso**.
  3. Hace clic en el botón **Generar Informe**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje indicando que no se puede generar el informe porque no hay hitos o tareas disponibles.
  - No se genera un informe en blanco.

#### Caso de Prueba 3: Validación de Acceso para Freelancers
- **Descripción**: Verificar que los freelancers no pueden generar informes de progreso para un proyecto.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe un proyecto creado por un cliente que tiene hitos y tareas.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto y accede a la sección **Progreso**.
  3. Busca el botón **Generar Informe**.
- **Resultado Esperado**:
  - El botón **Generar Informe** no está visible para el freelancer.
  - El sistema no permite al freelancer generar informes de progreso.

#### Caso de Prueba 4: Verificación de Contenido del Informe
- **Descripción**: Verificar que el informe generado contiene la información correcta y está bien estructurada.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente con hitos y tareas.
- **Pasos**:
  1. El cliente genera el informe desde la sección **Progreso**.
  2. Revisa el contenido del informe generado.
- **Resultado Esperado**:
  - El informe incluye:
    - Progreso de los hitos (porcentaje general).
    - Progreso de las tareas (porcentaje general).
    - Lista detallada de hitos y tareas con su estado (ej. pendiente, completada).
    - Fechas de entrega de las tareas y hitos.

#### Caso de Prueba 5: Verificación de Generación en Tiempo Real
- **Descripción**: Verificar que los cambios realizados en hitos y tareas se reflejan en el informe generado.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente que tiene hitos y tareas.
- **Pasos**:
  1. El cliente modifica el estado de uno o más hitos o tareas.
  2. Genera el informe desde la sección **Progreso**.
  3. Verifica que el informe refleja los cambios realizados.
- **Resultado Esperado**:
  - El informe generado incluye la información actualizada sobre los hitos y tareas.

### Gherkin

Feature: Generación de Informe de Reporte

  Scenario: Generación Exitosa de Informe
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente que tiene hitos y tareas
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto del cual desea generar un informe
    And accede a la sección Progreso dentro del proyecto
    And hace clic en el botón Generar Informe
    Then el informe se genera exitosamente y se muestra en pantalla o se descarga
    And el informe incluye el progreso de los hitos y tareas con información detallada según las especificaciones

  Scenario: Informe sin Progreso
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente que no tiene hitos ni tareas
    When el cliente inicia sesión y selecciona el proyecto
    And accede a la sección Progreso
    And hace clic en el botón Generar Informe
    Then el sistema muestra un mensaje indicando que no se puede generar el informe porque no hay hitos o tareas disponibles
    And no se genera un informe en blanco

  Scenario: Validación de Acceso para Freelancers
    Given el freelancer está registrado y autenticado
    And existe un proyecto creado por un cliente que tiene hitos y tareas
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto y accede a la sección Progreso
    And busca el botón Generar Informe
    Then el botón Generar Informe no está visible para el freelancer
    And el sistema no permite al freelancer generar informes de progreso

  Scenario: Verificación de Contenido del Informe
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente con hitos y tareas
    When el cliente genera el informe desde la sección Progreso
    And revisa el contenido del informe generado
    Then el informe incluye:
      | Progreso de los hitos        | porcentaje general   |
      | Progreso de las tareas       | porcentaje general   |
      | Lista detallada de hitos y tareas | estado (ej. pendiente, completada) |
      | Fechas de entrega de tareas y hitos |                      |

  Scenario: Verificación de Generación en Tiempo Real
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente que tiene hitos y tareas
    When el cliente modifica el estado de uno o más hitos o tareas
    And genera el informe desde la sección Progreso
    Then el informe generado incluye la información actualizada sobre los hitos y tareas


### Creación de Actualizaciones del Proyecto

#### Caso de Prueba 1: Creación Exitosa de Actualización
- **Descripción**: Verificar que un cliente puede crear una actualización de proyecto exitosamente.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto al que desea agregar una actualización.
  3. Accede a la sección de **Actualizaciones** dentro del proyecto.
  4. Hace clic en el botón **Crear Actualización**.
  5. Completa todos los campos requeridos (por ejemplo, título de la actualización, descripción, etc.).
  6. Hace clic en **Confirmar** o **Guardar**.
- **Resultado Esperado**:
  - La actualización se crea exitosamente.
  - La UI se actualiza y la nueva actualización aparece en la lista de actualizaciones del proyecto.
  - Aparece una notificación de confirmación indicando que la actualización fue creada correctamente.

#### Caso de Prueba 2: Creación Fallida por Campos Vacíos
- **Descripción**: Verificar que el sistema no permite crear una actualización si uno o más campos obligatorios están vacíos.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente inicia sesión y selecciona el proyecto.
  2. Navega a la sección de **Actualizaciones** y hace clic en **Crear Actualización**.
  3. Deja uno o varios campos obligatorios vacíos.
  4. Intenta confirmar la creación.
- **Resultado Esperado**:
  - El sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear la actualización.

#### Caso de Prueba 3: Restricción de Creación para Freelancers
- **Descripción**: Verificar que los freelancers no pueden crear actualizaciones del proyecto.
- **Precondiciones**:
  - El freelancer está registrado y autenticado.
  - Existe un proyecto creado por un cliente.
- **Pasos**:
  1. El freelancer inicia sesión y navega a la sección **Mis proyectos**.
  2. Selecciona el proyecto y verifica si puede ver el botón **Crear Actualización**.
- **Resultado Esperado**:
  - El botón **Crear Actualización** no está visible para el freelancer.
  - El sistema no permite al freelancer crear actualizaciones.

#### Caso de Prueba 4: Verificación de Contenido de la Actualización
- **Descripción**: Verificar que la actualización creada contiene la información correcta y está bien estructurada.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existe un proyecto creado por el cliente.
- **Pasos**:
  1. El cliente genera una actualización desde la sección **Actualizaciones**.
  2. Revisa el contenido de la actualización creada.
- **Resultado Esperado**:
  - La actualización incluye la información ingresada, como el título y la descripción, y está bien estructurada en la lista de actualizaciones.

### Gherkin

Feature: Creación de Actualizaciones del Proyecto

  Scenario: Creación Exitosa de Actualización
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto al que desea agregar una actualización
    And accede a la sección de Actualizaciones dentro del proyecto
    And hace clic en el botón Crear Actualización
    And completa todos los campos requeridos
    And hace clic en Confirmar
    Then la actualización se crea exitosamente
    And la UI se actualiza y la nueva actualización aparece en la lista de actualizaciones del proyecto
    And aparece una notificación de confirmación indicando que la actualización fue creada correctamente

  Scenario: Creación Fallida por Campos Vacíos
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente inicia sesión y selecciona el proyecto
    And navega a la sección de Actualizaciones y hace clic en Crear Actualización
    And deja uno o varios campos obligatorios vacíos
    And intenta confirmar la creación
    Then el sistema muestra un mensaje de error indicando que los campos obligatorios deben completarse antes de crear la actualización

  Scenario: Restricción de Creación para Freelancers
    Given el freelancer está registrado y autenticado
    And existe un proyecto creado por un cliente
    When el freelancer inicia sesión y navega a la sección Mis proyectos
    And selecciona el proyecto y verifica si puede ver el botón Crear Actualización
    Then el botón Crear Actualización no está visible para el freelancer
    And el sistema no permite al freelancer crear actualizaciones

  Scenario: Verificación de Contenido de la Actualización
    Given el cliente está registrado y autenticado
    And existe un proyecto creado por el cliente
    When el cliente genera una actualización desde la sección Actualizaciones
    And revisa el contenido de la actualización creada
    Then la actualización incluye la información ingresada, como el título y la descripción, y está bien estructurada en la lista de actualizaciones

### Búsqueda de un Proyecto

#### Caso de Prueba 1: Búsqueda Exitosa de Proyecto
- **Descripción**: Verificar que un cliente puede buscar un proyecto exitosamente desde el dashboard.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existen proyectos en la plataforma.
- **Pasos**:
  1. El cliente inicia sesión y accede al **Dashboard**.
  2. Introduce el nombre del proyecto en el campo de búsqueda.
  3. Hace clic en el botón **Buscar** o presiona **Enter**.
- **Resultado Esperado**:
  - Los resultados de búsqueda muestran el proyecto correspondiente al nombre ingresado.
  - El cliente puede hacer clic en el proyecto para acceder a su información.

#### Caso de Prueba 2: Búsqueda sin Resultados
- **Descripción**: Verificar que el sistema maneja correctamente la situación en la que no se encuentran proyectos que coincidan con la búsqueda.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existen proyectos en la plataforma.
- **Pasos**:
  1. El cliente inicia sesión y accede al **Dashboard**.
  2. Introduce un nombre de proyecto que no existe en la plataforma.
  3. Hace clic en el botón **Buscar** o presiona **Enter**.
- **Resultado Esperado**:
  - El sistema muestra un mensaje indicando que no se encontraron proyectos que coincidan con la búsqueda.

#### Caso de Prueba 3: Búsqueda con Término Parcial
- **Descripción**: Verificar que el sistema permite buscar proyectos usando términos parciales.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existen proyectos en la plataforma.
- **Pasos**:
  1. El cliente inicia sesión y accede al **Dashboard**.
  2. Introduce un término parcial del nombre del proyecto en el campo de búsqueda.
  3. Hace clic en el botón **Buscar** o presiona **Enter**.
- **Resultado Esperado**:
  - Los resultados de búsqueda muestran todos los proyectos que contienen el término parcial ingresado.

#### Caso de Prueba 4: Verificación de Búsqueda en Tiempo Real
- **Descripción**: Verificar que la búsqueda de proyectos se actualiza en tiempo real a medida que se escribe en el campo de búsqueda.
- **Precondiciones**:
  - El cliente está registrado y autenticado.
  - Existen proyectos en la plataforma.
- **Pasos**:
  1. El cliente inicia sesión y accede al **Dashboard**.
  2. Empieza a escribir en el campo de búsqueda.
- **Resultado Esperado**:
  - La lista de proyectos se actualiza en tiempo real, mostrando solo aquellos que coinciden con el término ingresado.

### Gherkin

Feature: Búsqueda de un Proyecto

  Scenario: Búsqueda Exitosa de Proyecto
    Given el cliente está registrado y autenticado
    And existen proyectos en la plataforma
    When el cliente inicia sesión y accede al Dashboard
    And introduce el nombre del proyecto en el campo de búsqueda
    And hace clic en el botón Buscar
    Then los resultados de búsqueda muestran el proyecto correspondiente al nombre ingresado
    And el cliente puede hacer clic en el proyecto para acceder a su información

  Scenario: Búsqueda sin Resultados
    Given el cliente está registrado y autenticado
    And existen proyectos en la plataforma
    When el cliente inicia sesión y accede al Dashboard
    And introduce un nombre de proyecto que no existe en la plataforma
    And hace clic en el botón Buscar
    Then el sistema muestra un mensaje indicando que no se encontraron proyectos que coincidan con la búsqueda

  Scenario: Búsqueda con Término Parcial
    Given el cliente está registrado y autenticado
    And existen proyectos en la plataforma
    When el cliente inicia sesión y accede al Dashboard
    And introduce un término parcial del nombre del proyecto en el campo de búsqueda
    And hace clic en el botón Buscar
    Then los resultados de búsqueda muestran todos los proyectos que contienen el término parcial ingresado

  Scenario: Verificación de Búsqueda en Tiempo Real
    Given el cliente está registrado y autenticado
    And existen proyectos en la plataforma
    When el cliente inicia sesión y accede al Dashboard
    And empieza a escribir en el campo de búsqueda
    Then la lista de proyectos se actualiza en tiempo real, mostrando solo aquellos que coinciden con el término ingresado
