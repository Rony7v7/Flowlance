## Configuración del Escenario para TestViews

| Nombre         | Clase                 | Escenario                                              |
|----------------|-----------------------|--------------------------------------------------------|
| user           | User                  | Usuario de prueba creado para la ejecución del test    |
| profile        | FreelancerProfile     | Perfil de freelancer asociado al usuario de prueba     |
| autenticado    | TestClient            | El usuario de prueba está autenticado en el sistema    |
| other_user     | User                  | Otro usuario creado para pruebas de interacciones      |
| other_profile  | FreelancerProfile     | Perfil de freelancer asociado al otro usuario de prueba |
| notification   | Notification          | Notificación de prueba asociada al usuario de prueba   |

---

### Pruebas

**Test:** `test_freelancer_profile_view_own_profile`

**Objetivo:** Verificar que un usuario pueda visualizar su propio perfil de freelancer correctamente. El test asegura que la página del perfil se cargue con la información del usuario autenticado.

**Precondiciones:**

- Un usuario (`testuser`) debe existir y estar autenticado.
- El perfil de freelancer (`FreelancerProfile`) debe estar creado y vinculado al usuario.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test.

**Pasos Realizados:**

1. Se configura el escenario creando un usuario y su perfil de freelancer.
2. Se realiza una solicitud GET a la URL del perfil (`freelancer_profile`).
3. Se verifica que el código de estado de la respuesta sea `200`.
4. Se comprueba que el nombre de usuario esté presente en la respuesta.

**Resultados Esperados:**

| **Resultado**                       | **Descripción**                                                     |
|-------------------------------------|---------------------------------------------------------------------|
| Código de estado correcto           | La respuesta debe tener un código de estado `200`.                  |
| Visualización del nombre de usuario | La respuesta debe contener el nombre de usuario `'testuser'`.       |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el perfil del usuario se visualiza correctamente.

---

**Test:** `test_freelancer_profile_view_other_user_profile`

**Objetivo:** Verificar que un usuario pueda ver el perfil de otro usuario de freelancer.

**Precondiciones:**

- Dos usuarios (`testuser` y `otheruser`) deben existir.
- Ambos perfiles de freelancer deben estar creados y asociados a sus respectivos usuarios.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test.

**Pasos Realizados:**

1. Se configura el escenario con los usuarios y sus perfiles correspondientes.
2. Se realiza una solicitud GET a la URL del perfil de otro usuario (`freelancer_profile_view`).
3. Se verifica que el código de estado de la respuesta sea `200`.
4. Se comprueba que la respuesta contiene el nombre del otro usuario.

**Resultados Esperados:**

| **Resultado**                       | **Descripción**                                                     |
|-------------------------------------|---------------------------------------------------------------------|
| Código de estado correcto           | La respuesta debe tener un código de estado `200`.                  |
| Visualización del nombre de usuario | La respuesta debe contener el nombre de `'otheruser'`.              |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el perfil del otro usuario se visualiza correctamente.

---

**Test:** `test_notifications_view`

**Objetivo:** Verificar que un usuario pueda ver correctamente sus notificaciones.

**Precondiciones:**

- El usuario (`testuser`) debe estar autenticado.
- Debe existir al menos una notificación asociada al usuario.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test.

**Pasos Realizados:**

1. Se configura el escenario con el usuario y una notificación.
2. Se realiza una solicitud GET a la URL de notificaciones (`notifications`).
3. Se verifica que el código de estado de la respuesta sea `200`.
4. Se comprueba que la notificación se muestra en la respuesta.

**Resultados Esperados:**

| **Resultado**                     | **Descripción**                                                   |
|-----------------------------------|-------------------------------------------------------------------|
| Código de estado correcto         | La respuesta debe tener un código de estado `200`.                |
| Contenido de la notificación      | La respuesta debe contener el mensaje de la notificación.         |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que las notificaciones se muestran correctamente.

---

**Test:** `test_add_skills_view_get`

**Objetivo:** Verificar que el formulario para agregar habilidades se cargue correctamente.

**Precondiciones:**

- El usuario (`testuser`) debe estar autenticado.
- El perfil de freelancer debe estar creado.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test.

**Pasos Realizados:**

1. Se configura el escenario con el usuario y su perfil.
2. Se realiza una solicitud GET a la URL para agregar habilidades (`add_skills`).
3. Se verifica que el código de estado de la respuesta sea `200`.
4. Se comprueba que el formulario `AddSkillsForm` esté presente en la respuesta.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                          |
|---------------------------------|----------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.       |
| Presencia del formulario        | El formulario `AddSkillsForm` debe estar en la respuesta.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que la página y el formulario se cargan correctamente.

---

**Test:** `test_add_skills_view_post`

**Objetivo:** Verificar que un usuario pueda agregar habilidades a su perfil de freelancer mediante el formulario.

**Precondiciones:**

- El usuario (`testuser`) debe estar autenticado.
- El perfil de freelancer debe estar creado.

**Datos de Entrada**

- Datos del formulario que contienen habilidades predefinidas seleccionadas.

**Pasos Realizados:**

