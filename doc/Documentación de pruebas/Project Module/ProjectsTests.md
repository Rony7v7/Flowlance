### Configuración del Escenario para ProjectViewsTest

| Nombre         | Clase        | Escenario                                                |
|----------------|--------------|----------------------------------------------------------|
| user           | User         | Usuario de prueba creado para la ejecución del test.     |
| project        | Project      | Proyecto de prueba asociado al usuario.                  |
| milestone      | Milestone    | Hito asociado al proyecto de prueba.                     |


---

### Pruebas

**Test:** `test_create_project_GET`

**Objetivo:** Verificar que la vista de creación de un proyecto se cargue correctamente al realizar una solicitud GET.

**Precondiciones:**
- Un usuario autenticado debe existir en el sistema.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un usuario autenticado.
2. Se realiza una solicitud GET a la vista `create_project`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/create_project.html'`.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                                    |
|---------------------------|--------------------------------------------------------------------|
| Código de estado correcto | La respuesta debe tener un código de estado `200`.                 |
| Uso de plantilla correcta | Debe utilizar la plantilla `'projects/create_project.html'`.       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de creación de proyecto se carga correctamente.

---

**Test:** `test_create_project_POST_valid`

**Objetivo:** Verificar que se pueda crear un nuevo proyecto con datos válidos mediante una solicitud POST.

**Precondiciones:**
- Un usuario autenticado debe existir en el sistema.

**Datos de Entrada:**

| **Campo**       | **Valor**                          |
|-----------------|------------------------------------|
| title           | New Project                        |
| description     | Description for new project        |
| requirements    | Requirements                       |
| budget          | 5000                               |
| start_date      | 2024-01-01                         |
| end_date        | 2024-12-31                         |

**Pasos Realizados:**
1. Se configura el escenario con un usuario autenticado.
2. Se realiza una solicitud POST a la vista `create_project` con datos válidos.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el nuevo proyecto se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                      |
|-------------------------------|----------------------------------------------------------------------|
| Redirección correcta          | La respuesta debe redirigir después de crear el proyecto.            |
| Creación del proyecto         | La base de datos debe contener el proyecto `'New Project'`.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el proyecto se crea correctamente con los datos proporcionados.

---

**Test:** `test_my_projects_GET`

**Objetivo:** Verificar que la vista de proyectos del usuario se cargue correctamente y muestre los proyectos del usuario autenticado.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario autenticado.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un usuario autenticado y un proyecto asociado.
2. Se realiza una solicitud GET a la vista `my_projects`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/project_list.html'`.
5. Se verifica que el título del proyecto esté presente en la respuesta.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                    |
|------------------------------|--------------------------------------------------------------------|
| Código de estado correcto    | La respuesta debe tener un código de estado `200`.                 |
| Uso de plantilla correcta    | Debe utilizar la plantilla `'projects/project_list.html'`.         |
| Proyecto visible             | La respuesta debe contener el título del proyecto `'Test Project'`.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de proyectos del usuario se carga y muestra los proyectos correctamente.

---

**Test:** `test_display_project_GET`

**Objetivo:** Verificar que se pueda visualizar un proyecto específico y mostrar la sección de hitos.

**Precondiciones:**
- Un proyecto y un hito deben existir.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un hito asociados.
2. Se realiza una solicitud GET a la vista `project` con la sección `'milestone'`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/milestones.html'`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                                       |
|-----------------------------|-----------------------------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.                    |
| Uso de plantilla correcta   | Debe utilizar la plantilla `'projects/milestones.html'`.              |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la sección de hitos del proyecto se muestra correctamente.


---

**Test:** `test_project_list_availableFreelancer_GET`

**Objetivo:** Verificar que un freelancer pueda visualizar la lista de proyectos disponibles mediante una solicitud GET.

**Precondiciones:**
- Un proyecto debe existir y estar disponible para freelancers.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un usuario autenticado.
2. Se realiza una solicitud GET a la vista `available_projectsFreelancer`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/project_list.html'`.
5. Se comprueba que el título del proyecto esté presente en la respuesta.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                     |
|---------------------------------|--------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'projects/project_list.html'`.          |
| Contenido del proyecto visible  | La respuesta debe contener el título del proyecto disponible.      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la lista de proyectos disponibles para freelancers se muestra correctamente.

---

**Test:** `test_project_list_GET`

**Objetivo:** Verificar que un usuario autenticado pueda visualizar la lista de sus proyectos mediante una solicitud GET.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario autenticado.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un usuario autenticado.
2. Se realiza una solicitud GET a la vista `project_list`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/project_main_view.html'`.
5. Se comprueba que el título del proyecto esté presente en la respuesta.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                     |
|---------------------------------|--------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'projects/project_main_view.html'`.     |
| Contenido del proyecto visible  | La respuesta debe contener el título del proyecto del usuario.     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la lista de proyectos del usuario autenticado se muestra correctamente.

---

**Test:** `test_project_edit_GET`

**Objetivo:** Verificar que la vista de edición de un proyecto se cargue correctamente al realizar una solicitud GET.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto asociado al usuario.
2. Se realiza una solicitud GET a la vista `project_edit`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/project_form.html'`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                                       |
|-----------------------------|-----------------------------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.                    |
| Uso de plantilla correcta   | Debe utilizar la plantilla `'projects/project_form.html'`.            |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de edición del proyecto se carga correctamente.

---

**Test:** `test_project_edit_POST_valid`

**Objetivo:** Verificar que un proyecto se actualice correctamente con datos válidos mediante una solicitud POST.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario.

**Datos de Entrada:**

