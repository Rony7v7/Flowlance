
## Configuración del Escenario para ProfileModuleTests

| Nombre       | Clase               | Escenario                                           |
|--------------|---------------------|-----------------------------------------------------|
| user         | User                | Usuario de prueba creado para la ejecución del test |
| profile      | FreelancerProfile   | Perfil de freelancer asociado al usuario de prueba  |
| autenticado  | TestClient          | El usuario de prueba está autenticado en el sistema |

---

## Pruebas

**Test:** `test_profile_creation`

**Objetivo:** Este test verifica que el perfil de freelancer se crea correctamente cuando se asocia con un usuario existente (`testuser`). Se asegura de que el perfil esté vinculado al usuario y que los datos sean consistentes en la base de datos.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test, ya que verifica la existencia y consistencia del perfil creado durante el `setUp()`.

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se verifica la cantidad de perfiles de freelancer en la base de datos.
3. Se comprueba que el perfil de freelancer esté correctamente asociado al usuario `testuser`.

**Resultados Esperados**

| **Resultado**                                          | **Descripción**                                                                 |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| Verificación de la cantidad de perfiles                | La base de datos debe contener exactamente un perfil de freelancer.             |
| Asociación correcta del perfil                         | El perfil de freelancer debe estar vinculado al usuario con el nombre `'testuser'`. |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el perfil de freelancer se crea y asocia correctamente con el usuario `testuser`.


---

**Test:** `test_view_own_profile`

**Objetivo:** Este test verifica que un usuario pueda visualizar correctamente su propio perfil de freelancer. Se asegura de que la página del perfil del freelancer se cargue correctamente y que contenga información específica del usuario autenticado.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- El usuario debe estar autenticado en la aplicación durante la ejecución del test.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test, ya que verifica la visualización del perfil del usuario autenticado.

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se realiza una solicitud GET a la URL del perfil del freelancer (`freelancer_profile`) para visualizar el perfil del usuario autenticado.
3. Se verifica que el código de estado de la respuesta sea `200`, lo que indica que la página se cargó correctamente.
4. Se comprueba que la respuesta contiene el nombre de usuario (`testuser`), lo que confirma que el perfil mostrado es el del usuario autenticado.

**Resultados Esperados**

| **Resultado**                                          | **Descripción**                                                                 |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| Código de estado correcto                              | La respuesta debe tener un código de estado `200`, indicando que la página se cargó correctamente. |
| Visualización del nombre de usuario                    | La respuesta debe contener el nombre de usuario `'testuser'`, confirmando que el perfil es visible. |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el usuario puede visualizar su propio perfil de freelancer correctamente.


---

**Test:** `test_view_other_profile`

**Objetivo:** Este test verifica que un usuario pueda visualizar correctamente el perfil de freelancer de otro usuario. Se asegura de que la página del perfil del otro usuario se cargue correctamente y contenga información específica de ese usuario.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- Un segundo usuario (`otheruser`) debe existir en el sistema y tener un perfil de freelancer creado automáticamente por señales.

**Datos de Entrada**

No se requieren datos de entrada específicos para este test, ya que verifica la visualización del perfil de otro usuario.

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se crea un segundo usuario (`otheruser`), y se verifica que su perfil de freelancer se cree automáticamente mediante señales.
3. Se realiza una solicitud GET a la URL del perfil del freelancer (`freelancer_profile_view`) del otro usuario (`otheruser`).
4. Se verifica que el código de estado de la respuesta sea `200`, lo que indica que la página se cargó correctamente.
5. Se comprueba que la respuesta contiene el nombre de usuario (`otheruser`), confirmando que se muestra el perfil del usuario correcto.

**Resultados Esperados**

| **Resultado**                                          | **Descripción**                                                                 |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| Código de estado correcto                              | La respuesta debe tener un código de estado `200`, indicando que la página se cargó correctamente. |
| Visualización del nombre de usuario                    | La respuesta debe contener el nombre de usuario `'otheruser'`, confirmando que el perfil mostrado es el correcto. |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que un usuario puede visualizar correctamente el perfil de otro usuario de freelancer.


---

**Test:** `test_add_skill`

**Objetivo:** Este test verifica que un usuario pueda agregar una habilidad predefinida a su perfil de freelancer. Se asegura de que la habilidad se agregue correctamente a la lista de habilidades del perfil.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.

