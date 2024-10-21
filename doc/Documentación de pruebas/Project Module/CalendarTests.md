# Documentación de Tests

## Configuración del Escenario para `AllEventsViewTest`

| Nombre        | Clase       | Escenario                                              |
|---------------|-------------|--------------------------------------------------------|
| user          | User        | Usuario de prueba creado para la ejecución del test.   |
| project       | Project     | Proyecto de prueba asociado al usuario.                |
| event         | Event       | Evento de prueba asociado al proyecto.                 |
| autenticado   | TestClient  | El usuario de prueba está autenticado en el sistema.   |

---

### Pruebas

**Test:** `test_invalid_project_id`

**Objetivo:** Verificar que la vista maneje correctamente un `project_id` inválido.

**Precondiciones:**
- Un proyecto y un evento deben existir.
- El usuario no ha proporcionado un `project_id` válido.

**Datos de Entrada:**

| **Campo**     | **Valor**      |
|---------------|----------------|
| project_id    | invalid        |

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un evento.
2. Se realiza una solicitud GET a la vista `all_events` con un `project_id` inválido.
3. Se verifica que el código de estado sea 400 y que el contenido de la respuesta contenga el mensaje de error adecuado.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `400`.                  |
| Error en el contenido         | El contenido debe incluir el mensaje `'Invalid project ID'`.        |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista maneja correctamente un `project_id` inválido.

---

**Test:** `test_no_project_id`

**Objetivo:** Verificar que la vista maneje correctamente cuando no se proporciona un `project_id`.

**Precondiciones:**
- No se ha proporcionado un `project_id`.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se realiza una solicitud GET a la vista `all_events` sin proporcionar un `project_id`.
2. Se verifica que el código de estado sea 400.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `400`.                  |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista maneja correctamente la falta de `project_id`.

---

**Test:** `test_valid_project_id`

**Objetivo:** Verificar que la vista de eventos retorne correctamente los eventos asociados a un `project_id` válido.

**Precondiciones:**
- El proyecto y el evento deben existir, y el `project_id` debe ser válido.

**Datos de Entrada:**

| **Campo**   | **Valor**       |
|-------------|-----------------|
| project_id  | ID del proyecto |

**Pasos Realizados:**
1. Se configura el escenario con un proyecto y un evento.
2. Se realiza una solicitud GET a la vista `all_events` con un `project_id` válido.
3. Se verifica que el código de estado sea 200 y que el evento esté presente en el contenido de la respuesta.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `200`.                  |
| Evento presente en la vista   | El evento `'Test Event'` debe aparecer en el contenido de la respuesta.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los eventos se retornan correctamente.

---

## Configuración del Escenario para `EditEventViewTest`

| Nombre        | Clase       | Escenario                                              |
|---------------|-------------|--------------------------------------------------------|
| user          | User        | Usuario de prueba creado para la ejecución del test.   |
| project       | Project     | Proyecto de prueba asociado al usuario.                |
| event         | Event       | Evento de prueba asociado al proyecto.                 |
| autenticado   | TestClient  | El usuario de prueba está autenticado en el sistema.   |

---

### Pruebas

**Test:** `test_edit_event_success`

**Objetivo:** Verificar que un evento existente se actualiza correctamente con datos válidos mediante una solicitud POST.

**Precondiciones:**
- El evento debe existir y estar asociado a un proyecto.

**Datos de Entrada:**

| **Campo**      | **Valor**               |
|----------------|-------------------------|
| name           | Updated Event           |
| start          | 2024-01-15T10:00:00     |
| end            | 2024-01-15T12:00:00     |
| description    | Updated description     |

**Pasos Realizados:**
1. Se configura el escenario con un evento existente.
2. Se realiza una solicitud POST con los nuevos datos del evento.
3. Se verifica que el código de estado sea 200 y que los datos del evento se hayan actualizado correctamente.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `200`.                  |
| Actualización de los datos    | Los datos del evento deben reflejar los nuevos valores.             |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los datos del evento se actualizan correctamente.

---

**Test:** `test_edit_event_invalid_data`

**Objetivo:** Verificar que la vista maneje correctamente los datos inválidos en la actualización de un evento.

**Precondiciones:**
- El evento debe existir y estar asociado a un proyecto.

**Datos de Entrada:**

| **Campo**      | **Valor**               |
|----------------|-------------------------|
| name           | (vacío)                 |
| start          | invalid-date            |
| end            | 2024-01-15T12:00:00     |

**Pasos Realizados:**
1. Se configura el escenario con un evento existente.
2. Se realiza una solicitud POST con datos inválidos.
3. Se verifica que el código de estado sea 400 y que la respuesta contenga un mensaje de error.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `400`.                  |
| Errores presentes en la vista | La respuesta debe contener los errores correspondientes a los datos inválidos.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista maneja correctamente los datos inválidos.

---

## Configuración del Escenario para `DisplayProjectViewTest`

| Nombre        | Clase       | Escenario                                              |
|---------------|-------------|--------------------------------------------------------|
| user          | User        | Usuario de prueba creado para la ejecución del test.   |
| project       | Project     | Proyecto de prueba asociado al usuario.                |
| event         | Event       | Evento de prueba asociado al proyecto.                 |
| autenticado   | TestClient  | El usuario de prueba está autenticado en el sistema.   |

---

### Pruebas

**Test:** `test_display_project_not_found`

**Objetivo:** Verificar que la vista maneje correctamente la situación en la que no se encuentra el proyecto solicitado.

**Precondiciones:**
- No se debe encontrar un proyecto con el ID proporcionado.

**Datos de Entrada:**

| **Campo**     | **Valor**  |
|---------------|------------|
| project_id    | 9999       |

**Pasos Realizados:**
1. Se configura el escenario sin un proyecto válido.
2. Se realiza una solicitud GET a la vista `project` con un `project_id` inexistente.
3. Se verifica que el código de estado sea 404.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Código de estado correcto     | La respuesta debe tener un código de estado `404`.                  |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la vista maneja correctamente la ausencia del proyecto.
