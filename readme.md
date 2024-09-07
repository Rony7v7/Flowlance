# Flow Lance

Simple overview of use/purpose.

## Description

FlowLance es una plataforma en línea diseñada para conectar freelancers con clientes que buscan contratar servicios especializados. El objetivo principal del proyecto es facilitar la interacción entre freelancers y clientes mediante la creación de perfiles detallados, la gestión de proyectos, un sistema de mensajería interna y un procesamiento seguro de pagos. La aplicación destaca por ofrecer funcionalidades innovadoras que optimizan la experiencia del usuario, asegurando una interacción fluida y segura en un entorno competitivo.


## Getting Started

### Dependencies

* Python version 3.10 or above.
* Python package manager (`pip`)
* PostgreSQL

### Installing

0. If you haven't created your own virtual enviroment please do:

    ```

        pip install virtualenv

        python -m venv flowlance_virtual_enviroment

    ```
1. git pull `https://github.com/2024-2-PI1-G3/202402-proyecto-gecko-team`
2. cd into the project (the src folder)
3. Start the virtual enviroment 
    * Linux: `source flowlance_virtual_enviroment/bin/activate`
    * Windows: `flowlance_virtual_enviroment\Scripts\activate`
4. Install all the requirements with: `pip install -r requirements.txt`

### Executing program

* First make the Django Migrations
    ```
        python manage.py makemigrations
        python manage.py migrate

    ```

* Run the server `python manage.py runserver`

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

- Rony Farid Ordoñez Código: A00397968

- Juan José De La Pava Código: A00381213

- Juan Pablo Parra Código: A00398004

- David Artunduaga Código: A00396342

- Pablo Andrés Guzmán Código: A00399523

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