**Datos de Entrada**

| **Campo**      | **Valor**    |
|----------------|--------------|
| Nombre         | Python       |
| Es Personalizada | False        |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se crea una habilidad predefinida (`Python`) que no es personalizada (`is_custom=False`).
3. Se añade la habilidad al perfil de freelancer del usuario.
4. Se verifica que la habilidad agregada esté presente en la lista de habilidades del perfil.

**Resultados Esperados**

| **Resultado**                       | **Descripción**                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Habilidad agregada correctamente    | La habilidad `'Python'` debe estar presente en la lista de habilidades del perfil del freelancer. |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que la habilidad predefinida se agrega correctamente al perfil de freelancer del usuario.


---

**Test:** `test_add_custom_skill`

**Objetivo:** Este test verifica que un usuario pueda agregar una habilidad personalizada a su perfil de freelancer mediante el formulario `AddSkillsForm`. Se asegura de que la habilidad personalizada se guarde correctamente en la base de datos y se asocie con el perfil del usuario.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.

**Datos de Entrada**

| **Campo**       | **Valor**  |
|-----------------|------------|
| Habilidades Personalizadas | Django     |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se llena el formulario `AddSkillsForm` con una habilidad personalizada (`Django`).
3. Se valida el formulario para asegurarse de que los datos son correctos.
4. Se guarda la habilidad personalizada en la base de datos asociándola con el usuario.
5. Se verifica que la habilidad `'Django'` esté presente en la base de datos como una habilidad personalizada (`is_custom=True`).

**Resultados Esperados**

| **Resultado**                                        | **Descripción**                                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------------|
| El formulario debe ser válido                        | `form.is_valid()` debe devolver `True`.                                         |
| Habilidad personalizada guardada correctamente       | La habilidad `'Django'` debe existir en la base de datos con `is_custom=True`.  |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que la habilidad personalizada se agrega correctamente al perfil del freelancer a través del formulario.


---


**Test:** `test_add_work_experience`

**Objetivo:** Este test verifica que un usuario pueda agregar una experiencia laboral correctamente a su perfil de freelancer mediante el formulario `AddWorkExperienceForm`. Se asegura de que los datos ingresados en el formulario se guarden en la base de datos y que la experiencia se asocie correctamente con el perfil del usuario.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- El usuario debe estar autenticado en la aplicación durante la ejecución del test.

**Datos de Entrada**

| **Campo**           | **Valor**                        |
|---------------------|----------------------------------|
| Título              | Software Developer               |
| Ocupación           | Software Development             |
| Compañía            | Tech Co                          |
| Fecha de Inicio     | 2022-01-01                       |
| Fecha de Fin        | 2023-01-01                       |
| Descripción         | Developed various web applications.|

**Pasos Realizados**

1. Se crea un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se llena el formulario `AddWorkExperienceForm` con los datos de la experiencia laboral.
3. Se valida el formulario para asegurarse de que los datos son correctos.
4. Se guarda la experiencia laboral en la base de datos, asociándola con el perfil del freelancer.
5. Se verifica que la cantidad de registros de experiencia laboral en la base de datos sea `1`.
6. Se verifica que el título de la primera experiencia laboral en el perfil del freelancer sea `'Software Developer'`.

**Resultados Esperados**

| **Resultado**                                          | **Descripción**                                                                 |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| El formulario debe ser válido                          | `form.is_valid()` debe devolver `True`.                                         |
| La experiencia laboral debe guardarse en la base de datos | El perfil del freelancer debe tener una nueva experiencia laboral asociada.     |
| Verificación de la cantidad de registros               | La base de datos debe contener exactamente un registro de experiencia laboral.  |
| Verificación del título                                | El título de la experiencia laboral debe ser `'Software Developer'`.            |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que la funcionalidad de agregar experiencia laboral funciona como se espera.


---


**Test:** `test_add_experience_view`

**Objetivo:** Este test verifica que un usuario pueda agregar una experiencia laboral a su perfil de freelancer mediante la vista `add_experience`. Se asegura de que la experiencia se guarde correctamente en la base de datos y que el usuario sea redirigido al perfil tras agregar la experiencia.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.

**Datos de Entrada**

