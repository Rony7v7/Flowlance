# Documentación de Tests

## Configuración del Escenario para `SettingsViewsTests`

| Nombre            | Clase                | Escenario                                                   |
|-------------------|----------------------|-------------------------------------------------------------|
| user              | User                 | Usuario de prueba creado para la ejecución del test.         |
| freelancer_profile| FreelancerProfile     | Perfil de freelancer asociado al usuario de prueba.          |
| settings_url      | URL                  | URL de la vista de configuración de cuenta.                 |
| security_settings_url | URL               | URL de la vista de configuración de seguridad.              |
| toggle_2fa_url    | URL                  | URL para habilitar/deshabilitar la autenticación de dos factores (2FA).|

---

### Pruebas

**Test:** `test_settings_view`

**Objetivo:** Verificar que la vista de configuración de cuenta se carga correctamente cuando el usuario está autenticado.

**Precondiciones:**
- El usuario debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `account_settings` con el usuario autenticado.
2. Se verifica que el código de estado sea 200 y que se esté utilizando la plantilla correcta.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                   |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'settings/account_settings.html'`.       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista se carga correctamente para el usuario autenticado.

---

**Test:** `test_settings_view_not_logged_in`

**Objetivo:** Verificar que la vista de configuración de cuenta redirige al login cuando el usuario no está autenticado.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `account_settings` sin estar autenticado.
2. Se verifica que el usuario es redirigido a la página de inicio de sesión.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Redirección al login            | La respuesta debe redirigir a la página de inicio de sesión.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario es redirigido al login si no está autenticado.

---

**Test:** `test_security_settings_view`

**Objetivo:** Verificar que la vista de configuración de seguridad se carga correctamente para un usuario autenticado y que muestra el estado de 2FA.

**Precondiciones:**
- El usuario debe estar autenticado y tener un perfil de freelancer asociado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `security_settings` con el usuario autenticado.
2. Se verifica que el código de estado sea 200, que se esté utilizando la plantilla correcta, y que el estado de 2FA esté desactivado.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                   |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'settings/security_settings.html'`.      |
| Estado de 2FA                  | El valor de `has_2FA_on` debe ser `False`.                           |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista muestra correctamente el estado de 2FA.

---

**Test:** `test_security_settings_view_not_logged_in`

**Objetivo:** Verificar que la vista de configuración de seguridad redirige al login cuando el usuario no está autenticado.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `security_settings` sin estar autenticado.
2. Se verifica que el usuario es redirigido a la página de inicio de sesión.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Redirección al login            | La respuesta debe redirigir a la página de inicio de sesión.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario es redirigido al login si no está autenticado.

---

**Test:** `test_toggle_2fa_view`

**Objetivo:** Verificar que el usuario puede habilitar y deshabilitar la autenticación de dos factores (2FA).

**Precondiciones:**
- El usuario debe estar autenticado y tener un perfil de freelancer asociado.

**Datos de Entrada:**

| **Campo**      | **Valor**          |
|----------------|--------------------|
| has_2FA_on     | `on` o vacío       |

**Pasos Realizados:**
1. Se realiza una solicitud POST para habilitar el 2FA.
2. Se verifica que el estado de 2FA en el perfil del usuario es `True`.
3. Se realiza una solicitud POST para deshabilitar el 2FA.
4. Se verifica que el estado de 2FA en el perfil del usuario es `False`.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Redirección correcta            | La respuesta debe redirigir a la vista `security_settings`.           |
| Estado de 2FA actualizado       | El valor de `has_2FA_on` debe ser actualizado correctamente.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario puede habilitar y deshabilitar 2FA correctamente.

---

**Test:** `test_toggle_2fa_view_not_logged_in`

**Objetivo:** Verificar que la vista de activación/desactivación de 2FA redirige al login cuando el usuario no está autenticado.

**Precondiciones:**
- El usuario no debe estar autenticado.

**Datos de Entrada:**

| **Campo**      | **Valor**          |
|----------------|--------------------|
| has_2FA_on     | `on`               |

