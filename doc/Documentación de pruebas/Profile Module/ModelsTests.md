## Configuración del Escenario para ModelsTests

| Nombre           | Clase                | Escenario                                                   |
|------------------|----------------------|-------------------------------------------------------------|
| user             | User                 | Usuario de prueba creado para los modelos                   |
| profile          | FreelancerProfile    | Perfil de freelancer asociado al usuario de prueba          |
| portfolio        | Portfolio            | Portafolio asociado al perfil de freelancer                 |
| project          | PortfolioProject     | Proyecto dentro del portafolio del freelancer               |
| course           | Course               | Curso asociado al portafolio del freelancer                 |
| work_experience  | WorkExperience       | Experiencia laboral asociada al perfil del freelancer       |
| curriculum_vitae | CurriculumVitae      | CV asociado al perfil del freelancer                        |
| rating           | Rating               | Calificación dada por un cliente al freelancer              |
| response         | RatingResponse       | Respuesta del freelancer a una calificación recibida        |
| notification     | Notification         | Notificación creada para el usuario de prueba               |

---

### Pruebas

**Test:** `test_skill_creation`

**Objetivo:** Verificar la creación de una habilidad (`Skill`) y su representación en formato de cadena.

**Precondiciones:**

- La habilidad `Python` debe crearse como no personalizada.

**Datos de Entrada**

- Nombre de la habilidad: `'Python'`
- Es personalizada: `False`

**Pasos Realizados:**

1. Se crea una habilidad con el nombre `'Python'`.
2. Se verifica que el nombre de la habilidad coincida con `'Python'`.
3. Se comprueba que la habilidad no sea personalizada.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                        |
|------------------------------- |----------------------------------------|
| Nombre correcto de la habilidad | El nombre de la habilidad debe ser `'Python'`.|
| Personalización correcta       | La habilidad no debe ser personalizada.  |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación correcta de la habilidad.

---

**Test:** `test_create_freelancer_profile`

**Objetivo:** Verificar que el perfil de freelancer se cree correctamente para un usuario dado.

**Precondiciones:**

- El usuario `testuser` debe existir en el sistema.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test.

**Pasos Realizados:**

1. Se crea un perfil de freelancer para el usuario `testuser`.
2. Se verifica que el perfil esté asociado al usuario correcto.
3. Se comprueba la representación del perfil en formato de cadena.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                             |
|-----------------------------|---------------------------------------------|
| Asociación correcta         | El perfil debe estar vinculado a `testuser`.|
| Representación en cadena    | La representación debe coincidir con `'testuser'`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y asociación del perfil.

---

**Test:** `test_portfolio_creation`

**Objetivo:** Verificar la creación de un portafolio para un perfil de freelancer.

**Precondiciones:**

- Un perfil de freelancer debe existir para el usuario `testuser`.

**Datos de Entrada**

No se requieren datos de entrada específicos.

**Pasos Realizados:**

1. Se crea un portafolio asociado al perfil del freelancer.
2. Se verifica la representación del portafolio en formato de cadena.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                       |
|----------------------------|-------------------------------------------------------|
| Representación en cadena   | La representación debe coincidir con `Portfolio of testuser`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y representación del portafolio.

---

**Test:** `test_portfolio_project_creation`

**Objetivo:** Verificar la creación de un proyecto dentro de un portafolio.

**Precondiciones:**

- Un portafolio debe existir para el perfil del freelancer.

**Datos de Entrada**

- Nombre del proyecto: `'Test Project'`
- Descripción: `'Project Description'`

**Pasos Realizados:**

1. Se crea un proyecto dentro del portafolio del freelancer.
2. Se verifica la representación del proyecto en formato de cadena.

**Resultados Esperados:**

| **Resultado**                 | **Descripción**                    |
|-------------------------------|------------------------------------|
| Representación en cadena      | La representación debe ser `'Test Project'`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y representación del proyecto.

---

**Test:** `test_course_creation`

**Objetivo:** Verificar la creación de un curso dentro del portafolio.

**Precondiciones:**

- Un portafolio debe existir para el perfil del freelancer.

**Datos de Entrada**

- Nombre del curso: `'Test Course'`
- Organización: `'Test Organization'`

**Pasos Realizados:**

1. Se crea un curso dentro del portafolio del freelancer.
2. Se verifica la representación del curso en formato de cadena.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                        |
|------------------------------|----------------------------------------|
| Representación en cadena     | La representación debe ser `'Test Course'`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y representación del curso.

---

**Test:** `test_work_experience_creation`

**Objetivo:** Verificar la creación de una experiencia laboral para un perfil de freelancer.

**Precondiciones:**

- Un perfil de freelancer debe existir.

**Datos de Entrada**

- Título: `'Developer'`
- Compañía: `'Test Company'`

**Pasos Realizados:**

1. Se crea una experiencia laboral para el freelancer.
2. Se verifica la representación de la experiencia en formato de cadena.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                           |
|----------------------------|-------------------------------------------|
| Representación en cadena   | La representación debe ser `'Developer en Test Company'`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y representación de la experiencia laboral.

---

**Test:** `test_curriculum_vitae_creation`

**Objetivo:** Verificar la creación de un CV asociado a un perfil de freelancer.

**Precondiciones:**

- Un perfil de freelancer debe existir.

**Datos de Entrada**

No se requieren datos de entrada específicos.

**Pasos Realizados:**

1. Se crea un CV para el perfil del freelancer.
2. Se verifica la representación del CV en formato de cadena.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                    |
|-----------------------------|----------------------------------------------------|
| Representación en cadena    | La representación debe ser `Curriculum Vitae de testuser`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y representación del CV.

---

**Test:** `test_rating_creation`

**Objetivo:** Verificar la creación de una calificación por parte de un cliente a un freelancer.

**Precondiciones:**

- Un perfil de freelancer debe existir.

**Datos de Entrada**

- Estrellas: `4`
- Comentario: `'Great job!'`

**Pasos Realizados:**

1. Se crea una calificación para el freelancer por parte de un cliente.
2. Se verifica la representación de la calificación en formato de cadena.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                       |
|-----------------------------|-------------------------------------------------------|
| Representación en cadena    | La representación debe ser `'clientuser's rating for freelanceruser'`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y representación de la calificación.

---

**Test:** `test_rating_response_creation`

**Objetivo:** Verificar la creación de una respuesta a una calificación por parte de un freelancer.

**Precondiciones:**

- Una calificación debe existir para el freelancer.

**Datos de Entrada**

- Texto de la respuesta: `'Thank you!'`

**Pasos Realizados:**

1. Se crea una respuesta a la calificación dada por un cliente.
2. Se verifica que la respuesta esté asociada correctamente a la calificación.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                 |
|------------------------------|-------------------------------------------------|
| Asociación correcta          | La respuesta debe estar asociada a la calificación creada.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y asociación correcta de la respuesta.

---

**Test:** `test_notification_creation`

**Objetivo:** Verificar la creación de una notificación para un usuario.

**Precondiciones:**

- Un usuario `testuser` debe existir en el sistema.

**Datos de Entrada**

- Mensaje: `'New notification message'`

**Pasos Realizados:**

1. Se crea una notificación para el usuario.
2. Se verifica la representación de la notificación en formato de cadena.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                      |
|-----------------------------|------------------------------------------------------|
| Representación en cadena    | La representación debe ser `'Notification for testuser: New notification message'`.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la creación y representación de la notificación.