| **Campo**          | **Valor**                             |
|--------------------|---------------------------------------|
| Título             | Backend Developer                     |
| Compañía           | Tech Innovators                       |
| Fecha de Inicio    | 2022-05-01                            |
| Fecha de Fin       | 2023-04-01                            |
| Descripción        | Worked on backend systems using Django.|

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se envía una solicitud POST a la vista `add_experience` con los datos de la experiencia laboral.
3. Se verifica que la respuesta redirija correctamente a la vista del perfil del freelancer (`freelancer_profile`).
4. Se comprueba que la experiencia laboral se haya agregado correctamente a la base de datos.
5. Se verifica que los datos de la experiencia laboral agregada coincidan con los datos proporcionados.
6. Se confirma que la experiencia laboral está asociada con el perfil del freelancer del usuario.

**Resultados Esperados**

| **Resultado**                                         | **Descripción**                                                                 |
|-------------------------------------------------------|---------------------------------------------------------------------------------|
| Redirección correcta                                  | La respuesta debe redirigir a la vista `freelancer_profile`.                    |
| Experiencia laboral guardada                          | La base de datos debe contener un registro de experiencia laboral.              |
| Verificación de los datos de la experiencia           | Los datos de la experiencia deben coincidir con `'Backend Developer'`, `'Tech Innovators'`, y `'Worked on backend systems using Django.'`. |
| Asociación correcta de la experiencia                 | La experiencia laboral debe estar asociada al perfil del freelancer.            |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que la experiencia laboral se agrega correctamente a través de la vista y que el usuario es redirigido al perfil.


---

**Test:** `test_add_project`

**Objetivo:** Este test verifica que un usuario pueda agregar un proyecto a su portafolio de freelancer mediante el formulario `AddProjectForm`. Se asegura de que el proyecto se guarde correctamente en la base de datos y se asocie al portafolio del perfil del freelancer.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- Un portafolio debe estar creado y asociado al perfil del freelancer.

**Datos de Entrada**

| **Campo**            | **Valor**                                 |
|----------------------|-------------------------------------------|
| Nombre del Proyecto  | Web App                                   |
| Cliente              | Client A                                  |
| Descripción del Proyecto | Developed a web app using Django      |
| Fecha de Inicio      | 2023-01-01                                |
| Fecha de Fin         | 2023-06-01                                |
| Actividades Realizadas | Development, Testing                    |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se crea un portafolio asociado al perfil del freelancer.
3. Se llena el formulario `AddProjectForm` con los datos del proyecto.
4. Se valida el formulario para asegurarse de que los datos son correctos.
5. Se guarda el proyecto en la base de datos, asociándolo al portafolio del freelancer.
6. Se verifica que el proyecto se haya agregado correctamente a la base de datos.
7. Se confirma que el nombre del primer proyecto en el portafolio coincida con `'Web App'`.

**Resultados Esperados**

| **Resultado**                                      | **Descripción**                                                                 |
|----------------------------------------------------|---------------------------------------------------------------------------------|
| El formulario debe ser válido                      | `form.is_valid()` debe devolver `True`.                                         |
| Proyecto guardado correctamente                    | La base de datos debe contener exactamente un proyecto asociado al portafolio.  |
| Verificación del nombre del proyecto               | El nombre del primer proyecto debe ser `'Web App'`.                             |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el proyecto se agrega correctamente al portafolio del freelancer a través del formulario.


---

**Test:** `test_upload_cv`

**Objetivo:** Este test verifica que un usuario pueda subir correctamente un archivo de Curriculum Vitae (CV) a su perfil de freelancer mediante el formulario `UploadCVForm`. Se asegura de que el archivo se guarde en la ruta esperada y se asocie al perfil del freelancer.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- Se verifica si ya existe un CV asociado al perfil del freelancer, de lo contrario, se prepara una nueva instancia.

**Datos de Entrada**

| **Campo**  | **Valor**                      |
|------------|-------------------------------|
| Archivo    | cv.pdf (contenido binario: `b'file_content'`) |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se verifica si el perfil del freelancer ya tiene un CV asociado; si no, se prepara una nueva instancia para el formulario.
3. Se llena el formulario `UploadCVForm` con el archivo de CV (`cv.pdf`).
4. Se valida el formulario para asegurarse de que los datos son correctos.
5. Se guarda el archivo de CV en la base de datos, asociándolo al perfil del freelancer.
6. Se verifica que el archivo de CV se haya subido correctamente y que la cantidad de registros en la base de datos sea `1`.
7. Se confirma que el archivo se guardó en la ruta esperada (`'resumes/cv'`).

