### Configuración del Escenario para LoginTests

| **Nombre**   | **Clase** | **Escenario**                                                                 |
|--------------|-----------|-------------------------------------------------------------------------------|
| client     | Client | Cliente de prueba configurado para simular solicitudes HTTP.                  |
| user       | User   | Usuario de prueba creado con credenciales válidas (username='testuser').    |
| login_url | str    | URL de inicio de sesión para probar la vista de login.                        |

### Pruebas

**Test:** `test_login_view_GET`

**Objetivo:** Verificar que la vista de inicio de sesión se cargue correctamente y utilice la plantilla adecuada.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema.
- No se requiere autenticación previa para acceder a la página de login.

**Datos de Entrada:**

No se requieren datos de entrada específicos para este test, ya que solo se verifica la visualización de la página.

**Pasos Realizados:**

1. Se envía una solicitud GET a la URL de login (`login_url`).
2. Se verifica que el código de estado de la respuesta sea `200`.
3. Se comprueba que se utiliza la plantilla `login/login.html`.
4. Se verifica que la respuesta contenga el texto 'Email / NIT', asegurando que el formulario de inicio de sesión se renderiza correctamente.

**Resultados Esperados:**

| **Resultado**                        | **Descripción**                                                     |
|--------------------------------------|---------------------------------------------------------------------|
| Código de estado correcto            | La respuesta debe tener un código de estado `200`.                  |
| Plantilla adecuada                   | Se debe utilizar la plantilla `login/login.html`.                   |
| Formulario renderizado correctamente | La respuesta debe contener el texto 'Email / NIT'.                  |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que la vista de inicio de sesión se carga y se muestra correctamente.

---

**Test:** `test_login_view_POST_valid_credentials`

**Objetivo:** Verificar que un usuario pueda iniciar sesión correctamente utilizando credenciales válidas.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema con la contraseña `12345`.

**Datos de Entrada:**

| **Campo**    | **Valor**      |
|--------------|----------------|
| `username`   | `testuser`     |
| `password`   | `12345`        |

**Pasos Realizados:**

1. Se envía una solicitud POST a la URL de login con credenciales válidas.
2. Se verifica que la respuesta redirija correctamente a `/dashboard/`, indicando un inicio de sesión exitoso.

**Resultados Esperados:**

| **Resultado**                         | **Descripción**                                                        |
|---------------------------------------|------------------------------------------------------------------------|
| Redirección correcta                  | La respuesta debe redirigir a `/dashboard/`, confirmando el login.     |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el usuario puede iniciar sesión con credenciales válidas.

---

**Test:** `test_login_view_POST_invalid_credentials`

**Objetivo:** Verificar que el sistema maneje adecuadamente el intento de inicio de sesión con credenciales inválidas.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema.

**Datos de Entrada:**

| **Campo**    | **Valor**          |
|--------------|--------------------|
| `username`   | `testuser`         |
| `password`   | `wrongpassword`    |

**Pasos Realizados:**

1. Se envía una solicitud POST a la URL de login con credenciales incorrectas.
2. Se verifica que el código de estado de la respuesta sea `200`, manteniendo al usuario en la página de inicio de sesión.
3. Se comprueba que se utiliza la plantilla `login/login.html`.
4. Se verifica que aparezca un mensaje de error indicando "Por favor revise su usuario y contraseña".

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                              |
|---------------------------------|------------------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                          |
| Plantilla de login mostrada     | Se debe utilizar la plantilla `login/login.html`.                           |
| Mensaje de error presente       | Debe mostrarse un mensaje indicando "Por favor revise su usuario y contraseña". |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el sistema maneja los intentos fallidos de inicio de sesión mostrando el mensaje de error adecuado.

---

**Test:** `test_login_view_POST_empty_fields`

**Objetivo:** Verificar que el sistema maneje adecuadamente el intento de inicio de sesión con campos vacíos.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema.

**Datos de Entrada:**

| **Campo**    | **Valor** |
|--------------|-----------|
| `username`   | ` `       |
| `password`   | ` `       |

**Pasos Realizados:**

1. Se envía una solicitud POST a la URL de login con campos vacíos.
2. Se verifica que el código de estado de la respuesta sea `200`, manteniendo al usuario en la página de inicio de sesión.
3. Se comprueba que se utiliza la plantilla `login/login.html`.
4. Se verifica que aparezca un mensaje de error indicando "Por favor revise su usuario y contraseña".

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                              |
|---------------------------------|------------------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                          |
| Plantilla de login mostrada     | Se debe utilizar la plantilla `login/login.html`.                           |
| Mensaje de error presente       | Debe mostrarse un mensaje indicando "Por favor revise su usuario y contraseña". |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el sistema maneja correctamente los intentos de inicio de sesión con campos vacíos.