| **Campo**       | **Valor**                    |
|-----------------|------------------------------|
| title           | Updated Project Title        |
| description     | Updated Description          |
| requirements    | Updated Requirements         |
| budget          | 1500                         |
| start_date      | 2024-01-01                   |
| end_date        | 2024-12-31                   |

**Pasos Realizados:**
1. Se configura el escenario con un proyecto existente.
2. Se realiza una solicitud POST a la vista `project_edit` con datos válidos.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que los datos del proyecto se hayan actualizado en la base de datos.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                                      |
|---------------------------------|---------------------------------------------------------------------|
| Redirección correcta            | La respuesta debe redirigir después de actualizar el proyecto.      |
| Actualización del proyecto      | Los datos del proyecto deben reflejar los nuevos valores.           |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el proyecto se actualiza correctamente.

---

**Test:** `test_project_delete_GET`

**Objetivo:** Verificar que la vista de confirmación para eliminar un proyecto se cargue correctamente.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto existente.
2. Se realiza una solicitud GET a la vista `project_delete`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/project_delete.html'`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto    | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta    | Debe utilizar la plantilla `'projects/project_delete.html'`.        |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de confirmación de eliminación del proyecto se carga correctamente.

---

**Test:** `test_project_delete_POST`

**Objetivo:** Verificar que un proyecto se elimine correctamente mediante una solicitud POST.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario.

**Datos de Entrada:**
- Ninguno, solo se necesita el ID del proyecto.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto existente.
2. Se realiza una solicitud POST a la vista `project_delete`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el proyecto haya sido eliminado de la base de datos.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                      |
|------------------------------|---------------------------------------------------------------------|
| Redirección correcta         | La respuesta debe redirigir después de eliminar el proyecto.        |
| Eliminación del proyecto     | El proyecto no debe existir en la base de datos.                    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el proyecto se elimina correctamente.

---

**Test:** `test_project_requirements_GET`

**Objetivo:** Verificar que la vista de requisitos del proyecto se cargue correctamente al realizar una solicitud GET.

**Precondiciones:**
- Un proyecto debe existir y estar asociado al usuario autenticado.

**Datos de Entrada:**
- Ninguno, solo se realiza una solicitud GET.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto asociado al usuario.
2. Se realiza una solicitud GET a la vista `project_requirements`.
3. Se verifica que la respuesta tenga un código de estado `200`.
4. Se confirma que se está utilizando la plantilla `'projects/project_requirements.html'`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                                        |
|-----------------------------|------------------------------------------------------------------------|
| Código de estado correcto   | La respuesta debe tener un código de estado `200`.                     |
| Uso de plantilla correcta   | Debe utilizar la plantilla `'projects/project_requirements.html'`.     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista de requisitos del proyecto se carga correctamente.

---

**Test:** `test_apply_project_POST`

**Objetivo:** Verificar que un usuario pueda aplicar correctamente a un proyecto mediante una solicitud POST.

**Precondiciones:**
- Un proyecto debe existir y estar disponible para la aplicación del usuario.

**Datos de Entrada:**
- Ninguno, solo se necesita el ID del proyecto.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto disponible.
2. Se realiza una solicitud POST a la vista `apply_project`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que la aplicación del usuario al proyecto se haya creado en la base de datos.

**Resultados Esperados:**

| **Resultado**                    | **Descripción**                                                      |
|----------------------------------|---------------------------------------------------------------------|
| Redirección correcta             | La respuesta debe redirigir después de aplicar al proyecto.         |
| Creación de la aplicación        | Debe existir una aplicación asociada al usuario y al proyecto.      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el usuario puede aplicar correctamente a un proyecto.

---

**Test:** `test_update_application_status_accept`

**Objetivo:** Verificar que el estado de una aplicación se actualice correctamente a "Aceptada" mediante una solicitud POST.

**Precondiciones:**
- Un proyecto y una aplicación deben existir.

**Datos de Entrada:**
- Estado de la aplicación a actualizar: `'accept'`.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y una aplicación asociada.
2. Se realiza una solicitud POST a la vista `update_application_status` con el estado `'accept'`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el estado de la aplicación se haya actualizado a `'Aceptada'` en la base de datos.

**Resultados Esperados:**

| **Resultado**                      | **Descripción**                                                      |
|------------------------------------|---------------------------------------------------------------------|
| Redirección correcta               | La respuesta debe redirigir después de actualizar el estado.        |
| Actualización del estado           | El estado de la aplicación debe ser `'Aceptada'`.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el estado de la aplicación se actualiza correctamente a "Aceptada".

---

**Test:** `test_update_application_status_reject`

**Objetivo:** Verificar que el estado de una aplicación se actualice correctamente a "Rechazada" mediante una solicitud POST.

**Precondiciones:**
- Un proyecto y una aplicación deben existir.

**Datos de Entrada:**
- Estado de la aplicación a actualizar: `'reject'`.

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y una aplicación asociada.
2. Se realiza una solicitud POST a la vista `update_application_status` con el estado `'reject'`.
3. Se verifica que la respuesta redirija correctamente.
4. Se comprueba que el estado de la aplicación se haya actualizado a `'Rechazada'` en la base de datos.

**Resultados Esperados:**

| **Resultado**                      | **Descripción**                                                      |
|------------------------------------|---------------------------------------------------------------------|
| Redirección correcta               | La respuesta debe redirigir después de actualizar el estado.        |
| Actualización del estado           | El estado de la aplicación debe ser `'Rechazada'`.                  |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el estado de la aplicación se actualiza correctamente a "Rechazada".