## Configuración del Escenario para FormsTests

| Nombre              | Clase                    | Escenario                                                             |
|---------------------|--------------------------|-----------------------------------------------------------------------|
| user                | User                     | Usuario de prueba creado para los tests                              |
| profile             | FreelancerProfile        | Perfil de freelancer asociado al usuario de prueba                   |
| skill               | Skill                    | Habilidad utilizada en los formularios de habilidades                |
| uploaded_file       | SimpleUploadedFile       | Archivo simulado para pruebas de carga de CV                         |
| form_data           | dict                     | Diccionario de datos utilizado para poblar los formularios en los tests |

---

### Pruebas

**Test:** `test_add_course_form_valid`

**Objetivo:** Verificar que el formulario de agregar curso (`AddCourseForm`) sea válido con datos correctos.

**Precondiciones:**

- Se proporcionan datos completos y válidos para el curso.

**Datos de Entrada**

- Nombre del curso: `'Django for Beginners'`
- Organización: `'Udemy'`
- Enlace del curso: `'https://udemy.com/django-course'`
- Fecha de expedición: `Fecha actual`

**Pasos Realizados:**

1. Se crea un formulario `AddCourseForm` con los datos proporcionados.
2. Se verifica que el formulario sea válido.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                      |
|----------------------------|--------------------------------------|
| Formulario válido          | El formulario debe ser considerado válido. |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el formulario se valida correctamente.

---

**Test:** `test_add_course_form_invalid`

**Objetivo:** Verificar que el formulario de agregar curso sea inválido con datos incompletos.

**Precondiciones:**

- Se proporciona un nombre de curso vacío.

**Datos de Entrada**

- Nombre del curso: `''`
- Descripción del curso: `'Learn Django basics'`

**Pasos Realizados:**

1. Se crea un formulario `AddCourseForm` con los datos proporcionados.
2. Se verifica que el formulario sea inválido.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                    |
|----------------------------|------------------------------------|
| Formulario inválido        | El formulario debe ser considerado inválido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el formulario se marca como inválido cuando faltan datos requeridos.

---

**Test:** `test_add_project_form_invalid`

**Objetivo:** Verificar que el formulario de agregar proyecto (`AddProjectForm`) sea inválido con datos incompletos.

**Precondiciones:**

- Se proporciona un nombre de proyecto vacío.

**Datos de Entrada**

- Nombre del proyecto: `''`
- Fecha de inicio: `01/01/2023`

**Pasos Realizados:**

1. Se crea un formulario `AddProjectForm` con los datos proporcionados.
2. Se verifica que el formulario sea inválido.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                    |
|---------------------------|------------------------------------|
| Formulario inválido       | El formulario debe ser considerado inválido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el formulario no es válido con datos incompletos.

---

**Test:** `test_upload_cv_form_valid`

**Objetivo:** Verificar que el formulario de carga de CV (`UploadCVForm`) acepte un archivo válido.

**Precondiciones:**

- Se proporciona un archivo PDF simulado.

**Datos de Entrada**

- Archivo: `test_cv.pdf`

**Pasos Realizados:**

1. Se crea un formulario `UploadCVForm` con un archivo PDF simulado.
2. Se verifica que el formulario sea válido.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                    |
|---------------------------|------------------------------------|
| Formulario válido         | El formulario debe aceptar el archivo. |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la validación correcta del formulario con un archivo PDF.

---

**Test:** `test_add_skills_form_valid`

**Objetivo:** Verificar que el formulario de agregar habilidades (`AddSkillsForm`) sea válido con habilidades predeterminadas y personalizadas.

**Precondiciones:**

- El usuario y su perfil deben existir en el sistema.

**Datos de Entrada**

- Habilidades predeterminadas: `[Python]`
- Habilidades personalizadas: `'React, Vue.js'`

**Pasos Realizados:**

1. Se crea un formulario `AddSkillsForm` con habilidades predeterminadas y personalizadas.
2. Se verifica que el formulario sea válido.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                      |
|-----------------------------|--------------------------------------|
| Formulario válido           | El formulario debe ser considerado válido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que el formulario acepta tanto habilidades predeterminadas como personalizadas.

---

**Test:** `test_add_skills_form_no_skills`

**Objetivo:** Verificar que el formulario de agregar habilidades sea válido incluso cuando no se seleccionan habilidades.

**Precondiciones:**

- El usuario y su perfil deben existir en el sistema.

