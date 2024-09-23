### Configuración del Escenario para MilestoneViewsTest

| Nombre        | Clase       | Escenario                                              |
|---------------|-------------|--------------------------------------------------------|
| user          | User        | Usuario de prueba creado para la ejecución del test.   |
| project       | Project     | Proyecto de prueba asociado al usuario.                |
| milestone     | Milestone   | Hito de prueba asociado al proyecto.                   |
| autenticado   | TestClient  | El usuario de prueba está autenticado en el sistema.   |

---

### Pruebas

**Test:** `test_add_milestone_POST_valid`

**Objetivo:** Verificar que se pueda agregar un nuevo hito al proyecto con datos válidos mediante una solicitud POST.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario autenticado.

**Datos de Entrada:**

| **Campo**      | **Valor**                  |
|----------------|----------------------------|
| name           | New Milestone              |
| description    | New Milestone Description  |
| end_date       | 2024-10-15                 |

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un usuario autenticado.
2. Se realiza una solicitud POST a la vista `add_milestone` con datos válidos.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el nuevo hito se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                                |
|------------------------------|-------------------------------------------------------------------------------|
| Redirección correcta         | La respuesta debe redirigir después de crear el hito.                         |
| Creación del hito            | La base de datos debe contener el hito `'New Milestone'`.                     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el hito se crea correctamente con los datos proporcionados.

---

**Test:** `test_add_milestone_POST_invalid`

**Objetivo:** Verificar que un hito no se crea cuando se envían datos inválidos mediante una solicitud POST.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario autenticado.

**Datos de Entrada:**

| **Campo**      | **Valor**      |
|----------------|----------------|
| name           | (vacío)        |
| description    | (vacío)        |
| end_date       | 2024-10-15     |

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un usuario autenticado.
2. Se realiza una solicitud POST a la vista `add_milestone` con datos inválidos (campos vacíos).
3. Se verifica que la respuesta redirija debido a la entrada inválida.
4. Se comprueba que el hito no se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                                |
|---------------------------------|--------------------------------------------------------------------------------|
| Redirección por datos inválidos | La respuesta debe redirigir debido a la entrada inválida.                      |
| No se crea el hito              | El hito no debe existir en la base de datos con campos vacíos.                 |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el hito no se crea cuando se envían datos inválidos.

---

**Test:** `test_edit_milestone_GET`

**Objetivo:** Verificar que la vista de edición de un hito se carga correctamente y muestra los datos actuales.

**Precondiciones:**
- Un hito debe existir y estar asociado al proyecto.

**Datos de Entrada:**
- Ninguno, ya que se realiza una solicitud GET para cargar la vista.

**Pasos Realizados:**
1. Se configura el escenario con un hito existente.
2. Se realiza una solicitud GET a la vista `edit_milestone`.
3. Se verifica que el estado de la respuesta sea 200 y que se esté usando la plantilla correcta.
4. Se comprueba que la vista está en modo de edición.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto      | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta      | Debe utilizar la plantilla `'projects/manage_milestone.html'`.      |
| Vista en modo de edición       | La respuesta debe contener el contexto `'is_editing': True`.        |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de edición se carga y muestra los datos correctamente.

---

**Test:** `test_edit_milestone_POST_valid`

**Objetivo:** Verificar que un hito se actualiza correctamente con datos válidos mediante una solicitud POST.

**Precondiciones:**
- Un hito debe existir y estar asociado al proyecto.

**Datos de Entrada:**

| **Campo**      | **Valor**             |
|----------------|-----------------------|
| name           | Updated Milestone     |
| description    | Updated Description   |
| end_date       | 2024-12-01            |
| start_date     | 2024-01-01            |

**Pasos Realizados:**
1. Se configura el escenario con un hito existente.
2. Se realiza una solicitud POST con datos válidos a la vista `edit_milestone`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que los datos del hito se hayan actualizado en la base de datos.

**Resultados Esperados:**

| **Resultado**                    | **Descripción**                                                      |
|----------------------------------|---------------------------------------------------------------------|
| Redirección correcta             | La respuesta debe redirigir después de actualizar el hito.          |
| Actualización del hito           | Los datos del hito deben reflejar los nuevos valores.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el hito se actualiza correctamente.

---

**Test:** `test_edit_milestone_POST_invalid`

**Objetivo:** Verificar que un hito no se actualiza cuando se envían datos inválidos mediante una solicitud POST.

**Precondiciones:**
- Un hito debe existir y estar asociado al proyecto.

**Datos de Entrada:**

| **Campo**      | **Valor**      |
|----------------|----------------|
| name           | (vacío)        |
| description    | (vacío)        |
| end_date       | 2024-12-01     |
| start_date     | 2024-01-01     |

**Pasos Realizados:**
1. Se configura el escenario con un hito existente.
2. Se realiza una solicitud POST con datos inválidos a la vista `edit_milestone`.
3. Se verifica que la respuesta redirija debido a la entrada inválida.
4. Se comprueba que el hito no se haya actualizado en la base de datos.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                               |
|---------------------------------|-------------------------------------------------------------------------------|
| Redirección por datos inválidos | La respuesta debe redirigir debido a la entrada inválida.                     |
| No se actualiza el hito         | El hito no debe actualizarse con los valores inválidos.                       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el hito no se actualiza con datos inválidos.

---

**Test:** `test_delete_milestone_POST`

**Objetivo:** Verificar que un hito se elimine correctamente mediante una solicitud POST.

**Precondiciones:**
- Un hito debe existir y estar asociado al proyecto.

**Datos de Entrada:**
- Ninguno, solo se necesita el ID del hito.

**Pasos Realizados:**
1. Se configura el escenario con un hito existente.
2. Se realiza una solicitud POST a la vista `delete_milestone`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el hito haya sido eliminado de la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                       |
|------------------------------|----------------------------------------------------------------------|
| Redirección correcta         | La respuesta debe redirigir después de eliminar el hito.             |
| Eliminación del hito         | El hito no debe existir en la base de datos.                         |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el hito se elimina correctamente.