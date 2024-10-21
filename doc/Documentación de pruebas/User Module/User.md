# Documentación de Tests

## Configuración del Escenario para `LoginViewTests`

| Nombre            | Clase                | Escenario                                                    |
|-------------------|----------------------|--------------------------------------------------------------|
| user              | User                 | Usuario de prueba creado para la ejecución del test.          |
| freelancer_profile| FreelancerProfile     | Perfil de freelancer asociado al usuario.                    |
| login_url         | URL                  | URL de la vista de inicio de sesión.                         |
| restore_password_url | URL               | URL de la vista de restauración de contraseña.               |

---

### Pruebas

**Test:** `test_login_view_GET`

**Objetivo:** Verificar que la vista de inicio de sesión se carga correctamente.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `login`.
2. Se verifica que el código de estado sea 200 y que se esté utilizando la plantilla correcta.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'login/login.html'`.                    |
| Texto visible en la vista       | La vista debe contener el texto `Email / NIT`.                      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de inicio de sesión se carga correctamente.

---

**Test:** `test_login_view_POST_valid_credentials`

**Objetivo:** Verificar que el usuario es redirigido correctamente al autenticarse con credenciales válidas y que el flujo de 2FA es activado.

**Precondiciones:**
- El usuario debe existir y tener habilitado el 2FA.

**Datos de Entrada:**

| **Campo**      | **Valor**      |
|----------------|----------------|
| username       | `testuser`     |
| password       | `12345`        |

**Pasos Realizados:**
1. Se realiza una solicitud POST a la vista `login` con credenciales válidas.
2. Se verifica que el usuario es redirigido a la vista de 2FA.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Redirección a 2FA              | La respuesta debe redirigir a la URL `/two_factor_auth/`.            |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario es redirigido al flujo de 2FA.

---

**Test:** `test_login_view_POST_invalid_credentials`

**Objetivo:** Verificar que el usuario recibe un mensaje de error al ingresar credenciales incorrectas.

**Precondiciones:**
- El usuario debe existir.

**Datos de Entrada:**

| **Campo**      | **Valor**          |
|----------------|--------------------|
| username       | `testuser`         |
| password       | `wrongpassword`    |

**Pasos Realizados:**
1. Se realiza una solicitud POST a la vista `login` con credenciales inválidas.
2. Se verifica que el código de estado sea 200 y que se muestre un mensaje de error.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Mensaje de error                | Debe mostrarse el mensaje `Por favor revise su usuario y contraseña`.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el mensaje de error se muestra correctamente.

---

**Test:** `test_login_view_POST_empty_fields`

**Objetivo:** Verificar que el usuario recibe un mensaje de error al enviar campos vacíos.

**Precondiciones:**
- Ninguna.

**Datos de Entrada:**

| **Campo**      | **Valor**          |
|----------------|--------------------|
| username       | (vacío)            |
| password       | (vacío)            |

**Pasos Realizados:**
1. Se realiza una solicitud POST a la vista `login` con campos vacíos.
2. Se verifica que el código de estado sea 200 y que se muestre un mensaje de error.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Mensaje de error                | Debe mostrarse el mensaje `Por favor revise su usuario y contraseña`.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el mensaje de error se muestra correctamente.

---

**Test:** `test_login_view_POST_otp_email_sent`

**Objetivo:** Verificar que al iniciar sesión, se guarda el usuario en sesión para el proceso de 2FA.

**Precondiciones:**
- El usuario debe tener habilitado el 2FA.

**Datos de Entrada:**

| **Campo**      | **Valor**      |
|----------------|----------------|
| username       | `testuser`     |
| password       | `12345`        |

**Pasos Realizados:**
1. Se realiza una solicitud POST a la vista `login`.
2. Se verifica que el usuario se guarda en la sesión para el proceso de 2FA.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Redirección a 2FA              | La respuesta debe redirigir a la URL `/two_factor_auth/`.            |
| Usuario guardado en sesión      | El ID del usuario debe guardarse en la sesión bajo la clave `pre_otp_user`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario se guarda en sesión para el proceso de 2FA.

---

**Test:** `test_two_factor_validator_success`

**Objetivo:** Verificar que el proceso de 2FA se completa correctamente cuando se ingresa un código OTP válido.

**Precondiciones:**
- El usuario debe haber iniciado sesión y estar en el flujo de 2FA.

**Datos de Entrada:**

| **Campo**      | **Valor**      |
|----------------|----------------|
| otp-code       | `123456`       |

**Pasos Realizados:**
1. Se simula que el código OTP es válido.
2. Se realiza una solicitud POST a la vista `two_factor_validator` con el código OTP.
3. Se verifica que el usuario es redirigido al dashboard y que se elimina la clave `pre_otp_user` de la sesión.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Redirección al dashboard        | La respuesta debe redirigir a la URL `/dashboard/`.                 |
| Usuario eliminado de la sesión  | La clave `pre_otp_user` debe eliminarse de la sesión.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el proceso de 2FA se completa correctamente.

---

**Test:** `test_two_factor_validator_invalid_otp`

**Objetivo:** Verificar que se muestra un mensaje de error cuando se ingresa un código OTP incorrecto.

**Precondiciones:**
- El usuario debe haber iniciado sesión y estar en el flujo de 2FA.

**Datos de Entrada:**

| **Campo**      | **Valor**          |
|----------------|--------------------|
| otp-code       | `wrong_code`       |

**Pasos Realizados:**
1. Se simula que el código OTP es inválido.
2. Se realiza una solicitud POST a la vista `two_factor_validator` con un código OTP incorrecto.
3. Se verifica que se muestra un mensaje de error.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Mensaje de error                | Debe mostrarse el mensaje `OTP incorrecto`.                         |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el mensaje de error se muestra correctamente.

---

**Test:** `test_restore_password_GET`

**Objetivo:** Verificar que la vista de restauración de contraseña se carga correctamente.

**Precondiciones:**
- El usuario debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `restore_password`.
2. Se verifica que el código de estado sea 200 y que se esté utilizando la plantilla correcta.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'settings/restore_password.html'`.      |
| Formulario correcto             | La vista debe contener un formulario de tipo `PasswordChangeForm`.  |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de restauración de contraseña se carga correctamente.

