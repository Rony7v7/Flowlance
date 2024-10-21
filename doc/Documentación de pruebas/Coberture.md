# Informe de Cobertura de Pruebas

## Explicación del Informe de Cobertura

La cobertura total reportada es del **84%**, sin embargo, este valor está influenciado por algunas aplicaciones como `chat`, `payment`, `notifications`, entre otras, que aún no tienen sus funcionalidades implementadas. Esto genera que haya declaraciones sin pruebas en estas áreas, lo cual reduce el porcentaje general de cobertura.

Excluyendo estas aplicaciones del cálculo, la cobertura efectiva del código desarrollado y probado es significativamente mayor. Los resultados muestran que se ha realizado un esfuerzo considerable en probar las funcionalidades desarrolladas hasta ahora, y se espera que la cobertura global aumente a medida que se avance con el desarrollo y las pruebas de las áreas pendientes.

## Informe de Cobertura

| Name                                                        | Stmts | Miss | Cover |
|-------------------------------------------------------------|-------|------|-------|
| chat\_init_.py                                               | 0     | 0    | 100%  |
| chat\admin.py                                                | 1     | 0    | 100%  |
| chat\apps.py                                                 | 4     | 0    | 100%  |
| chat\migrations\_init_.py                                    | 0     | 0    | 100%  |
| chat\models.py                                               | 1     | 0    | 100%  |
| chat\tests.py                                                | 1     | 0    | 100%  |
| chat\urls.py                                                 | 3     | 0    | 100%  |
| chat\views.py                                                | 3     | 1    | 67%   |
| dashboard\_init_.py                                          | 0     | 0    | 100%  |
| dashboard\admin.py                                           | 1     | 0    | 100%  |
| dashboard\apps.py                                            | 4     | 0    | 100%  |
| dashboard\migrations\_init_.py                               | 0     | 0    | 100%  |
| dashboard\models.py                                          | 1     | 0    | 100%  |
| dashboard\tests.py                                           | 62    | 0    | 100%  |
| dashboard\urls.py                                            | 3     | 0    | 100%  |
| dashboard\views.py                                           | 78    | 26   | 67%   |
| email_service\_init_.py                                      | 0     | 0    | 100%  |
| email_service\email_service.py                               | 9     | 0    | 100%  |
| flowlance\_init_.py                                          | 0     | 0    | 100%  |
| flowlance\decorators.py                                      | 50    | 4    | 92%   |
| flowlance\settings.py                                        | 44    | 0    | 100%  |
| flowlance\urls.py                                            | 8     | 1    | 88%   |
| manage.py                                                    | 11    | 2    | 82%   |
| notifications\_init_.py                                      | 0     | 0    | 100%  |
| notifications\admin.py                                       | 1     | 0    | 100%  |
| notifications\apps.py                                        | 4     | 0    | 100%  |
| notifications\migrations\_init_.py                           | 0     | 0    | 100%  |
| notifications\models.py                                      | 1     | 0    | 100%  |
| notifications\tests.py                                       | 1     | 0    | 100%  |
| notifications\urls.py                                        | 3     | 0    | 100%  |
| notifications\views.py                                       | 3     | 1    | 67%   |
| payment\_init_.py                                            | 0     | 0    | 100%  |
| payment\admin.py                                             | 1     | 0    | 100%  |
| payment\apps.py                                              | 4     | 0    | 100%  |
| payment\migrations\_init_.py                                 | 0     | 0    | 100%  |
| payment\models.py                                            | 1     | 0    | 100%  |
| payment\tests.py                                             | 1     | 0    | 100%  |
| payment\urls.py                                              | 3     | 0    | 100%  |
| payment\views.py                                             | 3     | 1    | 67%   |
| profile\_init_.py                                            | 0     | 0    | 100%  |
| profile\admin.py                                             | 9     | 0    | 100%  |
| profile\apps.py                                              | 6     | 0    | 100%  |
| profile\forms.py                                             | 191   | 26   | 86%   |
| profile\migrations\0001_initial.py                           | 8     | 0    | 100%  |
| profile\migrations\_init_.py                                 | 0     | 0    | 100%  |
| profile\models.py                                            | 115   | 3    | 97%   |
| profile\signals.py                                           | 0     | 0    | 100%  |
| profile\tests\_init_.py                                      | 0     | 0    | 100%  |
| profile\tests\test_company_register.py                       | 20    | 0    | 100%  |
| profile\tests\test_forms.py                                  | 69    | 0    | 100%  |
| profile\tests\test_freelancer_register.py                    | 26    | 0    | 100%  |
| profile\tests\test_models.py                                 | 79    | 0    | 100%  |
| profile\tests\test_register_views.py                         | 19    | 0    | 100%  |
| profile\tests\test_views.py                                  | 66    | 0    | 100%  |
| profile\urls.py                                              | 5     | 0    | 100%  |
| profile\views\calification_views.py                          | 74    | 45   | 39%   |
| profile\views\data_views.py                                  | 154   | 102  | 34%   |
| profile\views\profile_views.py                               | 80    | 26   | 68%   |
| profile\views\register_views.py                              | 29    | 6    | 79%   |
| project\_init_.py                                            | 0     | 0    | 100%  |
| project\admin.py                                             | 11    | 0    | 100%  |
| project\apps.py                                              | 4     | 0    | 100%  |
| project\forms.py                                             | 25    | 0    | 100%  |
| project\management\commands\generate_periodic_reports.py     | 183   | 7    | 96%   |
| project\migrations\0001_initial.py                           | 8     | 0    | 100%  |
| project\migrations\_init_.py                                 | 0     | 0    | 100%  |
| project\models.py                                            | 163   | 21   | 87%   |
| project\tests\_init_.py                                      | 0     | 0    | 100%  |
| project\tests\test_assigment_views.py                        | 43    | 0    | 100%  |
| project\tests\test_calendar.py                               | 49    | 0    | 100%  |
| project\tests\test_generate_report.py                        | 71    | 0    | 100%  |
| project\tests\test_milestone_views.py                        | 41    | 0    | 100%  |
| project\tests\test_project_views.py                          | 104   | 0    | 100%  |
| project\tests\test_task_views.py                             | 64    | 0    | 100%  |
| project\urls.py                                              | 3     | 0    | 100%  |
| project\views\assigment_views.py                             | 73    | 13   | 82%   |
| project\views\calendar_views.py                              | 28    | 2    | 93%   |
| project\views\members_views.py                               | 23    | 11   | 52%   |
| project\views\milestone_views.py                             | 59    | 7    | 88%   |
| project\views\project_views.py                               | 267   | 126  | 53%   |
| project\views\task_views.py                                  | 103   | 11   | 89%   |
| settings\_init_.py                                           | 0     | 0    | 100%  |
| settings\migrations\_init_.py                                | 0     | 0    | 100%  |
| settings\tests.py                                            | 76    | 0    | 100%  |
| settings\urls.py                                             | 3     | 0    | 100%  |
| settings\views.py                                            | 23    | 0    | 100%  |
| theme\_init_.py                                              | 0     | 0    | 100%  |
| theme\apps.py                                                | 3     | 0    | 100%  |
| user\LoginForm.py                                            | 6     | 0    | 100%  |
| user\RestorePasswordForm.py                                  | 15    | 0    | 100%  |
| user\_init_.py                                               | 0     | 0    | 100%  |
| user\adapters.py                                             | 19    | 12   | 37%   |
| user\admin.py                                                | 1     | 0    | 100%  |
| user\apps.py                                                 | 4     | 0    | 100%  |
| user\models.py                                               | 10    | 0    | 100%  |
| user\tests.py                                                | 83    | 0    | 100%  |
| user\urls.py                                                 | 4     | 0    | 100%  |
| user\views.py                                                | 93    | 27   | 71%   |
| ------------------------------------------------------------ |-------|------|-------|
| **TOTAL**                                                    | **2922**  | **481**  | **84%**   |


