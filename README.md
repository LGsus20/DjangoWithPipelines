# Django With Pipelines

This project demonstrates the use of Django with a CI/CD pipeline setup. Follow the instructions below to get started.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Create a `.env` file in the root directory of the project (at the same level as the `.env` file provided) with the following fields filled:
    ```properties
    POSTGRES_DB=<your_database_name>
    POSTGRES_USER=<your_database_user>
    POSTGRES_PASSWORD=<your_database_password>
    SQL_HOST=<your_sql_host>
    SQL_PORT=<your_sql_port>
    DJANGO_SECRET_KEY=<your_django_secret_key>
    DEBUG=<true_or_false>
    ```

## Getting Started

To run the project, use the following commands:

1. **Build and Start the Containers**:

    - **For Development**:
        ```bash
        docker compose -f docker-compose_development.yml up --build -d
        ```

    - **For Production**:
        ```bash
        docker compose -f docker-compose_production.yml up --build -d
        ```

2. Apply database migrations:
    ```bash
    docker compose -f docker-compose_development.yml exec web python manage.py makemigrations
    ```

    ```bash
    docker compose -f docker-compose_development.yml exec web python manage.py migrate
    ```

## Features

- Django framework for web development.
- Dockerized environment for easy setup and deployment.
- CI/CD pipeline integration.