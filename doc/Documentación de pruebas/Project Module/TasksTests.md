
### Configuración del Escenario para TasksViewsTest


| **Nombre**         | **Clase**          | **Escenario**                                                       |
|--------------------|--------------------|---------------------------------------------------------------------|
| user            | User            | Usuario de prueba creado y autenticado en el sistema.               |
| project         | Project          | Proyecto de prueba creado para asociar tareas y hitos.              |
| application      | Application      | Aplicación del usuario al proyecto, con estado aceptado.            |
| milestone       | Milestone        | Hito asociado al proyecto de prueba.                                |
| task            | Task            | Tarea creada para probar las vistas de tareas.                      |
| description     | TaskDescription  | Descripción asociada a la tarea creada para pruebas de edición.     |



---

### Pruebas

**Test:** `test_create_task_GET`

**Objetivo:** Verificar que la vista para la creación de tareas se cargue correctamente mediante una solicitud GET.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario autenticado.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un usuario autenticado.
2. Se realiza una solicitud GET a la vista `create_task`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/task_creation.html'`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                                        |
|-----------------------------|------------------------------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.                     |
| Uso de plantilla correcta   | Debe utilizar la plantilla `'projects/task_creation.html'`.            |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de creación de tareas se carga correctamente.

---

**Test:** `test_create_task_POST_valid`

**Objetivo:** Verificar que un usuario pueda crear correctamente una tarea mediante una solicitud POST con datos válidos.

**Precondiciones:**
- Un proyecto y un hito deben existir y estar asociados al usuario autenticado.

**Datos de Entrada:**
| **Campo**      | **Valor**                  |
|----------------|----------------------------|
| `name`         | New Task                   |
| `description`  | New Task Description       |
| `end_date`     | 2024-12-12                 |
| `priority`     | media                      |
| `state`        | pendiente                  |
| `user`         | ID del usuario             |
| `milestone`    | ID del hito                |

**Pasos Realizados:**
1. Se configura el escenario con un proyecto, un hito y un usuario autenticado.
2. Se realiza una solicitud POST a la vista `create_task` con los datos de la tarea.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que la tarea se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                    |
|-------------------------------|-------------------------------------------------------------------|
| Redirección correcta           | La respuesta debe redirigir después de la creación de la tarea.   |
| Creación de la tarea           | La base de datos debe contener una tarea con el título `'New Task'`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la tarea se crea correctamente.

---

**Test:** `test_edit_description_GET`

**Objetivo:** Verificar que la vista de edición de descripción de tarea se cargue correctamente mediante una solicitud GET.

**Precondiciones:**
- Una tarea y una descripción deben existir.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con una tarea, una descripción y un usuario autenticado.
2. Se realiza una solicitud GET a la vista `edit_description`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/edit_description.html'`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                                        |
|-----------------------------|------------------------------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.                     |
| Uso de plantilla correcta   | Debe utilizar la plantilla `'projects/edit_description.html'`.         |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de edición de descripción se carga correctamente.

---

**Test:** `test_edit_description_POST_valid`

**Objetivo:** Verificar que un usuario pueda editar correctamente la descripción de una tarea mediante una solicitud POST con datos válidos.

**Precondiciones:**
- Una tarea y una descripción deben existir.

**Datos de Entrada:**
| **Campo**    | **Valor**                     |
|--------------|-------------------------------|
| `content`    | Updated description content   |

**Pasos Realizados:**
1. Se configura el escenario con una tarea, una descripción y un usuario autenticado.
2. Se realiza una solicitud POST a la vista `edit_description` con los nuevos datos de la descripción.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que la descripción se haya actualizado en la base de datos.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|-------------------------------|---------------------------------------------------------------------|
| Redirección correcta           | La respuesta debe redirigir después de la actualización.            |
| Actualización de la descripción| La descripción debe contener el nuevo contenido `'Updated description content'`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la descripción de la tarea se actualiza correctamente.

---

**Test:** `test_add_description_POST_valid`

**Objetivo:** Verificar que un usuario pueda agregar una nueva descripción a una tarea mediante una solicitud POST con datos válidos.

**Precondiciones:**
- Una tarea debe existir.

**Datos de Entrada:**
| **Campo**    | **Valor**                     |
|--------------|-------------------------------|
| `content`    | New description content       |

**Pasos Realizados:**
1. Se configura el escenario con una tarea y un usuario autenticado.
2. Se realiza una solicitud POST a la vista `add_description` con los datos de la nueva descripción.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que la nueva descripción se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                    | **Descripción**                                                    |
|---------------------------------|-------------------------------------------------------------------|
| Redirección correcta             | La respuesta debe redirigir después de la creación de la descripción.|
| Creación de la descripción       | La base de datos debe contener una nueva descripción con el contenido `'New description content'`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la nueva descripción se agrega correctamente.

---

**Test:** `test_add_comment_POST_valid`

**Objetivo:** Verificar que un usuario pueda agregar un comentario a una tarea mediante una solicitud POST con datos válidos.

**Precondiciones:**
- Una tarea debe existir.

**Datos de Entrada:**
| **Campo**    | **Valor**               |
|--------------|-------------------------|
| `content`    | This is a test comment. |

**Pasos Realizados:**
1. Se configura el escenario con una tarea y un usuario autenticado.
2. Se realiza una solicitud POST a la vista `add_comment` con los datos del comentario.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el comentario se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                        |
|------------------------------|-----------------------------------------------------------------------|
| Redirección correcta         | La respuesta debe redirigir después de agregar el comentario.         |
| Creación del comentario      | La base de datos debe contener un comentario con el contenido `'This is a test comment.'`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el comentario se agrega correctamente.

---

**Test:** `test_add_file_POST_valid`

**Objetivo:** Verificar que un usuario pueda subir un archivo a una tarea mediante una solicitud POST con un archivo válido.

**Precondiciones:**
- Una tarea debe existir.

**Datos de Entrada:**
| **Campo**    | **Valor**               |
|--------------|-------------------------|
| `file`       | `file.txt` (contenido binario: `b'file_content'`) |

**Pasos Realizados:**
1. Se configura el escenario con una tarea y un usuario autenticado.
2. Se crea un archivo simulado (`file.txt`) para la prueba.
3. Se realiza una solicitud POST a la vista `add_file` con el archivo adjunto.
4. Se verifica que la respuesta redirija correctamente.
5. Se comprueba que el archivo se haya subido y asociado a la tarea en la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                        |
|------------------------------|-----------------------------------------------------------------------|
| Redirección correcta         | La respuesta debe redirigir después de subir el archivo.              |
| Archivo subido correctamente | La base de datos debe contener un registro de archivo asociado a la tarea. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el archivo se sube correctamente a la tarea.