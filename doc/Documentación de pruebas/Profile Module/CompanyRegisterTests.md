## Configuración del Escenario para `CompanyRegisterFormTest`

| Nombre             | Clase                | Escenario                                                    |
|--------------------|----------------------|--------------------------------------------------------------|
| user               | User                 | Usuario de prueba creado para la ejecución del test.          |
| company_profile    | CompanyProfile       | Perfil de empresa asociado al usuario de prueba.              |
| form               | CompanyRegisterForm  | Formulario de registro de empresa.                           |

---

### Pruebas

**Test:** `test_valid_company_registration`

**Objetivo:** Verificar que el formulario de registro de empresa es válido cuando se ingresan datos correctos y que se crea el perfil de empresa asociado al usuario.

**Precondiciones:**
- No debe haber un perfil de empresa registrado con el mismo NIT.

**Datos de Entrada:**

| **Campo**               | **Valor**                 |
|-------------------------|---------------------------|
| username                | `company_test`            |
| email                   | `company@example.com`     |
| password1               | `securePassword123!`      |
| password2               | `securePassword123!`      |
| company_name            | `Test Company`            |
| nit                     | `9001234567`              |
| business_type           | `Tecnología`              |
| country                 | `Colombia`                |
| business_vertical       | `Software`                |
| address                 | `Calle 123`               |
| legal_representative    | `John Doe`                |
| phone                   | `3012345678`              |

**Pasos Realizados:**
1. Se crea un formulario de registro de empresa con los datos proporcionados.
2. Se verifica que el formulario sea válido.
3. Se guarda el usuario asociado y se verifica que el perfil de empresa se haya creado correctamente en la base de datos.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Formulario válido               | El formulario debe ser válido.                                      |
| Creación del usuario            | El usuario debe ser guardado en la base de datos.                   |
| Creación del perfil de empresa  | El perfil de empresa debe ser creado correctamente.                 |
| NIT correcto                    | El valor del NIT en el perfil de empresa debe ser `9001234567`.      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario de registro es válido y que el perfil de empresa se crea correctamente.

---

**Test:** `test_company_registration_duplicate_nit`

**Objetivo:** Verificar que el formulario de registro de empresa no es válido cuando ya existe un perfil de empresa con el mismo NIT.

**Precondiciones:**
- Debe existir un perfil de empresa registrado con el NIT `9001234567`.

**Datos de Entrada:**

| **Campo**               | **Valor**                 |
|-------------------------|---------------------------|
| username                | `company_test`            |
| email                   | `company@example.com`     |
| password1               | `securePassword123!`      |
| password2               | `securePassword123!`      |
| company_name            | `Test Company`            |
| nit                     | `9001234567`              |
| business_type           | `Tecnología`              |
| country                 | `Colombia`                |
| business_vertical       | `Software`                |
| address                 | `Calle 123`               |
| legal_representative    | `John Doe`                |
| phone                   | `3012345678`              |

**Pasos Realizados:**
1. Se crea un usuario y un perfil de empresa existente con el NIT `9001234567`.
2. Se intenta registrar una nueva empresa con el mismo NIT.
3. Se verifica que el formulario no sea válido y que se muestre un mensaje de error relacionado con el NIT duplicado.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Formulario inválido             | El formulario no debe ser válido debido al NIT duplicado.            |
| Mensaje de error                | El mensaje de error debe indicar que el NIT ya está registrado.     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el formulario no es válido y que el mensaje de error aparece correctamente cuando ya existe un perfil de empresa con el mismo NIT.