**Resultados Esperados**

| **Resultado**                                         | **Descripción**                                                                 |
|-------------------------------------------------------|---------------------------------------------------------------------------------|
| El formulario debe ser válido                         | `form.is_valid()` debe devolver `True`.                                         |
| CV guardado correctamente                             | La base de datos debe contener exactamente un registro de CV asociado al perfil del freelancer. |
| Verificación de la ruta del archivo                   | El nombre del archivo debe contener `'resumes/cv'`.                             |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el CV se sube y guarda correctamente en la ruta esperada, asociado al perfil del freelancer.



---

**Test:** `test_add_project_with_attachments`

**Objetivo:** Este test verifica que un usuario pueda agregar un proyecto con archivos adjuntos a su portafolio de freelancer mediante el formulario `AddProjectForm`. Se asegura de que el proyecto y los archivos adjuntos se guarden correctamente en la base de datos y se asocien al portafolio del perfil del freelancer.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- Un portafolio debe estar creado y asociado al perfil del freelancer.

**Datos de Entrada**

| **Campo**              | **Valor**                              |
|------------------------|----------------------------------------|
| Nombre del Proyecto    | Test Project with File                 |
| Cliente                | Test Client                            |
| Descripción del Proyecto | Test Description                    |
| Fecha de Inicio        | 2024-01-01                             |
| Fecha de Fin           | 2024-06-01                             |
| Actividades Realizadas | Testing, Documentation                 |
| Archivos Adjuntos      | test_file.txt (contenido binario: `b'File content'`) |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se crea un portafolio asociado al perfil del freelancer.
3. Se llena el formulario `AddProjectForm` con los datos del proyecto y un archivo adjunto (`test_file.txt`).
4. Se valida el formulario para asegurarse de que los datos son correctos.
5. Se guarda el proyecto en la base de datos, asociándolo al portafolio del freelancer.
6. Se verifica que el proyecto se haya agregado correctamente a la base de datos y que el archivo adjunto esté asociado al proyecto.
7. Se confirma que el archivo se guardó en la ruta esperada (`'portfolio/test_file'`).

**Resultados Esperados**

| **Resultado**                                           | **Descripción**                                                                 |
|---------------------------------------------------------|---------------------------------------------------------------------------------|
| El formulario debe ser válido                           | `form.is_valid()` debe devolver `True`.                                         |
| Proyecto con archivo adjunto guardado correctamente     | La base de datos debe contener exactamente un registro de proyecto con un archivo adjunto. |
| Verificación de la ruta del archivo adjunto             | El nombre del archivo adjunto debe contener `'portfolio/test_file'`.            |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el proyecto con archivos adjuntos se agrega y guarda correctamente en el portafolio del freelancer.


---

**Test:** `test_add_project_with_external_link`

**Objetivo:** Este test verifica que un usuario pueda agregar un proyecto con un enlace externo a su portafolio de freelancer mediante el formulario `AddProjectForm`. Se asegura de que el proyecto y el enlace externo se guarden correctamente en la base de datos y se asocien al portafolio del perfil del freelancer.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- Un portafolio debe estar creado y asociado al perfil del freelancer.

**Datos de Entrada**

| **Campo**                | **Valor**                                   |
|--------------------------|---------------------------------------------|
| Nombre del Proyecto      | Test Project with Link                      |
| Cliente                  | Test Client                                 |
| Descripción del Proyecto | Project with external link                  |
| Fecha de Inicio          | 2024-01-01                                  |
| Fecha de Fin             | 2024-06-01                                  |
| Actividades Realizadas   | Development, Testing                        |
| Enlace Externo           | https://github.com/test                     |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se crea un portafolio asociado al perfil del freelancer.
3. Se llena el formulario `AddProjectForm` con los datos del proyecto, incluyendo un enlace externo (`https://github.com/test`).
4. Se valida el formulario para asegurarse de que los datos son correctos. Si el formulario no es válido, se muestran los errores para depuración.
5. Se guarda el proyecto en la base de datos, asociándolo al portafolio del freelancer.
6. Se verifica que el proyecto se haya agregado correctamente a la base de datos.
7. Se confirma que el enlace externo del proyecto coincida con `'https://github.com/test'`.

**Resultados Esperados**

