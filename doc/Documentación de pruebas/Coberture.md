# Informe de Cobertura de Pruebas

## Explicación del Informe de Cobertura

La cobertura total reportada es del **86%**, sin embargo, este valor está influenciado por algunas aplicaciones como `chat`, `payment`, `notifications`, entre otras, que aún no tienen sus funcionalidades implementadas. Esto genera que haya declaraciones sin pruebas en estas áreas, lo cual reduce el porcentaje general de cobertura.

Excluyendo estas aplicaciones del cálculo, la cobertura efectiva del código desarrollado y probado es significativamente mayor. Los resultados muestran que se ha realizado un esfuerzo considerable en probar las funcionalidades desarrolladas hasta ahora, y se espera que la cobertura global aumente a medida que se avance con el desarrollo y las pruebas de las áreas pendientes.

## Informe de Cobertura

| Nombre                                    | Declaraciones | Faltantes | Cobertura |
|-------------------------------------------|---------------|-----------|-----------|
| chat\__init__.py                          | 0             | 0         | 100%      |
| chat\admin.py                             | 1             | 0         | 100%      |
| chat\apps.py                              | 4             | 0         | 100%      |
| chat\migrations\__init__.py               | 0             | 0         | 100%      |
| chat\models.py                            | 1             | 0         | 100%      |
| chat\tests.py                             | 1             | 0         | 100%      |
| chat\urls.py                              | 3             | 0         | 100%      |
| chat\views.py                             | 3             | 1         | 67%       |
| dashboard\__init__.py                     | 0             | 0         | 100%      |
| dashboard\admin.py                        | 1             | 0         | 100%      |
| dashboard\apps.py                         | 4             | 0         | 100%      |
| dashboard\migrations\__init__.py          | 0             | 0         | 100%      |
| dashboard\models.py                       | 1             | 0         | 100%      |
| dashboard\tests.py                        | 1             | 0         | 100%      |
| dashboard\urls.py                         | 3             | 0         | 100%      |
| dashboard\views.py                        | 6             | 0         | 100%      |
| flowlance\__init__.py                     | 0             | 0         | 100%      |
| flowlance\settings.py                     | 26            | 0         | 100%      |
| flowlance\urls.py                         | 7             | 1         | 86%       |
| manage.py                                 | 11            | 2         | 82%       |
| notifications\__init__.py                 | 0             | 0         | 100%      |
| notifications\admin.py                    | 1             | 0         | 100%      |
| notifications\apps.py                     | 4             | 0         | 100%      |
| notifications\migrations\__init__.py      | 0             | 0         | 100%      |
| notifications\models.py                   | 1             | 0         | 100%      |
| notifications\tests.py                    | 1             | 0         | 100%      |
| notifications\urls.py                     | 3             | 0         | 100%      |
| notifications\views.py                    | 3             | 1         | 67%       |
| payment\__init__.py                       | 0             | 0         | 100%      |
| payment\admin.py                          | 1             | 0         | 100%      |
| payment\apps.py                           | 4             | 0         | 100%      |
| payment\migrations\__init__.py            | 0             | 0         | 100%      |
| payment\models.py                         | 1             | 0         | 100%      |
| payment\tests.py                          | 1             | 0         | 100%      |
| payment\urls.py                           | 3             | 0         | 100%      |
| payment\views.py                          | 3             | 1         | 67%       |
| profile\__init__.py                       | 0             | 0         | 100%      |
| profile\admin.py                          | 8             | 0         | 100%      |
| profile\apps.py                           | 6             | 0         | 100%      |
| profile\forms.py                          | 76            | 5         | 93%       |
| profile\migrations\0001_initial.py        | 8             | 0         | 100%      |
| profile\migrations\__init__.py            | 0             | 0         | 100%      |
| profile\models.py                         | 82            | 2         | 98%       |
| profile\signals.py                        | 15            | 2         | 87%       |
| profile\tests\__init__.py                 | 0             | 0         | 100%      |
| profile\tests\test_forms.py               | 69            | 0         | 100%      |
| profile\tests\test_models.py              | 79            | 0         | 100%      |
| profile\tests\test_views.py               | 71            | 0         | 100%      |
| profile\urls.py                           | 5             | 0         | 100%      |
| profile\views\calification_views.py       | 67            | 37        | 45%       |
| profile\views\data_views.py               | 152           | 99        | 35%       |
| profile\views\profile_views.py            | 31            | 2         | 94%       |
| project\__init__.py                       | 0             | 0         | 100%      |
| project\admin.py                          | 10            | 0         | 100%      |
| project\apps.py                           | 4             | 0         | 100%      |
| project\forms.py                          | 7             | 0         | 100%      |
| project\migrations\0001_initial.py        | 8             | 0         | 100%      |
| project\migrations\__init__.py            | 0             | 0         | 100%      |
| project\models.py                         | 106           | 18        | 83%       |
| project\tests\__init__.py                 | 0             | 0         | 100%      |
| project\tests\test_assigment_views.py     | 43            | 0         | 100%      |
| project\tests\test_milestone_views.py     | 38            | 0         | 100%      |
| project\tests\test_project_views.py       | 75            | 0         | 100%      |
| project\tests\test_task_views.py          | 46            | 0         | 100%      |
| project\urls.py                           | 3             | 0         | 100%      |
| project\views\assigment_views.py          | 62            | 11        | 82%       |
| project\views\milestone_views.py          | 53            | 7         | 87%       |
| project\views\project_views.py            | 100           | 9         | 91%       |
| project\views\task_views.py               | 85            | 10        | 88%       |
| settings\__init__.py                      | 0             | 0         | 100%      |
| settings\migrations\__init__.py           | 0             | 0         | 100%      |
| settings\tests.py                         | 1             | 0         | 100%      |
| settings\urls.py                          | 3             | 0         | 100%      |
| settings\views.py                         | 3             | 1         | 67%       |
| theme\__init__.py                         | 0             | 0         | 100%      |
| theme\apps.py                             | 3             | 0         | 100%      |
| user\LoginForm.py                         | 5             | 0         | 100%      |
| user\__init__.py                          | 0             | 0         | 100%      |
| user\admin.py                             | 1             | 0         | 100%      |
| user\apps.py                              | 4             | 0         | 100%      |
| user\models.py                            | 1             | 0         | 100%      |
| user\tests.py                             | 29            | 0         | 100%      |
| user\urls.py                              | 4             | 0         | 100%      |
| user\views.py                             | 20            | 2         | 90%       |
| **TOTAL**                                 | **1482**      | **211**   | **86%**   |