**Datos de Entrada**

- No se seleccionan habilidades.

**Pasos Realizados:**

1. Se crea un formulario `AddSkillsForm` sin seleccionar ninguna habilidad.
2. Se verifica que el formulario sea válido.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                  |
|----------------------------|----------------------------------|
| Formulario válido          | El formulario debe ser considerado válido. |

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando que no seleccionar habilidades es una opción válida.

---

**Test:** `test_add_work_experience_form_valid`

**Objetivo:** Verificar que el formulario de agregar experiencia laboral (`AddWorkExperienceForm`) sea válido con datos completos.

**Precondiciones:**

- El usuario y su perfil deben existir en el sistema.

**Datos de Entrada**

- Título: `'Software Developer'`
- Compañía: `'XYZ Ltd'`
- Fechas de inicio y fin: `01/01/2021 - 01/01/2022`

**Pasos Realizados:**

1. Se crea un formulario `AddWorkExperienceForm` con los datos proporcionados.
2. Se verifica que el formulario sea válido.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                       |
|---------------------------|---------------------------------------|
| Formulario válido         | El formulario debe ser considerado válido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la validación correcta del formulario.

---

**Test:** `test_add_work_experience_form_invalid`

**Objetivo:** Verificar que el formulario de agregar experiencia laboral sea inválido con datos incompletos.

**Precondiciones:**

- El usuario y su perfil deben existir en el sistema.

**Datos de Entrada**

- Título: `''`
- Fecha de inicio: `01/01/2021`

**Pasos Realizados:**

1. Se crea un formulario `AddWorkExperienceForm` con los datos incompletos.
2. Se verifica que el formulario sea inválido.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                      |
|-----------------------------|--------------------------------------|
| Formulario inválido         | El formulario debe ser considerado inválido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la validación incorrecta con datos incompletos.

---

**Test:** `test_rating_form_valid`

**Objetivo:** Verificar que el formulario de calificación (`RatingForm`) sea válido con un puntaje dentro del rango permitido.

**Precondiciones:**

- No se requieren precondiciones específicas.

**Datos de Entrada**

- Estrellas: `5`
- Comentario: `'Excellent job!'`

**Pasos Realizados:**

1. Se crea un formulario `RatingForm` con los datos proporcionados.
2. Se verifica que el formulario sea válido.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                       |
|---------------------------|---------------------------------------|
| Formulario válido         | El formulario debe ser considerado válido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la validez del formulario con un puntaje permitido.

---

**Test:** `test_rating_form_invalid`

**Objetivo:** Verificar que el formulario de calificación sea inválido con un puntaje fuera del rango permitido.

**Precondiciones:**

- No se requieren precondiciones específicas.

**Datos de Entrada**

- Estrellas: `6`

**Pasos Realizados:**

1. Se crea un formulario `RatingForm` con un puntaje fuera del rango.
2. Se verifica que el formulario sea inválido.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                      |
|-----------------------------|--------------------------------------|
| Formulario inválido         | El formulario debe ser considerado inválido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la invalidez con un puntaje fuera de los límites.

---

**Test:** `test_rating_response_form_valid`

**Objetivo:** Verificar que el formulario de respuesta a una calificación (`RatingResponseForm`) sea válido con un texto de respuesta adecuado.

**Precondiciones:**

- No se requieren precondiciones específicas.

**Datos de Entrada**

- Texto de respuesta: `'Thank you for your feedback!'`

**Pasos Realizados:**

1. Se crea un formulario `RatingResponseForm` con el texto de respuesta proporcionado.
2. Se verifica que

 el formulario sea válido.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                        |
|---------------------------|----------------------------------------|
| Formulario válido         | El formulario debe ser considerado válido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la validez del formulario con una respuesta adecuada.

---

**Test:** `test_rating_response_form_invalid`

**Objetivo:** Verificar que el formulario de respuesta a una calificación sea inválido con un texto vacío.

**Precondiciones:**

- No se requieren precondiciones específicas.

**Datos de Entrada**

- Texto de respuesta: `''`

**Pasos Realizados:**

1. Se crea un formulario `RatingResponseForm` con un texto vacío.
2. Se verifica que el formulario sea inválido.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                       |
|----------------------------|---------------------------------------|
| Formulario inválido        | El formulario debe ser considerado inválido.|

**Resultados Obtenidos:**

- El test pasa exitosamente, confirmando la invalidez del formulario con un texto vacío.
