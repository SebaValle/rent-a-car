# Austral Rent-a-Car

Austral Rent-a-Car es un proyecto de aplicación web desarrollado con Django, que permite a los usuarios explorar y reservar una variedad de vehículos para sus necesidades de transporte.

## Características

- **Exploración de Vehículos:** Explora una amplia gama de vehículos disponibles para alquilar, incluyendo sedanes, SUVs, minivans y camionetas.
- **Registro de Usuarios:** Permite a los usuarios registrarse para acceder a funcionalidades extendidas como reservas y seguimiento de historial.
- **Administración de Administradores:** Funcionalidad administrativa para gestionar usuarios, vehículos y reservas.

## Tecnologías Utilizadas

- **Django:** Framework de desarrollo web de alto nivel en Python.
- **Bootstrap 5:** Biblioteca de diseño front-end para estilos y componentes.
- **SQLite:** Base de datos relacional para almacenar datos del proyecto.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/SebaValle/rent-a-car
    cd austral-rent-a-car
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Uso

Una vez que el servidor esté en funcionamiento, accede a la aplicación en tu navegador web:

