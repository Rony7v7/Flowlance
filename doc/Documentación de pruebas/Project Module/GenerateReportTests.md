# Documentación de Tests

## Configuración del Escenario para `ReportGenerationCommandTest`

| Nombre        | Clase                        | Escenario                                                      |
|---------------|------------------------------|----------------------------------------------------------------|
| user          | User                         | Usuario de prueba creado para la ejecución del test.           |
| project       | Project                      | Proyecto de prueba asociado al usuario.                        |
| milestone     | Milestone                    | Hito de prueba asociado al proyecto.                           |
| task          | Task                         | Tarea de prueba asociada al hito.                              |
| report_settings | ProjectReportSettings       | Configuración de reporte del proyecto para el usuario.         |
| user_report_settings | UserProjectReportSettings | Configuración de reportes del usuario.                         |

---

### Pruebas

**Test:** `test_handle_method`

**Objetivo:** Verificar que el comando `generate_periodic_reports` se ejecute correctamente y que intente enviar un email.

**Precondiciones:**
- El proyecto, el hito y la tarea deben existir.
- Las configuraciones de reporte para el proyecto y el usuario deben estar definidas.

**Datos de Entrada:**
- Ninguno, ya que se realiza una llamada al comando de gestión.

**Pasos Realizados:**
1. Se realiza una llamada al comando `generate_periodic_reports`.
2. Se verifica que el comando se ejecuta sin errores.
3. Se comprueba que el método para enviar el email fue llamado.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Ejecución exitosa del comando | El comando debe ejecutarse sin errores.                             |
| Envío de email                | El método de envío de email debe ser llamado una vez.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el comando se ejecuta correctamente y el email es enviado.

---

**Test:** `test_should_generate_report`

**Objetivo:** Verificar que el comando determina correctamente si debe generar un reporte basado en la frecuencia configurada.

**Precondiciones:**
- Las configuraciones de reporte deben existir.

**Datos de Entrada:**

| **Campo**              | **Valor**                            |
|------------------------|--------------------------------------|
| report_frequency        | `daily`, `weekly`, `monthly`         |

**Pasos Realizados:**
1. Se verifica si el comando genera reportes según la frecuencia `daily`.
2. Se cambia la frecuencia a `weekly` y se verifica si el reporte se genera solo los lunes.
3. Se cambia la frecuencia a `monthly` y se verifica si el reporte se genera solo el primer día del mes.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Reporte diario                | El comando debe generar un reporte diariamente.                     |
| Reporte semanal               | El comando debe generar un reporte solo los lunes.                  |
| Reporte mensual               | El comando debe generar un reporte solo el primer día del mes.       |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la lógica de generación de reportes se comporta como se espera según la frecuencia.

---

**Test:** `test_calculate_milestone_progress`

**Objetivo:** Verificar el cálculo del progreso de los hitos en el proyecto.

**Precondiciones:**
- Un proyecto con hitos y tareas debe existir.

**Datos de Entrada:**
- Ninguno, se calcula el progreso con el estado de las tareas.

**Pasos Realizados:**
1. Se calcula el progreso inicial del hito (debe ser 0%).
2. Se agregan tareas al hito y se marcan como completadas.
3. Se recalcula el progreso y se verifica que sea del 100%.
4. Se agrega un nuevo hito con tareas incompletas y se recalcula el progreso.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Progreso inicial              | El progreso inicial debe ser 0%.                                    |
| Progreso completo             | El progreso debe ser 100% cuando todas las tareas están completadas.|
| Progreso parcial              | El progreso debe reflejar el porcentaje correcto con hitos incompletos.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cálculo de progreso de hitos funciona correctamente.

---

**Test:** `test_calculate_task_progress`

**Objetivo:** Verificar el cálculo del progreso de las tareas en el proyecto.

**Precondiciones:**
- El proyecto debe tener tareas asociadas a los hitos.

**Datos de Entrada:**
- Ninguno, se calcula el progreso con el estado de las tareas.

**Pasos Realizados:**
1. Se calcula el progreso inicial de las tareas (debe ser 0%).
2. Se completa una tarea y se recalcula el progreso (debe ser 100%).

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Progreso inicial              | El progreso inicial debe ser 0% si no hay tareas completadas.       |
| Progreso completo             | El progreso debe ser 100% cuando todas las tareas están completadas.|

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cálculo de progreso de tareas funciona correctamente.

---

**Test:** `test_generate_report`

**Objetivo:** Verificar que el reporte del proyecto se genera correctamente en formato PDF.

**Precondiciones:**
- El proyecto y las configuraciones de reporte deben existir.

**Datos de Entrada:**
- Ninguno, se genera el reporte para el proyecto.

**Pasos Realizados:**
1. Se genera el reporte del proyecto utilizando la configuración de reporte.
2. Se verifica que se crea un buffer PDF y que el método de creación de PDF es llamado.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Buffer PDF generado           | Se debe generar un buffer no vacío con el contenido del reporte.    |
| Llamada al método PDF         | El método para generar el PDF debe ser llamado una vez.             |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el reporte del proyecto se genera correctamente.

---

**Test:** `test_send_report_email`

**Objetivo:** Verificar que el email con el reporte se envía correctamente.

**Precondiciones:**
- El usuario y el proyecto deben existir.

**Datos de Entrada:**
- Ninguno, se envía el email con el reporte generado.

**Pasos Realizados:**
1. Se llama al método para enviar el email con el reporte.
2. Se verifica que el email es enviado correctamente.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                                     |
|------------------------------|---------------------------------------------------------------------|
| Envío de email                | El método de envío de email debe ser llamado una vez.               |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el email con el reporte se envía correctamente.