---

**Test:** `test_restore_password_POST_valid`

**Objetivo:** Verificar que el usuario puede cambiar su contraseña correctamente con datos válidos.

**Precondiciones:**
- El usuario debe estar autenticado.

**Datos de Entrada:**

| **Campo**          | **Valor**              |
|--------------------|------------------------|
| old_password       | `12345`                |
| new_password1      | `newpassword123`       |
| new_password2      | `newpassword123`       |

**Pasos Realizados:**
1. Se realiza una solicitud POST a la vista `restore_password` con una contraseña válida.
2. Se verifica que el usuario es redirigido a la vista de seguridad y que la contraseña ha sido cambiada.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Redirección correcta            | La respuesta debe redirigir a la vista `security_settings`.         |
| Mensaje de éxito                | Debe mostrarse el mensaje `Se ha actualizado con exito`.            |
| Contraseña actualizada          | La contraseña del usuario debe actualizarse correctamente.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario puede cambiar su contraseña correctamente.

---

**Test:** `test_restore_password_POST_invalid`

**Objetivo:** Verificar que se muestra un mensaje de error cuando se ingresa una contraseña incorrecta al cambiar la contraseña.

**Precondiciones:**
- El usuario debe estar autenticado.

**Datos de Entrada:**

| **Campo**          | **Valor**              |
|--------------------|------------------------|
| old_password       | `wrongoldpassword`     |
| new_password1      | `newpassword123`       |
| new_password2      | `newpassword123`       |

**Pasos Realizados:**
1. Se realiza una solicitud POST a la vista `restore_password` con una contraseña incorrecta.
2. Se verifica que el código de estado sea 200 y que el formulario sea inválido.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Formulario inválido             | El formulario de la vista debe ser inválido debido a la contraseña incorrecta.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario muestra errores correctamente.

---

**Test:** `test_restore_password_not_logged_in`

**Objetivo:** Verificar que la vista de restauración de contraseña redirige al login cuando el usuario no está autenticado.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `restore_password` sin estar autenticado.
2. Se verifica que el usuario es redirigido a la página de inicio de sesión.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Redirección al login            | La respuesta debe redirigir a la página de inicio de sesión.         |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario es redirigido al login si no está autenticado.