| **Resultado**                                 | **Descripción**                                                                 |
|-----------------------------------------------|---------------------------------------------------------------------------------|
| El formulario debe ser válido                 | `form.is_valid()` debe devolver `True`.                                         |
| Proyecto con enlace externo guardado correctamente | La base de datos debe contener exactamente un registro de proyecto con un enlace externo. |
| Verificación del enlace externo               | El enlace externo del proyecto debe ser `'https://github.com/test'`.            |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el proyecto con un enlace externo se agrega y guarda correctamente en el portafolio del freelancer.

---


**Test:** `test_portfolio_visibility`

**Objetivo:** Este test verifica que el portafolio de un freelancer sea visible en su perfil. Se asegura de que la página del perfil del freelancer cargue correctamente y muestre el contenido asociado al portafolio, como los proyectos.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- Un portafolio debe estar creado y asociado al perfil del freelancer.
- Un proyecto debe estar asociado al portafolio para asegurar que haya contenido visible.

**Datos de Entrada**

| **Campo**                | **Valor**                                      |
|--------------------------|------------------------------------------------|
| Nombre del Proyecto      | Test Project                                   |
| Descripción del Proyecto | A test project for visibility                  |
| Fecha de Inicio          | 2024-01-01                                     |
| Fecha de Fin             | 2024-06-01                                     |
| Actividades Realizadas   | Development, Testing                           |
| Imagen del Proyecto      | test_image.jpg (contenido binario: `b'Image content'`) |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se crea un portafolio asociado al perfil del freelancer.
3. Se agrega un proyecto al portafolio con datos relevantes, incluyendo una imagen del proyecto, para asegurar que haya contenido visible en la página.
4. Se realiza una solicitud GET a la página del perfil del freelancer.
5. Se verifica que la respuesta tenga un código de estado `200`, indicando que la página cargó correctamente.
6. Se comprueba que el nombre del proyecto `'Test Project'` o información relacionada con el portafolio esté presente en el HTML de la respuesta.

**Resultados Esperados**

| **Resultado**                                       | **Descripción**                                                                 |
|-----------------------------------------------------|---------------------------------------------------------------------------------|
| Código de estado correcto                           | La respuesta debe tener un código de estado `200`, indicando que la página se cargó correctamente. |
| Contenido del portafolio visible                    | La respuesta debe contener el nombre del proyecto `'Test Project'` o información relevante del portafolio. |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el portafolio es visible en el perfil del freelancer y muestra el contenido correctamente.


---

**Test:** `test_add_course`

**Objetivo:** Este test verifica que un usuario pueda agregar un curso a su portafolio de freelancer mediante el formulario `AddCourseForm`. Se asegura de que el curso se guarde correctamente en la base de datos y se asocie al portafolio del perfil del freelancer.

**Precondiciones:**

- Un usuario (`testuser`) debe existir en el sistema y estar autenticado.
- El perfil de freelancer asociado al usuario (`FreelancerProfile`) debe estar creado.
- Un portafolio debe estar creado y asociado al perfil del freelancer.

**Datos de Entrada**

| **Campo**             | **Valor**                           |
|-----------------------|-------------------------------------|
| Nombre del Curso      | Django Mastery                      |
| Descripción del Curso | Advanced Django course              |
| Organización          | Online Academy                      |
| Enlace del Curso      | http://example.com                  |
| Fecha de Expedición   | 2023-01-01                          |

**Pasos Realizados**

1. Se configura el escenario con la creación de un usuario de prueba y su perfil de freelancer correspondiente en el método `setUp()`.
2. Se crea un portafolio asociado al perfil del freelancer.
3. Se llena el formulario `AddCourseForm` con los datos del curso.
4. Se valida el formulario para asegurarse de que los datos son correctos.
5. Se guarda el curso en la base de datos.
6. Se verifica que el curso se haya agregado correctamente y que la base de datos contenga exactamente un registro de curso.

**Resultados Esperados**

| **Resultado**                           | **Descripción**                                                                 |
|-----------------------------------------|---------------------------------------------------------------------------------|
| El formulario debe ser válido           | `form.is_valid()` debe devolver `True`.                                         |
| Curso guardado correctamente            | La base de datos debe contener exactamente un registro de curso asociado al portafolio del freelancer. |

**Resultados Obtenidos**

- El test pasa exitosamente, lo que confirma que el curso se agrega y guarda correctamente en el portafolio del freelancer.
