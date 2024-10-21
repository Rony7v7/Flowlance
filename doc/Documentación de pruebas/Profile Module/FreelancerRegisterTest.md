# Documentación de Tests

## Configuración del Escenario para `FreelancerRegisterFormTest`

| Nombre             | Clase                | Escenario                                                    |
|--------------------|----------------------|--------------------------------------------------------------|
| user               | User                 | Usuario de prueba creado para la ejecución del test.          |
| freelancer_profile | FreelancerProfile    | Perfil de freelancer asociado al usuario de prueba.           |
| form               | FreelancerRegisterForm| Formulario de registro de freelancer.                        |

---

### Pruebas

**Test:** `test_valid_freelancer_registration`

**Objetivo:** Verificar que el formulario de registro de freelancer es válido cuando se ingresan datos correctos y que se crea el perfil de freelancer asociado al usuario.

**Precondiciones:**
- No debe haber un perfil de freelancer registrado con el mismo email o identificación.

**Datos de Entrada:**

| **Campo**             | **Valor**                 |
|-----------------------|---------------------------|
| username              | `freelancer_test`          |
| email                 | `freelancer@example.com`   |
| password1             | `securePassword123!`       |
| password2             | `securePassword123!`       |
| identification        | `1234567890`              |
| phone                 | `3001234567`              |

**Pasos Realizados:**
1. Se crea un formulario de registro de freelancer con los datos proporcionados.
2. Se verifica que el formulario sea válido.
3. Se guarda el usuario asociado y se verifica que el perfil de freelancer se haya creado correctamente en la base de datos.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Formulario válido               | El formulario debe ser válido.                                      |
| Creación del usuario            | El usuario debe ser guardado en la base de datos.                   |
| Creación del perfil de freelancer| El perfil de freelancer debe ser creado correctamente.              |
| Identificación correcta         | El valor de la identificación en el perfil de freelancer debe ser `1234567890`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario de registro es válido y que el perfil de freelancer se crea correctamente.

---

**Test:** `test_freelancer_registration_duplicate_email`

**Objetivo:** Verificar que el formulario de registro de freelancer no es válido cuando ya existe un usuario registrado con el mismo correo electrónico.

**Precondiciones:**
- Debe existir un usuario registrado con el correo electrónico `existing@example.com`.

**Datos de Entrada:**

| **Campo**             | **Valor**                 |
|-----------------------|---------------------------|
| username              | `freelancer_test`          |
| email                 | `existing@example.com`     |
| password1             | `securePassword123!`       |
| password2             | `securePassword123!`       |
| identification        | `1234567890`              |
| phone                 | `3001234567`              |

**Pasos Realizados:**
1. Se crea un usuario con el correo electrónico `existing@example.com`.
2. Se intenta registrar un nuevo freelancer con el mismo correo electrónico.
3. Se verifica que el formulario no sea válido y que se muestre un mensaje de error relacionado con el correo duplicado.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Formulario inválido             | El formulario no debe ser válido debido al correo electrónico duplicado. |
| Mensaje de error                | El mensaje de error debe indicar que el correo ya está registrado.  |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario no es válido y que el mensaje de error aparece correctamente cuando ya existe un usuario con el mismo correo electrónico.

---

**Test:** `test_freelancer_registration_duplicate_identification`

**Objetivo:** Verificar que el formulario de registro de freelancer no es válido cuando ya existe un perfil de freelancer con la misma identificación.

**Precondiciones:**
- Debe existir un perfil de freelancer registrado con la identificación `1234567890`.

**Datos de Entrada:**

| **Campo**             | **Valor**                 |
|-----------------------|---------------------------|
| username              | `freelancer_test`          |
| email                 | `freelancer2@example.com`  |
| password1             | `securePassword123!`       |
| password2             | `securePassword123!`       |
| identification        | `1234567890`              |
| phone                 | `3007654321`              |

**Pasos Realizados:**
1. Se crea un usuario y un perfil de freelancer existente con la identificación `1234567890`.
2. Se intenta registrar un nuevo freelancer con la misma identificación.
3. Se verifica que el formulario no sea válido y que se muestre un mensaje de error relacionado con la identificación duplicada.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Formulario inválido             | El formulario no debe ser válido debido a la identificación duplicada. |
| Mensaje de error                | El mensaje de error debe indicar que la identificación ya está registrada.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario no es válido y que el mensaje de error aparece correctamente cuando ya existe un perfil de freelancer con la misma identificación.