**Pasos Realizados:**
1. Se realiza una solicitud POST a la vista `toggle_2fa` sin estar autenticado.
2. Se verifica que el usuario es redirigido a la página de inicio de sesión.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Redirección al login            | La respuesta debe redirigir a la página de inicio de sesión.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario es redirigido al login si no está autenticado.

---

**Test:** `test_security_settings_no_profile`

**Objetivo:** Verificar que la vista de configuración de seguridad se carga correctamente para un usuario sin perfil asociado.

**Precondiciones:**
- El usuario debe estar autenticado, pero no tener un perfil asociado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se crea un usuario sin un perfil asociado.
2. Se realiza una solicitud GET a la vista `security_settings`.
3. Se verifica que el código de estado sea 200 y que el estado de 2FA sea `False`.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                   |
| Estado de 2FA                  | El valor de `has_2FA_on` debe ser `False` por defecto.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista se carga correctamente incluso si el usuario no tiene perfil asociado.

---

**Test:** `test_toggle_2fa_no_profile`

**Objetivo:** Verificar que el usuario puede intentar habilitar 2FA sin tener un perfil asociado, sin que ocurra un error.

**Precondiciones:**
- El usuario debe estar autenticado, pero no tener un perfil asociado.

**Datos de Entrada:**

| **Campo**      | **Valor**          |
|----------------|--------------------|
| has_2FA_on     | `on`               |

**Pasos Realizados:**
1. Se crea un usuario sin un perfil asociado.
2. Se realiza una solicitud POST a la vista `toggle_2fa`.
3. Se verifica que el usuario es redirigido correctamente y que no ocurre un error.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Redirección correcta            | La respuesta debe redirigir a la vista `security_settings`.           |
| No hay errores                  | No debe ocurrir ningún error aunque el usuario no tenga perfil.       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que no ocurre ningún error al intentar habilitar 2FA sin un perfil asociado.

---

## Configuración del Escenario para `CompanySettingsViewsTests`

| Nombre            | Clase                | Escenario                                                   |
|-------------------|----------------------|-------------------------------------------------------------|
| user              | User                 | Usuario de prueba creado para la ejecución del test.         |
| company_profile   | CompanyProfile       | Perfil de empresa asociado al usuario de prueba.             |
| security_settings_url | URL               | URL de la vista de configuración de seguridad.              |
| toggle_2fa_url    | URL                  | URL para habilitar/deshabilitar la autenticación de dos factores (2FA).|

---

### Pruebas

**Test:** `test_security_settings_view_company`

**Objetivo:** Verificar que la vista de configuración de seguridad se carga correctamente para un usuario con perfil de empresa y que muestra el estado de 2FA.

**Precondiciones:**
- El usuario debe estar autenticado y tener un perfil de empresa asociado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `security_settings` con el usuario autenticado.
2. Se verifica que el código de estado sea 200, que se esté utilizando la plantilla correcta, y que el estado de 2FA esté desactivado.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                   |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'settings/security_settings.html'`.      |
| Estado de 2FA                  | El valor de `has_2FA_on` debe ser `False`.                           |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista muestra correctamente el estado de 2FA.

---

**Test:** `test_toggle_2fa_view_company`

**Objetivo:** Verificar que el usuario con perfil de empresa puede habilitar y deshabilitar la autenticación de dos factores (2FA).

**Precondiciones:**
- El usuario debe estar autenticado y tener un perfil de empresa asociado.

**Datos de Entrada:**

| **Campo**      | **Valor**          |
|----------------|--------------------|
| has_2FA_on     | `on` o vacío       |

**Pasos Realizados:**
1. Se realiza una solicitud POST para habilitar el 2FA.
2. Se verifica que el estado de 2FA en el perfil de empresa del usuario es `True`.
3. Se realiza una solicitud POST para deshabilitar el 2FA.
4. Se verifica que el estado de 2FA en el perfil de empresa del usuario es `False`.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|--------------------------------|----------------------------------------------------------------------|
| Redirección correcta            | La respuesta debe redirigir a la vista `security_settings`.           |
| Estado de 2FA actualizado       | El valor de `has_2FA_on` debe ser actualizado correctamente.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario con perfil de empresa puede habilitar y deshabilitar 2FA correctamente.