1. Se configura el escenario con el usuario, perfil y una habilidad predefinida.
2. Se realiza una solicitud POST a la URL para agregar habilidades (`add_skills`).
3. Se verifica que la respuesta redirige al perfil del freelancer.
4. Se comprueba que la habilidad seleccionada se agregó al perfil del usuario.

**Resultados Esperados:**

| **Resultado**                    | **Descripción**                                                       |
|----------------------------------|-----------------------------------------------------------------------|
| Redirección correcta             | La respuesta debe redirigir al perfil (`freelancer_profile`).         |
| Habilidad agregada al perfil     | La habilidad seleccionada debe estar en las habilidades del perfil.   |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que las habilidades se agregan correctamente al perfil.

---

**Test:** `test_add_experience_view_get`

**Objetivo:** Verificar que el formulario para agregar experiencia laboral se cargue correctamente.

**Precondiciones:**

- El usuario (`testuser`) debe estar autenticado.
- El perfil de freelancer debe estar creado.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test.

**Pasos Realizados:**

1. Se configura el escenario con el usuario y su perfil.
2. Se realiza una solicitud GET a la URL para agregar experiencia laboral (`add_experience`).
3. Se verifica que el código de estado de la respuesta sea `200`.
4. Se comprueba que el formulario `AddWorkExperienceForm` esté presente en la respuesta.

**Resultados Esperados:**

| **Resultado**                   | **Descripción**                                          |
|---------------------------------|----------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.       |
| Presencia del formulario        | El formulario `AddWorkExperienceForm` debe estar presente.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que la página y el formulario se cargan correctamente.

---

**Test:** `test_add_experience_view_post`

**Objetivo:** Verificar que un usuario pueda agregar experiencia laboral a su perfil de freelancer.

**Precondiciones:**

- El usuario (`testuser`) debe estar autenticado.
- El perfil de freelancer debe estar creado.

**Datos de Entrada**

- Datos del formulario con información de la experiencia laboral.

**Pasos Realizados:**

1. Se configura el escenario con el usuario y su perfil.
2. Se realiza una solicitud POST a la URL para agregar experiencia (`add_experience`).
3. Se verifica que la respuesta redirige al perfil del freelancer.
4. Se comprueba que la experiencia laboral se haya creado y esté en la base de datos.

**Resultados Esperados:**

| **Resultado**                       | **Descripción**                                                         |
|-------------------------------------|-------------------------------------------------------------------------|
| Redirección correcta                | La respuesta debe redirigir al perfil (`freelancer_profile`).           |
| Experiencia laboral creada          | La experiencia laboral debe estar en la base de datos.                  |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que la experiencia laboral se agrega correctamente al perfil.

---

**Test:** `test_add_rating_view_get`

**Objetivo:** Verificar que la vista de agregar calificación se cargue correctamente con el formulario adecuado.

**Precondiciones:**

- El usuario (`testuser`) debe estar autenticado.
- El perfil de freelancer del otro usuario (`otheruser`) debe existir.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test.

**Pasos Realizados:**

1. Se configura el escenario con los usuarios (`testuser` y `otheruser`) y sus perfiles correspondientes.
2. Se realiza una solicitud GET a la URL para agregar una calificación (`add_rating`) utilizando el `username` del otro usuario.
3. Se verifica que el código de estado de la respuesta sea `200`, indicando que la página se cargó correctamente.
4. Se comprueba que la plantilla utilizada es `profile/add_rating.html`.
5. Se verifica que el formulario `RatingForm` esté presente en el contexto de la respuesta.

**Resultados Esperados:**

| **Resultado**                    | **Descripción**                                                        |
|----------------------------------|------------------------------------------------------------------------|
| Código de estado correcto        | La respuesta debe tener un código de estado `200`.                     |
| Plantilla correcta                | La plantilla utilizada debe ser `profile/add_rating.html`.             |
| Presencia del formulario         | El formulario `RatingForm` debe estar presente en el contexto.         |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que la vista de agregar calificación se carga con el formulario correcto.

---

**Test:** `test_delete_rating_response_view_post`

**Objetivo:** Verificar que un usuario pueda eliminar una respuesta a una calificación correctamente.

**Precondiciones:**

- El usuario (`testuser`) debe estar autenticado.
- Debe existir una calificación asociada al otro usuario (`otheruser`) y una respuesta correspondiente.

**Datos de Entrada**

- ID de la respuesta a eliminar.

**Pasos Realizados:**

1. Se configura el escenario con la creación de una calificación y una respuesta asociada.
2. Se realiza una solicitud POST a la URL para eliminar la respuesta (`delete_rating_response`), pasando el ID de la respuesta.
3. Se verifica que la respuesta redirige correctamente al perfil del freelancer (`freelancer_profile`).
4. Se comprueba que la respuesta a la calificación ha sido eliminada de la base de datos.

**Resultados Esperados:**

| **Resultado**                       | **Descripción**                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Redirección correcta                | La respuesta debe redirigir al perfil (`freelancer_profile`).             |
| Respuesta eliminada                 | La respuesta a la calificación no debe existir en la base de datos.       |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que la respuesta a la calificación se elimina correctamente.

