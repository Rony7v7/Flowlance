## Configuración del Escenario para `FreelancerDashboardViewTest`

| Nombre               | Clase                | Escenario                                                    |
|----------------------|----------------------|--------------------------------------------------------------|
| freelancer_user       | User                 | Usuario de prueba creado para la ejecución del test.          |
| freelancer_profile    | FreelancerProfile    | Perfil de freelancer asociado al usuario de prueba.           |

---

### Pruebas

**Test:** `test_freelancer_dashboard_access`

**Objetivo:** Verificar que el freelancer puede acceder a su dashboard y que se carga la plantilla correcta.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se accede al dashboard del freelancer con el usuario autenticado.
2. Se verifica que el código de estado sea 200 y que se esté utilizando la plantilla correcta.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'dashboard/freelancer_dashboard.html'`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede acceder a su dashboard.

---

**Test:** `test_freelancer_projects`

**Objetivo:** Verificar que los proyectos asignados al freelancer se muestran correctamente en su dashboard.

**Precondiciones:**
- Debe existir al menos un proyecto asignado al freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se crea un proyecto y se asigna al freelancer.
2. Se accede al dashboard del freelancer y se verifica que los proyectos asignados se muestren correctamente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Proyectos en el contexto        | La respuesta debe contener la clave `freelancer_projects`.          |
| Cantidad de proyectos           | La cantidad de proyectos en el contexto debe ser 1.                 |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los proyectos asignados se muestran correctamente.

---

**Test:** `test_freelancer_pending_tasks`

**Objetivo:** Verificar que las tareas pendientes del freelancer se muestran correctamente en su dashboard.

**Precondiciones:**
- Debe existir al menos una tarea pendiente asignada al freelancer.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se crea una tarea pendiente y se asigna al freelancer.
2. Se accede al dashboard del freelancer y se verifica que las tareas pendientes se muestren correctamente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Tareas pendientes en el contexto| La respuesta debe contener la clave `freelancer_pending_tasks`.      |
| Cantidad de tareas pendientes   | La cantidad de tareas pendientes en el contexto debe ser 1.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que las tareas pendientes se muestran correctamente.

---

## Configuración del Escenario para `CompanyDashboardViewTest`

| Nombre             | Clase                | Escenario                                                    |
|--------------------|----------------------|--------------------------------------------------------------|
| company_user       | User                 | Usuario de prueba creado para la ejecución del test.          |
| company_profile    | CompanyProfile       | Perfil de empresa asociado al usuario de prueba.              |

---

### Pruebas

**Test:** `test_company_dashboard_access`

**Objetivo:** Verificar que la empresa puede acceder a su dashboard y que se carga la plantilla correcta.

**Precondiciones:**
- El usuario debe estar autenticado como empresa.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se accede al dashboard de la empresa con el usuario autenticado.
2. Se verifica que el código de estado sea 200 y que se esté utilizando la plantilla correcta.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Uso de plantilla correcta       | Debe utilizar la plantilla `'dashboard/company_dashboard.html'`.    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la empresa puede acceder a su dashboard.

---

**Test:** `test_company_projects`

**Objetivo:** Verificar que los proyectos asignados a la empresa se muestran correctamente en su dashboard.

**Precondiciones:**
- Debe existir al menos un proyecto asignado a la empresa.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se crea un proyecto y se asigna a la empresa.
2. Se accede al dashboard de la empresa y se verifica que los proyectos asignados se muestren correctamente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Proyectos en el contexto        | La respuesta debe contener la clave `company_projects`.             |
| Cantidad de proyectos           | La cantidad de proyectos en el contexto debe ser 1.                 |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los proyectos asignados se muestran correctamente.

---

**Test:** `test_freelancers_associated_with_projects`

**Objetivo:** Verificar que los freelancers asignados a los proyectos de la empresa se muestran correctamente en su dashboard.

**Precondiciones:**
- Debe existir al menos un freelancer asignado a un proyecto de la empresa.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se crea un freelancer y se asigna a un proyecto de la empresa.
2. Se accede al dashboard de la empresa y se verifica que los freelancers asociados se muestren correctamente.

**Resultados Esperados:**

| **Resultado**                      | **Descripción**                                                     |
|------------------------------------|---------------------------------------------------------------------|
| Código de estado correcto           | La respuesta debe tener un código de estado `200`.                  |
| Freelancers en el contexto          | La respuesta debe contener la clave `recent_freelancers`.           |
| Cantidad de freelancers asociados   | La cantidad de freelancers en el contexto debe ser 1.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los freelancers asociados se muestran correctamente.

---

**Test:** `test_company_ratings_for_freelancers`

**Objetivo:** Verificar que las calificaciones dadas a los freelancers por la empresa se muestran correctamente en su dashboard.

**Precondiciones:**
- Debe existir al menos una calificación para un freelancer en un proyecto de la empresa.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Se crea un freelancer y se le asigna una calificación por parte de la empresa.
2. Se accede al dashboard de la empresa y se verifica que las calificaciones de los freelancers se muestren correctamente.

**Resultados Esperados:**

| **Resultado**                  | **Descripción**                                                     |
|--------------------------------|---------------------------------------------------------------------|
| Código de estado correcto       | La respuesta debe tener un código de estado `200`.                  |
| Freelancers en el contexto      | La respuesta debe contener la clave `recent_freelancers`.           |
| Cantidad de calificaciones      | Se debe mostrar la calificación del freelancer.                     |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que las calificaciones de los freelancers se muestran correctamente.
