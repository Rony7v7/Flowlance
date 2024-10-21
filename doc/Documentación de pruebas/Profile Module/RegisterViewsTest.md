## Configuración del Escenario para `RegisterViewTest`

| Nombre             | Clase                | Escenario                                                    |
|--------------------|----------------------|--------------------------------------------------------------|
| user               | User                 | Usuario de prueba creado para la ejecución del test.          |
| company_profile    | CompanyProfile       | Perfil de empresa asociado al usuario de prueba.              |

---

### Pruebas

**Test:** `test_freelancer_registration_view`

**Objetivo:** Verificar que el registro de freelancer se realiza correctamente y que el usuario es creado.

**Precondiciones:**
- No debe haber un usuario registrado con el mismo nombre de usuario o correo electrónico.

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
1. Se envía una solicitud POST a la vista `register_freelancer` con los datos de registro del freelancer.
2. Se verifica que la respuesta tenga un código de estado 200.
3. Se comprueba que el usuario con el nombre de usuario `freelancer_test` haya sido creado correctamente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Usuario creado                  | El usuario con el nombre de usuario `freelancer_test` debe existir en la base de datos. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el registro de freelancer se realiza correctamente y el usuario es creado.

---

**Test:** `test_company_registration_view`

**Objetivo:** Verificar que el registro de empresa se realiza correctamente y que el usuario es creado.

**Precondiciones:**
- No debe haber un usuario registrado con el mismo nombre de usuario o correo electrónico.

**Datos de Entrada:**

| **Campo**             | **Valor**                 |
|-----------------------|---------------------------|
| username              | `company_test`            |
| email                 | `company@example.com`     |
| password1             | `securePassword123!`      |
| password2             | `securePassword123!`      |
| company_name          | `Test Company`            |
| nit                   | `9001234567`              |
| business_type         | `Tecnología`              |
| country               | `Colombia`                |
| business_vertical     | `Software`                |
| address               | `Calle 123`               |
| legal_representative  | `John Doe`                |
| phone                 | `3012345678`              |

**Pasos Realizados:**
1. Se envía una solicitud POST a la vista `register_company` con los datos de registro de la empresa.
2. Se verifica que la respuesta tenga un código de estado 200.
3. Se comprueba que el usuario con el nombre de usuario `company_test` haya sido creado correctamente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Usuario creado                  | El usuario con el nombre de usuario `company_test` debe existir en la base de datos. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el registro de empresa se realiza correctamente y el usuario es creado.
