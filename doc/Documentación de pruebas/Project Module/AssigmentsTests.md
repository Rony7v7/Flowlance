### Configuración del Escenario para AssigmentViewsTest

| Nombre        | Clase       | Escenario                                              |
|---------------|-------------|--------------------------------------------------------|
| user          | User        | Usuario de prueba creado para la ejecución del test.   |
| project       | Project     | Proyecto de prueba asociado al usuario.                |
| milestone     | Milestone   | Hito de prueba asociado al proyecto.                   |
| assigment     | Assigment   | Entregable de prueba asociado al hito.                 |
| autenticado   | TestClient  | El usuario de prueba está autenticado en el sistema.   |

---

### Pruebas

**Test:** `test_create_assigment_GET`

**Objetivo:** Verificar que la vista de creación de un entregable se carga correctamente y muestra los campos esperados.

**Precondiciones:**
- Un proyecto y un hito deben existir y estar asociados al usuario autenticado.

**Datos de Entrada:**
- Ninguno, ya que se realiza una solicitud GET para cargar la vista.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto, un hito, y un usuario autenticado.
2. Se realiza una solicitud GET a la vista `create_assigment`.
3. Se verifica que el estado de la respuesta sea 200 y que se esté usando la plantilla correcta.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                            |
|------------------------------|---------------------------------------------------------------------------|
| Código de estado correcto    | La respuesta debe tener un código de estado `200`.                        |
| Uso de plantilla correcta    | Debe utilizar la plantilla `'projects/create_assigment.html'`.            |
| Campos presentes en la vista | Los campos `name`, `description`, `user` y `end_date` deben estar presentes en el HTML.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista se carga y muestra los campos esperados.

---

**Test:** `test_create_assigment_POST_valid`

**Objetivo:** Verificar que un entregable se crea correctamente con datos válidos mediante una solicitud POST.

**Precondiciones:**
- Un proyecto y un hito deben existir y estar asociados al usuario autenticado.

**Datos de Entrada:**

| **Campo**      | **Valor**                  |
|----------------|----------------------------|
| name           | Test Assignment            |
| description    | Assignment Description     |
| end_date       | 2024-10-01                 |
| user           | ID del usuario autenticado |

**Pasos Realizados:**
1. Se configura el escenario con un proyecto, un hito, y un usuario autenticado.
2. Se realiza una solicitud POST con datos válidos a la vista `create_assigment`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el entregable se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                                 |
|---------------------------------|---------------------------------------------------------------------------------|
| Redirección correcta            | La respuesta debe redirigir después de crear el entregable.                     |
| Creación del entregable         | La base de datos debe contener el entregable `'Test Assignment'`.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el entregable se crea correctamente con los datos proporcionados.

---

**Test:** `test_edit_assigment_GET`

**Objetivo:** Verificar que la vista de edición de un entregable se carga correctamente y muestra los datos actuales.

**Precondiciones:**
- Un entregable debe existir y estar asociado al hito del proyecto.

**Datos de Entrada:**
- Ninguno, ya que se realiza una solicitud GET para cargar la vista.

**Pasos Realizados:**
1. Se configura el escenario con un entregable existente.
2. Se realiza una solicitud GET a la vista `edit_assigment`.
3. Se verifica que el estado de la respuesta sea 200 y que se esté usando la plantilla correcta.
4. Se comprueba que la vista muestra los valores actuales del entregable.

**Resultados Esperados:**

| **Resultado**                      | **Descripción**                                               |
|------------------------------------|---------------------------------------------------------------|
| Código de estado correcto          | La respuesta debe tener un código de estado `200`.            |
| Uso de plantilla correcta          | Debe utilizar la plantilla `'projects/create_assigment.html'`.|
| Datos actuales del entregable      | La vista debe mostrar los valores actuales del entregable.    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de edición muestra los datos correctos.

---

**Test:** `test_edit_assigment_POST_valid`

**Objetivo:** Verificar que un entregable se actualiza correctamente con datos válidos mediante una solicitud POST.

**Precondiciones:**
- Un entregable debe existir y estar asociado al hito del proyecto.

**Datos de Entrada:**

| **Campo**      | **Valor**                  |
|----------------|----------------------------|
| name           | Updated Assignment         |
| description    | Updated Description        |
| end_date       | 2024-12-01                 |
| user           | ID del usuario autenticado |

**Pasos Realizados:**
1. Se configura el escenario con un entregable existente.
2. Se realiza una solicitud POST con datos válidos a la vista `edit_assigment`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que los datos del entregable se hayan actualizado en la base de datos.

**Resultados Esperados:**

| **Resultado**                    | **Descripción**                                                      |
|----------------------------------|---------------------------------------------------------------------|
| Redirección correcta             | La respuesta debe redirigir después de actualizar el entregable.    |
| Actualización del entregable     | Los datos del entregable deben reflejar los nuevos valores.         |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el entregable se actualiza correctamente.

---

**Test:** `test_delete_assigment_POST`

**Objetivo:** Verificar que un entregable se elimine correctamente mediante una solicitud POST.

**Precondiciones:**
- Un entregable debe existir y estar asociado al hito del proyecto.

**Datos de Entrada:**
- Ninguno, solo se necesita el ID del entregable.

**Pasos Realizados:**
1. Se configura el escenario con un entregable existente.
2. Se realiza una solicitud POST a la vista `delete_assigment`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el entregable haya sido eliminado de la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                       |
|------------------------------|----------------------------------------------------------------------|
| Redirección correcta         | La respuesta debe redirigir después de eliminar el entregable.       |
| Eliminación del entregable   | El entregable no debe existir en la base de datos.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el entregable se elimina correctamente.

---

**Test:** `test_upload_assigment_GET`

**Objetivo:** Verificar que la vista de carga de archivos de un entregable se carga correctamente.

**Precondiciones:**
- Un entregable debe existir y estar asociado al hito del proyecto.

**Datos de Entrada:**
- Ninguno, ya que se realiza una solicitud GET para cargar la vista.

**Pasos Realizados:**
1. Se configura el escenario con un entregable existente.
2. Se realiza una solicitud GET a la vista `upload_assigment`.
3. Se verifica que el estado de la respuesta sea 200 y que se esté usando la plantilla correcta.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                      |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto    | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta    | Debe utilizar la plantilla `'projects/upload_assigment_file.html'`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de carga de archivos se carga correctamente.